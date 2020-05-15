"""Revealjs support for Sphinx"""
import os

from .presentation import PresentationsManager, PresentationDirective, CONFIG, PresentationNode

from .presentation import process_presentations, generate_presentation_pages, process_presentation_list
from .presentation import generate_presentation_markdown

from . import presentation_embed_directive

__version__ = '0.0.1'


def builder_support(builder):
    """Return True when builder is supported. Supported builders output in
    html format, but exclude `PickleHTMLBuilder` and `JSONHTMLBuilder`,
    which run into issues when serializing blog objects."""

    if hasattr(builder, 'builder'):
        builder = builder.builder

    not_supported = set(['json', 'pickle'])
    return builder.format == 'html' and not builder.name in not_supported


def html_page_context(app, pagename, templatename, context, doctree):

    if builder_support(app):
        context['presentations'] = presentationManager = PresentationsManager(app)


def visit_dummy_node(self, node):
    pass

def depart_dummy_code(self, node=None):
    pass

def setup(app):
    """Setup Revealjs extension."""

    for args in CONFIG:
        app.add_config_value(*args)

    app.add_node(PresentationNode, html=(visit_dummy_node, depart_dummy_code))

    app.add_directive('presentation', PresentationDirective)

    app.connect('doctree-read', process_presentations)
    # //todo: support PresentationsList node
#    app.connect('doctree-resolved', process_presentation_list)
    app.connect('html-collect-pages', generate_presentation_pages)

#    app.connect('env-purge-doc', purge_slides)
#    app.connect('missing-reference', missing_reference)
#    # app.connect('html-collect-pages', ??)
    app.connect('html-page-context', html_page_context)

    pkgdir = os.path.abspath(os.path.dirname(__file__))
    locale_dir = os.path.join(pkgdir, 'locale')
    app.config.locale_dirs.append(locale_dir)

    app.add_node(presentation_embed_directive.presentationembed,
                 html=(presentation_embed_directive.visit, presentation_embed_directive.depart))
    app.add_directive('presentation_embed', presentation_embed_directive.PresentationEmbedDirective)

    return {'version': __version__}   # identifies the version of our extension


def get_html_templates_path():
    """Return path to RevealJS templates folder."""

    pkgdir = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(pkgdir, 'templates')
