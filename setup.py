#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
It paste a file and short the url.
Copyright (C) 2014 Julien Freyermuth
All Rights Reserved

See the file LICENSE for copying permission.
"""


#------
# Used http://www.python.org/dev/peps/pep-0314/ and
# http://getpython3.com/diveintopython3/packaging.html
#
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
#
# to wrote this script
#------------------------


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved',
    'Natural Language :: English',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3',
]

SCRIPTS = ['pastenshort', ]

setup(
    name             = 'pastenshort',
    version          = '0.1',
    description      = 'It paste a file and short the url',
    author           = 'Freyermuth Julien',
    author_email     = 'julien.chipster@gmail.com',
    license          = 'WTFPL',
    platforms        = 'Linux',
	url				 = 'github/pastenshort',
    scripts          = SCRIPTS,
    requires         = ['python (>=3.3)', 'requests'],
    classifiers      = CLASSIFIERS,
)
