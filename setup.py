#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


setup(
    name="playwright automation",
    version="1.0.0",
    author="Prashant Kumar Tiwari",
    author_email="prashant.0542@gmail.com",
    license="MIT",
    url="",
    description="Learning the playwright (python) automation tetsing tool",
    long_description=read("README.rst"),
    keywords=[],
    packages=find_packages(),
    python_requires=">=3.5",
    install_requires=["pytest", "pytest-playwright"],
    classifiers=[
        "Framework :: Playwright",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ]
)
