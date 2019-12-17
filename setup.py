from setuptools import setup, find_packages
import os

version = '1.3.1'

tests_require = [
    'ftw.testing',
    'plone.app.testing',
]

setup(name='collective.js.throttledebounce',
      version=version,
      description="Installs the throttle / debounce plugin",
      long_description=open("README.rst").read() + "\n" + \
          open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Programming Language :: Python',
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Framework :: Plone :: 5.1',
        ],
      keywords='',
      author='Jonas Baumann, 4teamwork GmbH',
      author_email='mailto:info@4teamwork.ch',
      url='https://github.com/collective/collective.js.throttledebounce',
      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'ftw.upgrade',
      ],
      tests_require=tests_require,
      extras_require={'tests': tests_require},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
