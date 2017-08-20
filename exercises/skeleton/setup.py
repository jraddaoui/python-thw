try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Base project',
    'author': 'José Raddaoui Marín',
    'url': '',
    'download_url': '',
    'author_email': 'raddaouimarin@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': ['bin/script.py'],
    'name': 'base-project'
}

setup(**config)
