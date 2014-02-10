from __future__ import with_statement
import os.path
import re
import sys

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup


def get_version():
    """Retrieve distribution version from `dispatch` package."""
    dir_ = os.path.dirname(os.path.abspath(__file__))
    version_pattern = r'''__version__ *\= *['"]([\d.]+)['"]'''
    with open(os.path.join(dir_, 'dispatch', '__init__.py')) as init:
        match = re.search(version_pattern, init.read())
    return match.group(1)


def get_long_description():
    """Retrieve long distribution description from README.txt, if available."""
    try:
        return open('README.txt').read()
    except IOError:
        return None


def _is_install():
    return len(sys.argv) >= 2 and sys.argv[1] == 'install'


def get_packages():
    """Packages to list.

    Include `tests` package except on install.

    """
    packages = ['dispatch']
    if not _is_install():
        packages.append('tests')
    return packages


def get_py_modules():
    """Modules to list.

    Don't include `ez_setup` on install.

    """
    if _is_install():
        return []
    return ['ez_setup']


setup(
    name="Paperboy",
    description="A simple fork of django.dispatch for use as a standalone "
                "PubSub library.",
    long_description=get_long_description(),
    version=get_version(),
    py_modules=get_py_modules(),
    packages=get_packages(),
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
