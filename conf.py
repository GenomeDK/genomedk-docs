#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os.path
import re

sys.path.append(os.path.abspath("exts"))

# -- General configuration ------------------------------------------------

extensions = ["kill_html_js"]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

project = "GenomeDK"
copyright = "2018, The GenomeDK Team"
author = "The GenomeDK Team"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = "friendly"

# -- Options for HTML output ----------------------------------------------

html_theme = "au"
html_theme_options = {
    "sitename": "GenomeDK",
    "phone": "+45 93 52 26 33",
    "email": "support@genome.au.dk",
    "show_breadcrumb": "no",
}
html_static_path = ["_static"]


def setup(app):
    app.add_css_file("gdk.css")


# -- Custom shell session lexer -------------------------------------------

from pygments.lexers.shell import ShellSessionBaseLexer, BashLexer
from sphinx.highlighting import lexers


def _optional(s):
    return "(?:" + s + ")?"


def _group(s):
    return "(" + s + ")"


_command = r".*\n?"
_conda_env = r"\(.*\)\s*"
_info = r"\[.*\]\s*"
_sep = r"[$]"
prompt_regex = _group(_optional(_conda_env) + _optional(_info) + _sep) + _group(
    _command
)
assert prompt_regex == r"((?:\(.*\)\s*)?(?:\[.*\]\s*)?[$])(.*\n?)"


class CustomBashSessionLexer(ShellSessionBaseLexer):
    name = "Bash Session"
    _innerLexerCls = BashLexer
    _ps1rgx = re.compile(prompt_regex)
    _ps2 = ">"


lexers["console"] = CustomBashSessionLexer()

