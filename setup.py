# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pandas_query_builder',
    version='0.0.1',
    description='pandas dataframe wrap',
    long_description=readme,
    author='@sakuV2',
    author_email='hoge',
    url='https://github.com/sakuv2/pandas_query_builder',
    license=license,
    install_requires=['pandas'],
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)

