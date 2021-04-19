#!/usr/bin/env python
from setuptools import setup, find_packages

version = "1.0.2"

with open("./README.rst", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="Yolo2Voc",
    version=version,
    author = "Willian Antunes",
    author_email = "wiliam-m-@hotmail.com",
    url="https://github.com/BrWillian/Yolo2Voc/",
    project_urls={
        "Documentation": "https://yolo2voc.readthedocs.io/",
    },
    license = "MIT",
    description="Yolo Annotation to PascalVOC annotation.",
    long_description=readme,
    python_requires=">=3.6",
    packages=find_packages(exclude=["tests*", "yolo2voc.tests*"])),
    install_requires=[
        'Pillow',
        'lxml',
        'tqdm',
        'defusedxml'
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="Yolo2Voc Yolo PascalVOC",
)