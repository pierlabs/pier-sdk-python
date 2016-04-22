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


class ConsultarExtratoContaResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ConsultarExtratoContaResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'codigo_retorno': 'int',
            'compras_nacionais': 'float',
            'cpf': 'str',
            'creditos_nacionais': 'float',
            'data_vencimento': 'str',
            'debitos_nacionais': 'float',
            'descricao_retorno': 'str',
            'extrato': 'list[ExtratoResponse]',
            'id_cartao': 'int',
            'id_conta': 'int',
            'multa': 'float',
            'pagamentos': 'float',
            'saldo_atual_final': 'float',
            'saldo_extrato_anterior': 'float',
            'tarifas_nacionais': 'float',
            'valor_minimo_extrato': 'float'
        }

        self.attribute_map = {
            'codigo_retorno': 'codigoRetorno',
            'compras_nacionais': 'comprasNacionais',
            'cpf': 'cpf',
            'creditos_nacionais': 'creditosNacionais',
            'data_vencimento': 'dataVencimento',
            'debitos_nacionais': 'debitosNacionais',
            'descricao_retorno': 'descricaoRetorno',
            'extrato': 'extrato',
            'id_cartao': 'idCartao',
            'id_conta': 'idConta',
            'multa': 'multa',
            'pagamentos': 'pagamentos',
            'saldo_atual_final': 'saldoAtualFinal',
            'saldo_extrato_anterior': 'saldoExtratoAnterior',
            'tarifas_nacionais': 'tarifasNacionais',
            'valor_minimo_extrato': 'valorMinimoExtrato'
        }

        self._codigo_retorno = None
        self._compras_nacionais = None
        self._cpf = None
        self._creditos_nacionais = None
        self._data_vencimento = None
        self._debitos_nacionais = None
        self._descricao_retorno = None
        self._extrato = None
        self._id_cartao = None
        self._id_conta = None
        self._multa = None
        self._pagamentos = None
        self._saldo_atual_final = None
        self._saldo_extrato_anterior = None
        self._tarifas_nacionais = None
        self._valor_minimo_extrato = None

    @property
    def codigo_retorno(self):
        """
        Gets the codigo_retorno of this ConsultarExtratoContaResponse.


        :return: The codigo_retorno of this ConsultarExtratoContaResponse.
        :rtype: int
        """
        return self._codigo_retorno

    @codigo_retorno.setter
    def codigo_retorno(self, codigo_retorno):
        """
        Sets the codigo_retorno of this ConsultarExtratoContaResponse.


        :param codigo_retorno: The codigo_retorno of this ConsultarExtratoContaResponse.
        :type: int
        """
        self._codigo_retorno = codigo_retorno

    @property
    def compras_nacionais(self):
        """
        Gets the compras_nacionais of this ConsultarExtratoContaResponse.


        :return: The compras_nacionais of this ConsultarExtratoContaResponse.
        :rtype: float
        """
        return self._compras_nacionais

    @compras_nacionais.setter
    def compras_nacionais(self, compras_nacionais):
        """
        Sets the compras_nacionais of this ConsultarExtratoContaResponse.


        :param compras_nacionais: The compras_nacionais of this ConsultarExtratoContaResponse.
        :type: float
        """
        self._compras_nacionais = compras_nacionais

    @property
    def cpf(self):
        """
        Gets the cpf of this ConsultarExtratoContaResponse.


        :return: The cpf of this ConsultarExtratoContaResponse.
        :rtype: str
        """
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        """
        Sets the cpf of this ConsultarExtratoContaResponse.


        :param cpf: The cpf of this ConsultarExtratoContaResponse.
        :type: str
        """
        self._cpf = cpf

    @property
    def creditos_nacionais(self):
        """
        Gets the creditos_nacionais of this ConsultarExtratoContaResponse.


        :return: The creditos_nacionais of this ConsultarExtratoContaResponse.
        :rtype: float
        """
        return self._creditos_nacionais

    @creditos_nacionais.setter
    def creditos_nacionais(self, creditos_nacionais):
        """
        Sets the creditos_nacionais of this ConsultarExtratoContaResponse.


        :param creditos_nacionais: The creditos_nacionais of this ConsultarExtratoContaResponse.
        :type: float
        """
        self._creditos_nacionais = creditos_nacionais

    @property
    def data_vencimento(self):
        """
        Gets the data_vencimento of this ConsultarExtratoContaResponse.


        :return: The data_vencimento of this ConsultarExtratoContaResponse.
        :rtype: str
        """
        return self._data_vencimento

    @data_vencimento.setter
    def data_vencimento(self, data_vencimento):
        """
        Sets the data_vencimento of this ConsultarExtratoContaResponse.


        :param data_vencimento: The data_vencimento of this ConsultarExtratoContaResponse.
        :type: str
        """
        self._data_vencimento = data_vencimento

    @property
    def debitos_nacionais(self):
        """
        Gets the debitos_nacionais of this ConsultarExtratoContaResponse.


        :return: The debitos_nacionais of this ConsultarExtratoContaResponse.
        :rtype: float
        """
        return self._debitos_nacionais

    @debitos_nacionais.setter
    def debitos_nacionais(self, debitos_nacionais):
        """
        Sets the debitos_nacionais of this ConsultarExtratoContaResponse.


        :param debitos_nacionais: The debitos_nacionais of this ConsultarExtratoContaResponse.
        :type: float
        """
        self._debitos_nacionais = debitos_nacionais

    @property
    def descricao_retorno(self):
        """
        Gets the descricao_retorno of this ConsultarExtratoContaResponse.


        :return: The descricao_retorno of this ConsultarExtratoContaResponse.
        :rtype: str
        """
        return self._descricao_retorno

    @descricao_retorno.setter
    def descricao_retorno(self, descricao_retorno):
        """
        Sets the descricao_retorno of this ConsultarExtratoContaResponse.


        :param descricao_retorno: The descricao_retorno of this ConsultarExtratoContaResponse.
        :type: str
        """
        self._descricao_retorno = descricao_retorno

    @property
    def extrato(self):
        """
        Gets the extrato of this ConsultarExtratoContaResponse.


        :return: The extrato of this ConsultarExtratoContaResponse.
        :rtype: list[ExtratoResponse]
        """
        return self._extrato

    @extrato.setter
    def extrato(self, extrato):
        """
        Sets the extrato of this ConsultarExtratoContaResponse.


        :param extrato: The extrato of this ConsultarExtratoContaResponse.
        :type: list[ExtratoResponse]
        """
        self._extrato = extrato

    @property
    def id_cartao(self):
        """
        Gets the id_cartao of this ConsultarExtratoContaResponse.


        :return: The id_cartao of this ConsultarExtratoContaResponse.
        :rtype: int
        """
        return self._id_cartao

    @id_cartao.setter
    def id_cartao(self, id_cartao):
        """
        Sets the id_cartao of this ConsultarExtratoContaResponse.


        :param id_cartao: The id_cartao of this ConsultarExtratoContaResponse.
        :type: int
        """
        self._id_cartao = id_cartao

    @property
    def id_conta(self):
        """
        Gets the id_conta of this ConsultarExtratoContaResponse.


        :return: The id_conta of this ConsultarExtratoContaResponse.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this ConsultarExtratoContaResponse.


        :param id_conta: The id_conta of this ConsultarExtratoContaResponse.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def multa(self):
        """
        Gets the multa of this ConsultarExtratoContaResponse.


        :return: The multa of this ConsultarExtratoContaResponse.
        :rtype: float
        """
        return self._multa

    @multa.setter
    def multa(self, multa):
        """
        Sets the multa of this ConsultarExtratoContaResponse.


        :param multa: The multa of this ConsultarExtratoContaResponse.
        :type: float
        """
        self._multa = multa

    @property
    def pagamentos(self):
        """
        Gets the pagamentos of this ConsultarExtratoContaResponse.


        :return: The pagamentos of this ConsultarExtratoContaResponse.
        :rtype: float
        """
        return self._pagamentos

    @pagamentos.setter
    def pagamentos(self, pagamentos):
        """
        Sets the pagamentos of this ConsultarExtratoContaResponse.


        :param pagamentos: The pagamentos of this ConsultarExtratoContaResponse.
        :type: float
        """
        self._pagamentos = pagamentos

    @property
    def saldo_atual_final(self):
        """
        Gets the saldo_atual_final of this ConsultarExtratoContaResponse.


        :return: The saldo_atual_final of this ConsultarExtratoContaResponse.
        :rtype: float
        """
        return self._saldo_atual_final

    @saldo_atual_final.setter
    def saldo_atual_final(self, saldo_atual_final):
        """
        Sets the saldo_atual_final of this ConsultarExtratoContaResponse.


        :param saldo_atual_final: The saldo_atual_final of this ConsultarExtratoContaResponse.
        :type: float
        """
        self._saldo_atual_final = saldo_atual_final

    @property
    def saldo_extrato_anterior(self):
        """
        Gets the saldo_extrato_anterior of this ConsultarExtratoContaResponse.


        :return: The saldo_extrato_anterior of this ConsultarExtratoContaResponse.
        :rtype: float
        """
        return self._saldo_extrato_anterior

    @saldo_extrato_anterior.setter
    def saldo_extrato_anterior(self, saldo_extrato_anterior):
        """
        Sets the saldo_extrato_anterior of this ConsultarExtratoContaResponse.


        :param saldo_extrato_anterior: The saldo_extrato_anterior of this ConsultarExtratoContaResponse.
        :type: float
        """
        self._saldo_extrato_anterior = saldo_extrato_anterior

    @property
    def tarifas_nacionais(self):
        """
        Gets the tarifas_nacionais of this ConsultarExtratoContaResponse.


        :return: The tarifas_nacionais of this ConsultarExtratoContaResponse.
        :rtype: float
        """
        return self._tarifas_nacionais

    @tarifas_nacionais.setter
    def tarifas_nacionais(self, tarifas_nacionais):
        """
        Sets the tarifas_nacionais of this ConsultarExtratoContaResponse.


        :param tarifas_nacionais: The tarifas_nacionais of this ConsultarExtratoContaResponse.
        :type: float
        """
        self._tarifas_nacionais = tarifas_nacionais

    @property
    def valor_minimo_extrato(self):
        """
        Gets the valor_minimo_extrato of this ConsultarExtratoContaResponse.


        :return: The valor_minimo_extrato of this ConsultarExtratoContaResponse.
        :rtype: float
        """
        return self._valor_minimo_extrato

    @valor_minimo_extrato.setter
    def valor_minimo_extrato(self, valor_minimo_extrato):
        """
        Sets the valor_minimo_extrato of this ConsultarExtratoContaResponse.


        :param valor_minimo_extrato: The valor_minimo_extrato of this ConsultarExtratoContaResponse.
        :type: float
        """
        self._valor_minimo_extrato = valor_minimo_extrato

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

