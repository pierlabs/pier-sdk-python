# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "br.com.conductor.pier.api.v2"
VERSION = "2.74.2"



# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.10", "six >= 1.9", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="PIER Labs",
    author_email="pierlabs@conductor.com.br",
    url="http://pierlabs.io",
    keywords=["Swagger", "PIER Labs"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Gest\u00E3o de pagamento eletr\u00F4nicos como servi\u00E7o
    """
)


