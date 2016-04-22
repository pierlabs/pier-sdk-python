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


class SaldoLimiteResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SaldoLimiteResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'disponib_compra_nac': 'float',
            'disponib_global_credito': 'float',
            'disponib_parcelado_nac': 'float',
            'disponib_parcelas_nac': 'float',
            'disponib_saque_nac_global': 'float',
            'flag_antecipacao': 'bool',
            'limite_compra_nac': 'float',
            'limite_credito_concedido': 'float',
            'limite_credito_disponivel': 'float',
            'limite_global_credito': 'float',
            'limite_parcelado_nac': 'float',
            'limite_parcelas_nac': 'float',
            'limite_pontuacao': 'float',
            'limite_saque_nac_global': 'float',
            'numero_ciclo': 'int',
            'pontos_concedidos': 'float',
            'pontos_remanescentes': 'float',
            'proximo_vencimento_padrao': 'str',
            'proximo_vencimento_real': 'str',
            'saldo_atual_final': 'float',
            'saldo_credor': 'float',
            'saldo_devedor': 'float',
            'saldo_devedor_oneroso': 'float',
            'saldo_devedor_total': 'float',
            'salta_extrato_anterior': 'float',
            'total_disponivel_utilizacao': 'float',
            'total_futuro': 'float',
            'valor_minimo_extrato': 'float',
            'valor_minimo_extrato_original': 'float',
            'vencimento_padrao_anterior': 'str',
            'vencimento_pos_prox': 'str',
            'vencimento_real_anterior': 'str'
        }

        self.attribute_map = {
            'disponib_compra_nac': 'disponibCompraNac',
            'disponib_global_credito': 'disponibGlobalCredito',
            'disponib_parcelado_nac': 'disponibParceladoNac',
            'disponib_parcelas_nac': 'disponibParcelasNac',
            'disponib_saque_nac_global': 'disponibSaqueNacGlobal',
            'flag_antecipacao': 'flagAntecipacao',
            'limite_compra_nac': 'limiteCompraNac',
            'limite_credito_concedido': 'limiteCreditoConcedido',
            'limite_credito_disponivel': 'limiteCreditoDisponivel',
            'limite_global_credito': 'limiteGlobalCredito',
            'limite_parcelado_nac': 'limiteParceladoNac',
            'limite_parcelas_nac': 'limiteParcelasNac',
            'limite_pontuacao': 'limitePontuacao',
            'limite_saque_nac_global': 'limiteSaqueNacGlobal',
            'numero_ciclo': 'numeroCiclo',
            'pontos_concedidos': 'pontosConcedidos',
            'pontos_remanescentes': 'pontosRemanescentes',
            'proximo_vencimento_padrao': 'proximoVencimentoPadrao',
            'proximo_vencimento_real': 'proximoVencimentoReal',
            'saldo_atual_final': 'saldoAtualFinal',
            'saldo_credor': 'saldoCredor',
            'saldo_devedor': 'saldoDevedor',
            'saldo_devedor_oneroso': 'saldoDevedorOneroso',
            'saldo_devedor_total': 'saldoDevedorTotal',
            'salta_extrato_anterior': 'saltaExtratoAnterior',
            'total_disponivel_utilizacao': 'totalDisponivelUtilizacao',
            'total_futuro': 'totalFuturo',
            'valor_minimo_extrato': 'valorMinimoExtrato',
            'valor_minimo_extrato_original': 'valorMinimoExtratoOriginal',
            'vencimento_padrao_anterior': 'vencimentoPadraoAnterior',
            'vencimento_pos_prox': 'vencimentoPosProx',
            'vencimento_real_anterior': 'vencimentoRealAnterior'
        }

        self._disponib_compra_nac = None
        self._disponib_global_credito = None
        self._disponib_parcelado_nac = None
        self._disponib_parcelas_nac = None
        self._disponib_saque_nac_global = None
        self._flag_antecipacao = None
        self._limite_compra_nac = None
        self._limite_credito_concedido = None
        self._limite_credito_disponivel = None
        self._limite_global_credito = None
        self._limite_parcelado_nac = None
        self._limite_parcelas_nac = None
        self._limite_pontuacao = None
        self._limite_saque_nac_global = None
        self._numero_ciclo = None
        self._pontos_concedidos = None
        self._pontos_remanescentes = None
        self._proximo_vencimento_padrao = None
        self._proximo_vencimento_real = None
        self._saldo_atual_final = None
        self._saldo_credor = None
        self._saldo_devedor = None
        self._saldo_devedor_oneroso = None
        self._saldo_devedor_total = None
        self._salta_extrato_anterior = None
        self._total_disponivel_utilizacao = None
        self._total_futuro = None
        self._valor_minimo_extrato = None
        self._valor_minimo_extrato_original = None
        self._vencimento_padrao_anterior = None
        self._vencimento_pos_prox = None
        self._vencimento_real_anterior = None

    @property
    def disponib_compra_nac(self):
        """
        Gets the disponib_compra_nac of this SaldoLimiteResponse.


        :return: The disponib_compra_nac of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._disponib_compra_nac

    @disponib_compra_nac.setter
    def disponib_compra_nac(self, disponib_compra_nac):
        """
        Sets the disponib_compra_nac of this SaldoLimiteResponse.


        :param disponib_compra_nac: The disponib_compra_nac of this SaldoLimiteResponse.
        :type: float
        """
        self._disponib_compra_nac = disponib_compra_nac

    @property
    def disponib_global_credito(self):
        """
        Gets the disponib_global_credito of this SaldoLimiteResponse.


        :return: The disponib_global_credito of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._disponib_global_credito

    @disponib_global_credito.setter
    def disponib_global_credito(self, disponib_global_credito):
        """
        Sets the disponib_global_credito of this SaldoLimiteResponse.


        :param disponib_global_credito: The disponib_global_credito of this SaldoLimiteResponse.
        :type: float
        """
        self._disponib_global_credito = disponib_global_credito

    @property
    def disponib_parcelado_nac(self):
        """
        Gets the disponib_parcelado_nac of this SaldoLimiteResponse.


        :return: The disponib_parcelado_nac of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._disponib_parcelado_nac

    @disponib_parcelado_nac.setter
    def disponib_parcelado_nac(self, disponib_parcelado_nac):
        """
        Sets the disponib_parcelado_nac of this SaldoLimiteResponse.


        :param disponib_parcelado_nac: The disponib_parcelado_nac of this SaldoLimiteResponse.
        :type: float
        """
        self._disponib_parcelado_nac = disponib_parcelado_nac

    @property
    def disponib_parcelas_nac(self):
        """
        Gets the disponib_parcelas_nac of this SaldoLimiteResponse.


        :return: The disponib_parcelas_nac of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._disponib_parcelas_nac

    @disponib_parcelas_nac.setter
    def disponib_parcelas_nac(self, disponib_parcelas_nac):
        """
        Sets the disponib_parcelas_nac of this SaldoLimiteResponse.


        :param disponib_parcelas_nac: The disponib_parcelas_nac of this SaldoLimiteResponse.
        :type: float
        """
        self._disponib_parcelas_nac = disponib_parcelas_nac

    @property
    def disponib_saque_nac_global(self):
        """
        Gets the disponib_saque_nac_global of this SaldoLimiteResponse.


        :return: The disponib_saque_nac_global of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._disponib_saque_nac_global

    @disponib_saque_nac_global.setter
    def disponib_saque_nac_global(self, disponib_saque_nac_global):
        """
        Sets the disponib_saque_nac_global of this SaldoLimiteResponse.


        :param disponib_saque_nac_global: The disponib_saque_nac_global of this SaldoLimiteResponse.
        :type: float
        """
        self._disponib_saque_nac_global = disponib_saque_nac_global

    @property
    def flag_antecipacao(self):
        """
        Gets the flag_antecipacao of this SaldoLimiteResponse.


        :return: The flag_antecipacao of this SaldoLimiteResponse.
        :rtype: bool
        """
        return self._flag_antecipacao

    @flag_antecipacao.setter
    def flag_antecipacao(self, flag_antecipacao):
        """
        Sets the flag_antecipacao of this SaldoLimiteResponse.


        :param flag_antecipacao: The flag_antecipacao of this SaldoLimiteResponse.
        :type: bool
        """
        self._flag_antecipacao = flag_antecipacao

    @property
    def limite_compra_nac(self):
        """
        Gets the limite_compra_nac of this SaldoLimiteResponse.


        :return: The limite_compra_nac of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._limite_compra_nac

    @limite_compra_nac.setter
    def limite_compra_nac(self, limite_compra_nac):
        """
        Sets the limite_compra_nac of this SaldoLimiteResponse.


        :param limite_compra_nac: The limite_compra_nac of this SaldoLimiteResponse.
        :type: float
        """
        self._limite_compra_nac = limite_compra_nac

    @property
    def limite_credito_concedido(self):
        """
        Gets the limite_credito_concedido of this SaldoLimiteResponse.


        :return: The limite_credito_concedido of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._limite_credito_concedido

    @limite_credito_concedido.setter
    def limite_credito_concedido(self, limite_credito_concedido):
        """
        Sets the limite_credito_concedido of this SaldoLimiteResponse.


        :param limite_credito_concedido: The limite_credito_concedido of this SaldoLimiteResponse.
        :type: float
        """
        self._limite_credito_concedido = limite_credito_concedido

    @property
    def limite_credito_disponivel(self):
        """
        Gets the limite_credito_disponivel of this SaldoLimiteResponse.


        :return: The limite_credito_disponivel of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._limite_credito_disponivel

    @limite_credito_disponivel.setter
    def limite_credito_disponivel(self, limite_credito_disponivel):
        """
        Sets the limite_credito_disponivel of this SaldoLimiteResponse.


        :param limite_credito_disponivel: The limite_credito_disponivel of this SaldoLimiteResponse.
        :type: float
        """
        self._limite_credito_disponivel = limite_credito_disponivel

    @property
    def limite_global_credito(self):
        """
        Gets the limite_global_credito of this SaldoLimiteResponse.


        :return: The limite_global_credito of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._limite_global_credito

    @limite_global_credito.setter
    def limite_global_credito(self, limite_global_credito):
        """
        Sets the limite_global_credito of this SaldoLimiteResponse.


        :param limite_global_credito: The limite_global_credito of this SaldoLimiteResponse.
        :type: float
        """
        self._limite_global_credito = limite_global_credito

    @property
    def limite_parcelado_nac(self):
        """
        Gets the limite_parcelado_nac of this SaldoLimiteResponse.


        :return: The limite_parcelado_nac of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._limite_parcelado_nac

    @limite_parcelado_nac.setter
    def limite_parcelado_nac(self, limite_parcelado_nac):
        """
        Sets the limite_parcelado_nac of this SaldoLimiteResponse.


        :param limite_parcelado_nac: The limite_parcelado_nac of this SaldoLimiteResponse.
        :type: float
        """
        self._limite_parcelado_nac = limite_parcelado_nac

    @property
    def limite_parcelas_nac(self):
        """
        Gets the limite_parcelas_nac of this SaldoLimiteResponse.


        :return: The limite_parcelas_nac of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._limite_parcelas_nac

    @limite_parcelas_nac.setter
    def limite_parcelas_nac(self, limite_parcelas_nac):
        """
        Sets the limite_parcelas_nac of this SaldoLimiteResponse.


        :param limite_parcelas_nac: The limite_parcelas_nac of this SaldoLimiteResponse.
        :type: float
        """
        self._limite_parcelas_nac = limite_parcelas_nac

    @property
    def limite_pontuacao(self):
        """
        Gets the limite_pontuacao of this SaldoLimiteResponse.


        :return: The limite_pontuacao of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._limite_pontuacao

    @limite_pontuacao.setter
    def limite_pontuacao(self, limite_pontuacao):
        """
        Sets the limite_pontuacao of this SaldoLimiteResponse.


        :param limite_pontuacao: The limite_pontuacao of this SaldoLimiteResponse.
        :type: float
        """
        self._limite_pontuacao = limite_pontuacao

    @property
    def limite_saque_nac_global(self):
        """
        Gets the limite_saque_nac_global of this SaldoLimiteResponse.


        :return: The limite_saque_nac_global of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._limite_saque_nac_global

    @limite_saque_nac_global.setter
    def limite_saque_nac_global(self, limite_saque_nac_global):
        """
        Sets the limite_saque_nac_global of this SaldoLimiteResponse.


        :param limite_saque_nac_global: The limite_saque_nac_global of this SaldoLimiteResponse.
        :type: float
        """
        self._limite_saque_nac_global = limite_saque_nac_global

    @property
    def numero_ciclo(self):
        """
        Gets the numero_ciclo of this SaldoLimiteResponse.


        :return: The numero_ciclo of this SaldoLimiteResponse.
        :rtype: int
        """
        return self._numero_ciclo

    @numero_ciclo.setter
    def numero_ciclo(self, numero_ciclo):
        """
        Sets the numero_ciclo of this SaldoLimiteResponse.


        :param numero_ciclo: The numero_ciclo of this SaldoLimiteResponse.
        :type: int
        """
        self._numero_ciclo = numero_ciclo

    @property
    def pontos_concedidos(self):
        """
        Gets the pontos_concedidos of this SaldoLimiteResponse.


        :return: The pontos_concedidos of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._pontos_concedidos

    @pontos_concedidos.setter
    def pontos_concedidos(self, pontos_concedidos):
        """
        Sets the pontos_concedidos of this SaldoLimiteResponse.


        :param pontos_concedidos: The pontos_concedidos of this SaldoLimiteResponse.
        :type: float
        """
        self._pontos_concedidos = pontos_concedidos

    @property
    def pontos_remanescentes(self):
        """
        Gets the pontos_remanescentes of this SaldoLimiteResponse.


        :return: The pontos_remanescentes of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._pontos_remanescentes

    @pontos_remanescentes.setter
    def pontos_remanescentes(self, pontos_remanescentes):
        """
        Sets the pontos_remanescentes of this SaldoLimiteResponse.


        :param pontos_remanescentes: The pontos_remanescentes of this SaldoLimiteResponse.
        :type: float
        """
        self._pontos_remanescentes = pontos_remanescentes

    @property
    def proximo_vencimento_padrao(self):
        """
        Gets the proximo_vencimento_padrao of this SaldoLimiteResponse.


        :return: The proximo_vencimento_padrao of this SaldoLimiteResponse.
        :rtype: str
        """
        return self._proximo_vencimento_padrao

    @proximo_vencimento_padrao.setter
    def proximo_vencimento_padrao(self, proximo_vencimento_padrao):
        """
        Sets the proximo_vencimento_padrao of this SaldoLimiteResponse.


        :param proximo_vencimento_padrao: The proximo_vencimento_padrao of this SaldoLimiteResponse.
        :type: str
        """
        self._proximo_vencimento_padrao = proximo_vencimento_padrao

    @property
    def proximo_vencimento_real(self):
        """
        Gets the proximo_vencimento_real of this SaldoLimiteResponse.


        :return: The proximo_vencimento_real of this SaldoLimiteResponse.
        :rtype: str
        """
        return self._proximo_vencimento_real

    @proximo_vencimento_real.setter
    def proximo_vencimento_real(self, proximo_vencimento_real):
        """
        Sets the proximo_vencimento_real of this SaldoLimiteResponse.


        :param proximo_vencimento_real: The proximo_vencimento_real of this SaldoLimiteResponse.
        :type: str
        """
        self._proximo_vencimento_real = proximo_vencimento_real

    @property
    def saldo_atual_final(self):
        """
        Gets the saldo_atual_final of this SaldoLimiteResponse.


        :return: The saldo_atual_final of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._saldo_atual_final

    @saldo_atual_final.setter
    def saldo_atual_final(self, saldo_atual_final):
        """
        Sets the saldo_atual_final of this SaldoLimiteResponse.


        :param saldo_atual_final: The saldo_atual_final of this SaldoLimiteResponse.
        :type: float
        """
        self._saldo_atual_final = saldo_atual_final

    @property
    def saldo_credor(self):
        """
        Gets the saldo_credor of this SaldoLimiteResponse.


        :return: The saldo_credor of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._saldo_credor

    @saldo_credor.setter
    def saldo_credor(self, saldo_credor):
        """
        Sets the saldo_credor of this SaldoLimiteResponse.


        :param saldo_credor: The saldo_credor of this SaldoLimiteResponse.
        :type: float
        """
        self._saldo_credor = saldo_credor

    @property
    def saldo_devedor(self):
        """
        Gets the saldo_devedor of this SaldoLimiteResponse.


        :return: The saldo_devedor of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._saldo_devedor

    @saldo_devedor.setter
    def saldo_devedor(self, saldo_devedor):
        """
        Sets the saldo_devedor of this SaldoLimiteResponse.


        :param saldo_devedor: The saldo_devedor of this SaldoLimiteResponse.
        :type: float
        """
        self._saldo_devedor = saldo_devedor

    @property
    def saldo_devedor_oneroso(self):
        """
        Gets the saldo_devedor_oneroso of this SaldoLimiteResponse.


        :return: The saldo_devedor_oneroso of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._saldo_devedor_oneroso

    @saldo_devedor_oneroso.setter
    def saldo_devedor_oneroso(self, saldo_devedor_oneroso):
        """
        Sets the saldo_devedor_oneroso of this SaldoLimiteResponse.


        :param saldo_devedor_oneroso: The saldo_devedor_oneroso of this SaldoLimiteResponse.
        :type: float
        """
        self._saldo_devedor_oneroso = saldo_devedor_oneroso

    @property
    def saldo_devedor_total(self):
        """
        Gets the saldo_devedor_total of this SaldoLimiteResponse.


        :return: The saldo_devedor_total of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._saldo_devedor_total

    @saldo_devedor_total.setter
    def saldo_devedor_total(self, saldo_devedor_total):
        """
        Sets the saldo_devedor_total of this SaldoLimiteResponse.


        :param saldo_devedor_total: The saldo_devedor_total of this SaldoLimiteResponse.
        :type: float
        """
        self._saldo_devedor_total = saldo_devedor_total

    @property
    def salta_extrato_anterior(self):
        """
        Gets the salta_extrato_anterior of this SaldoLimiteResponse.


        :return: The salta_extrato_anterior of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._salta_extrato_anterior

    @salta_extrato_anterior.setter
    def salta_extrato_anterior(self, salta_extrato_anterior):
        """
        Sets the salta_extrato_anterior of this SaldoLimiteResponse.


        :param salta_extrato_anterior: The salta_extrato_anterior of this SaldoLimiteResponse.
        :type: float
        """
        self._salta_extrato_anterior = salta_extrato_anterior

    @property
    def total_disponivel_utilizacao(self):
        """
        Gets the total_disponivel_utilizacao of this SaldoLimiteResponse.


        :return: The total_disponivel_utilizacao of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._total_disponivel_utilizacao

    @total_disponivel_utilizacao.setter
    def total_disponivel_utilizacao(self, total_disponivel_utilizacao):
        """
        Sets the total_disponivel_utilizacao of this SaldoLimiteResponse.


        :param total_disponivel_utilizacao: The total_disponivel_utilizacao of this SaldoLimiteResponse.
        :type: float
        """
        self._total_disponivel_utilizacao = total_disponivel_utilizacao

    @property
    def total_futuro(self):
        """
        Gets the total_futuro of this SaldoLimiteResponse.


        :return: The total_futuro of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._total_futuro

    @total_futuro.setter
    def total_futuro(self, total_futuro):
        """
        Sets the total_futuro of this SaldoLimiteResponse.


        :param total_futuro: The total_futuro of this SaldoLimiteResponse.
        :type: float
        """
        self._total_futuro = total_futuro

    @property
    def valor_minimo_extrato(self):
        """
        Gets the valor_minimo_extrato of this SaldoLimiteResponse.


        :return: The valor_minimo_extrato of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._valor_minimo_extrato

    @valor_minimo_extrato.setter
    def valor_minimo_extrato(self, valor_minimo_extrato):
        """
        Sets the valor_minimo_extrato of this SaldoLimiteResponse.


        :param valor_minimo_extrato: The valor_minimo_extrato of this SaldoLimiteResponse.
        :type: float
        """
        self._valor_minimo_extrato = valor_minimo_extrato

    @property
    def valor_minimo_extrato_original(self):
        """
        Gets the valor_minimo_extrato_original of this SaldoLimiteResponse.


        :return: The valor_minimo_extrato_original of this SaldoLimiteResponse.
        :rtype: float
        """
        return self._valor_minimo_extrato_original

    @valor_minimo_extrato_original.setter
    def valor_minimo_extrato_original(self, valor_minimo_extrato_original):
        """
        Sets the valor_minimo_extrato_original of this SaldoLimiteResponse.


        :param valor_minimo_extrato_original: The valor_minimo_extrato_original of this SaldoLimiteResponse.
        :type: float
        """
        self._valor_minimo_extrato_original = valor_minimo_extrato_original

    @property
    def vencimento_padrao_anterior(self):
        """
        Gets the vencimento_padrao_anterior of this SaldoLimiteResponse.


        :return: The vencimento_padrao_anterior of this SaldoLimiteResponse.
        :rtype: str
        """
        return self._vencimento_padrao_anterior

    @vencimento_padrao_anterior.setter
    def vencimento_padrao_anterior(self, vencimento_padrao_anterior):
        """
        Sets the vencimento_padrao_anterior of this SaldoLimiteResponse.


        :param vencimento_padrao_anterior: The vencimento_padrao_anterior of this SaldoLimiteResponse.
        :type: str
        """
        self._vencimento_padrao_anterior = vencimento_padrao_anterior

    @property
    def vencimento_pos_prox(self):
        """
        Gets the vencimento_pos_prox of this SaldoLimiteResponse.


        :return: The vencimento_pos_prox of this SaldoLimiteResponse.
        :rtype: str
        """
        return self._vencimento_pos_prox

    @vencimento_pos_prox.setter
    def vencimento_pos_prox(self, vencimento_pos_prox):
        """
        Sets the vencimento_pos_prox of this SaldoLimiteResponse.


        :param vencimento_pos_prox: The vencimento_pos_prox of this SaldoLimiteResponse.
        :type: str
        """
        self._vencimento_pos_prox = vencimento_pos_prox

    @property
    def vencimento_real_anterior(self):
        """
        Gets the vencimento_real_anterior of this SaldoLimiteResponse.


        :return: The vencimento_real_anterior of this SaldoLimiteResponse.
        :rtype: str
        """
        return self._vencimento_real_anterior

    @vencimento_real_anterior.setter
    def vencimento_real_anterior(self, vencimento_real_anterior):
        """
        Sets the vencimento_real_anterior of this SaldoLimiteResponse.


        :param vencimento_real_anterior: The vencimento_real_anterior of this SaldoLimiteResponse.
        :type: str
        """
        self._vencimento_real_anterior = vencimento_real_anterior

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

