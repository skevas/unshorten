#!/usr/bin/env python

from distutils.core import setup

setup(name='isurlshortener',
      version='0.1.6',
      description='Provides information if a given url is from an url shortener service',
      author='Raphael Ernst',
      author_email='github@matinale.de',
      packages=['isurlshortener'],
      data_files=[('isurlshortener', ['isurlshortener/data/shortener_services.txt',
                                      'isurlshortener/data/former_shortener_services.txt'])],
      license='MIT')
