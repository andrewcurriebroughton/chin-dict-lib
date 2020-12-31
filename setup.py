from setuptools import find_packages, setup
import re


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('chin_dict/chin_dict.py').read(),
    re.M
    ).group(1)
 
# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
 
setup(
    name="chin-dict",
    packages=find_packages(exclude=("tests")),
    entry_points = {
        "console_scripts": ['chindict = chin_dict.chin_dict:main']
        },
    version=version,
    description="Mandarin dictionary",
    author="Me",
    license="MIT",
    install_requires=[
        "SQLAlchemy==1.3.22",
        "treelib==1.6.1"
    ],
    data_files=[('data', ['chin_dict/hanlearn.db'])],
    long_description=long_description,
    long_description_content_type='text/markdown'
)