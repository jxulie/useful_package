# encoding: utf-8

from distutils.core import setup
import setuptools
setup(
    name='jxulie_package',
    description='A set of python package.',
    version='0.2',
    author='Xu Bo',
    author_email='bolang1988@gmail.com',
    url='http://github.com/jxulie',
    
    packages= setuptools.find_packages(exclude=["tests.*", "tests"]),
)
