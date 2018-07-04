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


class MaquinetaPersist(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MaquinetaPersist - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_terminal': 'int',
            'id_tipo_maquineta': 'int',
            'valor': 'float',
            'data_hora_implantacao': 'str'
        }

        self.attribute_map = {
            'id_terminal': 'idTerminal',
            'id_tipo_maquineta': 'idTipoMaquineta',
            'valor': 'valor',
            'data_hora_implantacao': 'dataHoraImplantacao'
        }

        self._id_terminal = None
        self._id_tipo_maquineta = None
        self._valor = None
        self._data_hora_implantacao = None

    @property
    def id_terminal(self):
        """
        Gets the id_terminal of this MaquinetaPersist.
        {{{maquineta_persist_id_terminal_value}}}

        :return: The id_terminal of this MaquinetaPersist.
        :rtype: int
        """
        return self._id_terminal

    @id_terminal.setter
    def id_terminal(self, id_terminal):
        """
        Sets the id_terminal of this MaquinetaPersist.
        {{{maquineta_persist_id_terminal_value}}}

        :param id_terminal: The id_terminal of this MaquinetaPersist.
        :type: int
        """
        self._id_terminal = id_terminal

    @property
    def id_tipo_maquineta(self):
        """
        Gets the id_tipo_maquineta of this MaquinetaPersist.
        {{{maquineta_persist_id_tipo_maquineta_value}}}

        :return: The id_tipo_maquineta of this MaquinetaPersist.
        :rtype: int
        """
        return self._id_tipo_maquineta

    @id_tipo_maquineta.setter
    def id_tipo_maquineta(self, id_tipo_maquineta):
        """
        Sets the id_tipo_maquineta of this MaquinetaPersist.
        {{{maquineta_persist_id_tipo_maquineta_value}}}

        :param id_tipo_maquineta: The id_tipo_maquineta of this MaquinetaPersist.
        :type: int
        """
        self._id_tipo_maquineta = id_tipo_maquineta

    @property
    def valor(self):
        """
        Gets the valor of this MaquinetaPersist.
        {{{maquineta_persist_valor_value}}}

        :return: The valor of this MaquinetaPersist.
        :rtype: float
        """
        return self._valor

    @valor.setter
    def valor(self, valor):
        """
        Sets the valor of this MaquinetaPersist.
        {{{maquineta_persist_valor_value}}}

        :param valor: The valor of this MaquinetaPersist.
        :type: float
        """
        self._valor = valor

    @property
    def data_hora_implantacao(self):
        """
        Gets the data_hora_implantacao of this MaquinetaPersist.
        {{{maquineta_persist_data_hora_implantacao_value}}}

        :return: The data_hora_implantacao of this MaquinetaPersist.
        :rtype: str
        """
        return self._data_hora_implantacao

    @data_hora_implantacao.setter
    def data_hora_implantacao(self, data_hora_implantacao):
        """
        Sets the data_hora_implantacao of this MaquinetaPersist.
        {{{maquineta_persist_data_hora_implantacao_value}}}

        :param data_hora_implantacao: The data_hora_implantacao of this MaquinetaPersist.
        :type: str
        """
        self._data_hora_implantacao = data_hora_implantacao

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

