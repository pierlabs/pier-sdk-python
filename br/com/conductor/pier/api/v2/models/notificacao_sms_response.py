# coding: utf-8

"""
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

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class NotificacaoSMSResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NotificacaoSMSResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'nsu': 'int',
            'id_emissor': 'int',
            'tipo_evento': 'str',
            'status': 'str',
            'descricao_status': 'str',
            'id_pessoa': 'int',
            'id_conta': 'int',
            'celular': 'str',
            'operadora': 'str',
            'conteudo': 'str',
            'resposta': 'str',
            'data_agendamento': 'str',
            'quantidade_tentativas_envio': 'int',
            'data_inclusao': 'str',
            'data_alteracao_status': 'str',
            'protocolo': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'nsu': 'nsu',
            'id_emissor': 'idEmissor',
            'tipo_evento': 'tipoEvento',
            'status': 'status',
            'descricao_status': 'descricaoStatus',
            'id_pessoa': 'idPessoa',
            'id_conta': 'idConta',
            'celular': 'celular',
            'operadora': 'operadora',
            'conteudo': 'conteudo',
            'resposta': 'resposta',
            'data_agendamento': 'dataAgendamento',
            'quantidade_tentativas_envio': 'quantidadeTentativasEnvio',
            'data_inclusao': 'dataInclusao',
            'data_alteracao_status': 'dataAlteracaoStatus',
            'protocolo': 'protocolo'
        }

        self._id = None
        self._nsu = None
        self._id_emissor = None
        self._tipo_evento = None
        self._status = None
        self._descricao_status = None
        self._id_pessoa = None
        self._id_conta = None
        self._celular = None
        self._operadora = None
        self._conteudo = None
        self._resposta = None
        self._data_agendamento = None
        self._quantidade_tentativas_envio = None
        self._data_inclusao = None
        self._data_alteracao_status = None
        self._protocolo = None

    @property
    def id(self):
        """
        Gets the id of this NotificacaoSMSResponse.
        C\u00C3\u00B3digo Identificador.

        :return: The id of this NotificacaoSMSResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this NotificacaoSMSResponse.
        C\u00C3\u00B3digo Identificador.

        :param id: The id of this NotificacaoSMSResponse.
        :type: int
        """
        self._id = id

    @property
    def nsu(self):
        """
        Gets the nsu of this NotificacaoSMSResponse.
        N\u00C3\u00BAmero sequencial \u00C3\u00BAnico.

        :return: The nsu of this NotificacaoSMSResponse.
        :rtype: int
        """
        return self._nsu

    @nsu.setter
    def nsu(self, nsu):
        """
        Sets the nsu of this NotificacaoSMSResponse.
        N\u00C3\u00BAmero sequencial \u00C3\u00BAnico.

        :param nsu: The nsu of this NotificacaoSMSResponse.
        :type: int
        """
        self._nsu = nsu

    @property
    def id_emissor(self):
        """
        Gets the id_emissor of this NotificacaoSMSResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do emissor (id).

        :return: The id_emissor of this NotificacaoSMSResponse.
        :rtype: int
        """
        return self._id_emissor

    @id_emissor.setter
    def id_emissor(self, id_emissor):
        """
        Sets the id_emissor of this NotificacaoSMSResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do emissor (id).

        :param id_emissor: The id_emissor of this NotificacaoSMSResponse.
        :type: int
        """
        self._id_emissor = id_emissor

    @property
    def tipo_evento(self):
        """
        Gets the tipo_evento of this NotificacaoSMSResponse.
        TipoEvento de notifica\u00C3\u00A7\u00C3\u00A3o

        :return: The tipo_evento of this NotificacaoSMSResponse.
        :rtype: str
        """
        return self._tipo_evento

    @tipo_evento.setter
    def tipo_evento(self, tipo_evento):
        """
        Sets the tipo_evento of this NotificacaoSMSResponse.
        TipoEvento de notifica\u00C3\u00A7\u00C3\u00A3o

        :param tipo_evento: The tipo_evento of this NotificacaoSMSResponse.
        :type: str
        """
        allowed_values = ["RISCO_FRAUDE", "OUTROS"]
        if tipo_evento not in allowed_values:
            raise ValueError(
                "Invalid value for `tipo_evento`, must be one of {0}"
                .format(allowed_values)
            )
        self._tipo_evento = tipo_evento

    @property
    def status(self):
        """
        Gets the status of this NotificacaoSMSResponse.
        Status de envio da notifica\u00C3\u00A7\u00C3\u00A3o

        :return: The status of this NotificacaoSMSResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this NotificacaoSMSResponse.
        Status de envio da notifica\u00C3\u00A7\u00C3\u00A3o

        :param status: The status of this NotificacaoSMSResponse.
        :type: str
        """
        allowed_values = ["PENDENTE", "ENCAMINHADO", "ENVIADO", "RESPONDIDO", "ERRO", "ERRO_RESPOSTA", "SUCESSO_RESPOSTA"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def descricao_status(self):
        """
        Gets the descricao_status of this NotificacaoSMSResponse.
        Descri\u00C3\u00A7\u00C3\u00A3o do status de envio da notifica\u00C3\u00A7\u00C3\u00A3o

        :return: The descricao_status of this NotificacaoSMSResponse.
        :rtype: str
        """
        return self._descricao_status

    @descricao_status.setter
    def descricao_status(self, descricao_status):
        """
        Sets the descricao_status of this NotificacaoSMSResponse.
        Descri\u00C3\u00A7\u00C3\u00A3o do status de envio da notifica\u00C3\u00A7\u00C3\u00A3o

        :param descricao_status: The descricao_status of this NotificacaoSMSResponse.
        :type: str
        """
        self._descricao_status = descricao_status

    @property
    def id_pessoa(self):
        """
        Gets the id_pessoa of this NotificacaoSMSResponse.
        C\u00C3\u00B3digo identificado da pessoa

        :return: The id_pessoa of this NotificacaoSMSResponse.
        :rtype: int
        """
        return self._id_pessoa

    @id_pessoa.setter
    def id_pessoa(self, id_pessoa):
        """
        Sets the id_pessoa of this NotificacaoSMSResponse.
        C\u00C3\u00B3digo identificado da pessoa

        :param id_pessoa: The id_pessoa of this NotificacaoSMSResponse.
        :type: int
        """
        self._id_pessoa = id_pessoa

    @property
    def id_conta(self):
        """
        Gets the id_conta of this NotificacaoSMSResponse.
        C\u00C3\u00B3digo identificador da conta

        :return: The id_conta of this NotificacaoSMSResponse.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this NotificacaoSMSResponse.
        C\u00C3\u00B3digo identificador da conta

        :param id_conta: The id_conta of this NotificacaoSMSResponse.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def celular(self):
        """
        Gets the celular of this NotificacaoSMSResponse.
        Apresenta o celular a ser eviado o SMS no formato 5588999999999 ou 5588999999999

        :return: The celular of this NotificacaoSMSResponse.
        :rtype: str
        """
        return self._celular

    @celular.setter
    def celular(self, celular):
        """
        Sets the celular of this NotificacaoSMSResponse.
        Apresenta o celular a ser eviado o SMS no formato 5588999999999 ou 5588999999999

        :param celular: The celular of this NotificacaoSMSResponse.
        :type: str
        """
        self._celular = celular

    @property
    def operadora(self):
        """
        Gets the operadora of this NotificacaoSMSResponse.
        Apresenta a operadora do celular a ser eviado o SMS

        :return: The operadora of this NotificacaoSMSResponse.
        :rtype: str
        """
        return self._operadora

    @operadora.setter
    def operadora(self, operadora):
        """
        Sets the operadora of this NotificacaoSMSResponse.
        Apresenta a operadora do celular a ser eviado o SMS

        :param operadora: The operadora of this NotificacaoSMSResponse.
        :type: str
        """
        self._operadora = operadora

    @property
    def conteudo(self):
        """
        Gets the conteudo of this NotificacaoSMSResponse.
        Apresenta o texto da notifica\u00C3\u00A7\u00C3\u00A3o a ser enviado

        :return: The conteudo of this NotificacaoSMSResponse.
        :rtype: str
        """
        return self._conteudo

    @conteudo.setter
    def conteudo(self, conteudo):
        """
        Sets the conteudo of this NotificacaoSMSResponse.
        Apresenta o texto da notifica\u00C3\u00A7\u00C3\u00A3o a ser enviado

        :param conteudo: The conteudo of this NotificacaoSMSResponse.
        :type: str
        """
        self._conteudo = conteudo

    @property
    def resposta(self):
        """
        Gets the resposta of this NotificacaoSMSResponse.
        Apresenta o texto da resposta da notifica\u00C3\u00A7\u00C3\u00A3o que foi enviada

        :return: The resposta of this NotificacaoSMSResponse.
        :rtype: str
        """
        return self._resposta

    @resposta.setter
    def resposta(self, resposta):
        """
        Sets the resposta of this NotificacaoSMSResponse.
        Apresenta o texto da resposta da notifica\u00C3\u00A7\u00C3\u00A3o que foi enviada

        :param resposta: The resposta of this NotificacaoSMSResponse.
        :type: str
        """
        self._resposta = resposta

    @property
    def data_agendamento(self):
        """
        Gets the data_agendamento of this NotificacaoSMSResponse.
        Apresenta a data e hora em que ser\u00C3\u00A1 enviado a notifica\u00C3\u00A7\u00C3\u00A3o

        :return: The data_agendamento of this NotificacaoSMSResponse.
        :rtype: str
        """
        return self._data_agendamento

    @data_agendamento.setter
    def data_agendamento(self, data_agendamento):
        """
        Sets the data_agendamento of this NotificacaoSMSResponse.
        Apresenta a data e hora em que ser\u00C3\u00A1 enviado a notifica\u00C3\u00A7\u00C3\u00A3o

        :param data_agendamento: The data_agendamento of this NotificacaoSMSResponse.
        :type: str
        """
        self._data_agendamento = data_agendamento

    @property
    def quantidade_tentativas_envio(self):
        """
        Gets the quantidade_tentativas_envio of this NotificacaoSMSResponse.
        Quantidade de tentativas e envio da notifica\u00C3\u00A7\u00C3\u00A3o

        :return: The quantidade_tentativas_envio of this NotificacaoSMSResponse.
        :rtype: int
        """
        return self._quantidade_tentativas_envio

    @quantidade_tentativas_envio.setter
    def quantidade_tentativas_envio(self, quantidade_tentativas_envio):
        """
        Sets the quantidade_tentativas_envio of this NotificacaoSMSResponse.
        Quantidade de tentativas e envio da notifica\u00C3\u00A7\u00C3\u00A3o

        :param quantidade_tentativas_envio: The quantidade_tentativas_envio of this NotificacaoSMSResponse.
        :type: int
        """
        self._quantidade_tentativas_envio = quantidade_tentativas_envio

    @property
    def data_inclusao(self):
        """
        Gets the data_inclusao of this NotificacaoSMSResponse.
        Apresenta a data e em que o registro foi inclu\u00C3\u00ADdo na base para ser enviado

        :return: The data_inclusao of this NotificacaoSMSResponse.
        :rtype: str
        """
        return self._data_inclusao

    @data_inclusao.setter
    def data_inclusao(self, data_inclusao):
        """
        Sets the data_inclusao of this NotificacaoSMSResponse.
        Apresenta a data e em que o registro foi inclu\u00C3\u00ADdo na base para ser enviado

        :param data_inclusao: The data_inclusao of this NotificacaoSMSResponse.
        :type: str
        """
        self._data_inclusao = data_inclusao

    @property
    def data_alteracao_status(self):
        """
        Gets the data_alteracao_status of this NotificacaoSMSResponse.
        Apresenta a data e em que o Stattjus do registro foi modificado

        :return: The data_alteracao_status of this NotificacaoSMSResponse.
        :rtype: str
        """
        return self._data_alteracao_status

    @data_alteracao_status.setter
    def data_alteracao_status(self, data_alteracao_status):
        """
        Sets the data_alteracao_status of this NotificacaoSMSResponse.
        Apresenta a data e em que o Stattjus do registro foi modificado

        :param data_alteracao_status: The data_alteracao_status of this NotificacaoSMSResponse.
        :type: str
        """
        self._data_alteracao_status = data_alteracao_status

    @property
    def protocolo(self):
        """
        Gets the protocolo of this NotificacaoSMSResponse.
        N\u00C3\u00BAmero do protocolo de envio de notifica\u00C3\u00A7\u00C3\u00B5es

        :return: The protocolo of this NotificacaoSMSResponse.
        :rtype: str
        """
        return self._protocolo

    @protocolo.setter
    def protocolo(self, protocolo):
        """
        Sets the protocolo of this NotificacaoSMSResponse.
        N\u00C3\u00BAmero do protocolo de envio de notifica\u00C3\u00A7\u00C3\u00B5es

        :param protocolo: The protocolo of this NotificacaoSMSResponse.
        :type: str
        """
        self._protocolo = protocolo

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

