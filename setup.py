from setuptools import setup, find_packages

setup(
name="confac",
version="1.0.0",
author="ROAM Lab",
description="Tool for assembling class objects using factory pattern",
url="https://github.com/roamlab/confac/",
packages=[package for package in find_packages()
                if package.startswith('confac')],
install_requires = [
    'configparser',
   ]
)
