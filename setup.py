# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "br.com.conductor.caas"
VERSION = "0.0.1"



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
    GestÃ£o de pagamento eletrÃ´nicos como serviÃ§o
    """
)


