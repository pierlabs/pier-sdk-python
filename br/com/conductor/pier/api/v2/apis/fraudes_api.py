# coding: utf-8

"""
FraudesApi.py
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


class FraudesApi(object):
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

    def consultar_using_get(self, id, **kwargs):
        """
        Apresenta os dados de um determinado Atendimento
        Este m\u00C3\u00A9todo permite consultar os par\u00C3\u00A2metros de um determinado Atendimento a partir do seu c\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o (idAtendimento).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.consultar_using_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do atendimento cliente (id). (required)
        :return: AtendimentoCliente
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
                    " to method consultar_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `consultar_using_get`")

        resource_path = '/api/atendimento-clientes/{id}'.replace('{format}', 'json')
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
        auth_settings = ['access_token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AtendimentoCliente',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_using_get(self, **kwargs):
        """
        Lista todos os atendimentos
        Este m\u00C3\u00A9todo permite que sejam listados todos os Registro de Atendimento, independente do Tipo.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_using_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page: P\u00C3\u00A1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00C3\u00A7\u00C3\u00A3o (Default = 100, Max = 100)
        :param int id_atendimento: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Atendimento (id)
        :param int id_tipo_atendimento: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Tipo de Atendimento (id)
        :param int id_conta: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o de conta (id).
        :param str nome_atendente: Apresenta o nome do Atendente que registrou o Atendimento.
        :param datetime data_atendimento: Apresenta a data em que o Atendimento foi realizado.
        :return: PageAtendimentoClientes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit', 'id_atendimento', 'id_tipo_atendimento', 'id_conta', 'nome_atendente', 'data_atendimento']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_using_get" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/atendimento-clientes'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'id_atendimento' in params:
            query_params['idAtendimento'] = params['id_atendimento']
        if 'id_tipo_atendimento' in params:
            query_params['idTipoAtendimento'] = params['id_tipo_atendimento']
        if 'id_conta' in params:
            query_params['idConta'] = params['id_conta']
        if 'nome_atendente' in params:
            query_params['nomeAtendente'] = params['nome_atendente']
        if 'data_atendimento' in params:
            query_params['dataAtendimento'] = params['data_atendimento']

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
                                            response_type='PageAtendimentoClientes',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def salvar_using_post(self, **kwargs):
        """
        Cadastro um novo Atendimento do tipo Gen\u00C3\u00A9rico para uma Conta
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.salvar_using_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id_conta: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Conta a qual o Atendimento est\u00C3\u00A1 associado
        :param str conteudo_atendimento: Apresenta as informa\u00C3\u00A7\u00C3\u00B5es que foram utilizadas para consultar, cadastrar ou alterar informa\u00C3\u00A7\u00C3\u00B5es relacionadas ao Atendimento.
        :param str detalhes_atendimento: Apresenta os detalhes lan\u00C3\u00A7ados pelo sistema ou pelo Atendente durante relacionados ao Atendimento.
        :param str nome_atendente: Apresenta o nome do Atendente que registrou o Atendimento.
        :param datetime data_atendimento: Apresenta a data em que o Atendimento foi realizado.
        :param datetime data_agendamento: Quando utilizado, de acordo com o Tipo de Atendimento, apresenta a data para processamento ou a data para retorno do Atendimento.
        :param datetime data_hora_inicio_atendimento: Apresenta a data e hora em que o Atendimento foi iniciado. Quando utilizado, serve para medir a performance dos Atendimentos.
        :param datetime data_hora_fim_atendimento: Apresenta a data e hora em que o Atendimento foi iniciado. Quando utilizado, serve para medir a performance dos Atendimentos.
        :return: AtendimentoCliente
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_conta', 'conteudo_atendimento', 'detalhes_atendimento', 'nome_atendente', 'data_atendimento', 'data_agendamento', 'data_hora_inicio_atendimento', 'data_hora_fim_atendimento']
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


        resource_path = '/api/atendimento-clientes'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'id_conta' in params:
            query_params['idConta'] = params['id_conta']
        if 'conteudo_atendimento' in params:
            query_params['conteudoAtendimento'] = params['conteudo_atendimento']
        if 'detalhes_atendimento' in params:
            query_params['detalhesAtendimento'] = params['detalhes_atendimento']
        if 'nome_atendente' in params:
            query_params['nomeAtendente'] = params['nome_atendente']
        if 'data_atendimento' in params:
            query_params['dataAtendimento'] = params['data_atendimento']
        if 'data_agendamento' in params:
            query_params['dataAgendamento'] = params['data_agendamento']
        if 'data_hora_inicio_atendimento' in params:
            query_params['dataHoraInicioAtendimento'] = params['data_hora_inicio_atendimento']
        if 'data_hora_fim_atendimento' in params:
            query_params['dataHoraFimAtendimento'] = params['data_hora_fim_atendimento']

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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AtendimentoCliente',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
