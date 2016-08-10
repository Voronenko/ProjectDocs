import os

from jinja2 import Environment
from generators.filters import indentation, headings


class AbstractGenerator(object):
    def generate(self):
        raise NotImplementedError


class AbstractTemplatedGenerator(AbstractGenerator):

    def get_path_from_repo_root(self, path):
        repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        path = os.path.join(repo_root, path)
        return path

    def get_template(self, path):
        env = Environment()
        env.filters['indentation'] = indentation
        env.filters['headings'] = headings
        filepath = self.get_path_from_repo_root(path)
        with open(filepath, 'rb+') as f:
            content = f.read()

        tmpl = env.from_string(content.decode('utf-8'))
        return tmpl
