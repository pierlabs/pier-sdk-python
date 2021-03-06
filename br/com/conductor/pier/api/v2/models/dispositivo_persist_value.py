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


class DispositivoPersistValue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DispositivoPersistValue - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'token': 'str',
            'id_aplicacao_mobile': 'int',
            'id_usuario': 'int'
        }

        self.attribute_map = {
            'token': 'token',
            'id_aplicacao_mobile': 'idAplicacaoMobile',
            'id_usuario': 'idUsuario'
        }

        self._token = None
        self._id_aplicacao_mobile = None
        self._id_usuario = None

    @property
    def token(self):
        """
        Gets the token of this DispositivoPersistValue.
        {{{dispositivo_persist_token_value}}}

        :return: The token of this DispositivoPersistValue.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this DispositivoPersistValue.
        {{{dispositivo_persist_token_value}}}

        :param token: The token of this DispositivoPersistValue.
        :type: str
        """
        self._token = token

    @property
    def id_aplicacao_mobile(self):
        """
        Gets the id_aplicacao_mobile of this DispositivoPersistValue.
        {{{dispositivo_persist_id_aplicacao_mobile_value}}}

        :return: The id_aplicacao_mobile of this DispositivoPersistValue.
        :rtype: int
        """
        return self._id_aplicacao_mobile

    @id_aplicacao_mobile.setter
    def id_aplicacao_mobile(self, id_aplicacao_mobile):
        """
        Sets the id_aplicacao_mobile of this DispositivoPersistValue.
        {{{dispositivo_persist_id_aplicacao_mobile_value}}}

        :param id_aplicacao_mobile: The id_aplicacao_mobile of this DispositivoPersistValue.
        :type: int
        """
        self._id_aplicacao_mobile = id_aplicacao_mobile

    @property
    def id_usuario(self):
        """
        Gets the id_usuario of this DispositivoPersistValue.
        {{{dispositivo_persist_id_usuario_value}}}

        :return: The id_usuario of this DispositivoPersistValue.
        :rtype: int
        """
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        """
        Sets the id_usuario of this DispositivoPersistValue.
        {{{dispositivo_persist_id_usuario_value}}}

        :param id_usuario: The id_usuario of this DispositivoPersistValue.
        :type: int
        """
        self._id_usuario = id_usuario

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

