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


class EstabelecimentoResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EstabelecimentoResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'numero_estabelecimento': 'str',
            'flag_matriz': 'int',
            'id_grupo_economico': 'int',
            'numero_receita_federal': 'int',
            'nome': 'str',
            'descricao': 'str',
            'nome_fantasia': 'str',
            'cep': 'str',
            'nome_logradouro': 'str',
            'numero_endereco': 'str',
            'bairro': 'str',
            'cidade': 'str',
            'complemento': 'str',
            'uf': 'str',
            'cep2': 'str',
            'nome_logradouro2': 'str',
            'numero_endereco2': 'str',
            'bairro2': 'str',
            'cidade2': 'str',
            'complemento2': 'str',
            'uf2': 'str',
            'obs': 'str',
            'contato': 'str',
            'email': 'str',
            'flag_arquivo_secr_fazenda': 'int',
            'flag_cartao_digitado': 'int',
            'inativo': 'int',
            'id_moeda': 'int',
            'id_pais': 'int',
            'associado_spc_brasil': 'int',
            'mcc': 'int',
            'id_tipo_estabelecimento': 'int',
            'correspondencia': 'int',
            'cargo_contato': 'str',
            'tipo_pagamento': 'str',
            'consulta': 'ConsultaCadastroEstabelecimentoDTO',
            'consulta2': 'ConsultaCadastroEstabelecimentoDTO',
            'consulta3': 'ConsultaCadastroEstabelecimentoDTO',
            'terminal': 'str',
            'data_cadastramento': 'str',
            'usuario': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'numero_estabelecimento': 'numeroEstabelecimento',
            'flag_matriz': 'flagMatriz',
            'id_grupo_economico': 'idGrupoEconomico',
            'numero_receita_federal': 'numeroReceitaFederal',
            'nome': 'nome',
            'descricao': 'descricao',
            'nome_fantasia': 'nomeFantasia',
            'cep': 'cep',
            'nome_logradouro': 'nomeLogradouro',
            'numero_endereco': 'numeroEndereco',
            'bairro': 'bairro',
            'cidade': 'cidade',
            'complemento': 'complemento',
            'uf': 'uf',
            'cep2': 'cep2',
            'nome_logradouro2': 'nomeLogradouro2',
            'numero_endereco2': 'numeroEndereco2',
            'bairro2': 'bairro2',
            'cidade2': 'cidade2',
            'complemento2': 'complemento2',
            'uf2': 'uf2',
            'obs': 'obs',
            'contato': 'contato',
            'email': 'email',
            'flag_arquivo_secr_fazenda': 'flagArquivoSecrFazenda',
            'flag_cartao_digitado': 'flagCartaoDigitado',
            'inativo': 'inativo',
            'id_moeda': 'idMoeda',
            'id_pais': 'idPais',
            'associado_spc_brasil': 'associadoSPCBrasil',
            'mcc': 'mcc',
            'id_tipo_estabelecimento': 'idTipoEstabelecimento',
            'correspondencia': 'correspondencia',
            'cargo_contato': 'cargoContato',
            'tipo_pagamento': 'tipoPagamento',
            'consulta': 'consulta',
            'consulta2': 'consulta2',
            'consulta3': 'consulta3',
            'terminal': 'terminal',
            'data_cadastramento': 'dataCadastramento',
            'usuario': 'usuario'
        }

        self._id = None
        self._numero_estabelecimento = None
        self._flag_matriz = None
        self._id_grupo_economico = None
        self._numero_receita_federal = None
        self._nome = None
        self._descricao = None
        self._nome_fantasia = None
        self._cep = None
        self._nome_logradouro = None
        self._numero_endereco = None
        self._bairro = None
        self._cidade = None
        self._complemento = None
        self._uf = None
        self._cep2 = None
        self._nome_logradouro2 = None
        self._numero_endereco2 = None
        self._bairro2 = None
        self._cidade2 = None
        self._complemento2 = None
        self._uf2 = None
        self._obs = None
        self._contato = None
        self._email = None
        self._flag_arquivo_secr_fazenda = None
        self._flag_cartao_digitado = None
        self._inativo = None
        self._id_moeda = None
        self._id_pais = None
        self._associado_spc_brasil = None
        self._mcc = None
        self._id_tipo_estabelecimento = None
        self._correspondencia = None
        self._cargo_contato = None
        self._tipo_pagamento = None
        self._consulta = None
        self._consulta2 = None
        self._consulta3 = None
        self._terminal = None
        self._data_cadastramento = None
        self._usuario = None

    @property
    def id(self):
        """
        Gets the id of this EstabelecimentoResponse.
        {{{estabelecimento_response_id_value}}}

        :return: The id of this EstabelecimentoResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EstabelecimentoResponse.
        {{{estabelecimento_response_id_value}}}

        :param id: The id of this EstabelecimentoResponse.
        :type: int
        """
        self._id = id

    @property
    def numero_estabelecimento(self):
        """
        Gets the numero_estabelecimento of this EstabelecimentoResponse.
        {{{estabelecimento_response_numero_estabelecimento_value}}}

        :return: The numero_estabelecimento of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._numero_estabelecimento

    @numero_estabelecimento.setter
    def numero_estabelecimento(self, numero_estabelecimento):
        """
        Sets the numero_estabelecimento of this EstabelecimentoResponse.
        {{{estabelecimento_response_numero_estabelecimento_value}}}

        :param numero_estabelecimento: The numero_estabelecimento of this EstabelecimentoResponse.
        :type: str
        """
        self._numero_estabelecimento = numero_estabelecimento

    @property
    def flag_matriz(self):
        """
        Gets the flag_matriz of this EstabelecimentoResponse.
        {{{estabelecimento_response_flag_matriz_value}}}

        :return: The flag_matriz of this EstabelecimentoResponse.
        :rtype: int
        """
        return self._flag_matriz

    @flag_matriz.setter
    def flag_matriz(self, flag_matriz):
        """
        Sets the flag_matriz of this EstabelecimentoResponse.
        {{{estabelecimento_response_flag_matriz_value}}}

        :param flag_matriz: The flag_matriz of this EstabelecimentoResponse.
        :type: int
        """
        self._flag_matriz = flag_matriz

    @property
    def id_grupo_economico(self):
        """
        Gets the id_grupo_economico of this EstabelecimentoResponse.
        {{{estabelecimento_response_id_grupo_economico_value}}}

        :return: The id_grupo_economico of this EstabelecimentoResponse.
        :rtype: int
        """
        return self._id_grupo_economico

    @id_grupo_economico.setter
    def id_grupo_economico(self, id_grupo_economico):
        """
        Sets the id_grupo_economico of this EstabelecimentoResponse.
        {{{estabelecimento_response_id_grupo_economico_value}}}

        :param id_grupo_economico: The id_grupo_economico of this EstabelecimentoResponse.
        :type: int
        """
        self._id_grupo_economico = id_grupo_economico

    @property
    def numero_receita_federal(self):
        """
        Gets the numero_receita_federal of this EstabelecimentoResponse.
        {{{estabelecimento_response_numero_receita_federal_value}}}

        :return: The numero_receita_federal of this EstabelecimentoResponse.
        :rtype: int
        """
        return self._numero_receita_federal

    @numero_receita_federal.setter
    def numero_receita_federal(self, numero_receita_federal):
        """
        Sets the numero_receita_federal of this EstabelecimentoResponse.
        {{{estabelecimento_response_numero_receita_federal_value}}}

        :param numero_receita_federal: The numero_receita_federal of this EstabelecimentoResponse.
        :type: int
        """
        self._numero_receita_federal = numero_receita_federal

    @property
    def nome(self):
        """
        Gets the nome of this EstabelecimentoResponse.
        {{{estabelecimento_response_nome_value}}}

        :return: The nome of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Sets the nome of this EstabelecimentoResponse.
        {{{estabelecimento_response_nome_value}}}

        :param nome: The nome of this EstabelecimentoResponse.
        :type: str
        """
        self._nome = nome

    @property
    def descricao(self):
        """
        Gets the descricao of this EstabelecimentoResponse.
        {{{estabelecimento_response_descricao_value}}}

        :return: The descricao of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        """
        Sets the descricao of this EstabelecimentoResponse.
        {{{estabelecimento_response_descricao_value}}}

        :param descricao: The descricao of this EstabelecimentoResponse.
        :type: str
        """
        self._descricao = descricao

    @property
    def nome_fantasia(self):
        """
        Gets the nome_fantasia of this EstabelecimentoResponse.
        {{{estabelecimento_response_nome_fantasia_value}}}

        :return: The nome_fantasia of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._nome_fantasia

    @nome_fantasia.setter
    def nome_fantasia(self, nome_fantasia):
        """
        Sets the nome_fantasia of this EstabelecimentoResponse.
        {{{estabelecimento_response_nome_fantasia_value}}}

        :param nome_fantasia: The nome_fantasia of this EstabelecimentoResponse.
        :type: str
        """
        self._nome_fantasia = nome_fantasia

    @property
    def cep(self):
        """
        Gets the cep of this EstabelecimentoResponse.
        {{{estabelecimento_response_cep_value}}}

        :return: The cep of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._cep

    @cep.setter
    def cep(self, cep):
        """
        Sets the cep of this EstabelecimentoResponse.
        {{{estabelecimento_response_cep_value}}}

        :param cep: The cep of this EstabelecimentoResponse.
        :type: str
        """
        self._cep = cep

    @property
    def nome_logradouro(self):
        """
        Gets the nome_logradouro of this EstabelecimentoResponse.
        {{{estabelecimento_response_nome_logradouro_value}}}

        :return: The nome_logradouro of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._nome_logradouro

    @nome_logradouro.setter
    def nome_logradouro(self, nome_logradouro):
        """
        Sets the nome_logradouro of this EstabelecimentoResponse.
        {{{estabelecimento_response_nome_logradouro_value}}}

        :param nome_logradouro: The nome_logradouro of this EstabelecimentoResponse.
        :type: str
        """
        self._nome_logradouro = nome_logradouro

    @property
    def numero_endereco(self):
        """
        Gets the numero_endereco of this EstabelecimentoResponse.
        {{{estabelecimento_response_numero_endereco_value}}}

        :return: The numero_endereco of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._numero_endereco

    @numero_endereco.setter
    def numero_endereco(self, numero_endereco):
        """
        Sets the numero_endereco of this EstabelecimentoResponse.
        {{{estabelecimento_response_numero_endereco_value}}}

        :param numero_endereco: The numero_endereco of this EstabelecimentoResponse.
        :type: str
        """
        self._numero_endereco = numero_endereco

    @property
    def bairro(self):
        """
        Gets the bairro of this EstabelecimentoResponse.
        {{{estabelecimento_response_bairro_value}}}

        :return: The bairro of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._bairro

    @bairro.setter
    def bairro(self, bairro):
        """
        Sets the bairro of this EstabelecimentoResponse.
        {{{estabelecimento_response_bairro_value}}}

        :param bairro: The bairro of this EstabelecimentoResponse.
        :type: str
        """
        self._bairro = bairro

    @property
    def cidade(self):
        """
        Gets the cidade of this EstabelecimentoResponse.
        {{{estabelecimento_response_cidade_value}}}

        :return: The cidade of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._cidade

    @cidade.setter
    def cidade(self, cidade):
        """
        Sets the cidade of this EstabelecimentoResponse.
        {{{estabelecimento_response_cidade_value}}}

        :param cidade: The cidade of this EstabelecimentoResponse.
        :type: str
        """
        self._cidade = cidade

    @property
    def complemento(self):
        """
        Gets the complemento of this EstabelecimentoResponse.
        {{{estabelecimento_response_complemento_value}}}

        :return: The complemento of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._complemento

    @complemento.setter
    def complemento(self, complemento):
        """
        Sets the complemento of this EstabelecimentoResponse.
        {{{estabelecimento_response_complemento_value}}}

        :param complemento: The complemento of this EstabelecimentoResponse.
        :type: str
        """
        self._complemento = complemento

    @property
    def uf(self):
        """
        Gets the uf of this EstabelecimentoResponse.
        {{{estabelecimento_response_uf_value}}}

        :return: The uf of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._uf

    @uf.setter
    def uf(self, uf):
        """
        Sets the uf of this EstabelecimentoResponse.
        {{{estabelecimento_response_uf_value}}}

        :param uf: The uf of this EstabelecimentoResponse.
        :type: str
        """
        self._uf = uf

    @property
    def cep2(self):
        """
        Gets the cep2 of this EstabelecimentoResponse.
        {{{estabelecimento_response_cep2_value}}}

        :return: The cep2 of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._cep2

    @cep2.setter
    def cep2(self, cep2):
        """
        Sets the cep2 of this EstabelecimentoResponse.
        {{{estabelecimento_response_cep2_value}}}

        :param cep2: The cep2 of this EstabelecimentoResponse.
        :type: str
        """
        self._cep2 = cep2

    @property
    def nome_logradouro2(self):
        """
        Gets the nome_logradouro2 of this EstabelecimentoResponse.
        {{{estabelecimento_response_nome_logradouro2_value}}}

        :return: The nome_logradouro2 of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._nome_logradouro2

    @nome_logradouro2.setter
    def nome_logradouro2(self, nome_logradouro2):
        """
        Sets the nome_logradouro2 of this EstabelecimentoResponse.
        {{{estabelecimento_response_nome_logradouro2_value}}}

        :param nome_logradouro2: The nome_logradouro2 of this EstabelecimentoResponse.
        :type: str
        """
        self._nome_logradouro2 = nome_logradouro2

    @property
    def numero_endereco2(self):
        """
        Gets the numero_endereco2 of this EstabelecimentoResponse.
        {{{estabelecimento_response_numero_endereco2_value}}}

        :return: The numero_endereco2 of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._numero_endereco2

    @numero_endereco2.setter
    def numero_endereco2(self, numero_endereco2):
        """
        Sets the numero_endereco2 of this EstabelecimentoResponse.
        {{{estabelecimento_response_numero_endereco2_value}}}

        :param numero_endereco2: The numero_endereco2 of this EstabelecimentoResponse.
        :type: str
        """
        self._numero_endereco2 = numero_endereco2

    @property
    def bairro2(self):
        """
        Gets the bairro2 of this EstabelecimentoResponse.
        {{{estabelecimento_response_bairro2_value}}}

        :return: The bairro2 of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._bairro2

    @bairro2.setter
    def bairro2(self, bairro2):
        """
        Sets the bairro2 of this EstabelecimentoResponse.
        {{{estabelecimento_response_bairro2_value}}}

        :param bairro2: The bairro2 of this EstabelecimentoResponse.
        :type: str
        """
        self._bairro2 = bairro2

    @property
    def cidade2(self):
        """
        Gets the cidade2 of this EstabelecimentoResponse.
        {{{estabelecimento_response_cidade2_value}}}

        :return: The cidade2 of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._cidade2

    @cidade2.setter
    def cidade2(self, cidade2):
        """
        Sets the cidade2 of this EstabelecimentoResponse.
        {{{estabelecimento_response_cidade2_value}}}

        :param cidade2: The cidade2 of this EstabelecimentoResponse.
        :type: str
        """
        self._cidade2 = cidade2

    @property
    def complemento2(self):
        """
        Gets the complemento2 of this EstabelecimentoResponse.
        {{{estabelecimento_response_complemento2_value}}}

        :return: The complemento2 of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._complemento2

    @complemento2.setter
    def complemento2(self, complemento2):
        """
        Sets the complemento2 of this EstabelecimentoResponse.
        {{{estabelecimento_response_complemento2_value}}}

        :param complemento2: The complemento2 of this EstabelecimentoResponse.
        :type: str
        """
        self._complemento2 = complemento2

    @property
    def uf2(self):
        """
        Gets the uf2 of this EstabelecimentoResponse.
        {{{estabelecimento_response_uf2_value}}}

        :return: The uf2 of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._uf2

    @uf2.setter
    def uf2(self, uf2):
        """
        Sets the uf2 of this EstabelecimentoResponse.
        {{{estabelecimento_response_uf2_value}}}

        :param uf2: The uf2 of this EstabelecimentoResponse.
        :type: str
        """
        self._uf2 = uf2

    @property
    def obs(self):
        """
        Gets the obs of this EstabelecimentoResponse.
        {{{estabelecimento_response_obs_value}}}

        :return: The obs of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        """
        Sets the obs of this EstabelecimentoResponse.
        {{{estabelecimento_response_obs_value}}}

        :param obs: The obs of this EstabelecimentoResponse.
        :type: str
        """
        self._obs = obs

    @property
    def contato(self):
        """
        Gets the contato of this EstabelecimentoResponse.
        {{{estabelecimento_response_contato_value}}}

        :return: The contato of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._contato

    @contato.setter
    def contato(self, contato):
        """
        Sets the contato of this EstabelecimentoResponse.
        {{{estabelecimento_response_contato_value}}}

        :param contato: The contato of this EstabelecimentoResponse.
        :type: str
        """
        self._contato = contato

    @property
    def email(self):
        """
        Gets the email of this EstabelecimentoResponse.
        {{{estabelecimento_response_email_value}}}

        :return: The email of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this EstabelecimentoResponse.
        {{{estabelecimento_response_email_value}}}

        :param email: The email of this EstabelecimentoResponse.
        :type: str
        """
        self._email = email

    @property
    def flag_arquivo_secr_fazenda(self):
        """
        Gets the flag_arquivo_secr_fazenda of this EstabelecimentoResponse.
        {{{estabelecimento_response_flag_arquivo_secr_fazenda_value}}}

        :return: The flag_arquivo_secr_fazenda of this EstabelecimentoResponse.
        :rtype: int
        """
        return self._flag_arquivo_secr_fazenda

    @flag_arquivo_secr_fazenda.setter
    def flag_arquivo_secr_fazenda(self, flag_arquivo_secr_fazenda):
        """
        Sets the flag_arquivo_secr_fazenda of this EstabelecimentoResponse.
        {{{estabelecimento_response_flag_arquivo_secr_fazenda_value}}}

        :param flag_arquivo_secr_fazenda: The flag_arquivo_secr_fazenda of this EstabelecimentoResponse.
        :type: int
        """
        self._flag_arquivo_secr_fazenda = flag_arquivo_secr_fazenda

    @property
    def flag_cartao_digitado(self):
        """
        Gets the flag_cartao_digitado of this EstabelecimentoResponse.
        {{{estabelecimento_response_flag_cartao_digitado_value}}}

        :return: The flag_cartao_digitado of this EstabelecimentoResponse.
        :rtype: int
        """
        return self._flag_cartao_digitado

    @flag_cartao_digitado.setter
    def flag_cartao_digitado(self, flag_cartao_digitado):
        """
        Sets the flag_cartao_digitado of this EstabelecimentoResponse.
        {{{estabelecimento_response_flag_cartao_digitado_value}}}

        :param flag_cartao_digitado: The flag_cartao_digitado of this EstabelecimentoResponse.
        :type: int
        """
        self._flag_cartao_digitado = flag_cartao_digitado

    @property
    def inativo(self):
        """
        Gets the inativo of this EstabelecimentoResponse.
        {{{estabelecimento_response_inativo_value}}}

        :return: The inativo of this EstabelecimentoResponse.
        :rtype: int
        """
        return self._inativo

    @inativo.setter
    def inativo(self, inativo):
        """
        Sets the inativo of this EstabelecimentoResponse.
        {{{estabelecimento_response_inativo_value}}}

        :param inativo: The inativo of this EstabelecimentoResponse.
        :type: int
        """
        self._inativo = inativo

    @property
    def id_moeda(self):
        """
        Gets the id_moeda of this EstabelecimentoResponse.
        {{{estabelecimento_response_id_moeda_value}}}

        :return: The id_moeda of this EstabelecimentoResponse.
        :rtype: int
        """
        return self._id_moeda

    @id_moeda.setter
    def id_moeda(self, id_moeda):
        """
        Sets the id_moeda of this EstabelecimentoResponse.
        {{{estabelecimento_response_id_moeda_value}}}

        :param id_moeda: The id_moeda of this EstabelecimentoResponse.
        :type: int
        """
        self._id_moeda = id_moeda

    @property
    def id_pais(self):
        """
        Gets the id_pais of this EstabelecimentoResponse.
        {{{estabelecimento_response_id_pais_value}}}

        :return: The id_pais of this EstabelecimentoResponse.
        :rtype: int
        """
        return self._id_pais

    @id_pais.setter
    def id_pais(self, id_pais):
        """
        Sets the id_pais of this EstabelecimentoResponse.
        {{{estabelecimento_response_id_pais_value}}}

        :param id_pais: The id_pais of this EstabelecimentoResponse.
        :type: int
        """
        self._id_pais = id_pais

    @property
    def associado_spc_brasil(self):
        """
        Gets the associado_spc_brasil of this EstabelecimentoResponse.
        {{{estabelecimento_response_associado_s_p_c_brasil_value}}}

        :return: The associado_spc_brasil of this EstabelecimentoResponse.
        :rtype: int
        """
        return self._associado_spc_brasil

    @associado_spc_brasil.setter
    def associado_spc_brasil(self, associado_spc_brasil):
        """
        Sets the associado_spc_brasil of this EstabelecimentoResponse.
        {{{estabelecimento_response_associado_s_p_c_brasil_value}}}

        :param associado_spc_brasil: The associado_spc_brasil of this EstabelecimentoResponse.
        :type: int
        """
        self._associado_spc_brasil = associado_spc_brasil

    @property
    def mcc(self):
        """
        Gets the mcc of this EstabelecimentoResponse.
        {{{estabelecimento_response_mcc_value}}}

        :return: The mcc of this EstabelecimentoResponse.
        :rtype: int
        """
        return self._mcc

    @mcc.setter
    def mcc(self, mcc):
        """
        Sets the mcc of this EstabelecimentoResponse.
        {{{estabelecimento_response_mcc_value}}}

        :param mcc: The mcc of this EstabelecimentoResponse.
        :type: int
        """
        self._mcc = mcc

    @property
    def id_tipo_estabelecimento(self):
        """
        Gets the id_tipo_estabelecimento of this EstabelecimentoResponse.
        {{{estabelecimento_response_id_tipo_estabelecimento_value}}}

        :return: The id_tipo_estabelecimento of this EstabelecimentoResponse.
        :rtype: int
        """
        return self._id_tipo_estabelecimento

    @id_tipo_estabelecimento.setter
    def id_tipo_estabelecimento(self, id_tipo_estabelecimento):
        """
        Sets the id_tipo_estabelecimento of this EstabelecimentoResponse.
        {{{estabelecimento_response_id_tipo_estabelecimento_value}}}

        :param id_tipo_estabelecimento: The id_tipo_estabelecimento of this EstabelecimentoResponse.
        :type: int
        """
        self._id_tipo_estabelecimento = id_tipo_estabelecimento

    @property
    def correspondencia(self):
        """
        Gets the correspondencia of this EstabelecimentoResponse.
        {{{estabelecimento_response_correspondencia_value}}}

        :return: The correspondencia of this EstabelecimentoResponse.
        :rtype: int
        """
        return self._correspondencia

    @correspondencia.setter
    def correspondencia(self, correspondencia):
        """
        Sets the correspondencia of this EstabelecimentoResponse.
        {{{estabelecimento_response_correspondencia_value}}}

        :param correspondencia: The correspondencia of this EstabelecimentoResponse.
        :type: int
        """
        self._correspondencia = correspondencia

    @property
    def cargo_contato(self):
        """
        Gets the cargo_contato of this EstabelecimentoResponse.
        {{{estabelecimento_response_cargo_contato_value}}}

        :return: The cargo_contato of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._cargo_contato

    @cargo_contato.setter
    def cargo_contato(self, cargo_contato):
        """
        Sets the cargo_contato of this EstabelecimentoResponse.
        {{{estabelecimento_response_cargo_contato_value}}}

        :param cargo_contato: The cargo_contato of this EstabelecimentoResponse.
        :type: str
        """
        self._cargo_contato = cargo_contato

    @property
    def tipo_pagamento(self):
        """
        Gets the tipo_pagamento of this EstabelecimentoResponse.
        {{{estabelecimento_response_tipo_pagamento_value}}}

        :return: The tipo_pagamento of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._tipo_pagamento

    @tipo_pagamento.setter
    def tipo_pagamento(self, tipo_pagamento):
        """
        Sets the tipo_pagamento of this EstabelecimentoResponse.
        {{{estabelecimento_response_tipo_pagamento_value}}}

        :param tipo_pagamento: The tipo_pagamento of this EstabelecimentoResponse.
        :type: str
        """
        allowed_values = ["CENTRALIZADO", "PV"]
        if tipo_pagamento not in allowed_values:
            raise ValueError(
                "Invalid value for `tipo_pagamento`, must be one of {0}"
                .format(allowed_values)
            )
        self._tipo_pagamento = tipo_pagamento

    @property
    def consulta(self):
        """
        Gets the consulta of this EstabelecimentoResponse.
        {{{estabelecimento_response_consulta_value}}}

        :return: The consulta of this EstabelecimentoResponse.
        :rtype: ConsultaCadastroEstabelecimentoDTO
        """
        return self._consulta

    @consulta.setter
    def consulta(self, consulta):
        """
        Sets the consulta of this EstabelecimentoResponse.
        {{{estabelecimento_response_consulta_value}}}

        :param consulta: The consulta of this EstabelecimentoResponse.
        :type: ConsultaCadastroEstabelecimentoDTO
        """
        self._consulta = consulta

    @property
    def consulta2(self):
        """
        Gets the consulta2 of this EstabelecimentoResponse.
        {{{estabelecimento_response_consulta2_value}}}

        :return: The consulta2 of this EstabelecimentoResponse.
        :rtype: ConsultaCadastroEstabelecimentoDTO
        """
        return self._consulta2

    @consulta2.setter
    def consulta2(self, consulta2):
        """
        Sets the consulta2 of this EstabelecimentoResponse.
        {{{estabelecimento_response_consulta2_value}}}

        :param consulta2: The consulta2 of this EstabelecimentoResponse.
        :type: ConsultaCadastroEstabelecimentoDTO
        """
        self._consulta2 = consulta2

    @property
    def consulta3(self):
        """
        Gets the consulta3 of this EstabelecimentoResponse.
        {{{estabelecimento_response_consulta3_value}}}

        :return: The consulta3 of this EstabelecimentoResponse.
        :rtype: ConsultaCadastroEstabelecimentoDTO
        """
        return self._consulta3

    @consulta3.setter
    def consulta3(self, consulta3):
        """
        Sets the consulta3 of this EstabelecimentoResponse.
        {{{estabelecimento_response_consulta3_value}}}

        :param consulta3: The consulta3 of this EstabelecimentoResponse.
        :type: ConsultaCadastroEstabelecimentoDTO
        """
        self._consulta3 = consulta3

    @property
    def terminal(self):
        """
        Gets the terminal of this EstabelecimentoResponse.
        {{{estabelecimento_response_terminal_value}}}

        :return: The terminal of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """
        Sets the terminal of this EstabelecimentoResponse.
        {{{estabelecimento_response_terminal_value}}}

        :param terminal: The terminal of this EstabelecimentoResponse.
        :type: str
        """
        self._terminal = terminal

    @property
    def data_cadastramento(self):
        """
        Gets the data_cadastramento of this EstabelecimentoResponse.
        {{{estabelecimento_response_data_cadastramento_value}}}

        :return: The data_cadastramento of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._data_cadastramento

    @data_cadastramento.setter
    def data_cadastramento(self, data_cadastramento):
        """
        Sets the data_cadastramento of this EstabelecimentoResponse.
        {{{estabelecimento_response_data_cadastramento_value}}}

        :param data_cadastramento: The data_cadastramento of this EstabelecimentoResponse.
        :type: str
        """
        self._data_cadastramento = data_cadastramento

    @property
    def usuario(self):
        """
        Gets the usuario of this EstabelecimentoResponse.
        {{{estabelecimento_response_usuario_value}}}

        :return: The usuario of this EstabelecimentoResponse.
        :rtype: str
        """
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        """
        Sets the usuario of this EstabelecimentoResponse.
        {{{estabelecimento_response_usuario_value}}}

        :param usuario: The usuario of this EstabelecimentoResponse.
        :type: str
        """
        self._usuario = usuario

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

