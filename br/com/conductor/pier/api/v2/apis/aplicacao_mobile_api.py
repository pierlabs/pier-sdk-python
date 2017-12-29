# coding: utf-8

"""
AplicacaoMobileApi.py
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


class AplicacaoMobileApi(object):
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

    def atualizar_using_put(self, id, update, **kwargs):
        """
        Atualiza Aplicacao Mobile
        Esse recurso permite atualizar aplicacao mobile.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.atualizar_using_put(id, update, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Aplicacao (id). (required)
        :param AplicacaoMobileUpdate update: update (required)
        :return: AplicacaoMobileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'update']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method atualizar_using_put" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `atualizar_using_put`")
        # verify the required parameter 'update' is set
        if ('update' not in params) or (params['update'] is None):
            raise ValueError("Missing the required parameter `update` when calling `atualizar_using_put`")

        resource_path = '/api/aplicacoes-mobile/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update' in params:
            body_params = params['update']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AplicacaoMobileResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_using_get2(self, **kwargs):
        """
        Lista os aplicacoes mobile cadastradas
        Este m\u00C3\u00A9todo permite que sejam listadas as aplicacoes mobile existentes na base do PIER.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_using_get2(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] sort: Tipo de ordena\u00C3\u00A7\u00C3\u00A3o dos registros.
        :param int page: P\u00C3\u00A1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00C3\u00A7\u00C3\u00A3o (Default = 50, Max = 50)
        :param str id: Identificador da Aplicacao Mobile
        :param int id_plataforma_mobile: Identificador da Plataforma Mobile
        :return: PageAplicacaoMobileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort', 'page', 'limit', 'id', 'id_plataforma_mobile']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_using_get2" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/aplicacoes-mobile'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'sort' in params:
            query_params['sort'] = params['sort']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'id' in params:
            query_params['id'] = params['id']
        if 'id_plataforma_mobile' in params:
            query_params['idPlataformaMobile'] = params['id_plataforma_mobile']

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
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PageAplicacaoMobileResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def salvar_using_post(self, persist, **kwargs):
        """
        Cadastra Aplicacao Mobile
        Esse recurso permite cadastrar aplicacoes mobile.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.salvar_using_post(persist, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AplicacaoMobilePersist persist: persist (required)
        :return: AplicacaoMobileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['persist']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method salvar_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'persist' is set
        if ('persist' not in params) or (params['persist'] is None):
            raise ValueError("Missing the required parameter `persist` when calling `salvar_using_post`")

        resource_path = '/api/aplicacoes-mobile'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'persist' in params:
            body_params = params['persist']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AplicacaoMobileResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
