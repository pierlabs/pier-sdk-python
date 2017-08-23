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


class PessoaFisicaAprovadaResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PessoaFisicaAprovadaResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'nome': 'str',
            'nome_mae': 'str',
            'data_nascimento': 'str',
            'sexo': 'str',
            'cpf': 'str',
            'numero_identidade': 'str',
            'orgao_expedidor_identidade': 'str',
            'unidade_federativa_identidade': 'str',
            'data_emissao_identidade': 'str',
            'id_estado_civil': 'int',
            'id_profissao': 'int',
            'id_natureza_ocupacao': 'int',
            'id_nacionalidade': 'int',
            'id_origem_comercial': 'int',
            'id_produto': 'int',
            'numero_agencia': 'int',
            'numero_conta_corrente': 'str',
            'email': 'str',
            'dia_vencimento': 'int',
            'nome_impresso': 'str',
            'nome_empresa': 'str',
            'id_conta': 'int',
            'id_proposta': 'int',
            'canal_entrada': 'str',
            'valor_pontuacao': 'int',
            'telefones': 'list[TelefonePessoaAprovadaResponse]',
            'enderecos': 'list[EnderecoAprovadoResponse]',
            'limite_global': 'float',
            'limite_maximo': 'float',
            'limite_parcelas': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'nome': 'nome',
            'nome_mae': 'nomeMae',
            'data_nascimento': 'dataNascimento',
            'sexo': 'sexo',
            'cpf': 'cpf',
            'numero_identidade': 'numeroIdentidade',
            'orgao_expedidor_identidade': 'orgaoExpedidorIdentidade',
            'unidade_federativa_identidade': 'unidadeFederativaIdentidade',
            'data_emissao_identidade': 'dataEmissaoIdentidade',
            'id_estado_civil': 'idEstadoCivil',
            'id_profissao': 'idProfissao',
            'id_natureza_ocupacao': 'idNaturezaOcupacao',
            'id_nacionalidade': 'idNacionalidade',
            'id_origem_comercial': 'idOrigemComercial',
            'id_produto': 'idProduto',
            'numero_agencia': 'numeroAgencia',
            'numero_conta_corrente': 'numeroContaCorrente',
            'email': 'email',
            'dia_vencimento': 'diaVencimento',
            'nome_impresso': 'nomeImpresso',
            'nome_empresa': 'nomeEmpresa',
            'id_conta': 'idConta',
            'id_proposta': 'idProposta',
            'canal_entrada': 'canalEntrada',
            'valor_pontuacao': 'valorPontuacao',
            'telefones': 'telefones',
            'enderecos': 'enderecos',
            'limite_global': 'limiteGlobal',
            'limite_maximo': 'limiteMaximo',
            'limite_parcelas': 'limiteParcelas'
        }

        self._id = None
        self._nome = None
        self._nome_mae = None
        self._data_nascimento = None
        self._sexo = None
        self._cpf = None
        self._numero_identidade = None
        self._orgao_expedidor_identidade = None
        self._unidade_federativa_identidade = None
        self._data_emissao_identidade = None
        self._id_estado_civil = None
        self._id_profissao = None
        self._id_natureza_ocupacao = None
        self._id_nacionalidade = None
        self._id_origem_comercial = None
        self._id_produto = None
        self._numero_agencia = None
        self._numero_conta_corrente = None
        self._email = None
        self._dia_vencimento = None
        self._nome_impresso = None
        self._nome_empresa = None
        self._id_conta = None
        self._id_proposta = None
        self._canal_entrada = None
        self._valor_pontuacao = None
        self._telefones = None
        self._enderecos = None
        self._limite_global = None
        self._limite_maximo = None
        self._limite_parcelas = None

    @property
    def id(self):
        """
        Gets the id of this PessoaFisicaAprovadaResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da pessoa fisica (id)

        :return: The id of this PessoaFisicaAprovadaResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PessoaFisicaAprovadaResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da pessoa fisica (id)

        :param id: The id of this PessoaFisicaAprovadaResponse.
        :type: int
        """
        self._id = id

    @property
    def nome(self):
        """
        Gets the nome of this PessoaFisicaAprovadaResponse.
        Apresenta o nome completo da pessoa fisica.

        :return: The nome of this PessoaFisicaAprovadaResponse.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Sets the nome of this PessoaFisicaAprovadaResponse.
        Apresenta o nome completo da pessoa fisica.

        :param nome: The nome of this PessoaFisicaAprovadaResponse.
        :type: str
        """
        self._nome = nome

    @property
    def nome_mae(self):
        """
        Gets the nome_mae of this PessoaFisicaAprovadaResponse.
        Apresenta o nome da m\u00C3\u00A3e da pessoa fisica

        :return: The nome_mae of this PessoaFisicaAprovadaResponse.
        :rtype: str
        """
        return self._nome_mae

    @nome_mae.setter
    def nome_mae(self, nome_mae):
        """
        Sets the nome_mae of this PessoaFisicaAprovadaResponse.
        Apresenta o nome da m\u00C3\u00A3e da pessoa fisica

        :param nome_mae: The nome_mae of this PessoaFisicaAprovadaResponse.
        :type: str
        """
        self._nome_mae = nome_mae

    @property
    def data_nascimento(self):
        """
        Gets the data_nascimento of this PessoaFisicaAprovadaResponse.
        Data de Nascimento da Pessoa. Essa data deve ser informada no formato aaaa-MM-dd.

        :return: The data_nascimento of this PessoaFisicaAprovadaResponse.
        :rtype: str
        """
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        """
        Sets the data_nascimento of this PessoaFisicaAprovadaResponse.
        Data de Nascimento da Pessoa. Essa data deve ser informada no formato aaaa-MM-dd.

        :param data_nascimento: The data_nascimento of this PessoaFisicaAprovadaResponse.
        :type: str
        """
        self._data_nascimento = data_nascimento

    @property
    def sexo(self):
        """
        Gets the sexo of this PessoaFisicaAprovadaResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do sexo da Pessoa, quando PF, sendo: (\"M\": Masculino), (\"F\": Feminino).

        :return: The sexo of this PessoaFisicaAprovadaResponse.
        :rtype: str
        """
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        """
        Sets the sexo of this PessoaFisicaAprovadaResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do sexo da Pessoa, quando PF, sendo: (\"M\": Masculino), (\"F\": Feminino).

        :param sexo: The sexo of this PessoaFisicaAprovadaResponse.
        :type: str
        """
        self._sexo = sexo

    @property
    def cpf(self):
        """
        Gets the cpf of this PessoaFisicaAprovadaResponse.
        N\u00C3\u00BAmero do Cadastro de Pessoa Fisica (CPF)

        :return: The cpf of this PessoaFisicaAprovadaResponse.
        :rtype: str
        """
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        """
        Sets the cpf of this PessoaFisicaAprovadaResponse.
        N\u00C3\u00BAmero do Cadastro de Pessoa Fisica (CPF)

        :param cpf: The cpf of this PessoaFisicaAprovadaResponse.
        :type: str
        """
        self._cpf = cpf

    @property
    def numero_identidade(self):
        """
        Gets the numero_identidade of this PessoaFisicaAprovadaResponse.
        N\u00C3\u00BAmero da identidade.

        :return: The numero_identidade of this PessoaFisicaAprovadaResponse.
        :rtype: str
        """
        return self._numero_identidade

    @numero_identidade.setter
    def numero_identidade(self, numero_identidade):
        """
        Sets the numero_identidade of this PessoaFisicaAprovadaResponse.
        N\u00C3\u00BAmero da identidade.

        :param numero_identidade: The numero_identidade of this PessoaFisicaAprovadaResponse.
        :type: str
        """
        self._numero_identidade = numero_identidade

    @property
    def orgao_expedidor_identidade(self):
        """
        Gets the orgao_expedidor_identidade of this PessoaFisicaAprovadaResponse.
        Org\u00C3\u00A3o expedidor da Identidade.

        :return: The orgao_expedidor_identidade of this PessoaFisicaAprovadaResponse.
        :rtype: str
        """
        return self._orgao_expedidor_identidade

    @orgao_expedidor_identidade.setter
    def orgao_expedidor_identidade(self, orgao_expedidor_identidade):
        """
        Sets the orgao_expedidor_identidade of this PessoaFisicaAprovadaResponse.
        Org\u00C3\u00A3o expedidor da Identidade.

        :param orgao_expedidor_identidade: The orgao_expedidor_identidade of this PessoaFisicaAprovadaResponse.
        :type: str
        """
        self._orgao_expedidor_identidade = orgao_expedidor_identidade

    @property
    def unidade_federativa_identidade(self):
        """
        Gets the unidade_federativa_identidade of this PessoaFisicaAprovadaResponse.
        Sigla da Unidade Federativa de onde foi expedido a Identidade

        :return: The unidade_federativa_identidade of this PessoaFisicaAprovadaResponse.
        :rtype: str
        """
        return self._unidade_federativa_identidade

    @unidade_federativa_identidade.setter
    def unidade_federativa_identidade(self, unidade_federativa_identidade):
        """
        Sets the unidade_federativa_identidade of this PessoaFisicaAprovadaResponse.
        Sigla da Unidade Federativa de onde foi expedido a Identidade

        :param unidade_federativa_identidade: The unidade_federativa_identidade of this PessoaFisicaAprovadaResponse.
        :type: str
        """
        self._unidade_federativa_identidade = unidade_federativa_identidade

    @property
    def data_emissao_identidade(self):
        """
        Gets the data_emissao_identidade of this PessoaFisicaAprovadaResponse.
        Data emiss\u00C3\u00A3o da Identidade no formato aaaa-MM-dd

        :return: The data_emissao_identidade of this PessoaFisicaAprovadaResponse.
        :rtype: str
        """
        return self._data_emissao_identidade

    @data_emissao_identidade.setter
    def data_emissao_identidade(self, data_emissao_identidade):
        """
        Sets the data_emissao_identidade of this PessoaFisicaAprovadaResponse.
        Data emiss\u00C3\u00A3o da Identidade no formato aaaa-MM-dd

        :param data_emissao_identidade: The data_emissao_identidade of this PessoaFisicaAprovadaResponse.
        :type: str
        """
        self._data_emissao_identidade = data_emissao_identidade

    @property
    def id_estado_civil(self):
        """
        Gets the id_estado_civil of this PessoaFisicaAprovadaResponse.
        Id Estado civil da pessoa fisica

        :return: The id_estado_civil of this PessoaFisicaAprovadaResponse.
        :rtype: int
        """
        return self._id_estado_civil

    @id_estado_civil.setter
    def id_estado_civil(self, id_estado_civil):
        """
        Sets the id_estado_civil of this PessoaFisicaAprovadaResponse.
        Id Estado civil da pessoa fisica

        :param id_estado_civil: The id_estado_civil of this PessoaFisicaAprovadaResponse.
        :type: int
        """
        self._id_estado_civil = id_estado_civil

    @property
    def id_profissao(self):
        """
        Gets the id_profissao of this PessoaFisicaAprovadaResponse.
        Profiss\u00C3\u00A3o da pessoa fisica

        :return: The id_profissao of this PessoaFisicaAprovadaResponse.
        :rtype: int
        """
        return self._id_profissao

    @id_profissao.setter
    def id_profissao(self, id_profissao):
        """
        Sets the id_profissao of this PessoaFisicaAprovadaResponse.
        Profiss\u00C3\u00A3o da pessoa fisica

        :param id_profissao: The id_profissao of this PessoaFisicaAprovadaResponse.
        :type: int
        """
        self._id_profissao = id_profissao

    @property
    def id_natureza_ocupacao(self):
        """
        Gets the id_natureza_ocupacao of this PessoaFisicaAprovadaResponse.
        Id Natureza Ocupa\u00C3\u00A7\u00C3\u00A3o da pessoa fisica

        :return: The id_natureza_ocupacao of this PessoaFisicaAprovadaResponse.
        :rtype: int
        """
        return self._id_natureza_ocupacao

    @id_natureza_ocupacao.setter
    def id_natureza_ocupacao(self, id_natureza_ocupacao):
        """
        Sets the id_natureza_ocupacao of this PessoaFisicaAprovadaResponse.
        Id Natureza Ocupa\u00C3\u00A7\u00C3\u00A3o da pessoa fisica

        :param id_natureza_ocupacao: The id_natureza_ocupacao of this PessoaFisicaAprovadaResponse.
        :type: int
        """
        self._id_natureza_ocupacao = id_natureza_ocupacao

    @property
    def id_nacionalidade(self):
        """
        Gets the id_nacionalidade of this PessoaFisicaAprovadaResponse.
        Id Nacionalidade da pessoa fisica

        :return: The id_nacionalidade of this PessoaFisicaAprovadaResponse.
        :rtype: int
        """
        return self._id_nacionalidade

    @id_nacionalidade.setter
    def id_nacionalidade(self, id_nacionalidade):
        """
        Sets the id_nacionalidade of this PessoaFisicaAprovadaResponse.
        Id Nacionalidade da pessoa fisica

        :param id_nacionalidade: The id_nacionalidade of this PessoaFisicaAprovadaResponse.
        :type: int
        """
        self._id_nacionalidade = id_nacionalidade

    @property
    def id_origem_comercial(self):
        """
        Gets the id_origem_comercial of this PessoaFisicaAprovadaResponse.
        Id da origem comercial

        :return: The id_origem_comercial of this PessoaFisicaAprovadaResponse.
        :rtype: int
        """
        return self._id_origem_comercial

    @id_origem_comercial.setter
    def id_origem_comercial(self, id_origem_comercial):
        """
        Sets the id_origem_comercial of this PessoaFisicaAprovadaResponse.
        Id da origem comercial

        :param id_origem_comercial: The id_origem_comercial of this PessoaFisicaAprovadaResponse.
        :type: int
        """
        self._id_origem_comercial = id_origem_comercial

    @property
    def id_produto(self):
        """
        Gets the id_produto of this PessoaFisicaAprovadaResponse.
        Id do produto

        :return: The id_produto of this PessoaFisicaAprovadaResponse.
        :rtype: int
        """
        return self._id_produto

    @id_produto.setter
    def id_produto(self, id_produto):
        """
        Sets the id_produto of this PessoaFisicaAprovadaResponse.
        Id do produto

        :param id_produto: The id_produto of this PessoaFisicaAprovadaResponse.
        :type: int
        """
        self._id_produto = id_produto

    @property
    def numero_agencia(self):
        """
        Gets the numero_agencia of this PessoaFisicaAprovadaResponse.
        N\u00C3\u00BAmero da ag\u00C3\u00AAncia.

        :return: The numero_agencia of this PessoaFisicaAprovadaResponse.
        :rtype: int
        """
        return self._numero_agencia

    @numero_agencia.setter
    def numero_agencia(self, numero_agencia):
        """
        Sets the numero_agencia of this PessoaFisicaAprovadaResponse.
        N\u00C3\u00BAmero da ag\u00C3\u00AAncia.

        :param numero_agencia: The numero_agencia of this PessoaFisicaAprovadaResponse.
        :type: int
        """
        self._numero_agencia = numero_agencia

    @property
    def numero_conta_corrente(self):
        """
        Gets the numero_conta_corrente of this PessoaFisicaAprovadaResponse.
        N\u00C3\u00BAmero da conta corrente.

        :return: The numero_conta_corrente of this PessoaFisicaAprovadaResponse.
        :rtype: str
        """
        return self._numero_conta_corrente

    @numero_conta_corrente.setter
    def numero_conta_corrente(self, numero_conta_corrente):
        """
        Sets the numero_conta_corrente of this PessoaFisicaAprovadaResponse.
        N\u00C3\u00BAmero da conta corrente.

        :param numero_conta_corrente: The numero_conta_corrente of this PessoaFisicaAprovadaResponse.
        :type: str
        """
        self._numero_conta_corrente = numero_conta_corrente

    @property
    def email(self):
        """
        Gets the email of this PessoaFisicaAprovadaResponse.
        Email da pessoa fisica

        :return: The email of this PessoaFisicaAprovadaResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this PessoaFisicaAprovadaResponse.
        Email da pessoa fisica

        :param email: The email of this PessoaFisicaAprovadaResponse.
        :type: str
        """
        self._email = email

    @property
    def dia_vencimento(self):
        """
        Gets the dia_vencimento of this PessoaFisicaAprovadaResponse.
        Dia vencimento

        :return: The dia_vencimento of this PessoaFisicaAprovadaResponse.
        :rtype: int
        """
        return self._dia_vencimento

    @dia_vencimento.setter
    def dia_vencimento(self, dia_vencimento):
        """
        Sets the dia_vencimento of this PessoaFisicaAprovadaResponse.
        Dia vencimento

        :param dia_vencimento: The dia_vencimento of this PessoaFisicaAprovadaResponse.
        :type: int
        """
        self._dia_vencimento = dia_vencimento

    @property
    def nome_impresso(self):
        """
        Gets the nome_impresso of this PessoaFisicaAprovadaResponse.
        Nome que deve ser impresso no cart\u00C3\u00A3o

        :return: The nome_impresso of this PessoaFisicaAprovadaResponse.
        :rtype: str
        """
        return self._nome_impresso

    @nome_impresso.setter
    def nome_impresso(self, nome_impresso):
        """
        Sets the nome_impresso of this PessoaFisicaAprovadaResponse.
        Nome que deve ser impresso no cart\u00C3\u00A3o

        :param nome_impresso: The nome_impresso of this PessoaFisicaAprovadaResponse.
        :type: str
        """
        self._nome_impresso = nome_impresso

    @property
    def nome_empresa(self):
        """
        Gets the nome_empresa of this PessoaFisicaAprovadaResponse.
        Nome da empresa

        :return: The nome_empresa of this PessoaFisicaAprovadaResponse.
        :rtype: str
        """
        return self._nome_empresa

    @nome_empresa.setter
    def nome_empresa(self, nome_empresa):
        """
        Sets the nome_empresa of this PessoaFisicaAprovadaResponse.
        Nome da empresa

        :param nome_empresa: The nome_empresa of this PessoaFisicaAprovadaResponse.
        :type: str
        """
        self._nome_empresa = nome_empresa

    @property
    def id_conta(self):
        """
        Gets the id_conta of this PessoaFisicaAprovadaResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da conta cadastrada

        :return: The id_conta of this PessoaFisicaAprovadaResponse.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this PessoaFisicaAprovadaResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da conta cadastrada

        :param id_conta: The id_conta of this PessoaFisicaAprovadaResponse.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def id_proposta(self):
        """
        Gets the id_proposta of this PessoaFisicaAprovadaResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da proposta

        :return: The id_proposta of this PessoaFisicaAprovadaResponse.
        :rtype: int
        """
        return self._id_proposta

    @id_proposta.setter
    def id_proposta(self, id_proposta):
        """
        Sets the id_proposta of this PessoaFisicaAprovadaResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da proposta

        :param id_proposta: The id_proposta of this PessoaFisicaAprovadaResponse.
        :type: int
        """
        self._id_proposta = id_proposta

    @property
    def canal_entrada(self):
        """
        Gets the canal_entrada of this PessoaFisicaAprovadaResponse.
        Indica o canal pelo qual o cadastro do cliente foi realizado

        :return: The canal_entrada of this PessoaFisicaAprovadaResponse.
        :rtype: str
        """
        return self._canal_entrada

    @canal_entrada.setter
    def canal_entrada(self, canal_entrada):
        """
        Sets the canal_entrada of this PessoaFisicaAprovadaResponse.
        Indica o canal pelo qual o cadastro do cliente foi realizado

        :param canal_entrada: The canal_entrada of this PessoaFisicaAprovadaResponse.
        :type: str
        """
        self._canal_entrada = canal_entrada

    @property
    def valor_pontuacao(self):
        """
        Gets the valor_pontuacao of this PessoaFisicaAprovadaResponse.
        Indica o valor da pontua\u00C3\u00A7\u00C3\u00A3o atribuido ao cliente (caso n\u00C3\u00A3o informado ser\u00C3\u00A1 atribuido o valor = 0)

        :return: The valor_pontuacao of this PessoaFisicaAprovadaResponse.
        :rtype: int
        """
        return self._valor_pontuacao

    @valor_pontuacao.setter
    def valor_pontuacao(self, valor_pontuacao):
        """
        Sets the valor_pontuacao of this PessoaFisicaAprovadaResponse.
        Indica o valor da pontua\u00C3\u00A7\u00C3\u00A3o atribuido ao cliente (caso n\u00C3\u00A3o informado ser\u00C3\u00A1 atribuido o valor = 0)

        :param valor_pontuacao: The valor_pontuacao of this PessoaFisicaAprovadaResponse.
        :type: int
        """
        self._valor_pontuacao = valor_pontuacao

    @property
    def telefones(self):
        """
        Gets the telefones of this PessoaFisicaAprovadaResponse.
        Apresenta os telefones da empresa

        :return: The telefones of this PessoaFisicaAprovadaResponse.
        :rtype: list[TelefonePessoaAprovadaResponse]
        """
        return self._telefones

    @telefones.setter
    def telefones(self, telefones):
        """
        Sets the telefones of this PessoaFisicaAprovadaResponse.
        Apresenta os telefones da empresa

        :param telefones: The telefones of this PessoaFisicaAprovadaResponse.
        :type: list[TelefonePessoaAprovadaResponse]
        """
        self._telefones = telefones

    @property
    def enderecos(self):
        """
        Gets the enderecos of this PessoaFisicaAprovadaResponse.
        Pode ser informado os seguintes tipos de endere\u00C3\u00A7o: Residencial, Comercial, e Outros

        :return: The enderecos of this PessoaFisicaAprovadaResponse.
        :rtype: list[EnderecoAprovadoResponse]
        """
        return self._enderecos

    @enderecos.setter
    def enderecos(self, enderecos):
        """
        Sets the enderecos of this PessoaFisicaAprovadaResponse.
        Pode ser informado os seguintes tipos de endere\u00C3\u00A7o: Residencial, Comercial, e Outros

        :param enderecos: The enderecos of this PessoaFisicaAprovadaResponse.
        :type: list[EnderecoAprovadoResponse]
        """
        self._enderecos = enderecos

    @property
    def limite_global(self):
        """
        Gets the limite_global of this PessoaFisicaAprovadaResponse.
        Valor do Limite Global

        :return: The limite_global of this PessoaFisicaAprovadaResponse.
        :rtype: float
        """
        return self._limite_global

    @limite_global.setter
    def limite_global(self, limite_global):
        """
        Sets the limite_global of this PessoaFisicaAprovadaResponse.
        Valor do Limite Global

        :param limite_global: The limite_global of this PessoaFisicaAprovadaResponse.
        :type: float
        """
        self._limite_global = limite_global

    @property
    def limite_maximo(self):
        """
        Gets the limite_maximo of this PessoaFisicaAprovadaResponse.
        Valor m\u00C3\u00A1ximo do limite de cr\u00C3\u00A9dito para realizar transa\u00C3\u00A7\u00C3\u00B5es

        :return: The limite_maximo of this PessoaFisicaAprovadaResponse.
        :rtype: float
        """
        return self._limite_maximo

    @limite_maximo.setter
    def limite_maximo(self, limite_maximo):
        """
        Sets the limite_maximo of this PessoaFisicaAprovadaResponse.
        Valor m\u00C3\u00A1ximo do limite de cr\u00C3\u00A9dito para realizar transa\u00C3\u00A7\u00C3\u00B5es

        :param limite_maximo: The limite_maximo of this PessoaFisicaAprovadaResponse.
        :type: float
        """
        self._limite_maximo = limite_maximo

    @property
    def limite_parcelas(self):
        """
        Gets the limite_parcelas of this PessoaFisicaAprovadaResponse.
        Valor do limite de cr\u00C3\u00A9dito acumulado da soma das parcelas das compras

        :return: The limite_parcelas of this PessoaFisicaAprovadaResponse.
        :rtype: float
        """
        return self._limite_parcelas

    @limite_parcelas.setter
    def limite_parcelas(self, limite_parcelas):
        """
        Sets the limite_parcelas of this PessoaFisicaAprovadaResponse.
        Valor do limite de cr\u00C3\u00A9dito acumulado da soma das parcelas das compras

        :param limite_parcelas: The limite_parcelas of this PessoaFisicaAprovadaResponse.
        :type: float
        """
        self._limite_parcelas = limite_parcelas

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

