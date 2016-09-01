# coding: utf-8

"""
ProdutoApi.py
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


class ProdutoApi(object):
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

    def consultar_produto_using_get(self, id_produto, **kwargs):
        """
        Opera\u00C3\u00A7\u00C3\u00A3o utilizada para consultar uma determinada Origem Comercial 
        Este m\u00C3\u00A9todo permite que sejam listados os registros de uma determinada Origem Comercial existente na base do emissor. Para isso, \u00C3\u00A9 preciso informar o seu respectivo c\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o (id). 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.consultar_produto_using_get(id_produto, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id_produto: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Produto (id) (required)
        :return: OrigemComercial
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_produto']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method consultar_produto_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id_produto' is set
        if ('id_produto' not in params) or (params['id_produto'] is None):
            raise ValueError("Missing the required parameter `id_produto` when calling `consultar_produto_using_get`")

        resource_path = '/api/produtos/{id_origem_comercial}'.replace('{format}', 'json')
        path_params = {}
        if 'id_produto' in params:
            path_params['id_produto'] = params['id_produto']

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
                                            response_type='OrigemComercial',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_produtos_using_get(self, **kwargs):
        """
        Lista os Produtos do Emissor
        Este m\u00C3\u00A9todo permite que sejam listados os Produtos existentes na base de dados do Emissor. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_produtos_using_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id_produto: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Produto (id)
        :param str nome: Descri\u00C3\u00A7\u00C3\u00A3o do Nome do Produto
        :param str status: Status do Produto, onde: (\"0\": Inativo), (\"1\": Ativo).
        :param int page: P\u00C3\u00A1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00C3\u00A7\u00C3\u00A3o (Default = 100, Max = 100)
        :return: ListaProdutos
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_produto', 'nome', 'status', 'page', 'limit']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_produtos_using_get" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/produtos'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'id_produto' in params:
            query_params['id_produto'] = params['id_produto']
        if 'nome' in params:
            query_params['nome'] = params['nome']
        if 'status' in params:
            query_params['status'] = params['status']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']

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
                                            response_type='ListaProdutos',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response