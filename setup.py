#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-runner',
    version='0.1.0',
    description='Run arbitrary script within Django environment',
    author='Kohei Suzuki',
    author_email='eagletmt@gmail.com',
    url='https://github.com/eagletmt/django-runner',
    packages=find_packages(),
    license='MIT',
    install_requires=[
        'django',
    ],
)
