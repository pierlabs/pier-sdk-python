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


class BoletoEmailRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BoletoEmailRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'email': 'str',
            'id_template_notificacao': 'int',
            'parametros': 'object'
        }

        self.attribute_map = {
            'email': 'email',
            'id_template_notificacao': 'idTemplateNotificacao',
            'parametros': 'parametros'
        }

        self._email = None
        self._id_template_notificacao = None
        self._parametros = None

    @property
    def email(self):
        """
        Gets the email of this BoletoEmailRequest.
        {{{boleto_email_request_value}}}

        :return: The email of this BoletoEmailRequest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this BoletoEmailRequest.
        {{{boleto_email_request_value}}}

        :param email: The email of this BoletoEmailRequest.
        :type: str
        """
        self._email = email

    @property
    def id_template_notificacao(self):
        """
        Gets the id_template_notificacao of this BoletoEmailRequest.
        {{{boleto_email_request_id_template_notificacao_value}}}

        :return: The id_template_notificacao of this BoletoEmailRequest.
        :rtype: int
        """
        return self._id_template_notificacao

    @id_template_notificacao.setter
    def id_template_notificacao(self, id_template_notificacao):
        """
        Sets the id_template_notificacao of this BoletoEmailRequest.
        {{{boleto_email_request_id_template_notificacao_value}}}

        :param id_template_notificacao: The id_template_notificacao of this BoletoEmailRequest.
        :type: int
        """
        self._id_template_notificacao = id_template_notificacao

    @property
    def parametros(self):
        """
        Gets the parametros of this BoletoEmailRequest.
        {{{boleto_email_request_parametros_value}}}

        :return: The parametros of this BoletoEmailRequest.
        :rtype: object
        """
        return self._parametros

    @parametros.setter
    def parametros(self, parametros):
        """
        Sets the parametros of this BoletoEmailRequest.
        {{{boleto_email_request_parametros_value}}}

        :param parametros: The parametros of this BoletoEmailRequest.
        :type: object
        """
        self._parametros = parametros

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

