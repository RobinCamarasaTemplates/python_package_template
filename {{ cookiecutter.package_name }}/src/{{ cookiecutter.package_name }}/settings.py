"""
**Author** : {{ cookiecutter.author_name }}

**Institution** : {{ cookiecutter.author_institution }}

**Position** : {{ cookiecutter.author_position }}

**Contact** : {{ cookiecutter.author_mail }}

**Date** : {% now 'utc', '%Y-%m-%d' %}

**Project** : {{ cookiecutter.package_name }}

** Settings of the {{ cookiecutter.package_name }} project**

"""
from pathlib import Path


# Define root path
ROOT_PATH = Path(
    __file__
).absolute().parents[2]

# Define src path
SRC_ROOT = ROOT_PATH / 'src'

# Define data path
DATA_PATH = ROOT_PATH / 'data'

# Results paths
RESULTS_PATH = ROOT_PATH / 'results'

# Ressources paths
RESSOURCES_PATH = SRC_ROOT / 'ressources'

# Ressources paths
TESTS_PATH = SRC_ROOT / 'tests'
