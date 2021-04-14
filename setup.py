"""Sets up the package"""

#!/usr/bin/env python
 # -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

with open('LICENSE.md') as f:
    LICENSE = f.read()

setup(
    name='DjangoFinanceApi',
    version='0.1.0',
    description='An api based on the django template provided by General Assembly',
    long_description=README,
    author='Matt Moore',
    author_email='Matt.M.Moore13@outlook.com',
    url='https://github.com/mmmoore1313/DjangoFinanceApi',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs'))
)
