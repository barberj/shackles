#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import shackles

setup(
    name='shackles',
    version='1.0',
    description='Recursive attribute tools.',
    long_description=open('README.rst').read(),
    author='Justin Barber',
    author_email='barber.justin@gmail.com',
    url='https://github.com/barberj/shackles',
    py_modules=["shackles"],
    classifiers=(
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
    ),
)
