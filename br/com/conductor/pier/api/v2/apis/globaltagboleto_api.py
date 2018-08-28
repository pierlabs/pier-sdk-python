# coding: utf-8

"""
GlobaltagboletoApi.py
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


class GlobaltagboletoApi(object):
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

    def consultar_using_get36(self, id, **kwargs):
        """
        {{{boleto_resource_consultar}}}
        {{{boleto_resource_consultar_notes}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.consultar_using_get36(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: {{{boleto_resource_consultar_param_id}}} (required)
        :param bool zera_valor_codigo_barras: {{{boleto_resource_consultar_param_zera_valor_codigo_barras}}}
        :return: BoletoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'zera_valor_codigo_barras']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method consultar_using_get36" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `consultar_using_get36`")

        resource_path = '/api/boletos/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'zera_valor_codigo_barras' in params:
            query_params['zeraValorCodigoBarras'] = params['zera_valor_codigo_barras']

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
                                            response_type='BoletoResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def enviar_boleto_email_using_post(self, id, request, **kwargs):
        """
        {{{boleto_resource_enviar_boleto_email}}}
        {{{boleto_resource_enviar_boleto_email_notes}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.enviar_boleto_email_using_post(id, request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: {{{boleto_resource_enviar_boleto_param_id}}} (required)
        :param BoletoEmailRequest request: request (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'request']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enviar_boleto_email_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `enviar_boleto_email_using_post`")
        # verify the required parameter 'request' is set
        if ('request' not in params) or (params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `enviar_boleto_email_using_post`")

        resource_path = '/api/boletos/{id}/enviar-email'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']

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

    def gerar_boleto_using_post(self, boleto_request, **kwargs):
        """
        {{{boleto_resource_gerar_boleto}}}
        {{{boleto_resource_gerar_boleto_notes}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.gerar_boleto_using_post(boleto_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BoletoRequest boleto_request: boletoRequest (required)
        :return: BoletoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['boleto_request']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method gerar_boleto_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'boleto_request' is set
        if ('boleto_request' not in params) or (params['boleto_request'] is None):
            raise ValueError("Missing the required parameter `boleto_request` when calling `gerar_boleto_using_post`")

        resource_path = '/api/boletos'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'boleto_request' in params:
            body_params = params['boleto_request']

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
                                            response_type='BoletoResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_using_get47(self, **kwargs):
        """
        {{{boleto_resource_listar}}}
        {{{boleto_resource_listar_notes}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_using_get47(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] sort: {{{global_menssagem_sort_sort}}}
        :param int page: {{{global_menssagem_sort_page_value}}}
        :param int limit: {{{global_menssagem_sort_limit}}}
        :param int id_conta: {{{boleto_listar_request_id_conta_value}}}
        :param str data_vencimento: {{{boleto_listar_request_data_vencimento_value}}}
        :param float valor_boleto: {{{boleto_listar_request_valor_value}}}
        :param int id_tipo_boleto: {{{boleto_listar_request_id_tipo_boleto_value}}}
        :return: PageBoletoListarResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort', 'page', 'limit', 'id_conta', 'data_vencimento', 'valor_boleto', 'id_tipo_boleto']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_using_get47" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/boletos'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'sort' in params:
            query_params['sort'] = params['sort']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'id_conta' in params:
            query_params['idConta'] = params['id_conta']
        if 'data_vencimento' in params:
            query_params['dataVencimento'] = params['data_vencimento']
        if 'valor_boleto' in params:
            query_params['valorBoleto'] = params['valor_boleto']
        if 'id_tipo_boleto' in params:
            query_params['idTipoBoleto'] = params['id_tipo_boleto']

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
                                            response_type='PageBoletoListarResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def registrar_boleto_using_post(self, id, **kwargs):
        """
        {{{registro_cobranca_resource_registrar_boleto}}}
        {{{registro_cobranca_resource_registrar_boleto_notes}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.registrar_boleto_using_post(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: {{{registro_cobranca_resource_registrar_boleto_param_id_boleto}}} (required)
        :return: BoletoResponse
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
                    " to method registrar_boleto_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `registrar_boleto_using_post`")

        resource_path = '/api/boletos/{id}/registrar'.replace('{format}', 'json')
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
                                            response_type='BoletoResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def visualizar_boleto_using_get(self, id, **kwargs):
        """
        {{{boleto_resource_visualizar_boleto}}}
        {{{boleto_resource_visualizar_boleto_notes}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.visualizar_boleto_using_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: {{{boleto_resource_visualizar_boleto_param_id}}} (required)
        :return: object
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
                    " to method visualizar_boleto_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `visualizar_boleto_using_get`")

        resource_path = '/api/boletos/{id}/arquivo.pdf'.replace('{format}', 'json')
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
            select_header_accept(['application/pdf'])
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
                                            response_type='object',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
