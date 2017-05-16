# coding: utf-8

"""
FAQApi.py
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


class FAQApi(object):
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

    def adicionar_using_post(self, pergunta, resposta, **kwargs):
        """
        Adiciona uma nova FAQ
        Adiciona uma nova FAQ

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.adicionar_using_post(pergunta, resposta, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str pergunta: Conte\u00C3\u00BAdo da pergunta. (required)
        :param str resposta: Conte\u00C3\u00BAdo da resposta. (required)
        :param int relevancia: N\u00C3\u00ADvel de relev\u00C3\u00A2ncia da pergunta.
        :param str plataforma: Plataforma em que a FAQ se encaixa.
        :param str categoria: Categoria de assunto do qual a FAQ se trata.
        :param str status: Status descrevendo a situa\u00C3\u00A7\u00C3\u00A3o atual da FAQ.
        :return: FAQ
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pergunta', 'resposta', 'relevancia', 'plataforma', 'categoria', 'status']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method adicionar_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'pergunta' is set
        if ('pergunta' not in params) or (params['pergunta'] is None):
            raise ValueError("Missing the required parameter `pergunta` when calling `adicionar_using_post`")
        # verify the required parameter 'resposta' is set
        if ('resposta' not in params) or (params['resposta'] is None):
            raise ValueError("Missing the required parameter `resposta` when calling `adicionar_using_post`")

        resource_path = '/api/faqs'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'pergunta' in params:
            query_params['pergunta'] = params['pergunta']
        if 'resposta' in params:
            query_params['resposta'] = params['resposta']
        if 'relevancia' in params:
            query_params['relevancia'] = params['relevancia']
        if 'plataforma' in params:
            query_params['plataforma'] = params['plataforma']
        if 'categoria' in params:
            query_params['categoria'] = params['categoria']
        if 'status' in params:
            query_params['status'] = params['status']

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
                                            response_type='FAQ',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def alterar_using_put2(self, id, pergunta, resposta, **kwargs):
        """
        Alterar FAQ
        Alterar FAQ

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.alterar_using_put2(id, pergunta, resposta, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Id (required)
        :param str pergunta: Conte\u00C3\u00BAdo da pergunta. (required)
        :param str resposta: Conte\u00C3\u00BAdo da resposta. (required)
        :param int relevancia: N\u00C3\u00ADvel de relev\u00C3\u00A2ncia da pergunta.
        :param str plataforma: Plataforma em que a FAQ se encaixa.
        :param str categoria: Categoria de assunto do qual a FAQ se trata.
        :param str status: Status descrevendo a situa\u00C3\u00A7\u00C3\u00A3o atual da FAQ.
        :return: FAQ
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'pergunta', 'resposta', 'relevancia', 'plataforma', 'categoria', 'status']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method alterar_using_put2" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `alterar_using_put2`")
        # verify the required parameter 'pergunta' is set
        if ('pergunta' not in params) or (params['pergunta'] is None):
            raise ValueError("Missing the required parameter `pergunta` when calling `alterar_using_put2`")
        # verify the required parameter 'resposta' is set
        if ('resposta' not in params) or (params['resposta'] is None):
            raise ValueError("Missing the required parameter `resposta` when calling `alterar_using_put2`")

        resource_path = '/api/faqs/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'pergunta' in params:
            query_params['pergunta'] = params['pergunta']
        if 'resposta' in params:
            query_params['resposta'] = params['resposta']
        if 'relevancia' in params:
            query_params['relevancia'] = params['relevancia']
        if 'plataforma' in params:
            query_params['plataforma'] = params['plataforma']
        if 'categoria' in params:
            query_params['categoria'] = params['categoria']
        if 'status' in params:
            query_params['status'] = params['status']

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

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='FAQ',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def consultar_using_get6(self, id, **kwargs):
        """
        Consultar FAQ por id
        Consulta os detalhes de uma determinada FAQ

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.consultar_using_get6(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Id (required)
        :return: FAQ
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

        resource_path = '/api/faqs/{id}'.replace('{format}', 'json')
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
                                            response_type='FAQ',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_using_get8(self, **kwargs):
        """
        Lista FAQs
        Lista todas as FAQs

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
        :param int limit: Limite de elementos por solicita\u00C3\u00A7\u00C3\u00A3o (Default = 100, Max = 100)
        :param int id_faq: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da FAQ (id).
        :param str pergunta: Conte\u00C3\u00BAdo da pergunta.
        :param str resposta: Conte\u00C3\u00BAdo da resposta.
        :param int relevancia: N\u00C3\u00ADvel de relev\u00C3\u00A2ncia da pergunta.
        :param str plataforma: Plataforma em que a FAQ se encaixa.
        :param str categoria: Categoria de assunto do qual a FAQ se trata.
        :param str status: Status descrevendo a situa\u00C3\u00A7\u00C3\u00A3o atual da FAQ.
        :return: PageFaqs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit', 'id_faq', 'pergunta', 'resposta', 'relevancia', 'plataforma', 'categoria', 'status']
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


        resource_path = '/api/faqs'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'id_faq' in params:
            query_params['idFaq'] = params['id_faq']
        if 'pergunta' in params:
            query_params['pergunta'] = params['pergunta']
        if 'resposta' in params:
            query_params['resposta'] = params['resposta']
        if 'relevancia' in params:
            query_params['relevancia'] = params['relevancia']
        if 'plataforma' in params:
            query_params['plataforma'] = params['plataforma']
        if 'categoria' in params:
            query_params['categoria'] = params['categoria']
        if 'status' in params:
            query_params['status'] = params['status']

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
                                            response_type='PageFaqs',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
