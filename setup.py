#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, print_function

import io
import os
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import relpath
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='deltacode',
    version='0.0.1.beta',
    license='Apache-2.0',
    description='Delta-related utilities.',
    long_description='Delta-related utilities.',
    author='nexB Inc.',
    author_email='info@nexb.com',
    url='https://github.com/nexb/deltacode',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    keywords=[],
    install_requires=[
        'click',
        'scancode-toolkit',
        'unicodecsv',
    ],

    entry_points={
        'console_scripts': [
            'deltacode=deltacode.cli:cli',
        ],
    },

    extras_require={
        # eg: 'rst': ['docutils>=0.11'],
    }
)