#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='sentry-runner',
    version='0.1.0',
    description='Run arbitrary script within Sentry environment',
    author='Kohei Suzuki',
    author_email='eagletmt@gmail.com',
    url='https://github.com/eagletmt/sentry-runner',
    packages=find_packages(),
    license='MIT',
    install_requires=[
        'sentry',
    ],
)
