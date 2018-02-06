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


class ArquivoPersist(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ArquivoPersist - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_tipo_arquivo': 'int',
            'arquivo': 'str',
            'nome': 'str',
            'extensao': 'str',
            'tipo_comunicacao': 'str',
            'detalhes': 'list[ArquivoDetalhesPersist]'
        }

        self.attribute_map = {
            'id_tipo_arquivo': 'idTipoArquivo',
            'arquivo': 'arquivo',
            'nome': 'nome',
            'extensao': 'extensao',
            'tipo_comunicacao': 'tipoComunicacao',
            'detalhes': 'detalhes'
        }

        self._id_tipo_arquivo = None
        self._arquivo = None
        self._nome = None
        self._extensao = None
        self._tipo_comunicacao = None
        self._detalhes = None

    @property
    def id_tipo_arquivo(self):
        """
        Gets the id_tipo_arquivo of this ArquivoPersist.
        Tipo do arquivo

        :return: The id_tipo_arquivo of this ArquivoPersist.
        :rtype: int
        """
        return self._id_tipo_arquivo

    @id_tipo_arquivo.setter
    def id_tipo_arquivo(self, id_tipo_arquivo):
        """
        Sets the id_tipo_arquivo of this ArquivoPersist.
        Tipo do arquivo

        :param id_tipo_arquivo: The id_tipo_arquivo of this ArquivoPersist.
        :type: int
        """
        self._id_tipo_arquivo = id_tipo_arquivo

    @property
    def arquivo(self):
        """
        Gets the arquivo of this ArquivoPersist.
        Conte\u00C3\u00BAdo do arquivo convertido em Base 64

        :return: The arquivo of this ArquivoPersist.
        :rtype: str
        """
        return self._arquivo

    @arquivo.setter
    def arquivo(self, arquivo):
        """
        Sets the arquivo of this ArquivoPersist.
        Conte\u00C3\u00BAdo do arquivo convertido em Base 64

        :param arquivo: The arquivo of this ArquivoPersist.
        :type: str
        """
        self._arquivo = arquivo

    @property
    def nome(self):
        """
        Gets the nome of this ArquivoPersist.
        Nome do arquivo.

        :return: The nome of this ArquivoPersist.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Sets the nome of this ArquivoPersist.
        Nome do arquivo.

        :param nome: The nome of this ArquivoPersist.
        :type: str
        """
        self._nome = nome

    @property
    def extensao(self):
        """
        Gets the extensao of this ArquivoPersist.
        Formato/extens\u00C3\u00A3o do arquivo.

        :return: The extensao of this ArquivoPersist.
        :rtype: str
        """
        return self._extensao

    @extensao.setter
    def extensao(self, extensao):
        """
        Sets the extensao of this ArquivoPersist.
        Formato/extens\u00C3\u00A3o do arquivo.

        :param extensao: The extensao of this ArquivoPersist.
        :type: str
        """
        self._extensao = extensao

    @property
    def tipo_comunicacao(self):
        """
        Gets the tipo_comunicacao of this ArquivoPersist.
        Tipo de comunica\u00C3\u00A7\u00C3\u00A3o.

        :return: The tipo_comunicacao of this ArquivoPersist.
        :rtype: str
        """
        return self._tipo_comunicacao

    @tipo_comunicacao.setter
    def tipo_comunicacao(self, tipo_comunicacao):
        """
        Sets the tipo_comunicacao of this ArquivoPersist.
        Tipo de comunica\u00C3\u00A7\u00C3\u00A3o.

        :param tipo_comunicacao: The tipo_comunicacao of this ArquivoPersist.
        :type: str
        """
        allowed_values = ["SOAP", "REST"]
        if tipo_comunicacao not in allowed_values:
            raise ValueError(
                "Invalid value for `tipo_comunicacao`, must be one of {0}"
                .format(allowed_values)
            )
        self._tipo_comunicacao = tipo_comunicacao

    @property
    def detalhes(self):
        """
        Gets the detalhes of this ArquivoPersist.
        Detalhes contendo informa\u00C3\u00A7\u00C3\u00B5es adicionais, relacionadas ao arquivo

        :return: The detalhes of this ArquivoPersist.
        :rtype: list[ArquivoDetalhesPersist]
        """
        return self._detalhes

    @detalhes.setter
    def detalhes(self, detalhes):
        """
        Sets the detalhes of this ArquivoPersist.
        Detalhes contendo informa\u00C3\u00A7\u00C3\u00B5es adicionais, relacionadas ao arquivo

        :param detalhes: The detalhes of this ArquivoPersist.
        :type: list[ArquivoDetalhesPersist]
        """
        self._detalhes = detalhes

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

