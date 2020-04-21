#!/usr/bin/env python

from setuptools import setup

setup(
    name = 'trusat_backend',
    version = '1.1.0',
    maintainer = 'Kenan ONeal',
    maintainer_email = 'email@here',
    description = 'Database and Server environment for TruSat',
    long_description=open('README.md').read(),
    url = 'https://TruSat.org/',
    packages = ['trusat_backend'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
