from setuptools import setup, find_packages
import os

version = '1.0'
maintainer = 'Jonas Baumann'

setup(name='collective.js.throttledebounce',
      version=version,
      description="Installs the throttle / debounce plugin",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='%s, 4teamwork GmbH',
      author_email='mailto:info@4teamwork.ch',
      url='',
      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
