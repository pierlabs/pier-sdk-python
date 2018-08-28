# coding: utf-8

"""
GlobaltaglogApi.py
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


class GlobaltaglogApi(object):
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

    def salvar_using_post19(self, log_acesso_usuario_persist, **kwargs):
        """
        {{{log_acesso_usuario_recurso_salvar}}}
        {{{log_acesso_usuario_recurso_salvar_notas}}}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.salvar_using_post19(log_acesso_usuario_persist, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param LogAcessoUsuarioPersistencia log_acesso_usuario_persist: logAcessoUsuarioPersist (required)
        :return: LogAcessoUsuarioResposta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['log_acesso_usuario_persist']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method salvar_using_post19" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'log_acesso_usuario_persist' is set
        if ('log_acesso_usuario_persist' not in params) or (params['log_acesso_usuario_persist'] is None):
            raise ValueError("Missing the required parameter `log_acesso_usuario_persist` when calling `salvar_using_post19`")

        resource_path = '/api/logs/log-acessos-usuario'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'log_acesso_usuario_persist' in params:
            body_params = params['log_acesso_usuario_persist']

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
                                            response_type='LogAcessoUsuarioResposta',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
