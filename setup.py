#! /usr/bin/env python
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

if __name__ == "__main__":
    setup(
        name="pubmed_parser",
        version="0.4.0",
        description="A python parser for Pubmed Open-Access Subset and MEDLINE XML repository",
        long_description=long_description,
        long_description_content_type='text/markdown',
        url="https://github.com/titipata/pubmed_parser",
        download_url="https://github.com/titipata/pubmed_parser.git",
        author="Titipat Achakulvisut",
        author_email="my.titipat@gmail.com",
        license="MIT (c) 2015 - 2019 Titipat Achakulvisut, Daniel E. Acuna",
        install_requires=[
            "lxml",
            "unidecode",
            "requests",
            "six",
            "numpy",
            "pytest",
            "pytest-cov",
        ],
        packages=["pubmed_parser"],
        package_data={"pubmed_parser.data": ["*.xml.gz", "*.nxml", "*.txt"],},
        keywords=[
            'Python',
            'MEDLINE',
            'PubMed',
            'Biomedical corpus',
            'Natural Language Processing'
        ],
        classifiers=[
            "Intended Audience :: Science/Research",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python",
            "Topic :: Software Development",
            "Topic :: Scientific/Engineering",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: Unix",
            "Operating System :: MacOS",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
        platforms="any",
        project_urls={
            "Source": "https://github.com/titipata/pubmed_parser",
            "Documentation": "http://titipata.github.io/pubmed_parser",
            "Bug Reports": "https://github.com/titipata/pubmed_parser/issues",
        },
    )
