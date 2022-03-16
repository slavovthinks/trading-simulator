from io import open
from typing import List
from setuptools import find_packages, setup


PROJECT = 'trading-simulator'
SRC_DIR = 'src'


def read_file(filename: str) -> str:
    """Read an ASCII file where you need.
    :param str filename: The path for the file we are going to read data from
    :return: the file content
    """
    with open(filename) as fp:
        return fp.read().strip()


def read_requirements(filename: str) -> List[str]:
    """Generate a list with dependencies `setup.py` needs,
    skipping commented lines.
    :param str filename: the requirements file name
    :return: a list of PEP-508-compliant req strings
    """
    return [line.strip() for line in read_file(filename).splitlines() if not line.startswith('#')]

REQUIREMENTS = read_requirements('requirements.txt')

setup_kwargs = {
    'name': PROJECT,
    'version': "1.0",
    'packages': find_packages(SRC_DIR),
    'package_dir': {"": SRC_DIR},
    'package_data': {'': ['*']},
    'install_requires': REQUIREMENTS,
    'python_requires': '>=3.8',
    'zip_safe': False,
}


if __name__ == '__main__':
    setup(**setup_kwargs)
