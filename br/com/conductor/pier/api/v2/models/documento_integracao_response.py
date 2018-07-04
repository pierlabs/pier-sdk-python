# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class DocumentoIntegracaoResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DocumentoIntegracaoResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_template': 'int',
            'nome': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'id_template': 'idTemplate',
            'nome': 'nome'
        }

        self._id = None
        self._id_template = None
        self._nome = None

    @property
    def id(self):
        """
        Gets the id of this DocumentoIntegracaoResponse.
        {{{documento_integracao_response_id_value}}}

        :return: The id of this DocumentoIntegracaoResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DocumentoIntegracaoResponse.
        {{{documento_integracao_response_id_value}}}

        :param id: The id of this DocumentoIntegracaoResponse.
        :type: int
        """
        self._id = id

    @property
    def id_template(self):
        """
        Gets the id_template of this DocumentoIntegracaoResponse.
        {{{documento_integracao_response_id_template_value}}}

        :return: The id_template of this DocumentoIntegracaoResponse.
        :rtype: int
        """
        return self._id_template

    @id_template.setter
    def id_template(self, id_template):
        """
        Sets the id_template of this DocumentoIntegracaoResponse.
        {{{documento_integracao_response_id_template_value}}}

        :param id_template: The id_template of this DocumentoIntegracaoResponse.
        :type: int
        """
        self._id_template = id_template

    @property
    def nome(self):
        """
        Gets the nome of this DocumentoIntegracaoResponse.
        {{{documento_integracao_response_nome_value}}}

        :return: The nome of this DocumentoIntegracaoResponse.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Sets the nome of this DocumentoIntegracaoResponse.
        {{{documento_integracao_response_nome_value}}}

        :param nome: The nome of this DocumentoIntegracaoResponse.
        :type: str
        """
        self._nome = nome

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

