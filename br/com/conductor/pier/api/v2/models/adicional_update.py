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


class AdicionalUpdate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AdicionalUpdate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'nome': 'str',
            'nome_impresso': 'str',
            'numero_receita_federal': 'str',
            'data_nascimento': 'str',
            'sexo': 'str',
            'numero_identidade': 'str',
            'orgao_expedidor_identidade': 'str',
            'unidade_federativa_identidade': 'str',
            'data_emissao_identidade': 'str',
            'id_parentesco': 'int',
            'telefones': 'list[TelefoneAdicionalUpdate]'
        }

        self.attribute_map = {
            'nome': 'nome',
            'nome_impresso': 'nomeImpresso',
            'numero_receita_federal': 'numeroReceitaFederal',
            'data_nascimento': 'dataNascimento',
            'sexo': 'sexo',
            'numero_identidade': 'numeroIdentidade',
            'orgao_expedidor_identidade': 'orgaoExpedidorIdentidade',
            'unidade_federativa_identidade': 'unidadeFederativaIdentidade',
            'data_emissao_identidade': 'dataEmissaoIdentidade',
            'id_parentesco': 'idParentesco',
            'telefones': 'telefones'
        }

        self._nome = None
        self._nome_impresso = None
        self._numero_receita_federal = None
        self._data_nascimento = None
        self._sexo = None
        self._numero_identidade = None
        self._orgao_expedidor_identidade = None
        self._unidade_federativa_identidade = None
        self._data_emissao_identidade = None
        self._id_parentesco = None
        self._telefones = None

    @property
    def nome(self):
        """
        Gets the nome of this AdicionalUpdate.
        {{{adicional_update_nome_value}}}

        :return: The nome of this AdicionalUpdate.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Sets the nome of this AdicionalUpdate.
        {{{adicional_update_nome_value}}}

        :param nome: The nome of this AdicionalUpdate.
        :type: str
        """
        self._nome = nome

    @property
    def nome_impresso(self):
        """
        Gets the nome_impresso of this AdicionalUpdate.
        {{{adicional_update_nome_impresso_value}}}

        :return: The nome_impresso of this AdicionalUpdate.
        :rtype: str
        """
        return self._nome_impresso

    @nome_impresso.setter
    def nome_impresso(self, nome_impresso):
        """
        Sets the nome_impresso of this AdicionalUpdate.
        {{{adicional_update_nome_impresso_value}}}

        :param nome_impresso: The nome_impresso of this AdicionalUpdate.
        :type: str
        """
        self._nome_impresso = nome_impresso

    @property
    def numero_receita_federal(self):
        """
        Gets the numero_receita_federal of this AdicionalUpdate.
        {{{adicional_update_numero_receita_federal_value}}}

        :return: The numero_receita_federal of this AdicionalUpdate.
        :rtype: str
        """
        return self._numero_receita_federal

    @numero_receita_federal.setter
    def numero_receita_federal(self, numero_receita_federal):
        """
        Sets the numero_receita_federal of this AdicionalUpdate.
        {{{adicional_update_numero_receita_federal_value}}}

        :param numero_receita_federal: The numero_receita_federal of this AdicionalUpdate.
        :type: str
        """
        self._numero_receita_federal = numero_receita_federal

    @property
    def data_nascimento(self):
        """
        Gets the data_nascimento of this AdicionalUpdate.
        {{{adicional_update_data_nascimento_value}}}

        :return: The data_nascimento of this AdicionalUpdate.
        :rtype: str
        """
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        """
        Sets the data_nascimento of this AdicionalUpdate.
        {{{adicional_update_data_nascimento_value}}}

        :param data_nascimento: The data_nascimento of this AdicionalUpdate.
        :type: str
        """
        self._data_nascimento = data_nascimento

    @property
    def sexo(self):
        """
        Gets the sexo of this AdicionalUpdate.
        {{{adicional_update_sexo_value}}}

        :return: The sexo of this AdicionalUpdate.
        :rtype: str
        """
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        """
        Sets the sexo of this AdicionalUpdate.
        {{{adicional_update_sexo_value}}}

        :param sexo: The sexo of this AdicionalUpdate.
        :type: str
        """
        self._sexo = sexo

    @property
    def numero_identidade(self):
        """
        Gets the numero_identidade of this AdicionalUpdate.
        {{{adicional_update_numero_identidade_value}}}

        :return: The numero_identidade of this AdicionalUpdate.
        :rtype: str
        """
        return self._numero_identidade

    @numero_identidade.setter
    def numero_identidade(self, numero_identidade):
        """
        Sets the numero_identidade of this AdicionalUpdate.
        {{{adicional_update_numero_identidade_value}}}

        :param numero_identidade: The numero_identidade of this AdicionalUpdate.
        :type: str
        """
        self._numero_identidade = numero_identidade

    @property
    def orgao_expedidor_identidade(self):
        """
        Gets the orgao_expedidor_identidade of this AdicionalUpdate.
        {{{adicional_update_orgao_expedidor_identidade_value}}}

        :return: The orgao_expedidor_identidade of this AdicionalUpdate.
        :rtype: str
        """
        return self._orgao_expedidor_identidade

    @orgao_expedidor_identidade.setter
    def orgao_expedidor_identidade(self, orgao_expedidor_identidade):
        """
        Sets the orgao_expedidor_identidade of this AdicionalUpdate.
        {{{adicional_update_orgao_expedidor_identidade_value}}}

        :param orgao_expedidor_identidade: The orgao_expedidor_identidade of this AdicionalUpdate.
        :type: str
        """
        self._orgao_expedidor_identidade = orgao_expedidor_identidade

    @property
    def unidade_federativa_identidade(self):
        """
        Gets the unidade_federativa_identidade of this AdicionalUpdate.
        {{{adicional_update_unidade_federativa_identidade_value}}}

        :return: The unidade_federativa_identidade of this AdicionalUpdate.
        :rtype: str
        """
        return self._unidade_federativa_identidade

    @unidade_federativa_identidade.setter
    def unidade_federativa_identidade(self, unidade_federativa_identidade):
        """
        Sets the unidade_federativa_identidade of this AdicionalUpdate.
        {{{adicional_update_unidade_federativa_identidade_value}}}

        :param unidade_federativa_identidade: The unidade_federativa_identidade of this AdicionalUpdate.
        :type: str
        """
        self._unidade_federativa_identidade = unidade_federativa_identidade

    @property
    def data_emissao_identidade(self):
        """
        Gets the data_emissao_identidade of this AdicionalUpdate.
        {{{adicional_update_data_emissao_identidade_value}}}

        :return: The data_emissao_identidade of this AdicionalUpdate.
        :rtype: str
        """
        return self._data_emissao_identidade

    @data_emissao_identidade.setter
    def data_emissao_identidade(self, data_emissao_identidade):
        """
        Sets the data_emissao_identidade of this AdicionalUpdate.
        {{{adicional_update_data_emissao_identidade_value}}}

        :param data_emissao_identidade: The data_emissao_identidade of this AdicionalUpdate.
        :type: str
        """
        self._data_emissao_identidade = data_emissao_identidade

    @property
    def id_parentesco(self):
        """
        Gets the id_parentesco of this AdicionalUpdate.
        {{{adicional_update_id_parentesco_value}}}

        :return: The id_parentesco of this AdicionalUpdate.
        :rtype: int
        """
        return self._id_parentesco

    @id_parentesco.setter
    def id_parentesco(self, id_parentesco):
        """
        Sets the id_parentesco of this AdicionalUpdate.
        {{{adicional_update_id_parentesco_value}}}

        :param id_parentesco: The id_parentesco of this AdicionalUpdate.
        :type: int
        """
        self._id_parentesco = id_parentesco

    @property
    def telefones(self):
        """
        Gets the telefones of this AdicionalUpdate.
        {{{adicional_update_telefones_value}}}

        :return: The telefones of this AdicionalUpdate.
        :rtype: list[TelefoneAdicionalUpdate]
        """
        return self._telefones

    @telefones.setter
    def telefones(self, telefones):
        """
        Sets the telefones of this AdicionalUpdate.
        {{{adicional_update_telefones_value}}}

        :param telefones: The telefones of this AdicionalUpdate.
        :type: list[TelefoneAdicionalUpdate]
        """
        self._telefones = telefones

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

