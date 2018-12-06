#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import sys

from setuptools import setup, find_packages

with open('README.md') as rmfile:
    readme = rmfile.read()

requirements = [
    'gitpython',
    'pandas==0.22',
    'requests',
    'goodtables',
    'tableschema',
    'graphviz',
    'statsmodels'
]

test_requirements = [
    'pytest',
]

setup(
    name='forecastcarddata',
    version='0.1.0dev',
    packages=find_packages(include=['forecastcarddata']),
    long_description=readme,
    author="Elizabeth Sall",
    author_email='easall@gmail.com',
    url='https://github.com/e-lo/forecastcarddata',
    include_package_data=True,
    dependency_links=['http://github.com/e-lo/forecastcards/tarball/master#egg=forecastcards'],
    install_requires=requirements,
    package_data={'forecastcarddata': ['data/*']},
    tests_suite = 'tests',
    tests_require=test_requirements,
)
