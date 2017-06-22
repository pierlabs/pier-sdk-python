# coding: utf-8

"""
NotificacoesApi.py
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


class NotificacoesApi(object):
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

    def atualizar_sms_using_post(self, **kwargs):
        """
        Atualizar SMS
        Esse recurso permite atualizar o status do SMS do emissor

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.atualizar_sms_using_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str nsu: Seu n\u00C3\u00BAmero
        :param str status: Status
        :param str data: Data
        :param str texto_status: TextoStatus
        :param str operadora: Operadora
        :return: NotificacaoSMSResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['nsu', 'status', 'data', 'texto_status', 'operadora']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method atualizar_sms_using_post" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/notificacoes/sms/atualizar-status'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'nsu' in params:
            query_params['nsu'] = params['nsu']
        if 'status' in params:
            query_params['status'] = params['status']
        if 'data' in params:
            query_params['data'] = params['data']
        if 'texto_status' in params:
            query_params['texto_status'] = params['texto_status']
        if 'operadora' in params:
            query_params['operadora'] = params['operadora']

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
                                            response_type='NotificacaoSMSResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_push_using_get(self, **kwargs):
        """
        Listar Push
        Esse recurso permite listar os Pushes do emissor

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_push_using_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page: P\u00C3\u00A1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00C3\u00A7\u00C3\u00A3o (Default = 50, Max = 50)
        :param str data_envio: Apresenta a data e em que o registro foi enviado para o dispositivo.
        :param str tipo_evento: Nome do tipoEvento da notifica\u00C3\u00A7\u00C3\u00A3o
        :param str status: Status de envio da notifica\u00C3\u00A7\u00C3\u00A3o
        :param str plataforma: Plataforma de Push notifications.
        :param str protocolo: N\u00C3\u00BAmero do protocolo de envio de notifica\u00C3\u00A7\u00C3\u00B5es
        :return: PagePushResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit', 'data_envio', 'tipo_evento', 'status', 'plataforma', 'protocolo']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_push_using_get" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/notificacoes/push'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'data_envio' in params:
            query_params['dataEnvio'] = params['data_envio']
        if 'tipo_evento' in params:
            query_params['tipoEvento'] = params['tipo_evento']
        if 'status' in params:
            query_params['status'] = params['status']
        if 'plataforma' in params:
            query_params['plataforma'] = params['plataforma']
        if 'protocolo' in params:
            query_params['protocolo'] = params['protocolo']

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
                                            response_type='PagePushResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_sms_using_get(self, **kwargs):
        """
        Listar SMS
        Esse recurso permite listar os SMS do emissor

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_sms_using_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page: P\u00C3\u00A1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00C3\u00A7\u00C3\u00A3o (Default = 50, Max = 50)
        :param str data_inclusao: Apresenta a data e em que o registro foi inclu\u00C3\u00ADdo na base para ser enviado
        :param str tipo_evento: Nome do tipoEvento da notifica\u00C3\u00A7\u00C3\u00A3o
        :param str status: Status de envio da notifica\u00C3\u00A7\u00C3\u00A3o
        :param str operadora: Nome da operadora a qual a notifica\u00C3\u00A7\u00C3\u00A3o foi enviada.
        :param str protocolo: N\u00C3\u00BAmero do protocolo de envio de notifica\u00C3\u00A7\u00C3\u00B5es
        :param int nsu: Apresenta o nsu da notifica\u00C3\u00A7\u00C3\u00A3o
        :return: PageSMSResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit', 'data_inclusao', 'tipo_evento', 'status', 'operadora', 'protocolo', 'nsu']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_sms_using_get" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/notificacoes/sms'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'data_inclusao' in params:
            query_params['dataInclusao'] = params['data_inclusao']
        if 'tipo_evento' in params:
            query_params['tipoEvento'] = params['tipo_evento']
        if 'status' in params:
            query_params['status'] = params['status']
        if 'operadora' in params:
            query_params['operadora'] = params['operadora']
        if 'protocolo' in params:
            query_params['protocolo'] = params['protocolo']
        if 'nsu' in params:
            query_params['nsu'] = params['nsu']

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
                                            response_type='PageSMSResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def responder_sms_using_post(self, **kwargs):
        """
        Responder SMS
        Esse recurso permite atualizar a resposta do SMS, fornecida pedo usu\u00C3\u00A1rio

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.responder_sms_using_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str nsu: Seu n\u00C3\u00BAmero
        :param str data: Data
        :param str resposta: TextoStatus
        :return: NotificacaoSMSResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['nsu', 'data', 'resposta']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method responder_sms_using_post" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/notificacoes/sms/responder'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'nsu' in params:
            query_params['nsu'] = params['nsu']
        if 'data' in params:
            query_params['data'] = params['data']
        if 'resposta' in params:
            query_params['resposta'] = params['resposta']

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
                                            response_type='NotificacaoSMSResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def salvar_push_fcm_using_post(self, push_persists, **kwargs):
        """
        Enviar Push FCM
        Esse recurso permite enviar Push para um determinado dipositivo movel atrav\u00C3\u00A9s da plataforma FCM (Firebase Cloud Messaging).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.salvar_push_fcm_using_post(push_persists, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[PushFCMEGCM] push_persists: pushPersists (required)
        :return: NotificacaoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['push_persists']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method salvar_push_fcm_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'push_persists' is set
        if ('push_persists' not in params) or (params['push_persists'] is None):
            raise ValueError("Missing the required parameter `push_persists` when calling `salvar_push_fcm_using_post`")

        resource_path = '/api/notificacoes/push/fcm'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'push_persists' in params:
            body_params = params['push_persists']

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
                                            response_type='NotificacaoResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def salvar_push_gcm_using_post(self, push_persists, **kwargs):
        """
        Enviar Push GCM
        Esse recurso permite enviar Push para um determinado dipositivo movel atrav\u00C3\u00A9s da plataforma GCM (Google Cloud Messaging).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.salvar_push_gcm_using_post(push_persists, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[PushFCMEGCM] push_persists: pushPersists (required)
        :return: NotificacaoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['push_persists']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method salvar_push_gcm_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'push_persists' is set
        if ('push_persists' not in params) or (params['push_persists'] is None):
            raise ValueError("Missing the required parameter `push_persists` when calling `salvar_push_gcm_using_post`")

        resource_path = '/api/notificacoes/push/gcm'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'push_persists' in params:
            body_params = params['push_persists']

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
                                            response_type='NotificacaoResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def salvar_push_using_post(self, push_persists, **kwargs):
        """
        Enviar Push APNS
        Esse recurso permite enviar Push para um determinado dipositivo movel atrav\u00C3\u00A9s da plataforma APNS (Apple Push Notification Service).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.salvar_push_using_post(push_persists, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[PushAPNS] push_persists: pushPersists (required)
        :return: NotificacaoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['push_persists']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method salvar_push_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'push_persists' is set
        if ('push_persists' not in params) or (params['push_persists'] is None):
            raise ValueError("Missing the required parameter `push_persists` when calling `salvar_push_using_post`")

        resource_path = '/api/notificacoes/push/apns'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'push_persists' in params:
            body_params = params['push_persists']

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
                                            response_type='NotificacaoResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def salvar_sms_using_post(self, lista_sms, **kwargs):
        """
        Enviar SMS
        Esse recurso permite enviar uma lista de SMS.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.salvar_sms_using_post(lista_sms, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[NotificacaoSMSBody] lista_sms: listaSMS (required)
        :return: NotificacaoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lista_sms']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method salvar_sms_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'lista_sms' is set
        if ('lista_sms' not in params) or (params['lista_sms'] is None):
            raise ValueError("Missing the required parameter `lista_sms` when calling `salvar_sms_using_post`")

        resource_path = '/api/notificacoes/sms'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'lista_sms' in params:
            body_params = params['lista_sms']

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
                                            response_type='NotificacaoResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
