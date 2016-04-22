# coding: utf-8

"""
Copyright 2015 SmartBear Software

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


class CancelarCartaoResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CancelarCartaoResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'codigo_retorno': 'int',
            'descricao_retorno': 'str',
            'id_cartao': 'int',
            'id_conta': 'int'
        }

        self.attribute_map = {
            'codigo_retorno': 'codigoRetorno',
            'descricao_retorno': 'descricaoRetorno',
            'id_cartao': 'idCartao',
            'id_conta': 'idConta'
        }

        self._codigo_retorno = None
        self._descricao_retorno = None
        self._id_cartao = None
        self._id_conta = None

    @property
    def codigo_retorno(self):
        """
        Gets the codigo_retorno of this CancelarCartaoResponse.


        :return: The codigo_retorno of this CancelarCartaoResponse.
        :rtype: int
        """
        return self._codigo_retorno

    @codigo_retorno.setter
    def codigo_retorno(self, codigo_retorno):
        """
        Sets the codigo_retorno of this CancelarCartaoResponse.


        :param codigo_retorno: The codigo_retorno of this CancelarCartaoResponse.
        :type: int
        """
        self._codigo_retorno = codigo_retorno

    @property
    def descricao_retorno(self):
        """
        Gets the descricao_retorno of this CancelarCartaoResponse.


        :return: The descricao_retorno of this CancelarCartaoResponse.
        :rtype: str
        """
        return self._descricao_retorno

    @descricao_retorno.setter
    def descricao_retorno(self, descricao_retorno):
        """
        Sets the descricao_retorno of this CancelarCartaoResponse.


        :param descricao_retorno: The descricao_retorno of this CancelarCartaoResponse.
        :type: str
        """
        self._descricao_retorno = descricao_retorno

    @property
    def id_cartao(self):
        """
        Gets the id_cartao of this CancelarCartaoResponse.


        :return: The id_cartao of this CancelarCartaoResponse.
        :rtype: int
        """
        return self._id_cartao

    @id_cartao.setter
    def id_cartao(self, id_cartao):
        """
        Sets the id_cartao of this CancelarCartaoResponse.


        :param id_cartao: The id_cartao of this CancelarCartaoResponse.
        :type: int
        """
        self._id_cartao = id_cartao

    @property
    def id_conta(self):
        """
        Gets the id_conta of this CancelarCartaoResponse.


        :return: The id_conta of this CancelarCartaoResponse.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this CancelarCartaoResponse.


        :param id_conta: The id_conta of this CancelarCartaoResponse.
        :type: int
        """
        self._id_conta = id_conta

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

