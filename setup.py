#!/usr/bin/env python3

import os

import setuptools

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'noob/version.py'), encoding='utf-8') as fp:
    exec(fp.read())
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as fp:
    long_description = fp.read()

setuptools.setup(
    name='homebrew-npm-noob',
    version=__version__,
    description='Generate Homebrew formulae for npm packages',
    long_description=long_description,
    url='https://github.com/zmwangx/homebrew-npm-noob',
    author='Zhiming Wang',
    author_email='zmwangx@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Code Generators',
    ],
    keywords='homebrew formula node npm',
    packages=['noob'],
    install_requires=['jinja2', 'requests'],
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'noob=noob.__main__:main',
        ]
    },
)
