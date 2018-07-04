# coding: utf-8

"""
GlobaltaginscricaoapnApi.py
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


class GlobaltaginscricaoapnApi(object):
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

    def desativar_using_put(self, id, **kwargs):
        """
        {{{inscricao_apn_recurso_desativar}}}
        {{{inscricao_apn_recurso_desativar_notas}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.desativar_using_put(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id (required)
        :return: InscricaoAPNResponse
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
                    " to method desativar_using_put" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `desativar_using_put`")

        resource_path = '/api/inscricoes-apn/{id}/desativar'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InscricaoAPNResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_using_get30(self, **kwargs):
        """
        {{{inscricao_apn_recurso_listar}}}
        {{{inscricao_apn_recurso_listar_notas}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_using_get30(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] sort: {{{global_menssagem_sort_sort}}}
        :param list[int] id_cartoes: {{{inscricao_apn_requisicao_id_cartoes_descricao}}}
        :param int page: {{{global_menssagem_sort_page_value}}}
        :param int limit: {{{global_menssagem_sort_limit}}}
        :param str device_token: {{{inscricao_apn_requisicao_device_token_descricao}}}
        :param str data_criacao: {{{inscricao_apn_requisicao_data_criacao_descricao}}}
        :param str data_desativacao: {{{inscricao_apn_requisicao_data_desativacao_descricao}}}
        :param bool ativo: {{{inscricao_apn_requisicao_ativo_descricao}}}
        :param int id_aplicacao_mobile: {{{inscricao_apn_requisicao_id_aplicacao_mobile_descricao}}}
        :return: PageInscricaoAPNResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort', 'id_cartoes', 'page', 'limit', 'device_token', 'data_criacao', 'data_desativacao', 'ativo', 'id_aplicacao_mobile']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_using_get30" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/inscricoes-apn'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'sort' in params:
            query_params['sort'] = params['sort']
        if 'id_cartoes' in params:
            query_params['idCartoes'] = params['id_cartoes']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'device_token' in params:
            query_params['deviceToken'] = params['device_token']
        if 'data_criacao' in params:
            query_params['dataCriacao'] = params['data_criacao']
        if 'data_desativacao' in params:
            query_params['dataDesativacao'] = params['data_desativacao']
        if 'ativo' in params:
            query_params['ativo'] = params['ativo']
        if 'id_aplicacao_mobile' in params:
            query_params['idAplicacaoMobile'] = params['id_aplicacao_mobile']

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
                                            response_type='PageInscricaoAPNResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def salvar_using_post14(self, inscricao_persist, **kwargs):
        """
        {{{inscricao_apn_recurso_salvar}}}
        {{{inscricao_apn_recurso_salvar_notas}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.salvar_using_post14(inscricao_persist, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param InscricaoApnPersistencia inscricao_persist: inscricaoPersist (required)
        :return: list[InscricaoAPNResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['inscricao_persist']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method salvar_using_post14" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'inscricao_persist' is set
        if ('inscricao_persist' not in params) or (params['inscricao_persist'] is None):
            raise ValueError("Missing the required parameter `inscricao_persist` when calling `salvar_using_post14`")

        resource_path = '/api/inscricoes-apn'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'inscricao_persist' in params:
            body_params = params['inscricao_persist']

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
                                            response_type='list[InscricaoAPNResponse]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
