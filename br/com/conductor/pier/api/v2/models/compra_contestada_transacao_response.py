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


class CompraContestadaTransacaoResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CompraContestadaTransacaoResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'aging_compras': 'int',
            'aging_contestacao': 'int',
            'bandeira': 'str',
            'codigo_autorizacao': 'str',
            'codigo_contestacao': 'str',
            'codigo_evento_compra': 'str',
            'codigo_moeda_destino': 'str',
            'data2_reapresentacao': 'str',
            'data_alteracao': 'datetime',
            'data_contestacao': 'datetime',
            'data_envio_cb': 'str',
            'data_transacao': 'datetime',
            'historico': 'str',
            'id_compra_contestada': 'int',
            'internacional': 'int',
            'mcc': 'str',
            'modo_de_entrada_descricao': 'str',
            'modo_entrada': 'str',
            'motivo2_reapresentacao': 'str',
            'nome_estabelecimento': 'str',
            'numero_controle': 'str',
            'razao_cb': 'str',
            'reference_number': 'str',
            'reporte_bandeira': 'str',
            'responsavel_abertuda': 'str',
            'responsavel_alteracao': 'str',
            'status_contestacao': 'str',
            'texto2_reapresentacao': 'str',
            'tipo_transacao': 'str',
            'transacao_segura': 'str',
            'valor_compra': 'float',
            'valor_contrato': 'float',
            'valor_destino': 'float'
        }

        self.attribute_map = {
            'aging_compras': 'agingCompras',
            'aging_contestacao': 'agingContestacao',
            'bandeira': 'bandeira',
            'codigo_autorizacao': 'codigoAutorizacao',
            'codigo_contestacao': 'codigoContestacao',
            'codigo_evento_compra': 'codigoEventoCompra',
            'codigo_moeda_destino': 'codigoMoedaDestino',
            'data2_reapresentacao': 'data2Reapresentacao',
            'data_alteracao': 'dataAlteracao',
            'data_contestacao': 'dataContestacao',
            'data_envio_cb': 'dataEnvioCB',
            'data_transacao': 'dataTransacao',
            'historico': 'historico',
            'id_compra_contestada': 'idCompraContestada',
            'internacional': 'internacional',
            'mcc': 'mcc',
            'modo_de_entrada_descricao': 'modoDeEntradaDescricao',
            'modo_entrada': 'modoEntrada',
            'motivo2_reapresentacao': 'motivo2Reapresentacao',
            'nome_estabelecimento': 'nomeEstabelecimento',
            'numero_controle': 'numeroControle',
            'razao_cb': 'razaoCB',
            'reference_number': 'referenceNumber',
            'reporte_bandeira': 'reporteBandeira',
            'responsavel_abertuda': 'responsavelAbertuda',
            'responsavel_alteracao': 'responsavelAlteracao',
            'status_contestacao': 'statusContestacao',
            'texto2_reapresentacao': 'texto2Reapresentacao',
            'tipo_transacao': 'tipoTransacao',
            'transacao_segura': 'transacaoSegura',
            'valor_compra': 'valorCompra',
            'valor_contrato': 'valorContrato',
            'valor_destino': 'valorDestino'
        }

        self._aging_compras = None
        self._aging_contestacao = None
        self._bandeira = None
        self._codigo_autorizacao = None
        self._codigo_contestacao = None
        self._codigo_evento_compra = None
        self._codigo_moeda_destino = None
        self._data2_reapresentacao = None
        self._data_alteracao = None
        self._data_contestacao = None
        self._data_envio_cb = None
        self._data_transacao = None
        self._historico = None
        self._id_compra_contestada = None
        self._internacional = None
        self._mcc = None
        self._modo_de_entrada_descricao = None
        self._modo_entrada = None
        self._motivo2_reapresentacao = None
        self._nome_estabelecimento = None
        self._numero_controle = None
        self._razao_cb = None
        self._reference_number = None
        self._reporte_bandeira = None
        self._responsavel_abertuda = None
        self._responsavel_alteracao = None
        self._status_contestacao = None
        self._texto2_reapresentacao = None
        self._tipo_transacao = None
        self._transacao_segura = None
        self._valor_compra = None
        self._valor_contrato = None
        self._valor_destino = None

    @property
    def aging_compras(self):
        """
        Gets the aging_compras of this CompraContestadaTransacaoResponse.


        :return: The aging_compras of this CompraContestadaTransacaoResponse.
        :rtype: int
        """
        return self._aging_compras

    @aging_compras.setter
    def aging_compras(self, aging_compras):
        """
        Sets the aging_compras of this CompraContestadaTransacaoResponse.


        :param aging_compras: The aging_compras of this CompraContestadaTransacaoResponse.
        :type: int
        """
        self._aging_compras = aging_compras

    @property
    def aging_contestacao(self):
        """
        Gets the aging_contestacao of this CompraContestadaTransacaoResponse.


        :return: The aging_contestacao of this CompraContestadaTransacaoResponse.
        :rtype: int
        """
        return self._aging_contestacao

    @aging_contestacao.setter
    def aging_contestacao(self, aging_contestacao):
        """
        Sets the aging_contestacao of this CompraContestadaTransacaoResponse.


        :param aging_contestacao: The aging_contestacao of this CompraContestadaTransacaoResponse.
        :type: int
        """
        self._aging_contestacao = aging_contestacao

    @property
    def bandeira(self):
        """
        Gets the bandeira of this CompraContestadaTransacaoResponse.


        :return: The bandeira of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._bandeira

    @bandeira.setter
    def bandeira(self, bandeira):
        """
        Sets the bandeira of this CompraContestadaTransacaoResponse.


        :param bandeira: The bandeira of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._bandeira = bandeira

    @property
    def codigo_autorizacao(self):
        """
        Gets the codigo_autorizacao of this CompraContestadaTransacaoResponse.


        :return: The codigo_autorizacao of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._codigo_autorizacao

    @codigo_autorizacao.setter
    def codigo_autorizacao(self, codigo_autorizacao):
        """
        Sets the codigo_autorizacao of this CompraContestadaTransacaoResponse.


        :param codigo_autorizacao: The codigo_autorizacao of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._codigo_autorizacao = codigo_autorizacao

    @property
    def codigo_contestacao(self):
        """
        Gets the codigo_contestacao of this CompraContestadaTransacaoResponse.


        :return: The codigo_contestacao of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._codigo_contestacao

    @codigo_contestacao.setter
    def codigo_contestacao(self, codigo_contestacao):
        """
        Sets the codigo_contestacao of this CompraContestadaTransacaoResponse.


        :param codigo_contestacao: The codigo_contestacao of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._codigo_contestacao = codigo_contestacao

    @property
    def codigo_evento_compra(self):
        """
        Gets the codigo_evento_compra of this CompraContestadaTransacaoResponse.


        :return: The codigo_evento_compra of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._codigo_evento_compra

    @codigo_evento_compra.setter
    def codigo_evento_compra(self, codigo_evento_compra):
        """
        Sets the codigo_evento_compra of this CompraContestadaTransacaoResponse.


        :param codigo_evento_compra: The codigo_evento_compra of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._codigo_evento_compra = codigo_evento_compra

    @property
    def codigo_moeda_destino(self):
        """
        Gets the codigo_moeda_destino of this CompraContestadaTransacaoResponse.


        :return: The codigo_moeda_destino of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._codigo_moeda_destino

    @codigo_moeda_destino.setter
    def codigo_moeda_destino(self, codigo_moeda_destino):
        """
        Sets the codigo_moeda_destino of this CompraContestadaTransacaoResponse.


        :param codigo_moeda_destino: The codigo_moeda_destino of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._codigo_moeda_destino = codigo_moeda_destino

    @property
    def data2_reapresentacao(self):
        """
        Gets the data2_reapresentacao of this CompraContestadaTransacaoResponse.


        :return: The data2_reapresentacao of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._data2_reapresentacao

    @data2_reapresentacao.setter
    def data2_reapresentacao(self, data2_reapresentacao):
        """
        Sets the data2_reapresentacao of this CompraContestadaTransacaoResponse.


        :param data2_reapresentacao: The data2_reapresentacao of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._data2_reapresentacao = data2_reapresentacao

    @property
    def data_alteracao(self):
        """
        Gets the data_alteracao of this CompraContestadaTransacaoResponse.


        :return: The data_alteracao of this CompraContestadaTransacaoResponse.
        :rtype: datetime
        """
        return self._data_alteracao

    @data_alteracao.setter
    def data_alteracao(self, data_alteracao):
        """
        Sets the data_alteracao of this CompraContestadaTransacaoResponse.


        :param data_alteracao: The data_alteracao of this CompraContestadaTransacaoResponse.
        :type: datetime
        """
        self._data_alteracao = data_alteracao

    @property
    def data_contestacao(self):
        """
        Gets the data_contestacao of this CompraContestadaTransacaoResponse.


        :return: The data_contestacao of this CompraContestadaTransacaoResponse.
        :rtype: datetime
        """
        return self._data_contestacao

    @data_contestacao.setter
    def data_contestacao(self, data_contestacao):
        """
        Sets the data_contestacao of this CompraContestadaTransacaoResponse.


        :param data_contestacao: The data_contestacao of this CompraContestadaTransacaoResponse.
        :type: datetime
        """
        self._data_contestacao = data_contestacao

    @property
    def data_envio_cb(self):
        """
        Gets the data_envio_cb of this CompraContestadaTransacaoResponse.


        :return: The data_envio_cb of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._data_envio_cb

    @data_envio_cb.setter
    def data_envio_cb(self, data_envio_cb):
        """
        Sets the data_envio_cb of this CompraContestadaTransacaoResponse.


        :param data_envio_cb: The data_envio_cb of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._data_envio_cb = data_envio_cb

    @property
    def data_transacao(self):
        """
        Gets the data_transacao of this CompraContestadaTransacaoResponse.


        :return: The data_transacao of this CompraContestadaTransacaoResponse.
        :rtype: datetime
        """
        return self._data_transacao

    @data_transacao.setter
    def data_transacao(self, data_transacao):
        """
        Sets the data_transacao of this CompraContestadaTransacaoResponse.


        :param data_transacao: The data_transacao of this CompraContestadaTransacaoResponse.
        :type: datetime
        """
        self._data_transacao = data_transacao

    @property
    def historico(self):
        """
        Gets the historico of this CompraContestadaTransacaoResponse.


        :return: The historico of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._historico

    @historico.setter
    def historico(self, historico):
        """
        Sets the historico of this CompraContestadaTransacaoResponse.


        :param historico: The historico of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._historico = historico

    @property
    def id_compra_contestada(self):
        """
        Gets the id_compra_contestada of this CompraContestadaTransacaoResponse.


        :return: The id_compra_contestada of this CompraContestadaTransacaoResponse.
        :rtype: int
        """
        return self._id_compra_contestada

    @id_compra_contestada.setter
    def id_compra_contestada(self, id_compra_contestada):
        """
        Sets the id_compra_contestada of this CompraContestadaTransacaoResponse.


        :param id_compra_contestada: The id_compra_contestada of this CompraContestadaTransacaoResponse.
        :type: int
        """
        self._id_compra_contestada = id_compra_contestada

    @property
    def internacional(self):
        """
        Gets the internacional of this CompraContestadaTransacaoResponse.


        :return: The internacional of this CompraContestadaTransacaoResponse.
        :rtype: int
        """
        return self._internacional

    @internacional.setter
    def internacional(self, internacional):
        """
        Sets the internacional of this CompraContestadaTransacaoResponse.


        :param internacional: The internacional of this CompraContestadaTransacaoResponse.
        :type: int
        """
        self._internacional = internacional

    @property
    def mcc(self):
        """
        Gets the mcc of this CompraContestadaTransacaoResponse.


        :return: The mcc of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._mcc

    @mcc.setter
    def mcc(self, mcc):
        """
        Sets the mcc of this CompraContestadaTransacaoResponse.


        :param mcc: The mcc of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._mcc = mcc

    @property
    def modo_de_entrada_descricao(self):
        """
        Gets the modo_de_entrada_descricao of this CompraContestadaTransacaoResponse.


        :return: The modo_de_entrada_descricao of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._modo_de_entrada_descricao

    @modo_de_entrada_descricao.setter
    def modo_de_entrada_descricao(self, modo_de_entrada_descricao):
        """
        Sets the modo_de_entrada_descricao of this CompraContestadaTransacaoResponse.


        :param modo_de_entrada_descricao: The modo_de_entrada_descricao of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._modo_de_entrada_descricao = modo_de_entrada_descricao

    @property
    def modo_entrada(self):
        """
        Gets the modo_entrada of this CompraContestadaTransacaoResponse.


        :return: The modo_entrada of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._modo_entrada

    @modo_entrada.setter
    def modo_entrada(self, modo_entrada):
        """
        Sets the modo_entrada of this CompraContestadaTransacaoResponse.


        :param modo_entrada: The modo_entrada of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._modo_entrada = modo_entrada

    @property
    def motivo2_reapresentacao(self):
        """
        Gets the motivo2_reapresentacao of this CompraContestadaTransacaoResponse.


        :return: The motivo2_reapresentacao of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._motivo2_reapresentacao

    @motivo2_reapresentacao.setter
    def motivo2_reapresentacao(self, motivo2_reapresentacao):
        """
        Sets the motivo2_reapresentacao of this CompraContestadaTransacaoResponse.


        :param motivo2_reapresentacao: The motivo2_reapresentacao of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._motivo2_reapresentacao = motivo2_reapresentacao

    @property
    def nome_estabelecimento(self):
        """
        Gets the nome_estabelecimento of this CompraContestadaTransacaoResponse.


        :return: The nome_estabelecimento of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._nome_estabelecimento

    @nome_estabelecimento.setter
    def nome_estabelecimento(self, nome_estabelecimento):
        """
        Sets the nome_estabelecimento of this CompraContestadaTransacaoResponse.


        :param nome_estabelecimento: The nome_estabelecimento of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._nome_estabelecimento = nome_estabelecimento

    @property
    def numero_controle(self):
        """
        Gets the numero_controle of this CompraContestadaTransacaoResponse.


        :return: The numero_controle of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._numero_controle

    @numero_controle.setter
    def numero_controle(self, numero_controle):
        """
        Sets the numero_controle of this CompraContestadaTransacaoResponse.


        :param numero_controle: The numero_controle of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._numero_controle = numero_controle

    @property
    def razao_cb(self):
        """
        Gets the razao_cb of this CompraContestadaTransacaoResponse.


        :return: The razao_cb of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._razao_cb

    @razao_cb.setter
    def razao_cb(self, razao_cb):
        """
        Sets the razao_cb of this CompraContestadaTransacaoResponse.


        :param razao_cb: The razao_cb of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._razao_cb = razao_cb

    @property
    def reference_number(self):
        """
        Gets the reference_number of this CompraContestadaTransacaoResponse.


        :return: The reference_number of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """
        Sets the reference_number of this CompraContestadaTransacaoResponse.


        :param reference_number: The reference_number of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._reference_number = reference_number

    @property
    def reporte_bandeira(self):
        """
        Gets the reporte_bandeira of this CompraContestadaTransacaoResponse.


        :return: The reporte_bandeira of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._reporte_bandeira

    @reporte_bandeira.setter
    def reporte_bandeira(self, reporte_bandeira):
        """
        Sets the reporte_bandeira of this CompraContestadaTransacaoResponse.


        :param reporte_bandeira: The reporte_bandeira of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._reporte_bandeira = reporte_bandeira

    @property
    def responsavel_abertuda(self):
        """
        Gets the responsavel_abertuda of this CompraContestadaTransacaoResponse.


        :return: The responsavel_abertuda of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._responsavel_abertuda

    @responsavel_abertuda.setter
    def responsavel_abertuda(self, responsavel_abertuda):
        """
        Sets the responsavel_abertuda of this CompraContestadaTransacaoResponse.


        :param responsavel_abertuda: The responsavel_abertuda of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._responsavel_abertuda = responsavel_abertuda

    @property
    def responsavel_alteracao(self):
        """
        Gets the responsavel_alteracao of this CompraContestadaTransacaoResponse.


        :return: The responsavel_alteracao of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._responsavel_alteracao

    @responsavel_alteracao.setter
    def responsavel_alteracao(self, responsavel_alteracao):
        """
        Sets the responsavel_alteracao of this CompraContestadaTransacaoResponse.


        :param responsavel_alteracao: The responsavel_alteracao of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._responsavel_alteracao = responsavel_alteracao

    @property
    def status_contestacao(self):
        """
        Gets the status_contestacao of this CompraContestadaTransacaoResponse.


        :return: The status_contestacao of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._status_contestacao

    @status_contestacao.setter
    def status_contestacao(self, status_contestacao):
        """
        Sets the status_contestacao of this CompraContestadaTransacaoResponse.


        :param status_contestacao: The status_contestacao of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._status_contestacao = status_contestacao

    @property
    def texto2_reapresentacao(self):
        """
        Gets the texto2_reapresentacao of this CompraContestadaTransacaoResponse.


        :return: The texto2_reapresentacao of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._texto2_reapresentacao

    @texto2_reapresentacao.setter
    def texto2_reapresentacao(self, texto2_reapresentacao):
        """
        Sets the texto2_reapresentacao of this CompraContestadaTransacaoResponse.


        :param texto2_reapresentacao: The texto2_reapresentacao of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._texto2_reapresentacao = texto2_reapresentacao

    @property
    def tipo_transacao(self):
        """
        Gets the tipo_transacao of this CompraContestadaTransacaoResponse.


        :return: The tipo_transacao of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._tipo_transacao

    @tipo_transacao.setter
    def tipo_transacao(self, tipo_transacao):
        """
        Sets the tipo_transacao of this CompraContestadaTransacaoResponse.


        :param tipo_transacao: The tipo_transacao of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._tipo_transacao = tipo_transacao

    @property
    def transacao_segura(self):
        """
        Gets the transacao_segura of this CompraContestadaTransacaoResponse.


        :return: The transacao_segura of this CompraContestadaTransacaoResponse.
        :rtype: str
        """
        return self._transacao_segura

    @transacao_segura.setter
    def transacao_segura(self, transacao_segura):
        """
        Sets the transacao_segura of this CompraContestadaTransacaoResponse.


        :param transacao_segura: The transacao_segura of this CompraContestadaTransacaoResponse.
        :type: str
        """
        self._transacao_segura = transacao_segura

    @property
    def valor_compra(self):
        """
        Gets the valor_compra of this CompraContestadaTransacaoResponse.


        :return: The valor_compra of this CompraContestadaTransacaoResponse.
        :rtype: float
        """
        return self._valor_compra

    @valor_compra.setter
    def valor_compra(self, valor_compra):
        """
        Sets the valor_compra of this CompraContestadaTransacaoResponse.


        :param valor_compra: The valor_compra of this CompraContestadaTransacaoResponse.
        :type: float
        """
        self._valor_compra = valor_compra

    @property
    def valor_contrato(self):
        """
        Gets the valor_contrato of this CompraContestadaTransacaoResponse.


        :return: The valor_contrato of this CompraContestadaTransacaoResponse.
        :rtype: float
        """
        return self._valor_contrato

    @valor_contrato.setter
    def valor_contrato(self, valor_contrato):
        """
        Sets the valor_contrato of this CompraContestadaTransacaoResponse.


        :param valor_contrato: The valor_contrato of this CompraContestadaTransacaoResponse.
        :type: float
        """
        self._valor_contrato = valor_contrato

    @property
    def valor_destino(self):
        """
        Gets the valor_destino of this CompraContestadaTransacaoResponse.


        :return: The valor_destino of this CompraContestadaTransacaoResponse.
        :rtype: float
        """
        return self._valor_destino

    @valor_destino.setter
    def valor_destino(self, valor_destino):
        """
        Sets the valor_destino of this CompraContestadaTransacaoResponse.


        :param valor_destino: The valor_destino of this CompraContestadaTransacaoResponse.
        :type: float
        """
        self._valor_destino = valor_destino

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

