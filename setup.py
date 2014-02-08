from __future__ import with_statement
import os.path
import re

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup


def get_version():
    dir_ = os.path.dirname(os.path.abspath(__file__))
    version_pattern = r'''__version__ *\= *['"]([\d.]+)['"]'''
    with open(os.path.join(dir_, 'dispatch', '__init__.py')) as init:
        match = re.search(version_pattern, init.read())
    return match.group(1)


def get_long_description():
    try:
        return open('README.txt').read()
    except IOError:
        return None


setup(
    name="Paperboy",
    description="A simple fork of django.dispatch for use as a standalone "
                "PubSub library.",
    long_description=get_long_description(),
    version=get_version(),
    packages=['dispatch'],
    install_requires=['six>=1.4.1'],
    test_suite='tests',
    maintainer="Jesse London",
    maintainer_email="jesse@edgeflip.com",
    url="http://github.com/edgeflip/dispatch",
    license='BSD',
    classifiers=(
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ),
)
