# coding: utf-8

"""
PortadorApi.py
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


class PortadorApi(object):
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

    def listar_using_get4(self, **kwargs):
        """
        Lista os Portadores existentes
        Este m\u00C3\u00A9todo permite que sejam listados os portadores cadastrados na base do emissor.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_using_get4(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id_conta: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Conta (id).
        :param int id_produto: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Produto (id).
        :param int id_pessoa: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Pessoa (id).
        :param int id_parentesco: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Parentesco (id)
        :param str tipo_portador: Apresenta o tipo do Portador do cart\u00C3\u00A3o, sendo: ('T': Titular, 'A': Adicional).
        :param str nome_impresso: Apresenta o nome a ser impresso no cart\u00C3\u00A3o.
        :param int id_imagem: Apresenta o c\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da imagem do cart\u00C3\u00A3o.
        :param int id_tipo_cartao: Apresenta o c\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do tipo do cart\u00C3\u00A3o (id), que ser\u00C3\u00A1 utilizado para gerar os cart\u00C3\u00B5es deste portador, vinculados a sua respectiva conta atrav\u00C3\u00A9s do campo idConta.
        :param int flag_ativo: Quanto ativa, indica que o cadastro do Portador est\u00C3\u00A1 ativo, em emissores que realizam este tipo de gest\u00C3\u00A3o.
        :param date data_cadastro_portador: Apresenta a data em que o Portador fora cadastrado, quando possuir esta informa\u00C3\u00A7\u00C3\u00A3o.
        :param date data_cancelamento_portador: Apresenta a data em que o Portador fora cancelado, quando possuir esta informa\u00C3\u00A7\u00C3\u00A3o.
        :param int page: P\u00C3\u00A1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00C3\u00A7\u00C3\u00A3o (Default = 100, Max = 100)
        :return: PagePortador
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_conta', 'id_produto', 'id_pessoa', 'id_parentesco', 'tipo_portador', 'nome_impresso', 'id_imagem', 'id_tipo_cartao', 'flag_ativo', 'data_cadastro_portador', 'data_cancelamento_portador', 'page', 'limit']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_using_get4" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/portadores'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'id_conta' in params:
            query_params['idConta'] = params['id_conta']
        if 'id_produto' in params:
            query_params['idProduto'] = params['id_produto']
        if 'id_pessoa' in params:
            query_params['idPessoa'] = params['id_pessoa']
        if 'id_parentesco' in params:
            query_params['idParentesco'] = params['id_parentesco']
        if 'tipo_portador' in params:
            query_params['tipoPortador'] = params['tipo_portador']
        if 'nome_impresso' in params:
            query_params['nomeImpresso'] = params['nome_impresso']
        if 'id_imagem' in params:
            query_params['idImagem'] = params['id_imagem']
        if 'id_tipo_cartao' in params:
            query_params['idTipoCartao'] = params['id_tipo_cartao']
        if 'flag_ativo' in params:
            query_params['flagAtivo'] = params['flag_ativo']
        if 'data_cadastro_portador' in params:
            query_params['dataCadastroPortador'] = params['data_cadastro_portador']
        if 'data_cancelamento_portador' in params:
            query_params['dataCancelamentoPortador'] = params['data_cancelamento_portador']
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
                                            response_type='PagePortador',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
