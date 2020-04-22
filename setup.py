#!/usr/bin/env python

from setuptools import setup

with open('requirements-database.txt') as f:
    requirements = f.read().splitlines()

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setup(
    name = 'trusat_backend',
    description = 'Server and database environment for TruSat',
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    version = '1.1.0',
    author = "Kenan O'Neal, Chris Lewicki",
    url = 'https://TruSat.org/',
    project_urls={
        "Source" : "https://github.com/TruSat/trusat-backend",
        "Tracker" : "https://github.com/TruSat/trusat-backend/issues",
        "Learning Hub" : "https://learn.trusat.org/docs/start-here",
        "Forums" : "https://discuss.trusat.org/"
    },
    packages = ['trusat_backend'],
    install_requires=[requirements],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: SQL',
        'Topic :: Database',
        'Topic :: Scientific/Engineering'
    ],
)
