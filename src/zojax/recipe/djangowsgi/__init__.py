import logging
import os
import zc.buildout
from zc.recipe.egg.egg import Eggs

WRAPPER_TEMPLATE = """\
import sys, os
syspaths = [
    %(syspath)s,
    ]

for path in reversed(syspaths):
    if path not in sys.path:
        sys.path[0:0]=[path]


import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    os.environ['DJANGO_SETTINGS_MODULE'] = environ['DJANGO_SETTINGS_MODULE']
    if environ['wsgi.url_scheme'] == 'https':
        environ['HTTPS'] = 'on'
    return _application(environ, start_response)

"""

class Recipe:
    def __init__(self, buildout, name, options):
        self.buildout=buildout
        self.name=name
        self.options=options
        self.logger=logging.getLogger(self.name)

    def install(self):
        egg=Eggs(self.buildout, self.options["recipe"], self.options)
        reqs,ws=egg.working_set()
        path=[pkg.location for pkg in ws]
        extra_paths = self.options.get('extra-paths', '')
        extra_paths = extra_paths.split()
        path.extend(extra_paths)

        output=WRAPPER_TEMPLATE % dict(
            syspath=",\n    ".join((repr(p) for p in path))
            )

        location=self.buildout["buildout"]["bin-directory"]
        if not os.path.exists(location):
            os.mkdir(location)
            self.options.created(location)

        target=os.path.join(location, self.name)
        f=open(target, "wt")
        f.write(output)
        f.close()
        os.chmod(target, 0755)
        self.options.created(target)

        return self.options.created()


    def update(self):
        self.install()
