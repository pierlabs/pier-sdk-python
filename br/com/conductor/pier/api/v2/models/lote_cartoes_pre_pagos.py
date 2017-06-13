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


class LoteCartoesPrePagos(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LoteCartoesPrePagos - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_origem_comercial': 'int',
            'id_produto': 'int',
            'id_tipo_cartao': 'int',
            'id_imagem': 'int',
            'id_endereco': 'int',
            'quantidade': 'int',
            'data_cadastro': 'str',
            'usuario_cadastro': 'str',
            'status_processamento': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'id_origem_comercial': 'idOrigemComercial',
            'id_produto': 'idProduto',
            'id_tipo_cartao': 'idTipoCartao',
            'id_imagem': 'idImagem',
            'id_endereco': 'idEndereco',
            'quantidade': 'quantidade',
            'data_cadastro': 'dataCadastro',
            'usuario_cadastro': 'usuarioCadastro',
            'status_processamento': 'statusProcessamento'
        }

        self._id = None
        self._id_origem_comercial = None
        self._id_produto = None
        self._id_tipo_cartao = None
        self._id_imagem = None
        self._id_endereco = None
        self._quantidade = None
        self._data_cadastro = None
        self._usuario_cadastro = None
        self._status_processamento = None

    @property
    def id(self):
        """
        Gets the id of this LoteCartoesPrePagos.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do lote de cart\u00C3\u00B5es pr\u00C3\u00A9-pagos (id).

        :return: The id of this LoteCartoesPrePagos.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LoteCartoesPrePagos.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do lote de cart\u00C3\u00B5es pr\u00C3\u00A9-pagos (id).

        :param id: The id of this LoteCartoesPrePagos.
        :type: int
        """
        self._id = id

    @property
    def id_origem_comercial(self):
        """
        Gets the id_origem_comercial of this LoteCartoesPrePagos.
        C\u00C3\u00B3digo identificador da origem comercial.

        :return: The id_origem_comercial of this LoteCartoesPrePagos.
        :rtype: int
        """
        return self._id_origem_comercial

    @id_origem_comercial.setter
    def id_origem_comercial(self, id_origem_comercial):
        """
        Sets the id_origem_comercial of this LoteCartoesPrePagos.
        C\u00C3\u00B3digo identificador da origem comercial.

        :param id_origem_comercial: The id_origem_comercial of this LoteCartoesPrePagos.
        :type: int
        """
        self._id_origem_comercial = id_origem_comercial

    @property
    def id_produto(self):
        """
        Gets the id_produto of this LoteCartoesPrePagos.
        C\u00C3\u00B3digo identificador do Produto.

        :return: The id_produto of this LoteCartoesPrePagos.
        :rtype: int
        """
        return self._id_produto

    @id_produto.setter
    def id_produto(self, id_produto):
        """
        Sets the id_produto of this LoteCartoesPrePagos.
        C\u00C3\u00B3digo identificador do Produto.

        :param id_produto: The id_produto of this LoteCartoesPrePagos.
        :type: int
        """
        self._id_produto = id_produto

    @property
    def id_tipo_cartao(self):
        """
        Gets the id_tipo_cartao of this LoteCartoesPrePagos.
        C\u00C3\u00B3digo identificador do tipo do cart\u00C3\u00A3o.

        :return: The id_tipo_cartao of this LoteCartoesPrePagos.
        :rtype: int
        """
        return self._id_tipo_cartao

    @id_tipo_cartao.setter
    def id_tipo_cartao(self, id_tipo_cartao):
        """
        Sets the id_tipo_cartao of this LoteCartoesPrePagos.
        C\u00C3\u00B3digo identificador do tipo do cart\u00C3\u00A3o.

        :param id_tipo_cartao: The id_tipo_cartao of this LoteCartoesPrePagos.
        :type: int
        """
        self._id_tipo_cartao = id_tipo_cartao

    @property
    def id_imagem(self):
        """
        Gets the id_imagem of this LoteCartoesPrePagos.
        C\u00C3\u00B3digo identificador da Imagem do cart\u00C3\u00A3o.

        :return: The id_imagem of this LoteCartoesPrePagos.
        :rtype: int
        """
        return self._id_imagem

    @id_imagem.setter
    def id_imagem(self, id_imagem):
        """
        Sets the id_imagem of this LoteCartoesPrePagos.
        C\u00C3\u00B3digo identificador da Imagem do cart\u00C3\u00A3o.

        :param id_imagem: The id_imagem of this LoteCartoesPrePagos.
        :type: int
        """
        self._id_imagem = id_imagem

    @property
    def id_endereco(self):
        """
        Gets the id_endereco of this LoteCartoesPrePagos.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Endere\u00C3\u00A7o.

        :return: The id_endereco of this LoteCartoesPrePagos.
        :rtype: int
        """
        return self._id_endereco

    @id_endereco.setter
    def id_endereco(self, id_endereco):
        """
        Sets the id_endereco of this LoteCartoesPrePagos.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Endere\u00C3\u00A7o.

        :param id_endereco: The id_endereco of this LoteCartoesPrePagos.
        :type: int
        """
        self._id_endereco = id_endereco

    @property
    def quantidade(self):
        """
        Gets the quantidade of this LoteCartoesPrePagos.
        N\u00C3\u00BAmero de cart\u00C3\u00B5es existentes no Lote.

        :return: The quantidade of this LoteCartoesPrePagos.
        :rtype: int
        """
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        """
        Sets the quantidade of this LoteCartoesPrePagos.
        N\u00C3\u00BAmero de cart\u00C3\u00B5es existentes no Lote.

        :param quantidade: The quantidade of this LoteCartoesPrePagos.
        :type: int
        """
        self._quantidade = quantidade

    @property
    def data_cadastro(self):
        """
        Gets the data_cadastro of this LoteCartoesPrePagos.
        Data de cadastro do lote de cart\u00C3\u00B5es pr\u00C3\u00A9-pagos.

        :return: The data_cadastro of this LoteCartoesPrePagos.
        :rtype: str
        """
        return self._data_cadastro

    @data_cadastro.setter
    def data_cadastro(self, data_cadastro):
        """
        Sets the data_cadastro of this LoteCartoesPrePagos.
        Data de cadastro do lote de cart\u00C3\u00B5es pr\u00C3\u00A9-pagos.

        :param data_cadastro: The data_cadastro of this LoteCartoesPrePagos.
        :type: str
        """
        self._data_cadastro = data_cadastro

    @property
    def usuario_cadastro(self):
        """
        Gets the usuario_cadastro of this LoteCartoesPrePagos.
        Nome do usu\u00C3\u00A1rio que criou o lote.

        :return: The usuario_cadastro of this LoteCartoesPrePagos.
        :rtype: str
        """
        return self._usuario_cadastro

    @usuario_cadastro.setter
    def usuario_cadastro(self, usuario_cadastro):
        """
        Sets the usuario_cadastro of this LoteCartoesPrePagos.
        Nome do usu\u00C3\u00A1rio que criou o lote.

        :param usuario_cadastro: The usuario_cadastro of this LoteCartoesPrePagos.
        :type: str
        """
        self._usuario_cadastro = usuario_cadastro

    @property
    def status_processamento(self):
        """
        Gets the status_processamento of this LoteCartoesPrePagos.
        Indica o status de processamento do lote.

        :return: The status_processamento of this LoteCartoesPrePagos.
        :rtype: int
        """
        return self._status_processamento

    @status_processamento.setter
    def status_processamento(self, status_processamento):
        """
        Sets the status_processamento of this LoteCartoesPrePagos.
        Indica o status de processamento do lote.

        :param status_processamento: The status_processamento of this LoteCartoesPrePagos.
        :type: int
        """
        self._status_processamento = status_processamento

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

