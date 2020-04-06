# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", 'r') as fr:
	description = fr.read()

setup(
    name='pynerator',
    version='1.0.0',
    url='https://github.com/jeffrichardchemistry/pynerator',
    license='GNU General Public License v3.0',
    author='Jefferson Richard',
    author_email='jrichardquimica@gmail.com',
    keywords='Password random generate GUI',
    description='A GUI for generate random passwords',
	long_description = description,
	long_description_content_type = "text/markdown",
    packages=['pynerator'],
    install_requires=['PyQt5==5.10'],
	classifiers = [
		'Environment :: X11 Applications :: Qt',
		'Intended Audience :: Developers',
		'Intended Audience :: End Users/Desktop',
		'Intended Audience :: Science/Research',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Natural Language :: English',
		'Operating System :: POSIX :: Linux',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: MacOS',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3']
)
