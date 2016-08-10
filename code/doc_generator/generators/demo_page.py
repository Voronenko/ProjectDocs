"""
Generates demo page.
"""

import json
import os

import arrow
import humanize

from generators.abstract_generator import AbstractTemplatedGenerator


def format_datetime(dt):
    dt = dt.to('Europe/Kiev')
    return dt.strftime('%A %d %b %Y at %H:%M %Z')


class DemoPageGenerator(AbstractTemplatedGenerator):

    demo_page_template = 'docs/project_specific/test_page.rst.jinja2'
    demo_page = 'docs/project_specific/test_page_generated.rst'


    def build_repo_list_page(self):
        # Render the template
        tmpl = self.get_template(self.demo_page_template)
        content = tmpl.render(
            generated_date=format_datetime(arrow.utcnow())
        )

        return content

    def generate(self):
        content = self.build_repo_list_page()

        with open(self.demo_page, 'wb+') as f:
            f.write(content)
