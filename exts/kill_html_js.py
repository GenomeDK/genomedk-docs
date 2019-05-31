"""
This extension removes the default javascript from the default html
builder in Sphinx (jquery, underscore.js, doctools, lang data).
As a result it is dependant on the implementation details for the
StandaloneHTMLBuilder class and might break at any time.
"""
from sphinx.builders.html import StandaloneHTMLBuilder

def remove_script_files(app):
    builder = app.builder
    if type(builder) == StandaloneHTMLBuilder and builder.script_files is not None:
        builder.script_files = []

def setup(app):
    app.connect('builder-inited', remove_script_files)
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
