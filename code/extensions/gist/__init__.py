#-*- coding:utf-8 -*-
u'''

.. code-block:: rst

   .. gist:: https://gist.github.com/user/id


'''

__version__ = '0.0.1'
__author__ = ''
__license__ = ''



def setup(app):

    from . import gist

    app.add_node(gist.gist,
                 html=(gist.visit, gist.depart))
    app.add_directive('gist', gist.GistDirective)

