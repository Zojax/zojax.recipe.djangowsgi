from setuptools import setup, find_packages
import os

version = '0.1dev'

setup(name='zojax.recipe.djangowsgi',
      version=version,
      description="WSGI recipe for Django.",
      long_description="",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Anatoly Bubenkov',
      author_email='bubenkoff@zojax.com',
      url='',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'':'src'},
      namespace_packages=['zojax', 'zojax.recipe'],
      include_package_data=True,
      zip_safe=False,
      extras_require = dict(
        test = []
        ),
      install_requires=[
          'setuptools',
          'zc.recipe.egg',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [zc.buildout]
      default = zojax.recipe.djangowsgi:Recipe
      """,
      dependency_links = [],
      )
