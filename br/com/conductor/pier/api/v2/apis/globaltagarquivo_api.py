# coding: utf-8

"""
GlobaltagarquivoApi.py
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


class GlobaltagarquivoApi(object):
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

    def consultar_using_get6(self, id, **kwargs):
        """
        {{{arquivo_resource_consultar}}}
        {{{arquivo_resource_consultar_notes}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.consultar_using_get6(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: {{{arquivo_resource_consultar_param_id}}} (required)
        :return: ArquivoDetalheResponse
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
                    " to method consultar_using_get6" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `consultar_using_get6`")

        resource_path = '/api/arquivos/{id}'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ArquivoDetalheResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def integrar_using_post(self, integrar_arquivo_request, **kwargs):
        """
        {{{arquivo_resource_integrar}}}
        {{{arquivo_resource_integrar_notes}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.integrar_using_post(integrar_arquivo_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param IntegrarArquivoRequest integrar_arquivo_request: integrarArquivoRequest (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integrar_arquivo_request']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method integrar_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integrar_arquivo_request' is set
        if ('integrar_arquivo_request' not in params) or (params['integrar_arquivo_request'] is None):
            raise ValueError("Missing the required parameter `integrar_arquivo_request` when calling `integrar_using_post`")

        resource_path = '/api/arquivos/integrar'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'integrar_arquivo_request' in params:
            body_params = params['integrar_arquivo_request']

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
                                            response_type='object',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_por_numero_receita_federal_using_get(self, numero_receita_federal, **kwargs):
        """
        {{{arquivo_a_u_d_resource_listar_por_numero_receita_federal}}}
        {{{arquivo_a_u_d_resource_listar_por_numero_receita_federal_notes}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_por_numero_receita_federal_using_get(numero_receita_federal, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str numero_receita_federal: {{{arquivo_a_u_d_resource_listar_por_numero_receita_federal_param_numero_receita_federal}}} (required)
        :param int page: P\u00E1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00E7\u00E3o (Default = 50, Max = 50)
        :return: PageArquivoAUDResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['numero_receita_federal', 'page', 'limit']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_por_numero_receita_federal_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'numero_receita_federal' is set
        if ('numero_receita_federal' not in params) or (params['numero_receita_federal'] is None):
            raise ValueError("Missing the required parameter `numero_receita_federal` when calling `listar_por_numero_receita_federal_using_get`")

        resource_path = '/api/arquivos-auditorias'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'numero_receita_federal' in params:
            query_params['numeroReceitaFederal'] = params['numero_receita_federal']
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
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PageArquivoAUDResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_status_arquivos_using_get(self, **kwargs):
        """
        {{{arquivo_resource_listar_status_arquivos}}}
        {{{arquivo_resource_listar_status_arquivos_notes}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_status_arquivos_using_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] sort: {{{global_menssagem_sort_sort}}}
        :param int page: {{{global_menssagem_sort_page_value}}}
        :param int limit: {{{global_menssagem_sort_limit}}}
        :param str nome: {{{status_arquivo_request_nome_value}}}
        :param str descricao: {{{status_arquivo_request_descricao_value}}}
        :return: PageStatusArquivoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort', 'page', 'limit', 'nome', 'descricao']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_status_arquivos_using_get" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/status-arquivos'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'sort' in params:
            query_params['sort'] = params['sort']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'nome' in params:
            query_params['nome'] = params['nome']
        if 'descricao' in params:
            query_params['descricao'] = params['descricao']

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
                                            response_type='PageStatusArquivoResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_tipos_arquivos_using_get(self, **kwargs):
        """
        {{{arquivo_resource_listar_tipos_arquivos}}}
        {{{arquivo_resource_listar_tipos_arquivos_notes}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_tipos_arquivos_using_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] sort: {{{global_menssagem_sort_sort}}}
        :param int page: {{{global_menssagem_sort_page_value}}}
        :param int limit: {{{global_menssagem_sort_limit}}}
        :param str nome: {{{tipo_arquivo_request_nome_value}}}
        :param str descricao: {{{tipo_arquivo_request_descricao_value}}}
        :return: PageTipoArquivoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort', 'page', 'limit', 'nome', 'descricao']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_tipos_arquivos_using_get" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/tipos-arquivos'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'sort' in params:
            query_params['sort'] = params['sort']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'nome' in params:
            query_params['nome'] = params['nome']
        if 'descricao' in params:
            query_params['descricao'] = params['descricao']

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
                                            response_type='PageTipoArquivoResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_using_get6(self, id, **kwargs):
        """
        {{{arquivo_a_u_d_resource_listar}}}
        {{{arquivo_a_u_d_resource_listar_notes}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_using_get6(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: {{{arquivo_a_u_d_resource_listar_param_id}}} (required)
        :param int page: P\u00E1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00E7\u00E3o (Default = 50, Max = 50)
        :return: PageArquivoAUDResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'page', 'limit']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_using_get6" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `listar_using_get6`")

        resource_path = '/api/arquivos/{id}/auditorias'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
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
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PageArquivoAUDResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_using_get7(self, **kwargs):
        """
        {{{arquivo_resource_listar}}}
        {{{arquivo_resource_listar_notes}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_using_get7(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] sort: {{{global_menssagem_sort_sort}}}
        :param int page: {{{global_menssagem_sort_page_value}}}
        :param int limit: {{{global_menssagem_sort_limit}}}
        :param str nome: {{{arquivo_request_nome_value}}}
        :param int id_tipo_arquivo: {{{arquivo_request_id_tipo_arquivo_value}}}
        :param int id_status_arquivo: {{{arquivo_request_id_status_arquivo_value}}}
        :param str extensao: {{{arquivo_request_extensao_value}}}
        :return: PageArquivoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort', 'page', 'limit', 'nome', 'id_tipo_arquivo', 'id_status_arquivo', 'extensao']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_using_get7" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/arquivos'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'sort' in params:
            query_params['sort'] = params['sort']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'nome' in params:
            query_params['nome'] = params['nome']
        if 'id_tipo_arquivo' in params:
            query_params['idTipoArquivo'] = params['id_tipo_arquivo']
        if 'id_status_arquivo' in params:
            query_params['idStatusArquivo'] = params['id_status_arquivo']
        if 'extensao' in params:
            query_params['extensao'] = params['extensao']

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
                                            response_type='PageArquivoResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def salvar_using_post1(self, arquivo_persist, **kwargs):
        """
        {{{arquivo_resource_salvar}}}
        {{{arquivo_resource_salvar_notes}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.salvar_using_post1(arquivo_persist, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ArquivoPersist arquivo_persist: arquivoPersist (required)
        :return: ArquivoDetalheResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['arquivo_persist']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method salvar_using_post1" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'arquivo_persist' is set
        if ('arquivo_persist' not in params) or (params['arquivo_persist'] is None):
            raise ValueError("Missing the required parameter `arquivo_persist` when calling `salvar_using_post1`")

        resource_path = '/api/arquivos'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'arquivo_persist' in params:
            body_params = params['arquivo_persist']

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
                                            response_type='ArquivoDetalheResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
