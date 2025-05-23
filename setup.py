#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

from insilicoseq_marbeldep.version import __version__

url = "https://github.com/jlab/InSilicoSeq"

with open("README.md") as f:
    long_description = f.read()

setup(
    name="insilicoseq_marbeldep",
    version=__version__,
    description="a sequencing simulator adjusted for marbel project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    download_url=url + "/tarball/" + __version__,
    author="Hadrien Gourlé, Timo Wentong Lin",
    author_email="hadrien.gourle@slu.se, timo.lin@uni-giessen.de",
    license="MIT",
    packages=find_packages(),
    tests_require=["pytest"],
    install_requires=["numpy", "scipy", "biopython>=1.79", "pysam>=0.15.1", "requests"],
    include_package_data=True,
)
