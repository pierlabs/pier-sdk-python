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


class DividaClienteResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DividaClienteResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'data_vencimento_fatura_atraso': 'str',
            'quantidade_dias_atraso': 'int',
            'data_vencimento_acordo': 'str',
            'quantidade_dias_atraso_corrigido': 'int',
            'valor_saldo_devedor': 'float',
            'taxa_correcao': 'float',
            'valor_correcao': 'float',
            'valor_iof': 'float',
            'valor_saldo_corrigido': 'float',
            'id_status_conta': 'int',
            'descricao_status_conta': 'str',
            'id_status_acordo': 'int',
            'descricao_status_acordo': 'str',
            'id_escritorio_cobranca': 'int',
            'nome_escritorio_cobranca': 'str',
            'email_pessoa_conta': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'data_vencimento_fatura_atraso': 'dataVencimentoFaturaAtraso',
            'quantidade_dias_atraso': 'quantidadeDiasAtraso',
            'data_vencimento_acordo': 'dataVencimentoAcordo',
            'quantidade_dias_atraso_corrigido': 'quantidadeDiasAtrasoCorrigido',
            'valor_saldo_devedor': 'valorSaldoDevedor',
            'taxa_correcao': 'taxaCorrecao',
            'valor_correcao': 'valorCorrecao',
            'valor_iof': 'valorIOF',
            'valor_saldo_corrigido': 'valorSaldoCorrigido',
            'id_status_conta': 'idStatusConta',
            'descricao_status_conta': 'descricaoStatusConta',
            'id_status_acordo': 'idStatusAcordo',
            'descricao_status_acordo': 'descricaoStatusAcordo',
            'id_escritorio_cobranca': 'idEscritorioCobranca',
            'nome_escritorio_cobranca': 'nomeEscritorioCobranca',
            'email_pessoa_conta': 'emailPessoaConta'
        }

        self._id = None
        self._data_vencimento_fatura_atraso = None
        self._quantidade_dias_atraso = None
        self._data_vencimento_acordo = None
        self._quantidade_dias_atraso_corrigido = None
        self._valor_saldo_devedor = None
        self._taxa_correcao = None
        self._valor_correcao = None
        self._valor_iof = None
        self._valor_saldo_corrigido = None
        self._id_status_conta = None
        self._descricao_status_conta = None
        self._id_status_acordo = None
        self._descricao_status_acordo = None
        self._id_escritorio_cobranca = None
        self._nome_escritorio_cobranca = None
        self._email_pessoa_conta = None

    @property
    def id(self):
        """
        Gets the id of this DividaClienteResponse.
        {{{divida_cliente_response_id_value}}}

        :return: The id of this DividaClienteResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DividaClienteResponse.
        {{{divida_cliente_response_id_value}}}

        :param id: The id of this DividaClienteResponse.
        :type: int
        """
        self._id = id

    @property
    def data_vencimento_fatura_atraso(self):
        """
        Gets the data_vencimento_fatura_atraso of this DividaClienteResponse.
        {{{divida_cliente_response_data_vencimento_fatura_atraso_value}}}

        :return: The data_vencimento_fatura_atraso of this DividaClienteResponse.
        :rtype: str
        """
        return self._data_vencimento_fatura_atraso

    @data_vencimento_fatura_atraso.setter
    def data_vencimento_fatura_atraso(self, data_vencimento_fatura_atraso):
        """
        Sets the data_vencimento_fatura_atraso of this DividaClienteResponse.
        {{{divida_cliente_response_data_vencimento_fatura_atraso_value}}}

        :param data_vencimento_fatura_atraso: The data_vencimento_fatura_atraso of this DividaClienteResponse.
        :type: str
        """
        self._data_vencimento_fatura_atraso = data_vencimento_fatura_atraso

    @property
    def quantidade_dias_atraso(self):
        """
        Gets the quantidade_dias_atraso of this DividaClienteResponse.
        {{{divida_cliente_response_quantidade_dias_atraso_value}}}

        :return: The quantidade_dias_atraso of this DividaClienteResponse.
        :rtype: int
        """
        return self._quantidade_dias_atraso

    @quantidade_dias_atraso.setter
    def quantidade_dias_atraso(self, quantidade_dias_atraso):
        """
        Sets the quantidade_dias_atraso of this DividaClienteResponse.
        {{{divida_cliente_response_quantidade_dias_atraso_value}}}

        :param quantidade_dias_atraso: The quantidade_dias_atraso of this DividaClienteResponse.
        :type: int
        """
        self._quantidade_dias_atraso = quantidade_dias_atraso

    @property
    def data_vencimento_acordo(self):
        """
        Gets the data_vencimento_acordo of this DividaClienteResponse.
        {{{divida_cliente_response_data_vencimento_acordo_value}}}

        :return: The data_vencimento_acordo of this DividaClienteResponse.
        :rtype: str
        """
        return self._data_vencimento_acordo

    @data_vencimento_acordo.setter
    def data_vencimento_acordo(self, data_vencimento_acordo):
        """
        Sets the data_vencimento_acordo of this DividaClienteResponse.
        {{{divida_cliente_response_data_vencimento_acordo_value}}}

        :param data_vencimento_acordo: The data_vencimento_acordo of this DividaClienteResponse.
        :type: str
        """
        self._data_vencimento_acordo = data_vencimento_acordo

    @property
    def quantidade_dias_atraso_corrigido(self):
        """
        Gets the quantidade_dias_atraso_corrigido of this DividaClienteResponse.
        {{{divida_cliente_response_quantidade_dias_atraso_corrigido_value}}}

        :return: The quantidade_dias_atraso_corrigido of this DividaClienteResponse.
        :rtype: int
        """
        return self._quantidade_dias_atraso_corrigido

    @quantidade_dias_atraso_corrigido.setter
    def quantidade_dias_atraso_corrigido(self, quantidade_dias_atraso_corrigido):
        """
        Sets the quantidade_dias_atraso_corrigido of this DividaClienteResponse.
        {{{divida_cliente_response_quantidade_dias_atraso_corrigido_value}}}

        :param quantidade_dias_atraso_corrigido: The quantidade_dias_atraso_corrigido of this DividaClienteResponse.
        :type: int
        """
        self._quantidade_dias_atraso_corrigido = quantidade_dias_atraso_corrigido

    @property
    def valor_saldo_devedor(self):
        """
        Gets the valor_saldo_devedor of this DividaClienteResponse.
        {{{divida_cliente_response_valor_saldo_devedor_value}}}

        :return: The valor_saldo_devedor of this DividaClienteResponse.
        :rtype: float
        """
        return self._valor_saldo_devedor

    @valor_saldo_devedor.setter
    def valor_saldo_devedor(self, valor_saldo_devedor):
        """
        Sets the valor_saldo_devedor of this DividaClienteResponse.
        {{{divida_cliente_response_valor_saldo_devedor_value}}}

        :param valor_saldo_devedor: The valor_saldo_devedor of this DividaClienteResponse.
        :type: float
        """
        self._valor_saldo_devedor = valor_saldo_devedor

    @property
    def taxa_correcao(self):
        """
        Gets the taxa_correcao of this DividaClienteResponse.
        {{{divida_cliente_response_taxa_correcao_value}}}

        :return: The taxa_correcao of this DividaClienteResponse.
        :rtype: float
        """
        return self._taxa_correcao

    @taxa_correcao.setter
    def taxa_correcao(self, taxa_correcao):
        """
        Sets the taxa_correcao of this DividaClienteResponse.
        {{{divida_cliente_response_taxa_correcao_value}}}

        :param taxa_correcao: The taxa_correcao of this DividaClienteResponse.
        :type: float
        """
        self._taxa_correcao = taxa_correcao

    @property
    def valor_correcao(self):
        """
        Gets the valor_correcao of this DividaClienteResponse.
        {{{divida_cliente_response_valor_correcao_value}}}

        :return: The valor_correcao of this DividaClienteResponse.
        :rtype: float
        """
        return self._valor_correcao

    @valor_correcao.setter
    def valor_correcao(self, valor_correcao):
        """
        Sets the valor_correcao of this DividaClienteResponse.
        {{{divida_cliente_response_valor_correcao_value}}}

        :param valor_correcao: The valor_correcao of this DividaClienteResponse.
        :type: float
        """
        self._valor_correcao = valor_correcao

    @property
    def valor_iof(self):
        """
        Gets the valor_iof of this DividaClienteResponse.
        {{{divida_cliente_response_valor_i_o_f_value}}}

        :return: The valor_iof of this DividaClienteResponse.
        :rtype: float
        """
        return self._valor_iof

    @valor_iof.setter
    def valor_iof(self, valor_iof):
        """
        Sets the valor_iof of this DividaClienteResponse.
        {{{divida_cliente_response_valor_i_o_f_value}}}

        :param valor_iof: The valor_iof of this DividaClienteResponse.
        :type: float
        """
        self._valor_iof = valor_iof

    @property
    def valor_saldo_corrigido(self):
        """
        Gets the valor_saldo_corrigido of this DividaClienteResponse.
        {{{divida_cliente_response_valor_saldo_corrigido_value}}}

        :return: The valor_saldo_corrigido of this DividaClienteResponse.
        :rtype: float
        """
        return self._valor_saldo_corrigido

    @valor_saldo_corrigido.setter
    def valor_saldo_corrigido(self, valor_saldo_corrigido):
        """
        Sets the valor_saldo_corrigido of this DividaClienteResponse.
        {{{divida_cliente_response_valor_saldo_corrigido_value}}}

        :param valor_saldo_corrigido: The valor_saldo_corrigido of this DividaClienteResponse.
        :type: float
        """
        self._valor_saldo_corrigido = valor_saldo_corrigido

    @property
    def id_status_conta(self):
        """
        Gets the id_status_conta of this DividaClienteResponse.
        {{{divida_cliente_response_id_status_conta_value}}}

        :return: The id_status_conta of this DividaClienteResponse.
        :rtype: int
        """
        return self._id_status_conta

    @id_status_conta.setter
    def id_status_conta(self, id_status_conta):
        """
        Sets the id_status_conta of this DividaClienteResponse.
        {{{divida_cliente_response_id_status_conta_value}}}

        :param id_status_conta: The id_status_conta of this DividaClienteResponse.
        :type: int
        """
        self._id_status_conta = id_status_conta

    @property
    def descricao_status_conta(self):
        """
        Gets the descricao_status_conta of this DividaClienteResponse.
        {{{divida_cliente_response_descricao_status_conta_value}}}

        :return: The descricao_status_conta of this DividaClienteResponse.
        :rtype: str
        """
        return self._descricao_status_conta

    @descricao_status_conta.setter
    def descricao_status_conta(self, descricao_status_conta):
        """
        Sets the descricao_status_conta of this DividaClienteResponse.
        {{{divida_cliente_response_descricao_status_conta_value}}}

        :param descricao_status_conta: The descricao_status_conta of this DividaClienteResponse.
        :type: str
        """
        self._descricao_status_conta = descricao_status_conta

    @property
    def id_status_acordo(self):
        """
        Gets the id_status_acordo of this DividaClienteResponse.
        {{{divida_cliente_response_id_status_acordo_value}}}

        :return: The id_status_acordo of this DividaClienteResponse.
        :rtype: int
        """
        return self._id_status_acordo

    @id_status_acordo.setter
    def id_status_acordo(self, id_status_acordo):
        """
        Sets the id_status_acordo of this DividaClienteResponse.
        {{{divida_cliente_response_id_status_acordo_value}}}

        :param id_status_acordo: The id_status_acordo of this DividaClienteResponse.
        :type: int
        """
        self._id_status_acordo = id_status_acordo

    @property
    def descricao_status_acordo(self):
        """
        Gets the descricao_status_acordo of this DividaClienteResponse.
        {{{divida_cliente_response_descricao_status_acordo_value}}}

        :return: The descricao_status_acordo of this DividaClienteResponse.
        :rtype: str
        """
        return self._descricao_status_acordo

    @descricao_status_acordo.setter
    def descricao_status_acordo(self, descricao_status_acordo):
        """
        Sets the descricao_status_acordo of this DividaClienteResponse.
        {{{divida_cliente_response_descricao_status_acordo_value}}}

        :param descricao_status_acordo: The descricao_status_acordo of this DividaClienteResponse.
        :type: str
        """
        self._descricao_status_acordo = descricao_status_acordo

    @property
    def id_escritorio_cobranca(self):
        """
        Gets the id_escritorio_cobranca of this DividaClienteResponse.
        {{{divida_cliente_response_id_escritorio_cobranca_value}}}

        :return: The id_escritorio_cobranca of this DividaClienteResponse.
        :rtype: int
        """
        return self._id_escritorio_cobranca

    @id_escritorio_cobranca.setter
    def id_escritorio_cobranca(self, id_escritorio_cobranca):
        """
        Sets the id_escritorio_cobranca of this DividaClienteResponse.
        {{{divida_cliente_response_id_escritorio_cobranca_value}}}

        :param id_escritorio_cobranca: The id_escritorio_cobranca of this DividaClienteResponse.
        :type: int
        """
        self._id_escritorio_cobranca = id_escritorio_cobranca

    @property
    def nome_escritorio_cobranca(self):
        """
        Gets the nome_escritorio_cobranca of this DividaClienteResponse.
        {{{divida_cliente_response_nome_escritorio_cobranca_value}}}

        :return: The nome_escritorio_cobranca of this DividaClienteResponse.
        :rtype: str
        """
        return self._nome_escritorio_cobranca

    @nome_escritorio_cobranca.setter
    def nome_escritorio_cobranca(self, nome_escritorio_cobranca):
        """
        Sets the nome_escritorio_cobranca of this DividaClienteResponse.
        {{{divida_cliente_response_nome_escritorio_cobranca_value}}}

        :param nome_escritorio_cobranca: The nome_escritorio_cobranca of this DividaClienteResponse.
        :type: str
        """
        self._nome_escritorio_cobranca = nome_escritorio_cobranca

    @property
    def email_pessoa_conta(self):
        """
        Gets the email_pessoa_conta of this DividaClienteResponse.
        {{{divida_cliente_response_email_pessoa_conta_value}}}

        :return: The email_pessoa_conta of this DividaClienteResponse.
        :rtype: str
        """
        return self._email_pessoa_conta

    @email_pessoa_conta.setter
    def email_pessoa_conta(self, email_pessoa_conta):
        """
        Sets the email_pessoa_conta of this DividaClienteResponse.
        {{{divida_cliente_response_email_pessoa_conta_value}}}

        :param email_pessoa_conta: The email_pessoa_conta of this DividaClienteResponse.
        :type: str
        """
        self._email_pessoa_conta = email_pessoa_conta

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

