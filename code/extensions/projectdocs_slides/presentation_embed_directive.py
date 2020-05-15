#-*- coding:utf-8 -*-

from docutils import nodes

from docutils.parsers import rst


class presentationembed(nodes.General, nodes.Element):
    pass

def visit(self, node):

    tag = u'''<iframe src="/slides/{0}.html" height="{1}" width="{2}"></iframe>'''.format(node.presentation, node.height, node.width)

    self.body.append(tag)

def depart(self, node):
    pass

class PresentationEmbedDirective(rst.Directive):

    name = 'presentation'
    node_class = presentationembed

    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'width': lambda a: a.strip(),
        'height': lambda a: a.strip(),
        'presentation': lambda a: a.strip()
    }


    def run(self):

        node = self.node_class()

        node.presentation = self.options["presentation"]
        node.height = self.options["height"]
        node.width = self.options["width"]

        return [node]
