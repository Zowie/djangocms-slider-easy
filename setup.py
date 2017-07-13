#!/usr/bin/env python
import os

import djangocms_slider_uploadcare

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = djangocms_slider_uploadcare.__version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


INSTALL_REQUIRES = [
    "django>=1.8.0, <1.11",
    "django-cms>=3.0",
    "pyuploadcare==2.2.1",
]

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Framework :: Django',
    'Framework :: Django :: 1.8',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Natural Language :: English',
    'Natural Language :: Dutch',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]

setup(
    name="djangocms-slider-easy-uploadcare",
    version=version,
    author="Luminum Solutions",
    author_email="zowie@akoten.com",
    description="A slider plugin for djangocms that lets you arrange slides like any other djangocms plugin. Fork of urga/djangocms-slider, but using uploadcare.",
    license="BSD",
    keywords=["slideshow", "django", "cms", "plugin", "uploadcare", "flexslider", "jquery"],
    url="https://github.com/Zowie/djangocms-slider-easy-uploadcare",
    packages=['djangocms_slider_uploadcare'],
    install_requires=INSTALL_REQUIRES,
    classifiers=CLASSIFIERS,
    long_description=read('README.md'),
    include_package_data=True,
    zip_safe=False
)
