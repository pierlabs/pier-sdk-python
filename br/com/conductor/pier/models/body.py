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


class Body(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Body - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'auth_token': 'AuthToken',
            'action': 'str',
            'user': 'str'
        }

        self.attribute_map = {
            'auth_token': 'AuthToken',
            'action': 'action',
            'user': 'user'
        }

        self._auth_token = None
        self._action = None
        self._user = None

    @property
    def auth_token(self):
        """
        Gets the auth_token of this Body.


        :return: The auth_token of this Body.
        :rtype: AuthToken
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        """
        Sets the auth_token of this Body.


        :param auth_token: The auth_token of this Body.
        :type: AuthToken
        """
        self._auth_token = auth_token

    @property
    def action(self):
        """
        Gets the action of this Body.


        :return: The action of this Body.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this Body.


        :param action: The action of this Body.
        :type: str
        """
        allowed_values = ["CREATED", "UPDATED", "DELETED"]
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action`, must be one of {0}"
                .format(allowed_values)
            )
        self._action = action

    @property
    def user(self):
        """
        Gets the user of this Body.


        :return: The user of this Body.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this Body.


        :param user: The user of this Body.
        :type: str
        """
        self._user = user

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

