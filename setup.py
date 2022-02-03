# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['betainc']

package_data = \
{'': ['*']}

install_requires = \
['Cython>=0.29.27,<0.30.0', 'numpy>=1.22.1,<2.0.0']

setup_kwargs = {
    'name': 'betainc',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'catethos',
    'author_email': 'cloverethos@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
