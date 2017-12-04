# -*- coding: utf-8 -*-
"""Classes for handling Presentations"""

import os, sys, re

from os.path import basename

import projectdocs_slides

try:
    from collections.abc import Container
except ImportError:
    from collections import Container

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


from docutils import nodes
from docutils.io import StringOutput

from unicodedata import normalize

from sphinx import addnodes
from sphinx.util.osutil import relative_uri
from sphinx.environment import dummy_reporter
from sphinx.locale import _
from sphinx.util.nodes import set_source_info
from sphinx.util.compat import Directive
from docutils.parsers.rst import directives


if sys.version_info >= (3, 0):
    text_type = str
    re_flag = 0
elif sys.version_info < (2, 7):
    text_type = unicode
    re_flag = None
else:
    text_type = unicode
    re_flag = re.UNICODE


class PresentationNode(nodes.Element):
    """Represent ``Presentation`` directive content and options in document tree."""

    pass


class PresentationList(nodes.General, nodes.Element):
    """Represent ``PresentationList`` directive converted to a list of links."""

    pass


class PresentationDirective(Directive):
    """Handle ``post`` directives."""

    def _split(a): return [s.strip()
                           for s in (a or '').split(',') if s.strip()]

    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        'tags': _split,
        'category': _split,
        'title': lambda a: a.strip(),
        'image': int,
        'excerpt': int,
        # 	Revealjs markdown note delimiter
        #   default note:
        'notesSeparator': directives.unchanged,
        # Revealjs markdown slide separator
        # default: ^( ?| )---( ?| )$
        'separator': directives.unchanged,
        # Revealjs markdown vertical separator
        # default: ^( ?| )--( ?| )$
        'verticalSeparator': directives.unchanged,
        # Revealjs Theme (black, white, league, beige, sky, night, serif, simple, solarized
        # default: black
        'theme': directives.unchanged,
        # Highlight Theme
        # default: Zenburn
        'highlightTheme': directives.unchanged,
        # Display controls in the bottom right corner
        # default: true
        'controls': directives.unchanged,
        # Display a presentation progress bar
        # default: true
        'progress': directives.unchanged,
        # Display the page number of the current slide
        'slideNumber': directives.unchanged,
        # Push each slide change to the browser history
        'history': directives.unchanged,
        # Enable keyboard shortcuts for navigation
        # default: true
        'keyboard': directives.unchanged,
        # Enable the slide overview mode
        # default: true
        'overview': directives.unchanged,
        # Vertical centering of slides
        # default: true
        'center': directives.unchanged,
        # Enables touch navigation on devices with touch input
        # default: true
        'touch': directives.unchanged,
        # Loop the presentation
        # default:
        'loop': directives.unchanged,
        # Change the presentation direction to be RTL
        # default:
        'rtl': directives.unchanged,
        # Randomizes the order of slides each time the presentation loads
        # default:
        'shuffle': directives.unchanged,
        # Turns fragments on and off globally
        # default: true
        'fragments': directives.unchanged,
        # Flags if the presentation is running in an embedded mode, i.e. contained within a limited portion of the screen
        # default:
        'embedded': directives.unchanged,
        # Flags if we should show a help overlay when the questionmark key is pressed
        # default: true
        'help': directives.unchanged,
        # Flags if speaker notes should be visible to all viewers
        # default:
        'showNotes': directives.unchanged,
        # Number of milliseconds between automatically proceeding to the next slide, disabled when set to 0, this value can be overwritten by using a data-autoslide attribute on your slides
        # default:
        'autoSlide': directives.unchanged,
        # Stop auto-sliding after user input
        # default: true
        'autoSlideStoppable': directives.unchanged,
        # Enable slide navigation via mouse wheel
        # default: 
        'mouseWheel': directives.unchanged,
        # Hides the address bar on mobile devices
        # default: true
        'hideAddressBar': directives.unchanged,
        # Opens links in an iframe preview overlay
        # default:
        'previewLinks': directives.unchanged,
        # Transition style (none/fade/slide/convex/concave/zoom)
        # default: default
        'transition': directives.unchanged,
        # Transition speed (default/fast/slow)
        # default: default
        'transitionSpeed': directives.unchanged,
        # Transition style for full page slide backgrounds (none/fade/slide/convex/concave/zoom)
        # default: default
        'backgroundTransition': directives.unchanged,
        # Number of slides away from the current that are visible
        # default: 3
        'viewDistance': directives.unchanged,
        # Parallax background image
        # default: 
        'parallaxBackgroundImage': directives.unchanged,
        # Parallax background size (CSS syntax, e.g. 2100px 900px)
        # default: 
        'parallaxBackgroundSize': directives.unchanged,
        # Number of pixels to move the parallax background per slide
        # default:
        'parallaxBackgroundHorizontal': directives.unchanged,
        # 	Number of pixels to move the parallax background per slide
        # default:
        'parallaxBackgroundVertical': directives.unchanged,


    }

    def run(self):

        node = PresentationNode()
        node.document = self.state.document
        set_source_info(self, node)

        # todo: support external presentation sources
        node['content'] = u'\n'.join(self.content)
        # self.state.nested_parse(self.content, self.content_offset,
        #                         node, match_titles=1)

        node['tags'] = self.options.get('tags', [])
        node['category'] = self.options.get('category', [])
        node['title'] = self.options.get('title', None)
        node['image'] = self.options.get('image', None)
        node['excerpt'] = self.options.get('excerpt', None)
        node['notesSeparator'] = self.options.get('notesSeparator', "note:")
        node['separator'] = self.options.get('separator', "^( ?| )---( ?| )$")
        node['verticalSeparator'] = self.options.get(
            'verticalSeparator', "^( ?| )--( ?| )$")
        node['theme'] = self.options.get('theme', "black")
        node['highlightTheme'] = self.options.get('highlightTheme', "Zenburn")
        node['progress'] = self.options.get('progress', "true")
        node['slideNumber'] = self.options.get('slideNumber', None)
        node['history'] = self.options.get('history', None)
        node['keyboard'] = self.options.get('keyboard', "true")
        node['overview'] = self.options.get('overview', "true")
        node['center'] = self.options.get('center', "true")
        node['touch'] = self.options.get('touch', "true")
        node['loop'] = self.options.get('loop', None)
        node['rtl'] = self.options.get('rtl', None)
        node['shuffle'] = self.options.get('shuffle', None)
        node['fragments'] = self.options.get('fragments', "true")
        node['embedded'] = self.options.get('embedded', None)
        node['help'] = self.options.get('help', "true")
        node['showNotes'] = self.options.get('showNotes', None)
        node['autoSlide'] = self.options.get('autoSlide', None)
        node['autoSlideStoppable'] = self.options.get(
            'autoSlideStoppable', "true")
        node['mouseWheel'] = self.options.get('mouseWheel', None)
        node['hideAddressBar'] = self.options.get('hideAddressBar', "true")
        node['previewLinks'] = self.options.get('previewLinks', None)
        node['transition'] = self.options.get('transition', "default")
        node['backgroundTransition'] = self.options.get(
            'backgroundTransition', "default")
        node['viewDistance'] = self.options.get('viewDistance', 3)
        node['parallaxBackgroundImage'] = self.options.get(
            'parallaxBackgroundImage', None)
        node['parallaxBackgroundSize'] = self.options.get(
            'parallaxBackgroundSize', None)
        node['parallaxBackgroundHorizontal'] = self.options.get(
            'parallaxBackgroundHorizontal', None)
        node['parallaxBackgroundVertical'] = self.options.get(
            'parallaxBackgroundVertical', None)

        return [node]


def slugify(string):
    """Slugify *s*."""

    string = text_type(string)
    string = normalize('NFKD', string)

    if re_flag is None:
        string = re.sub(r'[^\w\s-]', '', string).strip().lower()
        return re.sub(r'[-\s]+', '-', string)
    else:
        string = re.sub(r'[^\w\s-]', '', string, flags=re_flag).strip().lower()
        return re.sub(r'[-\s]+', '-', string, flags=re_flag)


def os_path_join(path, *paths):

    return os.path.join(path, *paths).replace(os.path.sep, '/')


def revise_pending_xrefs(doctree, docname):

    for node in doctree.traverse(addnodes.pending_xref):
        node['refdoc'] = docname


def _get_section_title(section):
    """Return section title as text."""

    for title in section.traverse(nodes.title):
        break
    if title:
        return title.astext()
    else:
        return ""


def html_builder_write_doc(self, docname, doctree):
    """Part of :meth:`sphinx.builders.html.StandaloneHTMLBuilder.write_doc`
    method used to convert *doctree* to HTML."""

    destination = StringOutput(encoding='utf-8')
    doctree.settings = self.docsettings

    self.secnumbers = {}
    self.imgpath = relative_uri(self.get_target_uri(docname), '_images')
    self.dlpath = relative_uri(self.get_target_uri(docname), '_downloads')
    self.current_docname = docname
    self.docwriter.write(doctree, destination)
    self.docwriter.assemble_parts()
    return self.docwriter.parts['fragment']

def process_presentations(app, doctree):
    """Process presentations and map posted document names to post details in the
    environment."""
    # todo
    env = app.builder.env

    if not hasattr(env, 'vs_presentations'):
        env.vs_presentations = {}

    presentation_nodes = list(doctree.traverse(PresentationNode))
    if not presentation_nodes:
        return

    docname = env.docname

    manager = PresentationsManager(app)

    # mark the presentation as 'orphan' so that
    #   "document isn't included in any toctree" warning is not issued
    #   and we can amend layout on own processing
    app.env.metadata[docname]['orphan'] = True

    for order, node in enumerate(presentation_nodes, start=1):

        section = doctree
        # are needed when resolving lists in documents
        title = node['title'] or _get_section_title(section)


        folder, label = os.path.split(docname)
        if label == 'index':
            folder, label = os.path.split(folder)
        if not label:
            label = slugify(title)

        section_name = ''
        app.env.domains['std'].data['labels'][label] = (docname, label, title)

        if docname not in env.vs_presentations:
            env.vs_presentations[docname] = []

        if section.parent is doctree:
            section_copy = section[0].deepcopy()
        else:
            section_copy = section.deepcopy()

        presentation_info = {
            'docname': docname,
            'section': section_name,
            'content': node['content'],
            'order': order,
            'title': title,
            'tags': node['tags'],
            'category': node['category'],
            'doctree': section_copy
        }
        env.vs_presentations[docname].append(presentation_info)


    pass


def generate_presentation_pages(app):

    if not projectdocs_slides.builder_support(app):
        return
 
    context = {}
    manager = PresentationsManager(app)
    manager.register_presentations()
    for presentation in manager.presentations['all']:
        context['external_presentation_address'] = basename(presentation.docname) + ".md"
        yield (presentation.docname, context, 'presentation.html')

    generate_presentation_markdown(app, manager.presentations)



def generate_presentation_markdown(app, presentations):

    markdown_path = os.path.join(app.builder.outdir, 'slides/')
    for presentation in presentations['all']:
        targetmd=os.path.join(markdown_path, basename(presentation.docname) + ".md")
        with open(targetmd, 'w') as out:
            try:
                out.write(presentation.options['content'].encode('utf-8'))
            except TypeError:
                out.write("error retrieving markdown document")



def process_presentation_list(app, doctree, docname):

    manager = PresentationsManager(app)
    manager.register_presentations()


def missing_reference(app, env, node, contnode):
    # todo
    pass


CONFIG = [
    # name, default, rebuild
    ('presentations_path', 'slides', True),
]

class PresentationsManager(Container):

    # using a shared state
    _dict = {}

    def __init__(self, app):

        self.__dict__ = self._dict
        if not self._dict:
            self._init(app)

    def _init(self, app):
        """Instantiate Presentations."""

        self.app = app
        self.config = {}

        self.references = refs = {}

        # get configuration from Sphinx app
        for opt in CONFIG:
            self.config[opt[0]] = getattr(app.config, opt[0])

        # catalog containing all Presentations
        self.presentations = Catalog(self, 'presentation', 'presentation', None)

        self.catalogs = cat = {}  # catalogs of user set labels
        self.tags = cat['tags'] = Catalog(self, 'tags', 'tag', 'tag')
        refs['presentation-tags'] = (self.tags.docname, 'Tags')

        self.category = cat['category'] = Catalog(self, 'category',
            'category', 'category')
        refs['presentation-categories'] = (self.category.docname, 'Categories')



    def __getattr__(self, name):

        try:
            attr = self.config[name]
        except KeyError:
            raise AttributeError('Projectdocs presentations have no configuration option {}'
                                 .format(repr(name)))
        return attr

    def __getitem__(self, key):

        return self.presentations[key]

    def __contains__(self, item):

        return item in self.presentations

    def __len__(self):

        return len(self.presentations)

    def __nonzero__(self):

        return len(self) > 0

    def register(self, docname, info):
        """Register presentation *docname*."""

        presentation = Presentation(self, docname, info)
        self.presentations.add(presentation)

    def page_id(self, pagename):
        """Return pagename, trimming :file:`index` from end when found.
        Return value is used as disqus page identifier."""

        if self.config['presentations_baseurl']:
            if pagename.endswith('index'):
                pagename = pagename[:-5]
            pagename = pagename.strip('/')
            return '/' + pagename + ('/' if pagename else '')

    def page_url(self, pagename):
        """Return page URL when :confval:`presentations_baseurl` is set, otherwise
        ``None``. When found, :file:`index.html` is trimmed from the end
        of the URL."""

        if self.config['presentations_baseurl']:
            url = urljoin(self.config['presentations_baseurl'], pagename)
            if url.endswith('index'):
                url = url[:-5]
            return url

    def register_presentations(self):
        """Register presentations found in the Sphinx build environment."""
        if (len(self.presentations) == 0):
            for docname, presentations in getattr(self.app.env, 'vs_presentations', {}).items():
                for presentation_info in presentations:
                    self.register(docname, presentation_info)



class PresentationPageMixin(object):

    def __str__(self):
        return self.title

    def __repr__(self):

        return str(self) + ' <' + text_type(self.docname) + '>'

    @property
    def presentationManager(self):
        """Reference to :class:`~PresentationManager` object."""

        return self._presentationManager

    @property
    def title(self):

        return getattr(self, 'name', getattr(self, '_title'))


class Presentation(PresentationPageMixin):

    """Handle presentation metadata."""

    def __init__(self, presentationManager, docname, info):

        self._presentationManager = presentationManager
        self.docname = docname
        self.section = info['section']
        self.order = info['order']
        self._title = info['title']
        self.doctree = info['doctree']
        self.options = info

    def to_html(self, pagename, fulltext=False, drop_h1=True):
        """Return excerpt or *fulltext* as HTML after resolving references
        with respect to *pagename*. By default, first `<h1>` tag is dropped
        from the output. More than one can be dropped by setting *drop_h1*
        to the desired number of tags to be dropped."""

        if fulltext:
            doctree = nodes.document({}, dummy_reporter)
            deepcopy = self.doctree.deepcopy()
            if isinstance(deepcopy, nodes.document):
                doctree.extend(deepcopy.children)
            else:
                doctree.append(deepcopy)
        else:
            doctree = nodes.document({}, dummy_reporter)
        app = self._presentationManager.app

        revise_pending_xrefs(doctree, pagename)
        app.env.resolve_references(doctree, pagename, app.builder)

        add_permalinks, app.builder.add_permalinks = (
            app.builder.add_permalinks, False)

        html = html_builder_write_doc(app.builder, pagename, doctree)

        app.builder.add_permalinks = add_permalinks

        if drop_h1:
            html = re.sub('<h1>(.*?)</h1>', '', html, count=abs(int(drop_h1)))
        return html


class Catalog(PresentationPageMixin):

    """Handles collections of presentations."""

    def __init__(self, presentationManager, name, xref, path, reverse=False):

        self._presentationManager = presentationManager
        self.name = name
        self.xref = xref  
        self.collections = {}

        if path:
            self.path = self.docname = os_path_join(
                presentationManager.presentations_path, path)
        else:
            self.path = self.docname = presentationManager.presentations_path

        self._coll_lens = None
        self._min_max = None
        self._reverse = reverse

    def __str__(self):

        return text_type(self.name)

    def __getitem__(self, name):

        try:
            return self.collections[name]
        except KeyError:
            return self.collections.setdefault(name, Collection(self, name))

    def __setitem__(self, name, item):

        self.collections[name] = item

    def __len__(self):

        return sum(len(coll) for coll in self)

    def __nonzero__(self):

        return len(self) > 0

    def __iter__(self):

        keys = list(self.collections)
        keys.sort(reverse=self._reverse)
        for key in keys:
            yield self.collections[key]

    def add(self, presentation):
        """Add presentation to appropriate collection(s) and replace collections
        labels with collection objects."""
        colls = []
        for label in getattr(presentation, self.name, []):
            coll = self[label]
            coll.add(presentation)
            colls.append(coll)
        coll = self['all']
        coll.add(presentation)
        colls.append(coll)
        setattr(presentation, self.name, colls)

    def _minmax(self):
        """Return minimum and maximum sizes of collections."""

        if (self._coll_lens is None or
                len(self._coll_lens) != len(self.collections)):
            self._coll_lens = [len(coll) for coll in self.collections.values()
                               if len(coll)]
            self._min_max = min(self._coll_lens), max(self._coll_lens)
        return self._min_max


class Collection(PresentationPageMixin):

    """Presentations sharing a label, i.e. tag, category."""

    def __init__(self, catalog, label, name=None, href=None, path=None, page=0):

        self._catalog = catalog
        self._presentationManager = catalog.presentationManager
        self.label = label
        self.name = name or self.label
        self.href = href
        self.page = page
        self._presentations = {}
        self._presentations_iter = None
        self._path = path
        self.xref = self.catalog.xref + '-' + slugify(label)
        self._slug = None
        self._html = None

        self._catalog.presentationManager.references[self.xref] = (self.docname, self.name)

    def __str__(self):

        return text_type(self.name)

    def __len__(self):

        return len(self._presentations)

    def __nonzero__(self):

        return len(self) > 0

    def __unicode__(self):

        return text_type(self.name)

    def __iter__(self):

        if self._presentations_iter is None:
            posts = list(self._presentations.values())
            posts.sort(reverse=True)
            self._presentations_iter = posts

        for post in self._presentations_iter:
            yield post

    def __getitem__(self, key):

        return self._presentations.get(key)

    def __contains__(self, item):

        return item in self._presentations

    @property
    def catalog(self):
        """:class:`~proectdocs_slides.presentation.Catalog` that the collection belongs to."""

        return self._catalog

    def add(self, post):
        """Add post to the collection."""

        post_name = post.docname
        if post.section:
            post_name += '#' + post.section
        self._presentations[post_name] = post

    def relsize(self, maxsize=5, minsize=1):
        """Relative size used in tag clouds."""

        min_, max_ = self.catalog._minmax()

        diff = maxsize - minsize
        if len(self.catalog) == 1 or min_ == max_:
            return int(round(diff / 2. + minsize))

        size = int(1. * (len(self) - min_) / (max_ - min_) * diff + minsize)
        return size

    @property
    def docname(self):
        """Collection page document name."""

        if self._path is None:
            self._path = os_path_join(self.catalog.path, slugify(self.name))
        return self._path

    path = docname

