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


class TransferenciaCreditoContaBancariaPersistValue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TransferenciaCreditoContaBancariaPersistValue - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'nsu_origem': 'int',
            'id_cartao': 'int',
            'id_conta_bancaria': 'int',
            'valor': 'float',
            'numero_parcelas': 'int',
            'numero_meses_carencia': 'int',
            'data_hora_terminal': 'str',
            'terminal_requisitante': 'str',
            'numero_estabelecimento': 'str'
        }

        self.attribute_map = {
            'nsu_origem': 'nsuOrigem',
            'id_cartao': 'idCartao',
            'id_conta_bancaria': 'idContaBancaria',
            'valor': 'valor',
            'numero_parcelas': 'numeroParcelas',
            'numero_meses_carencia': 'numeroMesesCarencia',
            'data_hora_terminal': 'dataHoraTerminal',
            'terminal_requisitante': 'terminalRequisitante',
            'numero_estabelecimento': 'numeroEstabelecimento'
        }

        self._nsu_origem = None
        self._id_cartao = None
        self._id_conta_bancaria = None
        self._valor = None
        self._numero_parcelas = None
        self._numero_meses_carencia = None
        self._data_hora_terminal = None
        self._terminal_requisitante = None
        self._numero_estabelecimento = None

    @property
    def nsu_origem(self):
        """
        Gets the nsu_origem of this TransferenciaCreditoContaBancariaPersistValue.
        {{{transferencia_credito_conta_bancaria_persist_nsu_origem_value}}}

        :return: The nsu_origem of this TransferenciaCreditoContaBancariaPersistValue.
        :rtype: int
        """
        return self._nsu_origem

    @nsu_origem.setter
    def nsu_origem(self, nsu_origem):
        """
        Sets the nsu_origem of this TransferenciaCreditoContaBancariaPersistValue.
        {{{transferencia_credito_conta_bancaria_persist_nsu_origem_value}}}

        :param nsu_origem: The nsu_origem of this TransferenciaCreditoContaBancariaPersistValue.
        :type: int
        """
        self._nsu_origem = nsu_origem

    @property
    def id_cartao(self):
        """
        Gets the id_cartao of this TransferenciaCreditoContaBancariaPersistValue.
        {{{transferencia_credito_conta_bancaria_persist_id_cartao_value}}}

        :return: The id_cartao of this TransferenciaCreditoContaBancariaPersistValue.
        :rtype: int
        """
        return self._id_cartao

    @id_cartao.setter
    def id_cartao(self, id_cartao):
        """
        Sets the id_cartao of this TransferenciaCreditoContaBancariaPersistValue.
        {{{transferencia_credito_conta_bancaria_persist_id_cartao_value}}}

        :param id_cartao: The id_cartao of this TransferenciaCreditoContaBancariaPersistValue.
        :type: int
        """
        self._id_cartao = id_cartao

    @property
    def id_conta_bancaria(self):
        """
        Gets the id_conta_bancaria of this TransferenciaCreditoContaBancariaPersistValue.
        {{{transferencia_credito_conta_bancaria_persist_id_conta_bancaria_value}}}

        :return: The id_conta_bancaria of this TransferenciaCreditoContaBancariaPersistValue.
        :rtype: int
        """
        return self._id_conta_bancaria

    @id_conta_bancaria.setter
    def id_conta_bancaria(self, id_conta_bancaria):
        """
        Sets the id_conta_bancaria of this TransferenciaCreditoContaBancariaPersistValue.
        {{{transferencia_credito_conta_bancaria_persist_id_conta_bancaria_value}}}

        :param id_conta_bancaria: The id_conta_bancaria of this TransferenciaCreditoContaBancariaPersistValue.
        :type: int
        """
        self._id_conta_bancaria = id_conta_bancaria

    @property
    def valor(self):
        """
        Gets the valor of this TransferenciaCreditoContaBancariaPersistValue.
        {{{transferencia_credito_conta_bancaria_persist_valor_value}}}

        :return: The valor of this TransferenciaCreditoContaBancariaPersistValue.
        :rtype: float
        """
        return self._valor

    @valor.setter
    def valor(self, valor):
        """
        Sets the valor of this TransferenciaCreditoContaBancariaPersistValue.
        {{{transferencia_credito_conta_bancaria_persist_valor_value}}}

        :param valor: The valor of this TransferenciaCreditoContaBancariaPersistValue.
        :type: float
        """
        self._valor = valor

    @property
    def numero_parcelas(self):
        """
        Gets the numero_parcelas of this TransferenciaCreditoContaBancariaPersistValue.
        {{{transferencia_credito_conta_bancaria_persist_numero_parcelas_value}}}

        :return: The numero_parcelas of this TransferenciaCreditoContaBancariaPersistValue.
        :rtype: int
        """
        return self._numero_parcelas

    @numero_parcelas.setter
    def numero_parcelas(self, numero_parcelas):
        """
        Sets the numero_parcelas of this TransferenciaCreditoContaBancariaPersistValue.
        {{{transferencia_credito_conta_bancaria_persist_numero_parcelas_value}}}

        :param numero_parcelas: The numero_parcelas of this TransferenciaCreditoContaBancariaPersistValue.
        :type: int
        """
        self._numero_parcelas = numero_parcelas

    @property
    def numero_meses_carencia(self):
        """
        Gets the numero_meses_carencia of this TransferenciaCreditoContaBancariaPersistValue.
        {{{transferencia_credito_conta_bancaria_persist_numero_meses_carencia_value}}}

        :return: The numero_meses_carencia of this TransferenciaCreditoContaBancariaPersistValue.
        :rtype: int
        """
        return self._numero_meses_carencia

    @numero_meses_carencia.setter
    def numero_meses_carencia(self, numero_meses_carencia):
        """
        Sets the numero_meses_carencia of this TransferenciaCreditoContaBancariaPersistValue.
        {{{transferencia_credito_conta_bancaria_persist_numero_meses_carencia_value}}}

        :param numero_meses_carencia: The numero_meses_carencia of this TransferenciaCreditoContaBancariaPersistValue.
        :type: int
        """
        self._numero_meses_carencia = numero_meses_carencia

    @property
    def data_hora_terminal(self):
        """
        Gets the data_hora_terminal of this TransferenciaCreditoContaBancariaPersistValue.
        {{{transferencia_credito_conta_bancaria_persist_data_hora_terminal_value}}}

        :return: The data_hora_terminal of this TransferenciaCreditoContaBancariaPersistValue.
        :rtype: str
        """
        return self._data_hora_terminal

    @data_hora_terminal.setter
    def data_hora_terminal(self, data_hora_terminal):
        """
        Sets the data_hora_terminal of this TransferenciaCreditoContaBancariaPersistValue.
        {{{transferencia_credito_conta_bancaria_persist_data_hora_terminal_value}}}

        :param data_hora_terminal: The data_hora_terminal of this TransferenciaCreditoContaBancariaPersistValue.
        :type: str
        """
        self._data_hora_terminal = data_hora_terminal

    @property
    def terminal_requisitante(self):
        """
        Gets the terminal_requisitante of this TransferenciaCreditoContaBancariaPersistValue.
        {{{transferencia_credito_conta_bancaria_persist_terminal_requisitante_value}}}

        :return: The terminal_requisitante of this TransferenciaCreditoContaBancariaPersistValue.
        :rtype: str
        """
        return self._terminal_requisitante

    @terminal_requisitante.setter
    def terminal_requisitante(self, terminal_requisitante):
        """
        Sets the terminal_requisitante of this TransferenciaCreditoContaBancariaPersistValue.
        {{{transferencia_credito_conta_bancaria_persist_terminal_requisitante_value}}}

        :param terminal_requisitante: The terminal_requisitante of this TransferenciaCreditoContaBancariaPersistValue.
        :type: str
        """
        self._terminal_requisitante = terminal_requisitante

    @property
    def numero_estabelecimento(self):
        """
        Gets the numero_estabelecimento of this TransferenciaCreditoContaBancariaPersistValue.
        {{{transferencia_credito_conta_bancaria_persist_numero_estabelecimento_value}}}

        :return: The numero_estabelecimento of this TransferenciaCreditoContaBancariaPersistValue.
        :rtype: str
        """
        return self._numero_estabelecimento

    @numero_estabelecimento.setter
    def numero_estabelecimento(self, numero_estabelecimento):
        """
        Sets the numero_estabelecimento of this TransferenciaCreditoContaBancariaPersistValue.
        {{{transferencia_credito_conta_bancaria_persist_numero_estabelecimento_value}}}

        :param numero_estabelecimento: The numero_estabelecimento of this TransferenciaCreditoContaBancariaPersistValue.
        :type: str
        """
        self._numero_estabelecimento = numero_estabelecimento

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

