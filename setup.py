from setuptools import setup, find_packages
import os

version = '0.1.0'

long_description = (
    open('README.rst').read()
    + '\n')

setup(name='beast.securelogin',
      version=version,
      description="A Simple product that overrides the login screen to allow the ajax window to login through https",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src', 'beast'),
      package_dir = {'': 'src'},
      namespace_packages=['beast'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-
  	  [z3c.autoinclude.plugin]
  	  target = plone
      """,
      )
