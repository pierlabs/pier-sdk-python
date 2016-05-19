# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "br.com.conductor.pier"
VERSION = "1.0.0"



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
    description="CaaS - Conductor as a Service",
    author_email="contato@conductor.com.br",
    url="http://www.conductor.com.br",
    keywords=["Swagger", "CaaS - Conductor as a Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Gest\u00C3\u00A3o de pagamento eletr\u00C3\u00B4nicos como servi\u00C3\u00A7o
    """
)


