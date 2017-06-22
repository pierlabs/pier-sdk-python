# coding: utf-8

"""
DispositivosApi.py
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


class DispositivosApi(object):
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

    def ativar_using_post(self, id, **kwargs):
        """
        Ativa Dispositivo
        Esse recurso permite ativar dispositivo.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.ativar_using_post(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Plataforma (id). (required)
        :return: DispositivoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ativar_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `ativar_using_post`")

        resource_path = '/api/dispositivos/{id}/ativar-dispositivo'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DispositivoResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def desativar_using_post(self, id, **kwargs):
        """
        Desativa Dispositivo
        Esse recurso permite desativar dispositivo.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.desativar_using_post(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Plataforma (id). (required)
        :return: DispositivoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method desativar_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `desativar_using_post`")

        resource_path = '/api/dispositivos/{id}/desativar-dispositivo'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DispositivoResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_using_get8(self, **kwargs):
        """
        Lista os dispositivos cadastrados
        Este m\u00C3\u00A9todo permite que sejam listados os dispositivos existentes na base do PIER.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_using_get8(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page: P\u00C3\u00A1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00C3\u00A7\u00C3\u00A3o (Default = 50, Max = 50)
        :param str token: Token do Dispositivo
        :param int id_usuario: Identificador do Usu\u00C3\u00A1rio
        :param int id_aplicacao_mobile: Identificador da aplica\u00C3\u00A7\u00C3\u00A3o
        :param str data_criacao: Apresenta a data e em que o registro foi criado.
        :param str data_desativacao: Apresenta a data e em que o registro foi desativado.
        :return: PageDispositivoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit', 'token', 'id_usuario', 'id_aplicacao_mobile', 'data_criacao', 'data_desativacao']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_using_get8" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/dispositivos'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'token' in params:
            query_params['token'] = params['token']
        if 'id_usuario' in params:
            query_params['idUsuario'] = params['id_usuario']
        if 'id_aplicacao_mobile' in params:
            query_params['idAplicacaoMobile'] = params['id_aplicacao_mobile']
        if 'data_criacao' in params:
            query_params['dataCriacao'] = params['data_criacao']
        if 'data_desativacao' in params:
            query_params['dataDesativacao'] = params['data_desativacao']

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
                                            response_type='PageDispositivoResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def salvar_using_post3(self, persist, **kwargs):
        """
        Cadastra Dispositivo
        Esse recurso permite cadastrar dispositivos.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.salvar_using_post3(persist, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DispositivoPersist persist: persist (required)
        :return: DispositivoResponse
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
                    " to method salvar_using_post3" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'persist' is set
        if ('persist' not in params) or (params['persist'] is None):
            raise ValueError("Missing the required parameter `persist` when calling `salvar_using_post3`")

        resource_path = '/api/dispositivos'.replace('{format}', 'json')
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
                                            response_type='DispositivoResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
