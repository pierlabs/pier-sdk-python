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


class InscricaoAPNResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        InscricaoAPNResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'aplicacao_mobile': 'AplicacaoMobileEmissorResponse',
            'ativo': 'bool',
            'cartao': 'CartaoEmissorResponse',
            'data_criacao': 'str',
            'data_desativacao': 'str',
            'device_token': 'str',
            'id': 'int'
        }

        self.attribute_map = {
            'aplicacao_mobile': 'aplicacaoMobile',
            'ativo': 'ativo',
            'cartao': 'cartao',
            'data_criacao': 'dataCriacao',
            'data_desativacao': 'dataDesativacao',
            'device_token': 'deviceToken',
            'id': 'id'
        }

        self._aplicacao_mobile = None
        self._ativo = None
        self._cartao = None
        self._data_criacao = None
        self._data_desativacao = None
        self._device_token = None
        self._id = None

    @property
    def aplicacao_mobile(self):
        """
        Gets the aplicacao_mobile of this InscricaoAPNResponse.
        {{{inscricao_apn_resposta_aplicacao_mobile_descricao}}}

        :return: The aplicacao_mobile of this InscricaoAPNResponse.
        :rtype: AplicacaoMobileEmissorResponse
        """
        return self._aplicacao_mobile

    @aplicacao_mobile.setter
    def aplicacao_mobile(self, aplicacao_mobile):
        """
        Sets the aplicacao_mobile of this InscricaoAPNResponse.
        {{{inscricao_apn_resposta_aplicacao_mobile_descricao}}}

        :param aplicacao_mobile: The aplicacao_mobile of this InscricaoAPNResponse.
        :type: AplicacaoMobileEmissorResponse
        """
        self._aplicacao_mobile = aplicacao_mobile

    @property
    def ativo(self):
        """
        Gets the ativo of this InscricaoAPNResponse.
        {{{inscricao_apn_resposta_ativo_descricao}}}

        :return: The ativo of this InscricaoAPNResponse.
        :rtype: bool
        """
        return self._ativo

    @ativo.setter
    def ativo(self, ativo):
        """
        Sets the ativo of this InscricaoAPNResponse.
        {{{inscricao_apn_resposta_ativo_descricao}}}

        :param ativo: The ativo of this InscricaoAPNResponse.
        :type: bool
        """
        self._ativo = ativo

    @property
    def cartao(self):
        """
        Gets the cartao of this InscricaoAPNResponse.
        {{{inscricao_apn_resposta_cartao_descricao}}}

        :return: The cartao of this InscricaoAPNResponse.
        :rtype: CartaoEmissorResponse
        """
        return self._cartao

    @cartao.setter
    def cartao(self, cartao):
        """
        Sets the cartao of this InscricaoAPNResponse.
        {{{inscricao_apn_resposta_cartao_descricao}}}

        :param cartao: The cartao of this InscricaoAPNResponse.
        :type: CartaoEmissorResponse
        """
        self._cartao = cartao

    @property
    def data_criacao(self):
        """
        Gets the data_criacao of this InscricaoAPNResponse.
        {{{inscricao_apn_resposta_data_criacao_descricao}}}

        :return: The data_criacao of this InscricaoAPNResponse.
        :rtype: str
        """
        return self._data_criacao

    @data_criacao.setter
    def data_criacao(self, data_criacao):
        """
        Sets the data_criacao of this InscricaoAPNResponse.
        {{{inscricao_apn_resposta_data_criacao_descricao}}}

        :param data_criacao: The data_criacao of this InscricaoAPNResponse.
        :type: str
        """
        self._data_criacao = data_criacao

    @property
    def data_desativacao(self):
        """
        Gets the data_desativacao of this InscricaoAPNResponse.
        {{{inscricao_apn_resposta_data_desativacao_descricao}}}

        :return: The data_desativacao of this InscricaoAPNResponse.
        :rtype: str
        """
        return self._data_desativacao

    @data_desativacao.setter
    def data_desativacao(self, data_desativacao):
        """
        Sets the data_desativacao of this InscricaoAPNResponse.
        {{{inscricao_apn_resposta_data_desativacao_descricao}}}

        :param data_desativacao: The data_desativacao of this InscricaoAPNResponse.
        :type: str
        """
        self._data_desativacao = data_desativacao

    @property
    def device_token(self):
        """
        Gets the device_token of this InscricaoAPNResponse.
        {{{inscricao_apn_resposta_device_token_descricao}}}

        :return: The device_token of this InscricaoAPNResponse.
        :rtype: str
        """
        return self._device_token

    @device_token.setter
    def device_token(self, device_token):
        """
        Sets the device_token of this InscricaoAPNResponse.
        {{{inscricao_apn_resposta_device_token_descricao}}}

        :param device_token: The device_token of this InscricaoAPNResponse.
        :type: str
        """
        self._device_token = device_token

    @property
    def id(self):
        """
        Gets the id of this InscricaoAPNResponse.
        {{{inscricao_apn_resposta_id_descricao}}}

        :return: The id of this InscricaoAPNResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InscricaoAPNResponse.
        {{{inscricao_apn_resposta_id_descricao}}}

        :param id: The id of this InscricaoAPNResponse.
        :type: int
        """
        self._id = id

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

