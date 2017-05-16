# coding: utf-8

"""
AutorizacoesApi.py
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


class AutorizacoesApi(object):
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

    def cancelar_using_post(self, cancelamento_request, **kwargs):
        """
        Cancela Transa\u00C3\u00A7\u00C3\u00A3o financeira
        Este m\u00C3\u00A9todo permite que seja cancelada uma transa\u00C3\u00A7\u00C3\u00A3o.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cancelar_using_post(cancelamento_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CancelamentoTransacaoOnUsRequest cancelamento_request: cancelamentoRequest (required)
        :return: TransacaoOnUsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cancelamento_request']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancelar_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'cancelamento_request' is set
        if ('cancelamento_request' not in params) or (params['cancelamento_request'] is None):
            raise ValueError("Missing the required parameter `cancelamento_request` when calling `cancelar_using_post`")

        resource_path = '/api/cancelar-transacao'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'cancelamento_request' in params:
            body_params = params['cancelamento_request']

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
                                            response_type='TransacaoOnUsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def desfazer_using_post(self, autorizacao_on_us_request, **kwargs):
        """
        Autoriza transa\u00C3\u00A7\u00C3\u00A3o financeira
        Este m\u00C3\u00A9todo faz uma autoriza\u00C3\u00A7\u00C3\u00A3o de transa\u00C3\u00A7\u00C3\u00A3o financeira.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.desfazer_using_post(autorizacao_on_us_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AutorizacaoOnUsRequest autorizacao_on_us_request: autorizacaoOnUsRequest (required)
        :return: TransacaoOnUsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['autorizacao_on_us_request']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method desfazer_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'autorizacao_on_us_request' is set
        if ('autorizacao_on_us_request' not in params) or (params['autorizacao_on_us_request'] is None):
            raise ValueError("Missing the required parameter `autorizacao_on_us_request` when calling `desfazer_using_post`")

        resource_path = '/api/autorizar-transacao'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'autorizacao_on_us_request' in params:
            body_params = params['autorizacao_on_us_request']

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
                                            response_type='TransacaoOnUsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def desfazer_using_post1(self, desfazimento_request, **kwargs):
        """
        Desfazimento de Transa\u00C3\u00A7\u00C3\u00A3o
        Este m\u00C3\u00A9todo permite que seja desfeita uma transa\u00C3\u00A7\u00C3\u00A3o.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.desfazer_using_post1(desfazimento_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DesfazimentoTransacaoOnURequest desfazimento_request: desfazimentoRequest (required)
        :return: TransacaoOnUsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['desfazimento_request']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method desfazer_using_post1" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'desfazimento_request' is set
        if ('desfazimento_request' not in params) or (params['desfazimento_request'] is None):
            raise ValueError("Missing the required parameter `desfazimento_request` when calling `desfazer_using_post1`")

        resource_path = '/api/desfazer-transacao'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'desfazimento_request' in params:
            body_params = params['desfazimento_request']

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
                                            response_type='TransacaoOnUsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def simular_using_post(self, transacoes_request, **kwargs):
        """
        Simula Compra Parcelada
        Este m\u00C3\u00A9todo permite que seja simulada uma compra parcelada.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.simular_using_post(transacoes_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param TransacaoOnUsRequest transacoes_request: transacoesRequest (required)
        :return: TransacaoOnUsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['transacoes_request']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method simular_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'transacoes_request' is set
        if ('transacoes_request' not in params) or (params['transacoes_request'] is None):
            raise ValueError("Missing the required parameter `transacoes_request` when calling `simular_using_post`")

        resource_path = '/api/simular-transacao'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'transacoes_request' in params:
            body_params = params['transacoes_request']

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
                                            response_type='TransacaoOnUsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
