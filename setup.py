#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='disbloom',
      version='0.1',
      description="Python bloom filter using redis as a shared backend",
      author="Guillaume Duhamel",
      author_email="guillaume.duhamel@gmail.com",
      url="https://github.com/Guillaumito/bloomfilter-redis",
      packages = find_packages(),
      zip_safe = True,
      test_suite="tests")
