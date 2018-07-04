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


class TransacaoPaySecureRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TransacaoPaySecureRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'data_hora_transacao': 'str',
            'numero_cartao': 'str',
            'id_cartao': 'int',
            'valor': 'float',
            'nsu_origem': 'str',
            'nome_portador_cartao': 'str',
            'origem': 'str',
            'terminal_requisitante': 'str',
            'codigo_processamento': 'str',
            'data_validade_cartao': 'str',
            'numero_estabelecimento': 'str',
            'numero_parcelas': 'int',
            'codigo_seguranca_cartao': 'str',
            'sort': 'list[str]'
        }

        self.attribute_map = {
            'data_hora_transacao': 'dataHoraTransacao',
            'numero_cartao': 'numeroCartao',
            'id_cartao': 'idCartao',
            'valor': 'valor',
            'nsu_origem': 'nsuOrigem',
            'nome_portador_cartao': 'nomePortadorCartao',
            'origem': 'origem',
            'terminal_requisitante': 'terminalRequisitante',
            'codigo_processamento': 'codigoProcessamento',
            'data_validade_cartao': 'dataValidadeCartao',
            'numero_estabelecimento': 'numeroEstabelecimento',
            'numero_parcelas': 'numeroParcelas',
            'codigo_seguranca_cartao': 'codigoSegurancaCartao',
            'sort': 'sort'
        }

        self._data_hora_transacao = None
        self._numero_cartao = None
        self._id_cartao = None
        self._valor = None
        self._nsu_origem = None
        self._nome_portador_cartao = None
        self._origem = None
        self._terminal_requisitante = None
        self._codigo_processamento = None
        self._data_validade_cartao = None
        self._numero_estabelecimento = None
        self._numero_parcelas = None
        self._codigo_seguranca_cartao = None
        self._sort = None

    @property
    def data_hora_transacao(self):
        """
        Gets the data_hora_transacao of this TransacaoPaySecureRequest.
        {{{transacao_pay_secure_request_data_hora_transacao_value}}}

        :return: The data_hora_transacao of this TransacaoPaySecureRequest.
        :rtype: str
        """
        return self._data_hora_transacao

    @data_hora_transacao.setter
    def data_hora_transacao(self, data_hora_transacao):
        """
        Sets the data_hora_transacao of this TransacaoPaySecureRequest.
        {{{transacao_pay_secure_request_data_hora_transacao_value}}}

        :param data_hora_transacao: The data_hora_transacao of this TransacaoPaySecureRequest.
        :type: str
        """
        self._data_hora_transacao = data_hora_transacao

    @property
    def numero_cartao(self):
        """
        Gets the numero_cartao of this TransacaoPaySecureRequest.
        {{{transacao_pay_generic_request_numero_cartao_value}}}

        :return: The numero_cartao of this TransacaoPaySecureRequest.
        :rtype: str
        """
        return self._numero_cartao

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao):
        """
        Sets the numero_cartao of this TransacaoPaySecureRequest.
        {{{transacao_pay_generic_request_numero_cartao_value}}}

        :param numero_cartao: The numero_cartao of this TransacaoPaySecureRequest.
        :type: str
        """
        self._numero_cartao = numero_cartao

    @property
    def id_cartao(self):
        """
        Gets the id_cartao of this TransacaoPaySecureRequest.
        {{{transacao_pay_generic_request_id_cartao_value}}}

        :return: The id_cartao of this TransacaoPaySecureRequest.
        :rtype: int
        """
        return self._id_cartao

    @id_cartao.setter
    def id_cartao(self, id_cartao):
        """
        Sets the id_cartao of this TransacaoPaySecureRequest.
        {{{transacao_pay_generic_request_id_cartao_value}}}

        :param id_cartao: The id_cartao of this TransacaoPaySecureRequest.
        :type: int
        """
        self._id_cartao = id_cartao

    @property
    def valor(self):
        """
        Gets the valor of this TransacaoPaySecureRequest.
        {{{transacao_pay_secure_request_valor_value}}}

        :return: The valor of this TransacaoPaySecureRequest.
        :rtype: float
        """
        return self._valor

    @valor.setter
    def valor(self, valor):
        """
        Sets the valor of this TransacaoPaySecureRequest.
        {{{transacao_pay_secure_request_valor_value}}}

        :param valor: The valor of this TransacaoPaySecureRequest.
        :type: float
        """
        self._valor = valor

    @property
    def nsu_origem(self):
        """
        Gets the nsu_origem of this TransacaoPaySecureRequest.
        {{{transacao_pay_secure_request_nsu_origem_value}}}

        :return: The nsu_origem of this TransacaoPaySecureRequest.
        :rtype: str
        """
        return self._nsu_origem

    @nsu_origem.setter
    def nsu_origem(self, nsu_origem):
        """
        Sets the nsu_origem of this TransacaoPaySecureRequest.
        {{{transacao_pay_secure_request_nsu_origem_value}}}

        :param nsu_origem: The nsu_origem of this TransacaoPaySecureRequest.
        :type: str
        """
        self._nsu_origem = nsu_origem

    @property
    def nome_portador_cartao(self):
        """
        Gets the nome_portador_cartao of this TransacaoPaySecureRequest.
        {{{transacao_pay_secure_request_nome_portador_cartao_value}}}

        :return: The nome_portador_cartao of this TransacaoPaySecureRequest.
        :rtype: str
        """
        return self._nome_portador_cartao

    @nome_portador_cartao.setter
    def nome_portador_cartao(self, nome_portador_cartao):
        """
        Sets the nome_portador_cartao of this TransacaoPaySecureRequest.
        {{{transacao_pay_secure_request_nome_portador_cartao_value}}}

        :param nome_portador_cartao: The nome_portador_cartao of this TransacaoPaySecureRequest.
        :type: str
        """
        self._nome_portador_cartao = nome_portador_cartao

    @property
    def origem(self):
        """
        Gets the origem of this TransacaoPaySecureRequest.
        {{{transacao_pay_generic_request_origem_value}}}

        :return: The origem of this TransacaoPaySecureRequest.
        :rtype: str
        """
        return self._origem

    @origem.setter
    def origem(self, origem):
        """
        Sets the origem of this TransacaoPaySecureRequest.
        {{{transacao_pay_generic_request_origem_value}}}

        :param origem: The origem of this TransacaoPaySecureRequest.
        :type: str
        """
        self._origem = origem

    @property
    def terminal_requisitante(self):
        """
        Gets the terminal_requisitante of this TransacaoPaySecureRequest.
        {{{transacao_pay_secure_request_terminal_requisitante_value}}}

        :return: The terminal_requisitante of this TransacaoPaySecureRequest.
        :rtype: str
        """
        return self._terminal_requisitante

    @terminal_requisitante.setter
    def terminal_requisitante(self, terminal_requisitante):
        """
        Sets the terminal_requisitante of this TransacaoPaySecureRequest.
        {{{transacao_pay_secure_request_terminal_requisitante_value}}}

        :param terminal_requisitante: The terminal_requisitante of this TransacaoPaySecureRequest.
        :type: str
        """
        self._terminal_requisitante = terminal_requisitante

    @property
    def codigo_processamento(self):
        """
        Gets the codigo_processamento of this TransacaoPaySecureRequest.
        {{{transacao_pay_secure_request_codigo_processamento_value}}}

        :return: The codigo_processamento of this TransacaoPaySecureRequest.
        :rtype: str
        """
        return self._codigo_processamento

    @codigo_processamento.setter
    def codigo_processamento(self, codigo_processamento):
        """
        Sets the codigo_processamento of this TransacaoPaySecureRequest.
        {{{transacao_pay_secure_request_codigo_processamento_value}}}

        :param codigo_processamento: The codigo_processamento of this TransacaoPaySecureRequest.
        :type: str
        """
        self._codigo_processamento = codigo_processamento

    @property
    def data_validade_cartao(self):
        """
        Gets the data_validade_cartao of this TransacaoPaySecureRequest.
        {{{transacao_pay_secure_request_data_validade_cartao_value}}}

        :return: The data_validade_cartao of this TransacaoPaySecureRequest.
        :rtype: str
        """
        return self._data_validade_cartao

    @data_validade_cartao.setter
    def data_validade_cartao(self, data_validade_cartao):
        """
        Sets the data_validade_cartao of this TransacaoPaySecureRequest.
        {{{transacao_pay_secure_request_data_validade_cartao_value}}}

        :param data_validade_cartao: The data_validade_cartao of this TransacaoPaySecureRequest.
        :type: str
        """
        self._data_validade_cartao = data_validade_cartao

    @property
    def numero_estabelecimento(self):
        """
        Gets the numero_estabelecimento of this TransacaoPaySecureRequest.
        {{{transacao_pay_secure_request_numero_estabelecimento_value}}}

        :return: The numero_estabelecimento of this TransacaoPaySecureRequest.
        :rtype: str
        """
        return self._numero_estabelecimento

    @numero_estabelecimento.setter
    def numero_estabelecimento(self, numero_estabelecimento):
        """
        Sets the numero_estabelecimento of this TransacaoPaySecureRequest.
        {{{transacao_pay_secure_request_numero_estabelecimento_value}}}

        :param numero_estabelecimento: The numero_estabelecimento of this TransacaoPaySecureRequest.
        :type: str
        """
        self._numero_estabelecimento = numero_estabelecimento

    @property
    def numero_parcelas(self):
        """
        Gets the numero_parcelas of this TransacaoPaySecureRequest.
        {{{transacao_pay_secure_request_numero_parcelas_value}}}

        :return: The numero_parcelas of this TransacaoPaySecureRequest.
        :rtype: int
        """
        return self._numero_parcelas

    @numero_parcelas.setter
    def numero_parcelas(self, numero_parcelas):
        """
        Sets the numero_parcelas of this TransacaoPaySecureRequest.
        {{{transacao_pay_secure_request_numero_parcelas_value}}}

        :param numero_parcelas: The numero_parcelas of this TransacaoPaySecureRequest.
        :type: int
        """
        self._numero_parcelas = numero_parcelas

    @property
    def codigo_seguranca_cartao(self):
        """
        Gets the codigo_seguranca_cartao of this TransacaoPaySecureRequest.
        {{{transacao_pay_secure_request_codigo_seguranca_cartao_value}}}

        :return: The codigo_seguranca_cartao of this TransacaoPaySecureRequest.
        :rtype: str
        """
        return self._codigo_seguranca_cartao

    @codigo_seguranca_cartao.setter
    def codigo_seguranca_cartao(self, codigo_seguranca_cartao):
        """
        Sets the codigo_seguranca_cartao of this TransacaoPaySecureRequest.
        {{{transacao_pay_secure_request_codigo_seguranca_cartao_value}}}

        :param codigo_seguranca_cartao: The codigo_seguranca_cartao of this TransacaoPaySecureRequest.
        :type: str
        """
        self._codigo_seguranca_cartao = codigo_seguranca_cartao

    @property
    def sort(self):
        """
        Gets the sort of this TransacaoPaySecureRequest.
        {{{global_menssagem_sort_sort}}}

        :return: The sort of this TransacaoPaySecureRequest.
        :rtype: list[str]
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """
        Sets the sort of this TransacaoPaySecureRequest.
        {{{global_menssagem_sort_sort}}}

        :param sort: The sort of this TransacaoPaySecureRequest.
        :type: list[str]
        """
        self._sort = sort

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

