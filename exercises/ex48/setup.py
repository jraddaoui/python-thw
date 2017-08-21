try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Exercise 48',
    'author': 'José Raddaoui Marín',
    'url': '',
    'download_url': '',
    'author_email': 'raddaouimarin@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['lexicon'],
    'scripts': [],
    'name': 'ex48'
}

setup(**config)
