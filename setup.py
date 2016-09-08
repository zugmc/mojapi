from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='UTF-8') as f:
    long_description = f.read()

setup(
    name='mojapi',
    version='0.0.1',
    url='https://github.com/zugmc/mojapi/',
    author='gozug',
    author_email='gozug@zugmc.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    description='Python library for interacting with Mojang APIs',
    long_description=long_description,
    packages=find_packages(),
    keywords=' '.join([
        'minecraft',
        'mojang',
        'api'
    ]),
    install_requires=[
        'requests>=2.11.1'
    ]
)
