import os.path
from datetime import datetime, timedelta

from dateutil.parser import parse as _parsedatetime
from dateutil.tz import tzutc, tzlocal
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.locale import _
from sphinx.util import logging
from sphinx.util.osutil import ensuredir, relative_uri
from sphinx.util.docutils import SphinxDirective


ICAL_DATETIME_FORMAT = '%Y%m%dT%H%M%SZ'

DATETIME_FORMAT = '%a, %b %d, %Y %H:%M %z'

ICAL_TEMPLATE = """
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//hacksw/handcal//NONSGML v1.0//EN
BEGIN:VEVENT
UID:{uid}@genome.au.dk
DTSTART:{start}
DTEND:{end}
SUMMARY:{title}
END:VEVENT
END:VCALENDAR
"""

logger = logging.getLogger(__name__)


def _parsetags(s):
    return s.split(' ')


def tznow():
    """Return the current date and time in the local time-zone"""
    return datetime.now(tzlocal())


class event(nodes.General, nodes.Element):
    pass


class eventlist(nodes.General, nodes.Element):
    pass


class eventlink(nodes.General, nodes.Element):
    pass


class EventDirective(SphinxDirective):

    required_arguments = 0
    optional_arguments = 5
    final_argument_whitespace = False
    has_content = True
    option_spec = {
        'uid': directives.unchanged_required,
        'start': _parsedatetime,
        'end': _parsedatetime,
        'actualend': _parsedatetime,
        'tags': _parsetags,
    }

    def make_definition_list(self, definitions):
        dl = nodes.definition_list()
        for term, description, _termclass in definitions:
            dli = nodes.definition_list_item(CLASSES=[_termclass])
            dli += nodes.term('', nodes.Text(term))
            dli += nodes.description('', nodes.Text(description))
            dl += dli
        return dl

    def run(self):
        title = ' '.join(self.arguments)
        uid = self.options['uid']
        start = self.options['start']
        end = self.options['end']
        actualend = self.options.get('actualend')
        tags = self.options.get('tags')
    
        _end = actualend or end
        now = tznow()
        if start < now < _end:
           status = 'ongoing'
        elif now < start:
           status = 'upcoming'
        elif now - timedelta(hours=48) < _end:
           status = 'recent'
        else:
           status = 'ended'

        event_node = nodes.section(
            ids=[uid,], CLASSES=['event', 'status-{}'.format(status)]
        )
        event_node['status'] = status

        title_par = nodes.title('', title, CLASSES=['event-title'])
        event_node += title_par

        definitions=[
            ('Planned start', start, 'event-start'),
            ('Planned end', start, 'event-end'),
        ]
        if actualend:
            definitions.append(('Actual end', actualend, 'event-actualend'))

        event_node += self.make_definition_list(definitions)

        tag_list = nodes.bullet_list(CLASSES=['event-tags'])
        for tag in tags:
            tag_list += nodes.list_item('', nodes.Text(tag), CLASSES=['event-tag'])
        event_node += tag_list

        self.state.nested_parse(self.content, self.content_offset, event_node)

        lnk = eventlink()
        lnk['title'] = title
        lnk['uid'] = uid
        lnk['start'] = start
        lnk['end'] = end
        event_node += lnk

        if not hasattr(self.env, 'event_all_events'):
            self.env.event_all_events = []
        self.env.event_all_events.append({
            'docname': self.env.docname,
            'lineno': self.lineno,
            'event': event_node.deepcopy(),
        })
        return []


class EventlistDirective(SphinxDirective):
    optional_arguments = 1
    option_spec = {
        'status': directives.unchanged_required,
        'quiet': directives.unchanged,
    }

    def run(self):
        lst = eventlist('')
        lst['status'] = self.options['status']
        lst['quiet'] = self.options.get('quiet', False)
        return [lst]


def html_visit_eventlink(self, node):
    def generate_ical():
        ical_str = ICAL_TEMPLATE.format(
            title=node['title'],
            uid=node['uid'],
            start=node['start'].astimezone(tzutc()).strftime(ICAL_DATETIME_FORMAT),
            end=node['end'].astimezone(tzutc()).strftime(ICAL_DATETIME_FORMAT),
        )

        filename = '{}.ics'.format(node['uid'])

        downloads_dir = os.path.join(self.builder.outdir, '_downloads')
        ensuredir(downloads_dir)
        
        outpath = os.path.join(downloads_dir, filename)
        dlpath = os.path.join(self.builder.dlpath, filename)
        
        with open(outpath, 'w') as fp:
            fp.write(ical_str)
        return dlpath
    
    src = generate_ical()
    self.body.append('<a href="{}">Add to calendar</a>'.format(src))


def html_depart_eventlink(self, node):
    pass


def html_visit_event(self, node):
    pass


def process_event_nodes(app, doctree, fromdocname):
    env = app.builder.env
    for event_list in doctree.traverse(eventlist):
        content = []
        for event_info in env.event_all_events:
            event = event_info['event']
            if event['status'] == event_list['status']:
                content.append(event)
        if content:
            event_list.replace_self(content)
        elif not event_list['quiet']:
            event_list.replace_self(nodes.Text(_('No events.', _('No events.'))))
        else:
            event_list.replace_self([])


def purge_events(app, env, docname):
    if not hasattr(env, 'event_all_events'):
        return

    env.event_all_events = [
        event for event in env.event_all_events
        if event['docname'] != docname
    ]


def setup(app):
    app.add_node(event, html=(html_visit_event, None))
    app.add_node(eventlink, html=(html_visit_eventlink, html_depart_eventlink))
    app.add_directive('event', EventDirective)
    app.add_directive('eventlist', EventlistDirective)
    app.connect('doctree-resolved', process_event_nodes)
    app.connect('env-purge-doc', purge_events)
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
