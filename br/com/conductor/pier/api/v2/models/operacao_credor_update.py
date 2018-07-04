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


class OperacaoCredorUpdate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        OperacaoCredorUpdate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_operacao': 'int',
            'id_grupo_economico': 'int',
            'id_produto': 'int',
            'remuneracao_percentual': 'float',
            'remuneracao_fixa': 'float',
            'periodicidade': 'str',
            'vencimento_primeira_parcela': 'int',
            'dias_afastamento': 'int',
            'fator_multiplicador': 'str',
            'flag_taxa_fixada': 'bool',
            'plano_minimo': 'int',
            'plano_maximo': 'int'
        }

        self.attribute_map = {
            'id_operacao': 'idOperacao',
            'id_grupo_economico': 'idGrupoEconomico',
            'id_produto': 'idProduto',
            'remuneracao_percentual': 'remuneracaoPercentual',
            'remuneracao_fixa': 'remuneracaoFixa',
            'periodicidade': 'periodicidade',
            'vencimento_primeira_parcela': 'vencimentoPrimeiraParcela',
            'dias_afastamento': 'diasAfastamento',
            'fator_multiplicador': 'fatorMultiplicador',
            'flag_taxa_fixada': 'flagTaxaFixada',
            'plano_minimo': 'planoMinimo',
            'plano_maximo': 'planoMaximo'
        }

        self._id_operacao = None
        self._id_grupo_economico = None
        self._id_produto = None
        self._remuneracao_percentual = None
        self._remuneracao_fixa = None
        self._periodicidade = None
        self._vencimento_primeira_parcela = None
        self._dias_afastamento = None
        self._fator_multiplicador = None
        self._flag_taxa_fixada = None
        self._plano_minimo = None
        self._plano_maximo = None

    @property
    def id_operacao(self):
        """
        Gets the id_operacao of this OperacaoCredorUpdate.
        {{{operacao_credor_update_id_operacao_value}}}

        :return: The id_operacao of this OperacaoCredorUpdate.
        :rtype: int
        """
        return self._id_operacao

    @id_operacao.setter
    def id_operacao(self, id_operacao):
        """
        Sets the id_operacao of this OperacaoCredorUpdate.
        {{{operacao_credor_update_id_operacao_value}}}

        :param id_operacao: The id_operacao of this OperacaoCredorUpdate.
        :type: int
        """
        self._id_operacao = id_operacao

    @property
    def id_grupo_economico(self):
        """
        Gets the id_grupo_economico of this OperacaoCredorUpdate.
        {{{operacao_credor_update_id_grupo_economico_value}}}

        :return: The id_grupo_economico of this OperacaoCredorUpdate.
        :rtype: int
        """
        return self._id_grupo_economico

    @id_grupo_economico.setter
    def id_grupo_economico(self, id_grupo_economico):
        """
        Sets the id_grupo_economico of this OperacaoCredorUpdate.
        {{{operacao_credor_update_id_grupo_economico_value}}}

        :param id_grupo_economico: The id_grupo_economico of this OperacaoCredorUpdate.
        :type: int
        """
        self._id_grupo_economico = id_grupo_economico

    @property
    def id_produto(self):
        """
        Gets the id_produto of this OperacaoCredorUpdate.
        {{{operacao_credor_update_id_produto_value}}}

        :return: The id_produto of this OperacaoCredorUpdate.
        :rtype: int
        """
        return self._id_produto

    @id_produto.setter
    def id_produto(self, id_produto):
        """
        Sets the id_produto of this OperacaoCredorUpdate.
        {{{operacao_credor_update_id_produto_value}}}

        :param id_produto: The id_produto of this OperacaoCredorUpdate.
        :type: int
        """
        self._id_produto = id_produto

    @property
    def remuneracao_percentual(self):
        """
        Gets the remuneracao_percentual of this OperacaoCredorUpdate.
        {{{operacao_credor_update_remuneracao_percentual_value}}}

        :return: The remuneracao_percentual of this OperacaoCredorUpdate.
        :rtype: float
        """
        return self._remuneracao_percentual

    @remuneracao_percentual.setter
    def remuneracao_percentual(self, remuneracao_percentual):
        """
        Sets the remuneracao_percentual of this OperacaoCredorUpdate.
        {{{operacao_credor_update_remuneracao_percentual_value}}}

        :param remuneracao_percentual: The remuneracao_percentual of this OperacaoCredorUpdate.
        :type: float
        """
        self._remuneracao_percentual = remuneracao_percentual

    @property
    def remuneracao_fixa(self):
        """
        Gets the remuneracao_fixa of this OperacaoCredorUpdate.
        {{{operacao_credor_update_remuneracao_fixa_value}}}

        :return: The remuneracao_fixa of this OperacaoCredorUpdate.
        :rtype: float
        """
        return self._remuneracao_fixa

    @remuneracao_fixa.setter
    def remuneracao_fixa(self, remuneracao_fixa):
        """
        Sets the remuneracao_fixa of this OperacaoCredorUpdate.
        {{{operacao_credor_update_remuneracao_fixa_value}}}

        :param remuneracao_fixa: The remuneracao_fixa of this OperacaoCredorUpdate.
        :type: float
        """
        self._remuneracao_fixa = remuneracao_fixa

    @property
    def periodicidade(self):
        """
        Gets the periodicidade of this OperacaoCredorUpdate.
        {{{operacao_credor_update_periodicidade_value}}}

        :return: The periodicidade of this OperacaoCredorUpdate.
        :rtype: str
        """
        return self._periodicidade

    @periodicidade.setter
    def periodicidade(self, periodicidade):
        """
        Sets the periodicidade of this OperacaoCredorUpdate.
        {{{operacao_credor_update_periodicidade_value}}}

        :param periodicidade: The periodicidade of this OperacaoCredorUpdate.
        :type: str
        """
        allowed_values = ["DIARIO", "SEMANAL", "MENSAL", "DECENDIAL", "QUINZENAL"]
        if periodicidade not in allowed_values:
            raise ValueError(
                "Invalid value for `periodicidade`, must be one of {0}"
                .format(allowed_values)
            )
        self._periodicidade = periodicidade

    @property
    def vencimento_primeira_parcela(self):
        """
        Gets the vencimento_primeira_parcela of this OperacaoCredorUpdate.
        {{{operacao_credor_update_vencimento_primeira_parcela_value}}}

        :return: The vencimento_primeira_parcela of this OperacaoCredorUpdate.
        :rtype: int
        """
        return self._vencimento_primeira_parcela

    @vencimento_primeira_parcela.setter
    def vencimento_primeira_parcela(self, vencimento_primeira_parcela):
        """
        Sets the vencimento_primeira_parcela of this OperacaoCredorUpdate.
        {{{operacao_credor_update_vencimento_primeira_parcela_value}}}

        :param vencimento_primeira_parcela: The vencimento_primeira_parcela of this OperacaoCredorUpdate.
        :type: int
        """
        self._vencimento_primeira_parcela = vencimento_primeira_parcela

    @property
    def dias_afastamento(self):
        """
        Gets the dias_afastamento of this OperacaoCredorUpdate.
        {{{operacao_credor_update_dias_afastamento_value}}}

        :return: The dias_afastamento of this OperacaoCredorUpdate.
        :rtype: int
        """
        return self._dias_afastamento

    @dias_afastamento.setter
    def dias_afastamento(self, dias_afastamento):
        """
        Sets the dias_afastamento of this OperacaoCredorUpdate.
        {{{operacao_credor_update_dias_afastamento_value}}}

        :param dias_afastamento: The dias_afastamento of this OperacaoCredorUpdate.
        :type: int
        """
        self._dias_afastamento = dias_afastamento

    @property
    def fator_multiplicador(self):
        """
        Gets the fator_multiplicador of this OperacaoCredorUpdate.
        {{{operacao_credor_update_fator_multiplicador_value}}}

        :return: The fator_multiplicador of this OperacaoCredorUpdate.
        :rtype: str
        """
        return self._fator_multiplicador

    @fator_multiplicador.setter
    def fator_multiplicador(self, fator_multiplicador):
        """
        Sets the fator_multiplicador of this OperacaoCredorUpdate.
        {{{operacao_credor_update_fator_multiplicador_value}}}

        :param fator_multiplicador: The fator_multiplicador of this OperacaoCredorUpdate.
        :type: str
        """
        allowed_values = ["FORA_AGENDA", "AGENDA", "AGENDA_NEGATIVA"]
        if fator_multiplicador not in allowed_values:
            raise ValueError(
                "Invalid value for `fator_multiplicador`, must be one of {0}"
                .format(allowed_values)
            )
        self._fator_multiplicador = fator_multiplicador

    @property
    def flag_taxa_fixada(self):
        """
        Gets the flag_taxa_fixada of this OperacaoCredorUpdate.
        {{{operacao_credor_update_flag_taxa_fixada_value}}}

        :return: The flag_taxa_fixada of this OperacaoCredorUpdate.
        :rtype: bool
        """
        return self._flag_taxa_fixada

    @flag_taxa_fixada.setter
    def flag_taxa_fixada(self, flag_taxa_fixada):
        """
        Sets the flag_taxa_fixada of this OperacaoCredorUpdate.
        {{{operacao_credor_update_flag_taxa_fixada_value}}}

        :param flag_taxa_fixada: The flag_taxa_fixada of this OperacaoCredorUpdate.
        :type: bool
        """
        self._flag_taxa_fixada = flag_taxa_fixada

    @property
    def plano_minimo(self):
        """
        Gets the plano_minimo of this OperacaoCredorUpdate.
        {{{operacao_credor_update_plano_minimo_value}}}

        :return: The plano_minimo of this OperacaoCredorUpdate.
        :rtype: int
        """
        return self._plano_minimo

    @plano_minimo.setter
    def plano_minimo(self, plano_minimo):
        """
        Sets the plano_minimo of this OperacaoCredorUpdate.
        {{{operacao_credor_update_plano_minimo_value}}}

        :param plano_minimo: The plano_minimo of this OperacaoCredorUpdate.
        :type: int
        """
        self._plano_minimo = plano_minimo

    @property
    def plano_maximo(self):
        """
        Gets the plano_maximo of this OperacaoCredorUpdate.
        {{{operacao_credor_update_plano_maximo_value}}}

        :return: The plano_maximo of this OperacaoCredorUpdate.
        :rtype: int
        """
        return self._plano_maximo

    @plano_maximo.setter
    def plano_maximo(self, plano_maximo):
        """
        Sets the plano_maximo of this OperacaoCredorUpdate.
        {{{operacao_credor_update_plano_maximo_value}}}

        :param plano_maximo: The plano_maximo of this OperacaoCredorUpdate.
        :type: int
        """
        self._plano_maximo = plano_maximo

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

