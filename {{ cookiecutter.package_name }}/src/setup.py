"""
**Author** : {{ cookiecutter.author_name }}

**Institution** : {{ cookiecutter.package_name }}

**Position** : {{ cookiecutter.author_institution }}

**Contact** : {{ cookiecutter.author_mail }}

**Date** : {% now 'utc', '%Y-%m-%d' %}

**Project** : {{ cookiecutter.package_name }}

** {{ cookiecutter.package_name }} setup file**

"""
import os
import sys
from subprocess import check_output
from pathlib import Path

from setuptools import find_packages, setup


# Main path
SRC_ROOT = Path(
    __file__
).absolute().parent

# Get long description
try:
    readme_path = SRC_ROOT / 'README.md'
    with readme_path.open('r') as readme_handler:
        long_description = readme_handler.read()
except:
    long_description = 'Error'


# Get version
try:
    command = 'git --git-dir {}/.git rev-parse HEAD'.format(
        root
    )
    with os.popen(cmd=command) as stream:
          version = stream.read()[:-1]
except:
    version='Error'

# Get requirements
try:
    requirements_path = SRC_ROOT / 'requirements.txt'
    with requirements_path.open('r') as requirements_handler:
        requirements = [
            dependency
            for dependency in requirements_handler.readlines()
            if not '{{ cookiecutter.package_name }}' in dependency
        ]
except:
    requirements=[]


setup(
    name='{{ cookiecutter.package_name }}',
    author='{{ cookiecutter.author_name }}',
    version=version,
    packages=find_packages(),
    description='{{ cookiecutter.package_description }}',
    long_description=long_description,
    install_requires=requirements,
    author_email='{{ cookiecutter.author_mail }}',
)

