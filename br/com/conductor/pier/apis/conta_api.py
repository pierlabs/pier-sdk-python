# coding: utf-8

"""
ContaApi.py
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
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ContaApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def buscar_conta_using_get(self, **kwargs):
        """
        /contas/buscar
        Consulte contas filtrando pelos campos id do emissor, n\u00C3\u00BAmero do cart\u00C3\u00A3o, nome ou CPF/CNPJ 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.buscar_conta_using_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str nome: Nome
        :param str cpf: CPF (opcional caso nao informe o n\u00C3\u00BAmero do cart\u00C3\u00A3o ou id da conta)
        :param str numero_cartao: N\u00C3\u00BAmero do cart\u00C3\u00A3o (opcional caso n\u00C3\u00A3o informa o cpf ou id da conta)
        :param int id_conta: ID da Conta (opcional caso n\u00C3\u00A3o informe o n\u00C3\u00BAmero do cart\u00C3\u00A3o ou cpf)
        :return: ConsultarContaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['nome', 'cpf', 'numero_cartao', 'id_conta']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method buscar_conta_using_get" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/v1/contas/buscar'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'nome' in params:
            query_params['nome'] = params['nome']
        if 'cpf' in params:
            query_params['cpf'] = params['cpf']
        if 'numero_cartao' in params:
            query_params['numeroCartao'] = params['numero_cartao']
        if 'id_conta' in params:
            query_params['idConta'] = params['id_conta']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['access_token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ConsultarContaResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def consultar_conta_using_get(self, id_conta, **kwargs):
        """
        /contas/{idConta}
        Consulte informa\u00C3\u00A7\u00C3\u00B5es de uma determinada conta

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.consultar_conta_using_get(id_conta, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id_conta: ID da Conta (required)
        :return: ContaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_conta']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method consultar_conta_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id_conta' is set
        if ('id_conta' not in params) or (params['id_conta'] is None):
            raise ValueError("Missing the required parameter `id_conta` when calling `consultar_conta_using_get`")

        resource_path = '/api/v1/contas/{idConta}'.replace('{format}', 'json')
        path_params = {}
        if 'id_conta' in params:
            path_params['idConta'] = params['id_conta']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['access_token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ContaResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
