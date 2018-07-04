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


class CartaoImpressaoResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CartaoImpressaoResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_conta': 'int',
            'id_pessoa': 'int',
            'id_cartao': 'int',
            'id_bandeira': 'int',
            'id_tipo_cartao': 'int',
            'numero_cartao': 'str',
            'nome_plastico': 'str',
            'cvv2': 'str',
            'data_geracao': 'str',
            'data_validade': 'str',
            'nome_origem_comercial': 'str',
            'nome_empresa': 'str',
            'numero_agencia': 'int',
            'numero_conta_corente': 'str',
            'nome_empresa_beneficio': 'str',
            'cpf': 'str',
            'tipo_portador': 'str',
            'nome_empregador': 'str',
            'trilha1': 'str',
            'trilha2': 'str',
            'trilha_cvv1': 'str',
            'trilha_cvv2': 'str',
            'flag_virtual': 'int',
            'numero_cartao_hash': 'int'
        }

        self.attribute_map = {
            'id_conta': 'idConta',
            'id_pessoa': 'idPessoa',
            'id_cartao': 'idCartao',
            'id_bandeira': 'idBandeira',
            'id_tipo_cartao': 'idTipoCartao',
            'numero_cartao': 'numeroCartao',
            'nome_plastico': 'nomePlastico',
            'cvv2': 'cvv2',
            'data_geracao': 'dataGeracao',
            'data_validade': 'dataValidade',
            'nome_origem_comercial': 'nomeOrigemComercial',
            'nome_empresa': 'nomeEmpresa',
            'numero_agencia': 'numeroAgencia',
            'numero_conta_corente': 'numeroContaCorente',
            'nome_empresa_beneficio': 'nomeEmpresaBeneficio',
            'cpf': 'cpf',
            'tipo_portador': 'tipoPortador',
            'nome_empregador': 'nomeEmpregador',
            'trilha1': 'trilha1',
            'trilha2': 'trilha2',
            'trilha_cvv1': 'trilhaCVV1',
            'trilha_cvv2': 'trilhaCVV2',
            'flag_virtual': 'flagVirtual',
            'numero_cartao_hash': 'numeroCartaoHash'
        }

        self._id_conta = None
        self._id_pessoa = None
        self._id_cartao = None
        self._id_bandeira = None
        self._id_tipo_cartao = None
        self._numero_cartao = None
        self._nome_plastico = None
        self._cvv2 = None
        self._data_geracao = None
        self._data_validade = None
        self._nome_origem_comercial = None
        self._nome_empresa = None
        self._numero_agencia = None
        self._numero_conta_corente = None
        self._nome_empresa_beneficio = None
        self._cpf = None
        self._tipo_portador = None
        self._nome_empregador = None
        self._trilha1 = None
        self._trilha2 = None
        self._trilha_cvv1 = None
        self._trilha_cvv2 = None
        self._flag_virtual = None
        self._numero_cartao_hash = None

    @property
    def id_conta(self):
        """
        Gets the id_conta of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_id_conta_value}}}

        :return: The id_conta of this CartaoImpressaoResponse.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_id_conta_value}}}

        :param id_conta: The id_conta of this CartaoImpressaoResponse.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def id_pessoa(self):
        """
        Gets the id_pessoa of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_id_pessoa_value}}}

        :return: The id_pessoa of this CartaoImpressaoResponse.
        :rtype: int
        """
        return self._id_pessoa

    @id_pessoa.setter
    def id_pessoa(self, id_pessoa):
        """
        Sets the id_pessoa of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_id_pessoa_value}}}

        :param id_pessoa: The id_pessoa of this CartaoImpressaoResponse.
        :type: int
        """
        self._id_pessoa = id_pessoa

    @property
    def id_cartao(self):
        """
        Gets the id_cartao of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_id_cartao_value}}}

        :return: The id_cartao of this CartaoImpressaoResponse.
        :rtype: int
        """
        return self._id_cartao

    @id_cartao.setter
    def id_cartao(self, id_cartao):
        """
        Sets the id_cartao of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_id_cartao_value}}}

        :param id_cartao: The id_cartao of this CartaoImpressaoResponse.
        :type: int
        """
        self._id_cartao = id_cartao

    @property
    def id_bandeira(self):
        """
        Gets the id_bandeira of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_id_bandeira_value}}}

        :return: The id_bandeira of this CartaoImpressaoResponse.
        :rtype: int
        """
        return self._id_bandeira

    @id_bandeira.setter
    def id_bandeira(self, id_bandeira):
        """
        Sets the id_bandeira of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_id_bandeira_value}}}

        :param id_bandeira: The id_bandeira of this CartaoImpressaoResponse.
        :type: int
        """
        self._id_bandeira = id_bandeira

    @property
    def id_tipo_cartao(self):
        """
        Gets the id_tipo_cartao of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_id_tipo_cartao_value}}}

        :return: The id_tipo_cartao of this CartaoImpressaoResponse.
        :rtype: int
        """
        return self._id_tipo_cartao

    @id_tipo_cartao.setter
    def id_tipo_cartao(self, id_tipo_cartao):
        """
        Sets the id_tipo_cartao of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_id_tipo_cartao_value}}}

        :param id_tipo_cartao: The id_tipo_cartao of this CartaoImpressaoResponse.
        :type: int
        """
        self._id_tipo_cartao = id_tipo_cartao

    @property
    def numero_cartao(self):
        """
        Gets the numero_cartao of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_numero_cartao_value}}}

        :return: The numero_cartao of this CartaoImpressaoResponse.
        :rtype: str
        """
        return self._numero_cartao

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao):
        """
        Sets the numero_cartao of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_numero_cartao_value}}}

        :param numero_cartao: The numero_cartao of this CartaoImpressaoResponse.
        :type: str
        """
        self._numero_cartao = numero_cartao

    @property
    def nome_plastico(self):
        """
        Gets the nome_plastico of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_nome_plastico_value}}}

        :return: The nome_plastico of this CartaoImpressaoResponse.
        :rtype: str
        """
        return self._nome_plastico

    @nome_plastico.setter
    def nome_plastico(self, nome_plastico):
        """
        Sets the nome_plastico of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_nome_plastico_value}}}

        :param nome_plastico: The nome_plastico of this CartaoImpressaoResponse.
        :type: str
        """
        self._nome_plastico = nome_plastico

    @property
    def cvv2(self):
        """
        Gets the cvv2 of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_cvv2_value}}}

        :return: The cvv2 of this CartaoImpressaoResponse.
        :rtype: str
        """
        return self._cvv2

    @cvv2.setter
    def cvv2(self, cvv2):
        """
        Sets the cvv2 of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_cvv2_value}}}

        :param cvv2: The cvv2 of this CartaoImpressaoResponse.
        :type: str
        """
        self._cvv2 = cvv2

    @property
    def data_geracao(self):
        """
        Gets the data_geracao of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_data_geracao_value}}}

        :return: The data_geracao of this CartaoImpressaoResponse.
        :rtype: str
        """
        return self._data_geracao

    @data_geracao.setter
    def data_geracao(self, data_geracao):
        """
        Sets the data_geracao of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_data_geracao_value}}}

        :param data_geracao: The data_geracao of this CartaoImpressaoResponse.
        :type: str
        """
        self._data_geracao = data_geracao

    @property
    def data_validade(self):
        """
        Gets the data_validade of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_data_validade_value}}}

        :return: The data_validade of this CartaoImpressaoResponse.
        :rtype: str
        """
        return self._data_validade

    @data_validade.setter
    def data_validade(self, data_validade):
        """
        Sets the data_validade of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_data_validade_value}}}

        :param data_validade: The data_validade of this CartaoImpressaoResponse.
        :type: str
        """
        self._data_validade = data_validade

    @property
    def nome_origem_comercial(self):
        """
        Gets the nome_origem_comercial of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_nome_origem_comercial_value}}}

        :return: The nome_origem_comercial of this CartaoImpressaoResponse.
        :rtype: str
        """
        return self._nome_origem_comercial

    @nome_origem_comercial.setter
    def nome_origem_comercial(self, nome_origem_comercial):
        """
        Sets the nome_origem_comercial of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_nome_origem_comercial_value}}}

        :param nome_origem_comercial: The nome_origem_comercial of this CartaoImpressaoResponse.
        :type: str
        """
        self._nome_origem_comercial = nome_origem_comercial

    @property
    def nome_empresa(self):
        """
        Gets the nome_empresa of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_nome_empresa_value}}}

        :return: The nome_empresa of this CartaoImpressaoResponse.
        :rtype: str
        """
        return self._nome_empresa

    @nome_empresa.setter
    def nome_empresa(self, nome_empresa):
        """
        Sets the nome_empresa of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_nome_empresa_value}}}

        :param nome_empresa: The nome_empresa of this CartaoImpressaoResponse.
        :type: str
        """
        self._nome_empresa = nome_empresa

    @property
    def numero_agencia(self):
        """
        Gets the numero_agencia of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_numero_agencia_value}}}

        :return: The numero_agencia of this CartaoImpressaoResponse.
        :rtype: int
        """
        return self._numero_agencia

    @numero_agencia.setter
    def numero_agencia(self, numero_agencia):
        """
        Sets the numero_agencia of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_numero_agencia_value}}}

        :param numero_agencia: The numero_agencia of this CartaoImpressaoResponse.
        :type: int
        """
        self._numero_agencia = numero_agencia

    @property
    def numero_conta_corente(self):
        """
        Gets the numero_conta_corente of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_numero_conta_corente_value}}}

        :return: The numero_conta_corente of this CartaoImpressaoResponse.
        :rtype: str
        """
        return self._numero_conta_corente

    @numero_conta_corente.setter
    def numero_conta_corente(self, numero_conta_corente):
        """
        Sets the numero_conta_corente of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_numero_conta_corente_value}}}

        :param numero_conta_corente: The numero_conta_corente of this CartaoImpressaoResponse.
        :type: str
        """
        self._numero_conta_corente = numero_conta_corente

    @property
    def nome_empresa_beneficio(self):
        """
        Gets the nome_empresa_beneficio of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_nome_empresa_beneficio_value}}}

        :return: The nome_empresa_beneficio of this CartaoImpressaoResponse.
        :rtype: str
        """
        return self._nome_empresa_beneficio

    @nome_empresa_beneficio.setter
    def nome_empresa_beneficio(self, nome_empresa_beneficio):
        """
        Sets the nome_empresa_beneficio of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_nome_empresa_beneficio_value}}}

        :param nome_empresa_beneficio: The nome_empresa_beneficio of this CartaoImpressaoResponse.
        :type: str
        """
        self._nome_empresa_beneficio = nome_empresa_beneficio

    @property
    def cpf(self):
        """
        Gets the cpf of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_cpf_value}}}

        :return: The cpf of this CartaoImpressaoResponse.
        :rtype: str
        """
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        """
        Sets the cpf of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_cpf_value}}}

        :param cpf: The cpf of this CartaoImpressaoResponse.
        :type: str
        """
        self._cpf = cpf

    @property
    def tipo_portador(self):
        """
        Gets the tipo_portador of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_tipo_portador_value}}}

        :return: The tipo_portador of this CartaoImpressaoResponse.
        :rtype: str
        """
        return self._tipo_portador

    @tipo_portador.setter
    def tipo_portador(self, tipo_portador):
        """
        Sets the tipo_portador of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_tipo_portador_value}}}

        :param tipo_portador: The tipo_portador of this CartaoImpressaoResponse.
        :type: str
        """
        self._tipo_portador = tipo_portador

    @property
    def nome_empregador(self):
        """
        Gets the nome_empregador of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_nome_empregador_value}}}

        :return: The nome_empregador of this CartaoImpressaoResponse.
        :rtype: str
        """
        return self._nome_empregador

    @nome_empregador.setter
    def nome_empregador(self, nome_empregador):
        """
        Sets the nome_empregador of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_nome_empregador_value}}}

        :param nome_empregador: The nome_empregador of this CartaoImpressaoResponse.
        :type: str
        """
        self._nome_empregador = nome_empregador

    @property
    def trilha1(self):
        """
        Gets the trilha1 of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_trilha1_value}}}

        :return: The trilha1 of this CartaoImpressaoResponse.
        :rtype: str
        """
        return self._trilha1

    @trilha1.setter
    def trilha1(self, trilha1):
        """
        Sets the trilha1 of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_trilha1_value}}}

        :param trilha1: The trilha1 of this CartaoImpressaoResponse.
        :type: str
        """
        self._trilha1 = trilha1

    @property
    def trilha2(self):
        """
        Gets the trilha2 of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_trilha2_value}}}

        :return: The trilha2 of this CartaoImpressaoResponse.
        :rtype: str
        """
        return self._trilha2

    @trilha2.setter
    def trilha2(self, trilha2):
        """
        Sets the trilha2 of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_trilha2_value}}}

        :param trilha2: The trilha2 of this CartaoImpressaoResponse.
        :type: str
        """
        self._trilha2 = trilha2

    @property
    def trilha_cvv1(self):
        """
        Gets the trilha_cvv1 of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_trilha_c_v_v1_value}}}

        :return: The trilha_cvv1 of this CartaoImpressaoResponse.
        :rtype: str
        """
        return self._trilha_cvv1

    @trilha_cvv1.setter
    def trilha_cvv1(self, trilha_cvv1):
        """
        Sets the trilha_cvv1 of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_trilha_c_v_v1_value}}}

        :param trilha_cvv1: The trilha_cvv1 of this CartaoImpressaoResponse.
        :type: str
        """
        self._trilha_cvv1 = trilha_cvv1

    @property
    def trilha_cvv2(self):
        """
        Gets the trilha_cvv2 of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_trilha_c_v_v2_value}}}

        :return: The trilha_cvv2 of this CartaoImpressaoResponse.
        :rtype: str
        """
        return self._trilha_cvv2

    @trilha_cvv2.setter
    def trilha_cvv2(self, trilha_cvv2):
        """
        Sets the trilha_cvv2 of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_trilha_c_v_v2_value}}}

        :param trilha_cvv2: The trilha_cvv2 of this CartaoImpressaoResponse.
        :type: str
        """
        self._trilha_cvv2 = trilha_cvv2

    @property
    def flag_virtual(self):
        """
        Gets the flag_virtual of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_flag_virtual_value}}}

        :return: The flag_virtual of this CartaoImpressaoResponse.
        :rtype: int
        """
        return self._flag_virtual

    @flag_virtual.setter
    def flag_virtual(self, flag_virtual):
        """
        Sets the flag_virtual of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_flag_virtual_value}}}

        :param flag_virtual: The flag_virtual of this CartaoImpressaoResponse.
        :type: int
        """
        self._flag_virtual = flag_virtual

    @property
    def numero_cartao_hash(self):
        """
        Gets the numero_cartao_hash of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_numero_cartao_hash_value}}}

        :return: The numero_cartao_hash of this CartaoImpressaoResponse.
        :rtype: int
        """
        return self._numero_cartao_hash

    @numero_cartao_hash.setter
    def numero_cartao_hash(self, numero_cartao_hash):
        """
        Sets the numero_cartao_hash of this CartaoImpressaoResponse.
        {{{cartao_impressao_response_numero_cartao_hash_value}}}

        :param numero_cartao_hash: The numero_cartao_hash of this CartaoImpressaoResponse.
        :type: int
        """
        self._numero_cartao_hash = numero_cartao_hash

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

