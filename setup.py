from glob import glob
import os
from os.path import join as pjoin
from setuptools import setup, find_packages

HERE = os.path.dirname(os.path.abspath(__file__))

setup_args = dict(
    name='stl-viewer-widget',
    description='A jupyter notebook widget for STL model visualization',
    version='0.1.0',

    packages=['stl_viewer'],
    author='xloc',
    author_email='xloc.cc@outlook.com',
    url='https://github.com/xloc/stl-viewer-widget',
    install_requires=[
        'ipywidgets>=7.0.0',
    ],
)

if __name__ == '__main__':
    setup(**setup_args)
