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


class TransacoesCorrentes(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TransacoesCorrentes - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'tipo_transacao': 'str',
            'status_transacao': 'str',
            'id_evento': 'int',
            'tipo_evento': 'str',
            'id_conta': 'int',
            'cartao_mascarado': 'str',
            'nome_portador': 'str',
            'data_transacao_utc': 'str',
            'data_faturamento': 'str',
            'data_vencimento': 'str',
            'modo_entrada_transacao': 'str',
            'valor_taxa_embarque': 'float',
            'valor_entrada': 'float',
            'valor_brl': 'float',
            'valor_usd': 'float',
            'cotacao_usd': 'float',
            'data_cotacao_usd': 'str',
            'codigo_moeda_origem': 'str',
            'codigo_moeda_destino': 'str',
            'codigo_autorizacao': 'str',
            'codigo_referencia': 'str',
            'codigo_terminal': 'str',
            'codigo_mcc': 'int',
            'grupo_mcc': 'int',
            'grupo_descricao_mcc': 'str',
            'id_estabelecimento': 'int',
            'nome_estabelecimento': 'str',
            'localidade_estabelecimento': 'str',
            'plano_parcelamento': 'int',
            'numero_parcela': 'int',
            'detalhes_transacao': 'str',
            'flag_credito': 'int',
            'flag_faturado': 'int',
            'flag_estorno': 'int',
            'id_transacao_estorno': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'tipo_transacao': 'tipoTransacao',
            'status_transacao': 'statusTransacao',
            'id_evento': 'idEvento',
            'tipo_evento': 'tipoEvento',
            'id_conta': 'idConta',
            'cartao_mascarado': 'cartaoMascarado',
            'nome_portador': 'nomePortador',
            'data_transacao_utc': 'dataTransacaoUTC',
            'data_faturamento': 'dataFaturamento',
            'data_vencimento': 'dataVencimento',
            'modo_entrada_transacao': 'modoEntradaTransacao',
            'valor_taxa_embarque': 'valorTaxaEmbarque',
            'valor_entrada': 'valorEntrada',
            'valor_brl': 'valorBRL',
            'valor_usd': 'valorUSD',
            'cotacao_usd': 'cotacaoUSD',
            'data_cotacao_usd': 'dataCotacaoUSD',
            'codigo_moeda_origem': 'codigoMoedaOrigem',
            'codigo_moeda_destino': 'codigoMoedaDestino',
            'codigo_autorizacao': 'codigoAutorizacao',
            'codigo_referencia': 'codigoReferencia',
            'codigo_terminal': 'codigoTerminal',
            'codigo_mcc': 'codigoMCC',
            'grupo_mcc': 'grupoMCC',
            'grupo_descricao_mcc': 'grupoDescricaoMCC',
            'id_estabelecimento': 'idEstabelecimento',
            'nome_estabelecimento': 'nomeEstabelecimento',
            'localidade_estabelecimento': 'localidadeEstabelecimento',
            'plano_parcelamento': 'planoParcelamento',
            'numero_parcela': 'numeroParcela',
            'detalhes_transacao': 'detalhesTransacao',
            'flag_credito': 'flagCredito',
            'flag_faturado': 'flagFaturado',
            'flag_estorno': 'flagEstorno',
            'id_transacao_estorno': 'idTransacaoEstorno'
        }

        self._id = None
        self._tipo_transacao = None
        self._status_transacao = None
        self._id_evento = None
        self._tipo_evento = None
        self._id_conta = None
        self._cartao_mascarado = None
        self._nome_portador = None
        self._data_transacao_utc = None
        self._data_faturamento = None
        self._data_vencimento = None
        self._modo_entrada_transacao = None
        self._valor_taxa_embarque = None
        self._valor_entrada = None
        self._valor_brl = None
        self._valor_usd = None
        self._cotacao_usd = None
        self._data_cotacao_usd = None
        self._codigo_moeda_origem = None
        self._codigo_moeda_destino = None
        self._codigo_autorizacao = None
        self._codigo_referencia = None
        self._codigo_terminal = None
        self._codigo_mcc = None
        self._grupo_mcc = None
        self._grupo_descricao_mcc = None
        self._id_estabelecimento = None
        self._nome_estabelecimento = None
        self._localidade_estabelecimento = None
        self._plano_parcelamento = None
        self._numero_parcela = None
        self._detalhes_transacao = None
        self._flag_credito = None
        self._flag_faturado = None
        self._flag_estorno = None
        self._id_transacao_estorno = None

    @property
    def id(self):
        """
        Gets the id of this TransacoesCorrentes.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da transfer\u00C3\u00AAncia (id).

        :return: The id of this TransacoesCorrentes.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TransacoesCorrentes.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da transfer\u00C3\u00AAncia (id).

        :param id: The id of this TransacoesCorrentes.
        :type: int
        """
        self._id = id

    @property
    def tipo_transacao(self):
        """
        Gets the tipo_transacao of this TransacoesCorrentes.
        Descri\u00C3\u00A7\u00C3\u00A3o do Tipo da Transa\u00C3\u00A7\u00C3\u00A3o.

        :return: The tipo_transacao of this TransacoesCorrentes.
        :rtype: str
        """
        return self._tipo_transacao

    @tipo_transacao.setter
    def tipo_transacao(self, tipo_transacao):
        """
        Sets the tipo_transacao of this TransacoesCorrentes.
        Descri\u00C3\u00A7\u00C3\u00A3o do Tipo da Transa\u00C3\u00A7\u00C3\u00A3o.

        :param tipo_transacao: The tipo_transacao of this TransacoesCorrentes.
        :type: str
        """
        self._tipo_transacao = tipo_transacao

    @property
    def status_transacao(self):
        """
        Gets the status_transacao of this TransacoesCorrentes.
        Status de Processamento da Transa\u00C3\u00A7\u00C3\u00A3o.

        :return: The status_transacao of this TransacoesCorrentes.
        :rtype: str
        """
        return self._status_transacao

    @status_transacao.setter
    def status_transacao(self, status_transacao):
        """
        Sets the status_transacao of this TransacoesCorrentes.
        Status de Processamento da Transa\u00C3\u00A7\u00C3\u00A3o.

        :param status_transacao: The status_transacao of this TransacoesCorrentes.
        :type: str
        """
        self._status_transacao = status_transacao

    @property
    def id_evento(self):
        """
        Gets the id_evento of this TransacoesCorrentes.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Evento que originou a Transa\u00C3\u00A7\u00C3\u00A3o (id).

        :return: The id_evento of this TransacoesCorrentes.
        :rtype: int
        """
        return self._id_evento

    @id_evento.setter
    def id_evento(self, id_evento):
        """
        Sets the id_evento of this TransacoesCorrentes.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Evento que originou a Transa\u00C3\u00A7\u00C3\u00A3o (id).

        :param id_evento: The id_evento of this TransacoesCorrentes.
        :type: int
        """
        self._id_evento = id_evento

    @property
    def tipo_evento(self):
        """
        Gets the tipo_evento of this TransacoesCorrentes.
        Descri\u00C3\u00A7\u00C3\u00A3o do Evento que representa a Transa\u00C3\u00A7\u00C3\u00A3o.

        :return: The tipo_evento of this TransacoesCorrentes.
        :rtype: str
        """
        return self._tipo_evento

    @tipo_evento.setter
    def tipo_evento(self, tipo_evento):
        """
        Sets the tipo_evento of this TransacoesCorrentes.
        Descri\u00C3\u00A7\u00C3\u00A3o do Evento que representa a Transa\u00C3\u00A7\u00C3\u00A3o.

        :param tipo_evento: The tipo_evento of this TransacoesCorrentes.
        :type: str
        """
        self._tipo_evento = tipo_evento

    @property
    def id_conta(self):
        """
        Gets the id_conta of this TransacoesCorrentes.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Conta (id).

        :return: The id_conta of this TransacoesCorrentes.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this TransacoesCorrentes.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Conta (id).

        :param id_conta: The id_conta of this TransacoesCorrentes.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def cartao_mascarado(self):
        """
        Gets the cartao_mascarado of this TransacoesCorrentes.
        N\u00C3\u00BAmero do Cart\u00C3\u00A3o em Formato 0000XXXXXXXX0000.

        :return: The cartao_mascarado of this TransacoesCorrentes.
        :rtype: str
        """
        return self._cartao_mascarado

    @cartao_mascarado.setter
    def cartao_mascarado(self, cartao_mascarado):
        """
        Sets the cartao_mascarado of this TransacoesCorrentes.
        N\u00C3\u00BAmero do Cart\u00C3\u00A3o em Formato 0000XXXXXXXX0000.

        :param cartao_mascarado: The cartao_mascarado of this TransacoesCorrentes.
        :type: str
        """
        self._cartao_mascarado = cartao_mascarado

    @property
    def nome_portador(self):
        """
        Gets the nome_portador of this TransacoesCorrentes.
        Nome completo do Portador do Cart\u00C3\u00A3o.

        :return: The nome_portador of this TransacoesCorrentes.
        :rtype: str
        """
        return self._nome_portador

    @nome_portador.setter
    def nome_portador(self, nome_portador):
        """
        Sets the nome_portador of this TransacoesCorrentes.
        Nome completo do Portador do Cart\u00C3\u00A3o.

        :param nome_portador: The nome_portador of this TransacoesCorrentes.
        :type: str
        """
        self._nome_portador = nome_portador

    @property
    def data_transacao_utc(self):
        """
        Gets the data_transacao_utc of this TransacoesCorrentes.
        Data em que a Transa\u00C3\u00A7\u00C3\u00A3o foi realizada sob o padr\u00C3\u00A3o de Tempo Universal Coordenado (UTC).

        :return: The data_transacao_utc of this TransacoesCorrentes.
        :rtype: str
        """
        return self._data_transacao_utc

    @data_transacao_utc.setter
    def data_transacao_utc(self, data_transacao_utc):
        """
        Sets the data_transacao_utc of this TransacoesCorrentes.
        Data em que a Transa\u00C3\u00A7\u00C3\u00A3o foi realizada sob o padr\u00C3\u00A3o de Tempo Universal Coordenado (UTC).

        :param data_transacao_utc: The data_transacao_utc of this TransacoesCorrentes.
        :type: str
        """
        self._data_transacao_utc = data_transacao_utc

    @property
    def data_faturamento(self):
        """
        Gets the data_faturamento of this TransacoesCorrentes.
        Data de Faturamento da Transa\u00C3\u00A7\u00C3\u00A3o.

        :return: The data_faturamento of this TransacoesCorrentes.
        :rtype: str
        """
        return self._data_faturamento

    @data_faturamento.setter
    def data_faturamento(self, data_faturamento):
        """
        Sets the data_faturamento of this TransacoesCorrentes.
        Data de Faturamento da Transa\u00C3\u00A7\u00C3\u00A3o.

        :param data_faturamento: The data_faturamento of this TransacoesCorrentes.
        :type: str
        """
        self._data_faturamento = data_faturamento

    @property
    def data_vencimento(self):
        """
        Gets the data_vencimento of this TransacoesCorrentes.
        Data de Vencimento da Fatura.

        :return: The data_vencimento of this TransacoesCorrentes.
        :rtype: str
        """
        return self._data_vencimento

    @data_vencimento.setter
    def data_vencimento(self, data_vencimento):
        """
        Sets the data_vencimento of this TransacoesCorrentes.
        Data de Vencimento da Fatura.

        :param data_vencimento: The data_vencimento of this TransacoesCorrentes.
        :type: str
        """
        self._data_vencimento = data_vencimento

    @property
    def modo_entrada_transacao(self):
        """
        Gets the modo_entrada_transacao of this TransacoesCorrentes.
        Descreve o modo utilizado para realizar a leitura dos dados do cart\u00C3\u00A3o para realizar a Transa\u00C3\u00A7\u00C3\u00A3o.

        :return: The modo_entrada_transacao of this TransacoesCorrentes.
        :rtype: str
        """
        return self._modo_entrada_transacao

    @modo_entrada_transacao.setter
    def modo_entrada_transacao(self, modo_entrada_transacao):
        """
        Sets the modo_entrada_transacao of this TransacoesCorrentes.
        Descreve o modo utilizado para realizar a leitura dos dados do cart\u00C3\u00A3o para realizar a Transa\u00C3\u00A7\u00C3\u00A3o.

        :param modo_entrada_transacao: The modo_entrada_transacao of this TransacoesCorrentes.
        :type: str
        """
        self._modo_entrada_transacao = modo_entrada_transacao

    @property
    def valor_taxa_embarque(self):
        """
        Gets the valor_taxa_embarque of this TransacoesCorrentes.
        Valor da Taxa de Embarque em Real (BRL) quando a transa\u00C3\u00A7\u00C3\u00A3o for relacionada a Compra de Passagens A\u00C3\u00A9reas.

        :return: The valor_taxa_embarque of this TransacoesCorrentes.
        :rtype: float
        """
        return self._valor_taxa_embarque

    @valor_taxa_embarque.setter
    def valor_taxa_embarque(self, valor_taxa_embarque):
        """
        Sets the valor_taxa_embarque of this TransacoesCorrentes.
        Valor da Taxa de Embarque em Real (BRL) quando a transa\u00C3\u00A7\u00C3\u00A3o for relacionada a Compra de Passagens A\u00C3\u00A9reas.

        :param valor_taxa_embarque: The valor_taxa_embarque of this TransacoesCorrentes.
        :type: float
        """
        self._valor_taxa_embarque = valor_taxa_embarque

    @property
    def valor_entrada(self):
        """
        Gets the valor_entrada of this TransacoesCorrentes.
        Valor da Entrada em Real (BRL) quando a transa\u00C3\u00A7\u00C3\u00A3o for do tipo Parcelada com o pagamento de um valor de Entrada.

        :return: The valor_entrada of this TransacoesCorrentes.
        :rtype: float
        """
        return self._valor_entrada

    @valor_entrada.setter
    def valor_entrada(self, valor_entrada):
        """
        Sets the valor_entrada of this TransacoesCorrentes.
        Valor da Entrada em Real (BRL) quando a transa\u00C3\u00A7\u00C3\u00A3o for do tipo Parcelada com o pagamento de um valor de Entrada.

        :param valor_entrada: The valor_entrada of this TransacoesCorrentes.
        :type: float
        """
        self._valor_entrada = valor_entrada

    @property
    def valor_brl(self):
        """
        Gets the valor_brl of this TransacoesCorrentes.
        Valor da Transa\u00C3\u00A7\u00C3\u00A3o em Real (BRL).

        :return: The valor_brl of this TransacoesCorrentes.
        :rtype: float
        """
        return self._valor_brl

    @valor_brl.setter
    def valor_brl(self, valor_brl):
        """
        Sets the valor_brl of this TransacoesCorrentes.
        Valor da Transa\u00C3\u00A7\u00C3\u00A3o em Real (BRL).

        :param valor_brl: The valor_brl of this TransacoesCorrentes.
        :type: float
        """
        self._valor_brl = valor_brl

    @property
    def valor_usd(self):
        """
        Gets the valor_usd of this TransacoesCorrentes.
        Valor da Transa\u00C3\u00A7\u00C3\u00A3o em D\u00C3\u00B3lar Americano (USD).

        :return: The valor_usd of this TransacoesCorrentes.
        :rtype: float
        """
        return self._valor_usd

    @valor_usd.setter
    def valor_usd(self, valor_usd):
        """
        Sets the valor_usd of this TransacoesCorrentes.
        Valor da Transa\u00C3\u00A7\u00C3\u00A3o em D\u00C3\u00B3lar Americano (USD).

        :param valor_usd: The valor_usd of this TransacoesCorrentes.
        :type: float
        """
        self._valor_usd = valor_usd

    @property
    def cotacao_usd(self):
        """
        Gets the cotacao_usd of this TransacoesCorrentes.
        Valor do D\u00C3\u00B3lar Americano (USD) convertido em Real (BRL).

        :return: The cotacao_usd of this TransacoesCorrentes.
        :rtype: float
        """
        return self._cotacao_usd

    @cotacao_usd.setter
    def cotacao_usd(self, cotacao_usd):
        """
        Sets the cotacao_usd of this TransacoesCorrentes.
        Valor do D\u00C3\u00B3lar Americano (USD) convertido em Real (BRL).

        :param cotacao_usd: The cotacao_usd of this TransacoesCorrentes.
        :type: float
        """
        self._cotacao_usd = cotacao_usd

    @property
    def data_cotacao_usd(self):
        """
        Gets the data_cotacao_usd of this TransacoesCorrentes.
        Data de Fechamento da Cota\u00C3\u00A7\u00C3\u00A3o do D\u00C3\u00B3lar Americano (USD).

        :return: The data_cotacao_usd of this TransacoesCorrentes.
        :rtype: str
        """
        return self._data_cotacao_usd

    @data_cotacao_usd.setter
    def data_cotacao_usd(self, data_cotacao_usd):
        """
        Sets the data_cotacao_usd of this TransacoesCorrentes.
        Data de Fechamento da Cota\u00C3\u00A7\u00C3\u00A3o do D\u00C3\u00B3lar Americano (USD).

        :param data_cotacao_usd: The data_cotacao_usd of this TransacoesCorrentes.
        :type: str
        """
        self._data_cotacao_usd = data_cotacao_usd

    @property
    def codigo_moeda_origem(self):
        """
        Gets the codigo_moeda_origem of this TransacoesCorrentes.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Moeda utilizada na Transa\u00C3\u00A7\u00C3\u00A3o, seguindo padr\u00C3\u00A3o ISO 4217.

        :return: The codigo_moeda_origem of this TransacoesCorrentes.
        :rtype: str
        """
        return self._codigo_moeda_origem

    @codigo_moeda_origem.setter
    def codigo_moeda_origem(self, codigo_moeda_origem):
        """
        Sets the codigo_moeda_origem of this TransacoesCorrentes.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Moeda utilizada na Transa\u00C3\u00A7\u00C3\u00A3o, seguindo padr\u00C3\u00A3o ISO 4217.

        :param codigo_moeda_origem: The codigo_moeda_origem of this TransacoesCorrentes.
        :type: str
        """
        self._codigo_moeda_origem = codigo_moeda_origem

    @property
    def codigo_moeda_destino(self):
        """
        Gets the codigo_moeda_destino of this TransacoesCorrentes.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Moeda da Transa\u00C3\u00A7\u00C3\u00A3o ap\u00C3\u00B3s a convers\u00C3\u00A3o, seguindo padr\u00C3\u00A3o ISO 4217.

        :return: The codigo_moeda_destino of this TransacoesCorrentes.
        :rtype: str
        """
        return self._codigo_moeda_destino

    @codigo_moeda_destino.setter
    def codigo_moeda_destino(self, codigo_moeda_destino):
        """
        Sets the codigo_moeda_destino of this TransacoesCorrentes.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Moeda da Transa\u00C3\u00A7\u00C3\u00A3o ap\u00C3\u00B3s a convers\u00C3\u00A3o, seguindo padr\u00C3\u00A3o ISO 4217.

        :param codigo_moeda_destino: The codigo_moeda_destino of this TransacoesCorrentes.
        :type: str
        """
        self._codigo_moeda_destino = codigo_moeda_destino

    @property
    def codigo_autorizacao(self):
        """
        Gets the codigo_autorizacao of this TransacoesCorrentes.
        C\u00C3\u00B3digo de Autoriza\u00C3\u00A7\u00C3\u00A3o da Transa\u00C3\u00A7\u00C3\u00A3o.

        :return: The codigo_autorizacao of this TransacoesCorrentes.
        :rtype: str
        """
        return self._codigo_autorizacao

    @codigo_autorizacao.setter
    def codigo_autorizacao(self, codigo_autorizacao):
        """
        Sets the codigo_autorizacao of this TransacoesCorrentes.
        C\u00C3\u00B3digo de Autoriza\u00C3\u00A7\u00C3\u00A3o da Transa\u00C3\u00A7\u00C3\u00A3o.

        :param codigo_autorizacao: The codigo_autorizacao of this TransacoesCorrentes.
        :type: str
        """
        self._codigo_autorizacao = codigo_autorizacao

    @property
    def codigo_referencia(self):
        """
        Gets the codigo_referencia of this TransacoesCorrentes.
        C\u00C3\u00B3digo de Refer\u00C3\u00AAncia da Transa\u00C3\u00A7\u00C3\u00A3o quando utilizado Cart\u00C3\u00A3o Bandeirado.

        :return: The codigo_referencia of this TransacoesCorrentes.
        :rtype: str
        """
        return self._codigo_referencia

    @codigo_referencia.setter
    def codigo_referencia(self, codigo_referencia):
        """
        Sets the codigo_referencia of this TransacoesCorrentes.
        C\u00C3\u00B3digo de Refer\u00C3\u00AAncia da Transa\u00C3\u00A7\u00C3\u00A3o quando utilizado Cart\u00C3\u00A3o Bandeirado.

        :param codigo_referencia: The codigo_referencia of this TransacoesCorrentes.
        :type: str
        """
        self._codigo_referencia = codigo_referencia

    @property
    def codigo_terminal(self):
        """
        Gets the codigo_terminal of this TransacoesCorrentes.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da origem da captura da Transa\u00C3\u00A7\u00C3\u00A3o.

        :return: The codigo_terminal of this TransacoesCorrentes.
        :rtype: str
        """
        return self._codigo_terminal

    @codigo_terminal.setter
    def codigo_terminal(self, codigo_terminal):
        """
        Sets the codigo_terminal of this TransacoesCorrentes.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da origem da captura da Transa\u00C3\u00A7\u00C3\u00A3o.

        :param codigo_terminal: The codigo_terminal of this TransacoesCorrentes.
        :type: str
        """
        self._codigo_terminal = codigo_terminal

    @property
    def codigo_mcc(self):
        """
        Gets the codigo_mcc of this TransacoesCorrentes.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da categoria do Estabelecimento.

        :return: The codigo_mcc of this TransacoesCorrentes.
        :rtype: int
        """
        return self._codigo_mcc

    @codigo_mcc.setter
    def codigo_mcc(self, codigo_mcc):
        """
        Sets the codigo_mcc of this TransacoesCorrentes.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da categoria do Estabelecimento.

        :param codigo_mcc: The codigo_mcc of this TransacoesCorrentes.
        :type: int
        """
        self._codigo_mcc = codigo_mcc

    @property
    def grupo_mcc(self):
        """
        Gets the grupo_mcc of this TransacoesCorrentes.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do grupo do Estabelecimento.

        :return: The grupo_mcc of this TransacoesCorrentes.
        :rtype: int
        """
        return self._grupo_mcc

    @grupo_mcc.setter
    def grupo_mcc(self, grupo_mcc):
        """
        Sets the grupo_mcc of this TransacoesCorrentes.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do grupo do Estabelecimento.

        :param grupo_mcc: The grupo_mcc of this TransacoesCorrentes.
        :type: int
        """
        self._grupo_mcc = grupo_mcc

    @property
    def grupo_descricao_mcc(self):
        """
        Gets the grupo_descricao_mcc of this TransacoesCorrentes.
        Descri\u00C3\u00A7\u00C3\u00A3o do grupo do Estabelecimento.

        :return: The grupo_descricao_mcc of this TransacoesCorrentes.
        :rtype: str
        """
        return self._grupo_descricao_mcc

    @grupo_descricao_mcc.setter
    def grupo_descricao_mcc(self, grupo_descricao_mcc):
        """
        Sets the grupo_descricao_mcc of this TransacoesCorrentes.
        Descri\u00C3\u00A7\u00C3\u00A3o do grupo do Estabelecimento.

        :param grupo_descricao_mcc: The grupo_descricao_mcc of this TransacoesCorrentes.
        :type: str
        """
        self._grupo_descricao_mcc = grupo_descricao_mcc

    @property
    def id_estabelecimento(self):
        """
        Gets the id_estabelecimento of this TransacoesCorrentes.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Estabelecimento (id).

        :return: The id_estabelecimento of this TransacoesCorrentes.
        :rtype: int
        """
        return self._id_estabelecimento

    @id_estabelecimento.setter
    def id_estabelecimento(self, id_estabelecimento):
        """
        Sets the id_estabelecimento of this TransacoesCorrentes.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Estabelecimento (id).

        :param id_estabelecimento: The id_estabelecimento of this TransacoesCorrentes.
        :type: int
        """
        self._id_estabelecimento = id_estabelecimento

    @property
    def nome_estabelecimento(self):
        """
        Gets the nome_estabelecimento of this TransacoesCorrentes.
        Nome do Estabelecimento.

        :return: The nome_estabelecimento of this TransacoesCorrentes.
        :rtype: str
        """
        return self._nome_estabelecimento

    @nome_estabelecimento.setter
    def nome_estabelecimento(self, nome_estabelecimento):
        """
        Sets the nome_estabelecimento of this TransacoesCorrentes.
        Nome do Estabelecimento.

        :param nome_estabelecimento: The nome_estabelecimento of this TransacoesCorrentes.
        :type: str
        """
        self._nome_estabelecimento = nome_estabelecimento

    @property
    def localidade_estabelecimento(self):
        """
        Gets the localidade_estabelecimento of this TransacoesCorrentes.
        Localidade do Estabelecimento.

        :return: The localidade_estabelecimento of this TransacoesCorrentes.
        :rtype: str
        """
        return self._localidade_estabelecimento

    @localidade_estabelecimento.setter
    def localidade_estabelecimento(self, localidade_estabelecimento):
        """
        Sets the localidade_estabelecimento of this TransacoesCorrentes.
        Localidade do Estabelecimento.

        :param localidade_estabelecimento: The localidade_estabelecimento of this TransacoesCorrentes.
        :type: str
        """
        self._localidade_estabelecimento = localidade_estabelecimento

    @property
    def plano_parcelamento(self):
        """
        Gets the plano_parcelamento of this TransacoesCorrentes.
        Quando a Transa\u00C3\u00A7\u00C3\u00A3o for do tipo Parcelada, apresenta o n\u00C3\u00BAmero total de Parcelas.

        :return: The plano_parcelamento of this TransacoesCorrentes.
        :rtype: int
        """
        return self._plano_parcelamento

    @plano_parcelamento.setter
    def plano_parcelamento(self, plano_parcelamento):
        """
        Sets the plano_parcelamento of this TransacoesCorrentes.
        Quando a Transa\u00C3\u00A7\u00C3\u00A3o for do tipo Parcelada, apresenta o n\u00C3\u00BAmero total de Parcelas.

        :param plano_parcelamento: The plano_parcelamento of this TransacoesCorrentes.
        :type: int
        """
        self._plano_parcelamento = plano_parcelamento

    @property
    def numero_parcela(self):
        """
        Gets the numero_parcela of this TransacoesCorrentes.
        Quando a Transa\u00C3\u00A7\u00C3\u00A3o for do tipo Parcelada, apresenta o n\u00C3\u00BAmero da Parcela.

        :return: The numero_parcela of this TransacoesCorrentes.
        :rtype: int
        """
        return self._numero_parcela

    @numero_parcela.setter
    def numero_parcela(self, numero_parcela):
        """
        Sets the numero_parcela of this TransacoesCorrentes.
        Quando a Transa\u00C3\u00A7\u00C3\u00A3o for do tipo Parcelada, apresenta o n\u00C3\u00BAmero da Parcela.

        :param numero_parcela: The numero_parcela of this TransacoesCorrentes.
        :type: int
        """
        self._numero_parcela = numero_parcela

    @property
    def detalhes_transacao(self):
        """
        Gets the detalhes_transacao of this TransacoesCorrentes.
        Detalhes complementares a respeito da Transa\u00C3\u00A7\u00C3\u00A3o.

        :return: The detalhes_transacao of this TransacoesCorrentes.
        :rtype: str
        """
        return self._detalhes_transacao

    @detalhes_transacao.setter
    def detalhes_transacao(self, detalhes_transacao):
        """
        Sets the detalhes_transacao of this TransacoesCorrentes.
        Detalhes complementares a respeito da Transa\u00C3\u00A7\u00C3\u00A3o.

        :param detalhes_transacao: The detalhes_transacao of this TransacoesCorrentes.
        :type: str
        """
        self._detalhes_transacao = detalhes_transacao

    @property
    def flag_credito(self):
        """
        Gets the flag_credito of this TransacoesCorrentes.
        Quando ativa, indica que a Transa\u00C3\u00A7\u00C3\u00A3o \u00C3\u00A9 do Tipo 'Cr\u00C3\u00A9dito'.

        :return: The flag_credito of this TransacoesCorrentes.
        :rtype: int
        """
        return self._flag_credito

    @flag_credito.setter
    def flag_credito(self, flag_credito):
        """
        Sets the flag_credito of this TransacoesCorrentes.
        Quando ativa, indica que a Transa\u00C3\u00A7\u00C3\u00A3o \u00C3\u00A9 do Tipo 'Cr\u00C3\u00A9dito'.

        :param flag_credito: The flag_credito of this TransacoesCorrentes.
        :type: int
        """
        self._flag_credito = flag_credito

    @property
    def flag_faturado(self):
        """
        Gets the flag_faturado of this TransacoesCorrentes.
        Quando ativa, indica que a Transa\u00C3\u00A7\u00C3\u00A3o foi consolidada em uma Fatura.

        :return: The flag_faturado of this TransacoesCorrentes.
        :rtype: int
        """
        return self._flag_faturado

    @flag_faturado.setter
    def flag_faturado(self, flag_faturado):
        """
        Sets the flag_faturado of this TransacoesCorrentes.
        Quando ativa, indica que a Transa\u00C3\u00A7\u00C3\u00A3o foi consolidada em uma Fatura.

        :param flag_faturado: The flag_faturado of this TransacoesCorrentes.
        :type: int
        """
        self._flag_faturado = flag_faturado

    @property
    def flag_estorno(self):
        """
        Gets the flag_estorno of this TransacoesCorrentes.
        Quando ativa, indica que a Transa\u00C3\u00A7\u00C3\u00A3o foi estornada.

        :return: The flag_estorno of this TransacoesCorrentes.
        :rtype: int
        """
        return self._flag_estorno

    @flag_estorno.setter
    def flag_estorno(self, flag_estorno):
        """
        Sets the flag_estorno of this TransacoesCorrentes.
        Quando ativa, indica que a Transa\u00C3\u00A7\u00C3\u00A3o foi estornada.

        :param flag_estorno: The flag_estorno of this TransacoesCorrentes.
        :type: int
        """
        self._flag_estorno = flag_estorno

    @property
    def id_transacao_estorno(self):
        """
        Gets the id_transacao_estorno of this TransacoesCorrentes.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Transa\u00C3\u00A7\u00C3\u00A3o (id) que gerou o estorno.

        :return: The id_transacao_estorno of this TransacoesCorrentes.
        :rtype: int
        """
        return self._id_transacao_estorno

    @id_transacao_estorno.setter
    def id_transacao_estorno(self, id_transacao_estorno):
        """
        Sets the id_transacao_estorno of this TransacoesCorrentes.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Transa\u00C3\u00A7\u00C3\u00A3o (id) que gerou o estorno.

        :param id_transacao_estorno: The id_transacao_estorno of this TransacoesCorrentes.
        :type: int
        """
        self._id_transacao_estorno = id_transacao_estorno

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

