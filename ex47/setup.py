try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'exercise 47 from LPTHW',
    'author': 'Arshad Khan',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'arshdkhn1@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['e47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)

