#!/usr/bin/env python

from setuptools import setup

setup(name='tap-zendesk',
      version='2.0.0',
      description='Singer.io tap for extracting data from the Zendesk API',
      author='Stitch',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_zendesk'],
      install_requires=[
          'singer-python @ git+https://git@github.com/ameier38/singer-python@master#egg=singer-python',
          'zenpy'
      ],
      extras_require={
          'dev': [
              'ipdb',
              'pylint',
              'nose',
              'nose-watch',
          ]
      },
      entry_points='''
          [console_scripts]
          tap-zendesk=tap_zendesk:main
      ''',
      packages=['tap_zendesk'],
      include_package_data=True,
)
