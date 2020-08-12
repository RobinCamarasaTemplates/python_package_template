"""
**Author** : Robin Camarasa

**Institution** : Erasmus Medical Center

**Position** : PhD student

**Contact** : r.camarasa@erasmusmc.nl

**Date** : 2020-08-06

**Project** : Slide latex template ErasmusMC

**Test project generation of Erasmus MC Slides**

"""
import sys
from datetime import datetime
import pytest
import shutil
from pathlib import Path
from cookiecutter import main


ROOT = Path(__file__).parents[1]
TESTS_ROOT = ROOT / 'test_output'
EXTRA_CONTEXT = {
    "package_name": "test_package",
    "package_description": "This package is a test of cookiecutter",
    "repo_url": "https://test.github.com",

    "author_name": "John Doe",
    "author_position": "Intern",
    "author_institution": "Lambda company",
    "author_github": "https://johndoe.github.io",
    "author_mail": "john.doe@lambda.com",

    "python_version": "3.6",

    "open_source_license": ["MIT", "BSD-3-Clause", "No license file"]
}

def test_generate_project() -> None:
    """
    Test project generation

    :return: None
    """
    # Clean
    if TESTS_ROOT.exists():
        shutil.rmtree(TESTS_ROOT)
    TESTS_ROOT.mkdir()

    # Get path
    output_dir = TESTS_ROOT.resolve()

    # Launch project generation
    main.cookiecutter(
        str(ROOT),
        no_input=True,
        extra_context=EXTRA_CONTEXT,
        output_dir=output_dir
    )

    # Test project generation
    project_name = ''.format(
        datetime.now().strftime('%Y-%m-%d')
    )
    assert (
        TESTS_ROOT / EXTRA_CONTEXT['package_name']
    ).exists()

    empty_subfolders = ['data', 'results']
    for subfolder in empty_subfolders:
        assert (
            TESTS_ROOT / EXTRA_CONTEXT['package_name'] / subfolder
        ).exists()

    files_and_empty_folders = [
        'README.md', 'README.rst', 'requirements.txt',
        'ressources', 'setup.py', 'tests',
        'tests_output', 'tox.ini',
    ]
    for item in files_and_empty_folders:
        assert (
            TESTS_ROOT / EXTRA_CONTEXT['package_name'] / 'src' / item
        ).exists()

    assert (
        TESTS_ROOT / EXTRA_CONTEXT['package_name'] / 'src' / \
        EXTRA_CONTEXT['package_name'] / '__init__.py'
    ).exists()

    assert (
        TESTS_ROOT / EXTRA_CONTEXT['package_name'] / 'src' / \
        EXTRA_CONTEXT['package_name'] / 'settings.py'
    ).exists()

