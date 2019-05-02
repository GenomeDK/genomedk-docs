import os.path

from docutils import nodes
from docutils.parsers.rst import directives


from sphinx.locale import _
from sphinx.util import logging
from sphinx.util.osutil import ensuredir, relative_uri
from sphinx.util.docutils import SphinxDirective

from datetime import datetime
from dateutil.parser import parse as _parsedatetime
from dateutil.tz import tzutc, tzlocal

CALENDAR_ICON = ''.join("""
data:image/svg+xml;base64,
PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIy
NCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBz
dHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGlu
ZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJmZWF0
aGVyIGZlYXRoZXItY2FsZW5kYXIiPjxyZWN0IHg9IjMiIHk9IjQiIHdpZHRoPSIx
OCIgaGVpZ2h0PSIxOCIgcng9IjIiIHJ5PSIyIj48L3JlY3Q+PGxpbmUgeDE9IjE2
IiB5MT0iMiIgeDI9IjE2IiB5Mj0iNiI+PC9saW5lPjxsaW5lIHgxPSI4IiB5MT0i
MiIgeDI9IjgiIHkyPSI2Ij48L2xpbmU+PGxpbmUgeDE9IjMiIHkxPSIxMCIgeDI9
IjIxIiB5Mj0iMTAiPjwvbGluZT48L3N2Zz4=
""".strip().splitlines())


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
""".strip()

logger = logging.getLogger(__name__)


def _parsetags(s):
    return s.split(' ')


def render_ical(title, uid, start, end):
    date_format = '%Y%m%dT%H%M%SZ'
    start_str = start.astimezone(tzutc()).strftime(date_format)
    end_str = end.astimezone(tzutc()).strftime(date_format)
    return ICAL_TEMPLATE.format(title=title, uid=uid, start=start_str, end=end_str)


class event(nodes.General, nodes.Element):
    pass


class EventDirective(SphinxDirective):

    required_arguments = 1
    optional_arguments = 3
    final_argument_whitespace = False
    has_content = True
    option_spec = {
        'uid': directives.unchanged_required,
        'start': _parsedatetime,
        'end': _parsedatetime,
        'tags': _parsetags,
    }

    def run(self):
        document = self.state.document

        node = event()
        node['title'] = ' '.join(self.arguments)
        node['uid'] = self.options['uid']
        node['start'] = self.options['start']
        node['end'] = self.options['end']
        node['tags'] = self.options.get('tags')

        self.state.nested_parse(self.content, self.content_offset, node)

        if datetime.now(tzlocal()) > node['end']:
            return [
                document.reporter.warning(
                    _('skipping event "%s" since it is in the past') % node['title'],
                    line=self.lineno
                )
            ]
        return [node]


def render_event_html(self, node, ical_path):
    title = node['title']
    start = node['start'].strftime('%a, %b %d, %Y %H:%M')
    end = node['end'].strftime('%a, %b %d, %Y %H:%M')

    self.body.append('<section class="event">')
    self.body.append('<h3 class="event-title">{}<a type="text/calendar" alt="Add to calendar" href="{}"><img src="{}"></a></h3>'.format(title, ical_path, CALENDAR_ICON))
    self.body.append('<div class="event-start">{}</div>'.format(start))
    self.body.append('<div class="event-end">{}</div>'.format(end))
    self.body.append('<ul class="event-tags">')
    for tag in node['tags']:
        self.body.append('<li class="event-tag">{}</li>'.format(tag))
    self.body.append('</ul>')
    self.body.append('<div class="event-description">')
    for child in node.children:
        self.body.append(child.astext())
    self.body.append('</div>')
    self.body.append('</section>')
    raise nodes.SkipNode


def render_event(self, node):
    ical = render_ical(node['title'], node['uid'], node['start'], node['end'])
    ensuredir(os.path.join(self.builder.outdir, '_downloads'))
    outpath = os.path.join(self.builder.outdir, '_downloads', '{}.ics'.format(node['uid']))
    dlpath = os.path.join(self.builder.dlpath, '{}.ics'.format(node['uid']))
    with open(outpath, 'w') as fp:
        fp.write(ical)
    render_event_html(self, node, dlpath)


def html_visit_event(self, node):
    render_event(self, node)


def setup(app):
    app.add_node(event, html=(html_visit_event, None))
    app.add_directive('event', EventDirective)
    return {'version': '1.0', 'parallel_read_safe': True}
