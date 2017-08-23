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


class AntecipacaoSimuladaResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AntecipacaoSimuladaResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_antecipacao_simulada': 'int',
            'id_conta': 'int',
            'id_compra': 'int',
            'id_tipo_transacao': 'int',
            'quantidade_parcelas_antecipaveis': 'int',
            'valor_parcela': 'float',
            'data_hora_simulacao': 'str',
            'taxa_antecipacao_ano': 'float',
            'detalhes': 'list[AntecipacaoSimuladaDetalhesResponse]'
        }

        self.attribute_map = {
            'id_antecipacao_simulada': 'idAntecipacaoSimulada',
            'id_conta': 'idConta',
            'id_compra': 'idCompra',
            'id_tipo_transacao': 'idTipoTransacao',
            'quantidade_parcelas_antecipaveis': 'quantidadeParcelasAntecipaveis',
            'valor_parcela': 'valorParcela',
            'data_hora_simulacao': 'dataHoraSimulacao',
            'taxa_antecipacao_ano': 'taxaAntecipacaoAno',
            'detalhes': 'detalhes'
        }

        self._id_antecipacao_simulada = None
        self._id_conta = None
        self._id_compra = None
        self._id_tipo_transacao = None
        self._quantidade_parcelas_antecipaveis = None
        self._valor_parcela = None
        self._data_hora_simulacao = None
        self._taxa_antecipacao_ano = None
        self._detalhes = None

    @property
    def id_antecipacao_simulada(self):
        """
        Gets the id_antecipacao_simulada of this AntecipacaoSimuladaResponse.
        C\u00C3\u00B3digo identificador da simula\u00C3\u00A7\u00C3\u00A3o de antecipa\u00C3\u00A7\u00C3\u00A3o.

        :return: The id_antecipacao_simulada of this AntecipacaoSimuladaResponse.
        :rtype: int
        """
        return self._id_antecipacao_simulada

    @id_antecipacao_simulada.setter
    def id_antecipacao_simulada(self, id_antecipacao_simulada):
        """
        Sets the id_antecipacao_simulada of this AntecipacaoSimuladaResponse.
        C\u00C3\u00B3digo identificador da simula\u00C3\u00A7\u00C3\u00A3o de antecipa\u00C3\u00A7\u00C3\u00A3o.

        :param id_antecipacao_simulada: The id_antecipacao_simulada of this AntecipacaoSimuladaResponse.
        :type: int
        """
        self._id_antecipacao_simulada = id_antecipacao_simulada

    @property
    def id_conta(self):
        """
        Gets the id_conta of this AntecipacaoSimuladaResponse.
        C\u00C3\u00B3digo identificador da conta.

        :return: The id_conta of this AntecipacaoSimuladaResponse.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this AntecipacaoSimuladaResponse.
        C\u00C3\u00B3digo identificador da conta.

        :param id_conta: The id_conta of this AntecipacaoSimuladaResponse.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def id_compra(self):
        """
        Gets the id_compra of this AntecipacaoSimuladaResponse.
        C\u00C3\u00B3digo identificador do evento compra.

        :return: The id_compra of this AntecipacaoSimuladaResponse.
        :rtype: int
        """
        return self._id_compra

    @id_compra.setter
    def id_compra(self, id_compra):
        """
        Sets the id_compra of this AntecipacaoSimuladaResponse.
        C\u00C3\u00B3digo identificador do evento compra.

        :param id_compra: The id_compra of this AntecipacaoSimuladaResponse.
        :type: int
        """
        self._id_compra = id_compra

    @property
    def id_tipo_transacao(self):
        """
        Gets the id_tipo_transacao of this AntecipacaoSimuladaResponse.
        C\u00C3\u00B3digo identificador do tipo do evento compra.

        :return: The id_tipo_transacao of this AntecipacaoSimuladaResponse.
        :rtype: int
        """
        return self._id_tipo_transacao

    @id_tipo_transacao.setter
    def id_tipo_transacao(self, id_tipo_transacao):
        """
        Sets the id_tipo_transacao of this AntecipacaoSimuladaResponse.
        C\u00C3\u00B3digo identificador do tipo do evento compra.

        :param id_tipo_transacao: The id_tipo_transacao of this AntecipacaoSimuladaResponse.
        :type: int
        """
        self._id_tipo_transacao = id_tipo_transacao

    @property
    def quantidade_parcelas_antecipaveis(self):
        """
        Gets the quantidade_parcelas_antecipaveis of this AntecipacaoSimuladaResponse.
        Quantidade de parcelas antecip\u00C3\u00A1veis.

        :return: The quantidade_parcelas_antecipaveis of this AntecipacaoSimuladaResponse.
        :rtype: int
        """
        return self._quantidade_parcelas_antecipaveis

    @quantidade_parcelas_antecipaveis.setter
    def quantidade_parcelas_antecipaveis(self, quantidade_parcelas_antecipaveis):
        """
        Sets the quantidade_parcelas_antecipaveis of this AntecipacaoSimuladaResponse.
        Quantidade de parcelas antecip\u00C3\u00A1veis.

        :param quantidade_parcelas_antecipaveis: The quantidade_parcelas_antecipaveis of this AntecipacaoSimuladaResponse.
        :type: int
        """
        self._quantidade_parcelas_antecipaveis = quantidade_parcelas_antecipaveis

    @property
    def valor_parcela(self):
        """
        Gets the valor_parcela of this AntecipacaoSimuladaResponse.
        Valor da parcela.

        :return: The valor_parcela of this AntecipacaoSimuladaResponse.
        :rtype: float
        """
        return self._valor_parcela

    @valor_parcela.setter
    def valor_parcela(self, valor_parcela):
        """
        Sets the valor_parcela of this AntecipacaoSimuladaResponse.
        Valor da parcela.

        :param valor_parcela: The valor_parcela of this AntecipacaoSimuladaResponse.
        :type: float
        """
        self._valor_parcela = valor_parcela

    @property
    def data_hora_simulacao(self):
        """
        Gets the data_hora_simulacao of this AntecipacaoSimuladaResponse.
        Data e hora em que a simula\u00C3\u00A7\u00C3\u00A3o foi feita.

        :return: The data_hora_simulacao of this AntecipacaoSimuladaResponse.
        :rtype: str
        """
        return self._data_hora_simulacao

    @data_hora_simulacao.setter
    def data_hora_simulacao(self, data_hora_simulacao):
        """
        Sets the data_hora_simulacao of this AntecipacaoSimuladaResponse.
        Data e hora em que a simula\u00C3\u00A7\u00C3\u00A3o foi feita.

        :param data_hora_simulacao: The data_hora_simulacao of this AntecipacaoSimuladaResponse.
        :type: str
        """
        self._data_hora_simulacao = data_hora_simulacao

    @property
    def taxa_antecipacao_ano(self):
        """
        Gets the taxa_antecipacao_ano of this AntecipacaoSimuladaResponse.
        Taxa de antecipa\u00C3\u00A7\u00C3\u00A3o aplicada (ao ano).

        :return: The taxa_antecipacao_ano of this AntecipacaoSimuladaResponse.
        :rtype: float
        """
        return self._taxa_antecipacao_ano

    @taxa_antecipacao_ano.setter
    def taxa_antecipacao_ano(self, taxa_antecipacao_ano):
        """
        Sets the taxa_antecipacao_ano of this AntecipacaoSimuladaResponse.
        Taxa de antecipa\u00C3\u00A7\u00C3\u00A3o aplicada (ao ano).

        :param taxa_antecipacao_ano: The taxa_antecipacao_ano of this AntecipacaoSimuladaResponse.
        :type: float
        """
        self._taxa_antecipacao_ano = taxa_antecipacao_ano

    @property
    def detalhes(self):
        """
        Gets the detalhes of this AntecipacaoSimuladaResponse.
        Detalhes da simula\u00C3\u00A7\u00C3\u00A3o.

        :return: The detalhes of this AntecipacaoSimuladaResponse.
        :rtype: list[AntecipacaoSimuladaDetalhesResponse]
        """
        return self._detalhes

    @detalhes.setter
    def detalhes(self, detalhes):
        """
        Sets the detalhes of this AntecipacaoSimuladaResponse.
        Detalhes da simula\u00C3\u00A7\u00C3\u00A3o.

        :param detalhes: The detalhes of this AntecipacaoSimuladaResponse.
        :type: list[AntecipacaoSimuladaDetalhesResponse]
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
