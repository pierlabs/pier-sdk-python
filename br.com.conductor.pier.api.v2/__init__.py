from __future__ import absolute_import

# import models into sdk package
from .models.adicional_detalhe_response import AdicionalDetalheResponse
from .models.adicional_persist import AdicionalPersist
from .models.adicional_response import AdicionalResponse
from .models.adicional_update import AdicionalUpdate
from .models.ajuste_financeiro_response import AjusteFinanceiroResponse
from .models.alterar_produto_request import AlterarProdutoRequest
from .models.anexo_notificacao_email_request import AnexoNotificacaoEmailRequest
from .models.antecipacao_response import AntecipacaoResponse
from .models.antecipacao_simulada_detalhes_response import AntecipacaoSimuladaDetalhesResponse
from .models.antecipacao_simulada_lote_response import AntecipacaoSimuladaLoteResponse
from .models.antecipacao_simulada_response import AntecipacaoSimuladaResponse
from .models.anuidade_response import AnuidadeResponse
from .models.aplicacao_mobile_persist import AplicacaoMobilePersist
from .models.aplicacao_mobile_response import AplicacaoMobileResponse
from .models.aplicacao_mobile_update import AplicacaoMobileUpdate
from .models.arquivo_detalhes_persist import ArquivoDetalhesPersist
from .models.arquivo_parametro_response import ArquivoParametroResponse
from .models.arquivo_persist import ArquivoPersist
from .models.arquivo_response import ArquivoResponse
from .models.atendimento_cliente_response import AtendimentoClienteResponse
from .models.atribuir_assinatura_cliente_persist import AtribuirAssinaturaClientePersist
from .models.auth_token import AuthToken
from .models.autorizacao_on_us_request import AutorizacaoOnUsRequest
from .models.banco_response import BancoResponse
from .models.base_response import BaseResponse
from .models.beneficio_pagamento_atraso_response import BeneficioPagamentoAtrasoResponse
from .models.body_access_token import BodyAccessToken
from .models.boleto_response import BoletoResponse
from .models.campanha_persist import CampanhaPersist
from .models.campanha_response import CampanhaResponse
from .models.campanha_update import CampanhaUpdate
from .models.campo_codificado_descricao_response import CampoCodificadoDescricaoResponse
from .models.cancelamento_transacao_on_us_request import CancelamentoTransacaoOnUsRequest
from .models.cancelamento_transacao_por_id_cartao_request import CancelamentoTransacaoPorIdCartaoRequest
from .models.cartao_detalhe_response import CartaoDetalheResponse
from .models.cartao_embossing_request import CartaoEmbossingRequest
from .models.cartao_embossing_response import CartaoEmbossingResponse
from .models.cartao_impressao_provisorio_response import CartaoImpressaoProvisorioResponse
from .models.cartao_impressao_response import CartaoImpressaoResponse
from .models.cartao_pay_atualizar_chave_response import CartaoPayAtualizarChaveResponse
from .models.cartao_pay_cadastro_response import CartaoPayCadastroResponse
from .models.cartao_pay_confirmar_chave_response import CartaoPayConfirmarChaveResponse
from .models.cartao_pay_detalhe_response import CartaoPayDetalheResponse
from .models.cartao_pay_key_update import CartaoPayKeyUpdate
from .models.cartao_pay_persist import CartaoPayPersist
from .models.cartao_pay_response import CartaoPayResponse
from .models.cartao_pay_update import CartaoPayUpdate
from .models.cartao_response import CartaoResponse
from .models.cdt_detalhe_oportunidade_aud import CdtDetalheOportunidadeAUD
from .models.codigo_seguranca_email_persist import CodigoSegurancaEMAILPersist
from .models.codigo_seguranca_response import CodigoSegurancaResponse
from .models.codigo_seguranca_sms_persist import CodigoSegurancaSMSPersist
from .models.codigo_seguranca_sms_request import CodigoSegurancaSMSRequest
from .models.compra_response import CompraResponse
from .models.configuracao_email_persist import ConfiguracaoEmailPersist
from .models.configuracao_email_response import ConfiguracaoEmailResponse
from .models.configuracao_registro_cobranca_persist import ConfiguracaoRegistroCobrancaPersist
from .models.configuracao_registro_cobranca_response import ConfiguracaoRegistroCobrancaResponse
from .models.configuracao_rotativo_detalhe_response import ConfiguracaoRotativoDetalheResponse
from .models.configuracao_rotativo_persist import ConfiguracaoRotativoPersist
from .models.conta_bancaria_portador_persist import ContaBancariaPortadorPersist
from .models.conta_bancaria_portador_response import ContaBancariaPortadorResponse
from .models.conta_bancaria_portador_update import ContaBancariaPortadorUpdate
from .models.conta_detalhe_response import ContaDetalheResponse
from .models.conta_historico_pagamento_response import ContaHistoricoPagamentoResponse
from .models.conta_response import ContaResponse
from .models.controle_vencimento_response import ControleVencimentoResponse
from .models.credor_dto import CredorDTO
from .models.credor_response import CredorResponse
from .models.dados_cartao_impressao_response import DadosCartaoImpressaoResponse
from .models.dados_cartao_response import DadosCartaoResponse
from .models.desfazimento_transacao_on_us_request import DesfazimentoTransacaoOnUsRequest
from .models.detalhe_operacao_response import DetalheOperacaoResponse
from .models.detalhe_oportunidade_persist import DetalheOportunidadePersist
from .models.detalhe_oportunidade_response import DetalheOportunidadeResponse
from .models.detalhe_oportunidade_update import DetalheOportunidadeUpdate
from .models.detalhes_fatura_consignada_response import DetalhesFaturaConsignadaResponse
from .models.detalhes_fatura_response import DetalhesFaturaResponse
from .models.dispositivo_persist import DispositivoPersist
from .models.dispositivo_response import DispositivoResponse
from .models.divida_cliente_response import DividaClienteResponse
from .models.documento_detalhado_response import DocumentoDetalhadoResponse
from .models.documento_detalhe_response import DocumentoDetalheResponse
from .models.documento_integracao_response import DocumentoIntegracaoResponse
from .models.documento_parametros_request import DocumentoParametrosRequest
from .models.documento_response import DocumentoResponse
from .models.documento_template_persist import DocumentoTemplatePersist
from .models.documento_template_response import DocumentoTemplateResponse
from .models.emprestimo_pessoal_request import EmprestimoPessoalRequest
from .models.emprestimo_pessoal_response import EmprestimoPessoalResponse
from .models.endereco_aprovado_persist import EnderecoAprovadoPersist
from .models.endereco_aprovado_response import EnderecoAprovadoResponse
from .models.endereco_response import EnderecoResponse
from .models.estabelecimento_response import EstabelecimentoResponse
from .models.estagio_cartao_response import EstagioCartaoResponse
from .models.extra_info import ExtraInfo
from .models.fantasia_basica_response import FantasiaBasicaResponse
from .models.faq_response import FaqResponse
from .models.fatura_consignada_detalhe_response import FaturaConsignadaDetalheResponse
from .models.fatura_consignada_response import FaturaConsignadaResponse
from .models.fatura_detalhe_response import FaturaDetalheResponse
from .models.fatura_fechada_response import FaturaFechadaResponse
from .models.fatura_response import FaturaResponse
from .models.grade_pendente_request import GradePendenteRequest
from .models.historico_assessoria_response import HistoricoAssessoriaResponse
from .models.historico_atraso_fatura_response import HistoricoAtrasoFaturaResponse
from .models.historico_eventos_response import HistoricoEventosResponse
from .models.historico_impressao_cartao_response import HistoricoImpressaoCartaoResponse
from .models.historico_telefone_response import HistoricoTelefoneResponse
from .models.integracao_emissor_persist import IntegracaoEmissorPersist
from .models.integracao_emissor_response import IntegracaoEmissorResponse
from .models.integrar_documento_request import IntegrarDocumentoRequest
from .models.job_response import JobResponse
from .models.lancamento_fatura_response import LancamentoFaturaResponse
from .models.limite_disponibilidade_response import LimiteDisponibilidadeResponse
from .models.lote_cartoes_pre_pagos_response import LoteCartoesPrePagosResponse
from .models.map_ofstring_andstring import MapOfstringAndstring
from .models.notificacao_email_request import NotificacaoEmailRequest
from .models.notificacao_push_response import NotificacaoPushResponse
from .models.notificacao_response import NotificacaoResponse
from .models.notificacao_sms_body import NotificacaoSMSBody
from .models.notificacao_sms_response import NotificacaoSMSResponse
from .models.operacao_response import OperacaoResponse
from .models.operadora_response import OperadoraResponse
from .models.oportunidade_aud_response import OportunidadeAUDResponse
from .models.oportunidade_persist import OportunidadePersist
from .models.oportunidade_response import OportunidadeResponse
from .models.oportunidade_update import OportunidadeUpdate
from .models.origem_comercial_response import OrigemComercialResponse
from .models.page_ajuste_response import PageAjusteResponse
from .models.page_anuidade_response import PageAnuidadeResponse
from .models.page_aplicacao_mobile_response import PageAplicacaoMobileResponse
from .models.page_atendimento_cliente_response import PageAtendimentoClienteResponse
from .models.page_banco_response import PageBancoResponse
from .models.page_base_response import PageBaseResponse
from .models.page_campanha_response import PageCampanhaResponse
from .models.page_campo_codificado_descricao_response import PageCampoCodificadoDescricaoResponse
from .models.page_cartao_pay_response import PageCartaoPayResponse
from .models.page_cartao_response import PageCartaoResponse
from .models.page_codigo_seguranca_response import PageCodigoSegurancaResponse
from .models.page_compra_response import PageCompraResponse
from .models.page_configuracao_email_response import PageConfiguracaoEmailResponse
from .models.page_configuracao_rotativo_response import PageConfiguracaoRotativoResponse
from .models.page_conta_bancaria_portador_response import PageContaBancariaPortadorResponse
from .models.page_conta_detalhe_response import PageContaDetalheResponse
from .models.page_conta_historico_pagamento_response import PageContaHistoricoPagamentoResponse
from .models.page_conta_response import PageContaResponse
from .models.page_controle_vencimento_response import PageControleVencimentoResponse
from .models.page_credor_response import PageCredorResponse
from .models.page_dispositivo_response import PageDispositivoResponse
from .models.page_documento_response import PageDocumentoResponse
from .models.page_documento_template_response import PageDocumentoTemplateResponse
from .models.page_endereco_response import PageEnderecoResponse
from .models.page_estabelecimento_response import PageEstabelecimentoResponse
from .models.page_estagio_cartao_response import PageEstagioCartaoResponse
from .models.page_fantasia_basica_response import PageFantasiaBasicaResponse
from .models.page_faq_response import PageFaqResponse
from .models.page_fatura_consignada_response import PageFaturaConsignadaResponse
from .models.page_fatura_fechada_response import PageFaturaFechadaResponse
from .models.page_fatura_response import PageFaturaResponse
from .models.page_historico_assessoria_response import PageHistoricoAssessoriaResponse
from .models.page_historico_atraso_fatura_response import PageHistoricoAtrasoFaturaResponse
from .models.page_historico_eventos_response import PageHistoricoEventosResponse
from .models.page_job_response import PageJobResponse
from .models.page_lote_cartoes_pre_pagos_response import PageLoteCartoesPrePagosResponse
from .models.page_operacao_response import PageOperacaoResponse
from .models.page_operadora_response import PageOperadoraResponse
from .models.page_oportunidade_aud_response import PageOportunidadeAUDResponse
from .models.page_oportunidade_response import PageOportunidadeResponse
from .models.page_origem_comercial_response import PageOrigemComercialResponse
from .models.page_pais_response import PagePaisResponse
from .models.page_pessoa_detalhe_response import PagePessoaDetalheResponse
from .models.page_pessoa_juridica_response import PagePessoaJuridicaResponse
from .models.page_pessoa_response import PagePessoaResponse
from .models.page_plano_parcelamento_response import PagePlanoParcelamentoResponse
from .models.page_plataforma_mobile_response import PagePlataformaMobileResponse
from .models.page_portador_response import PagePortadorResponse
from .models.page_produto_response import PageProdutoResponse
from .models.page_promotor_response import PagePromotorResponse
from .models.page_push_response import PagePushResponse
from .models.page_risco_fraude_response import PageRiscoFraudeResponse
from .models.page_sms_response import PageSMSResponse
from .models.page_status_cartao_response import PageStatusCartaoResponse
from .models.page_status_conta_response import PageStatusContaResponse
from .models.page_status_impressao_response import PageStatusImpressaoResponse
from .models.page_status_oportunidade_aud_response import PageStatusOportunidadeAUDResponse
from .models.page_status_oportunidade_response import PageStatusOportunidadeResponse
from .models.page_taxas_refinanciamento_response import PageTaxasRefinanciamentoResponse
from .models.page_telefone_estabelecimento_response import PageTelefoneEstabelecimentoResponse
from .models.page_telefone_response import PageTelefoneResponse
from .models.page_template_notificacao_response import PageTemplateNotificacaoResponse
from .models.page_terminal_response import PageTerminalResponse
from .models.page_tipo_ajuste_response import PageTipoAjusteResponse
from .models.page_tipo_boleto_response import PageTipoBoletoResponse
from .models.page_tipo_campanha_response import PageTipoCampanhaResponse
from .models.page_tipo_debito_recorrente_response import PageTipoDebitoRecorrenteResponse
from .models.page_tipo_endereco_response import PageTipoEnderecoResponse
from .models.page_tipo_oportunidade_aud_response import PageTipoOportunidadeAUDResponse
from .models.page_tipo_oportunidade_response import PageTipoOportunidadeResponse
from .models.page_tipo_telefone_response import PageTipoTelefoneResponse
from .models.page_tipo_template_response import PageTipoTemplateResponse
from .models.page_transacao_nao_processada_response import PageTransacaoNaoProcessadaResponse
from .models.page_transacao_response import PageTransacaoResponse
from .models.page_transacoes_correntes_response import PageTransacoesCorrentesResponse
from .models.page_transferencia_bancaria_response import PageTransferenciaBancariaResponse
from .models.page_transferencia_credito_conta_bancaria_response import PageTransferenciaCreditoContaBancariaResponse
from .models.page_transferencia_response import PageTransferenciaResponse
from .models.page_usuario_response import PageUsuarioResponse
from .models.page_web_hook_response import PageWebHookResponse
from .models.pais_response import PaisResponse
from .models.parametro_produto_response import ParametroProdutoResponse
from .models.parcelamento_transferencia_response import ParcelamentoTransferenciaResponse
from .models.pessoa_detalhe_response import PessoaDetalheResponse
from .models.pessoa_fisica_aprovada_persist import PessoaFisicaAprovadaPersist
from .models.pessoa_fisica_aprovada_response import PessoaFisicaAprovadaResponse
from .models.pessoa_juridica_aprovada_persist import PessoaJuridicaAprovadaPersist
from .models.pessoa_juridica_aprovada_response import PessoaJuridicaAprovadaResponse
from .models.pessoa_juridica_response import PessoaJuridicaResponse
from .models.pessoa_persist import PessoaPersist
from .models.pessoa_response import PessoaResponse
from .models.plano_campanha_persist import PlanoCampanhaPersist
from .models.plano_campanha_response import PlanoCampanhaResponse
from .models.plano_campanha_update import PlanoCampanhaUpdate
from .models.plano_parcelamento_emprestimo_response import PlanoParcelamentoEmprestimoResponse
from .models.plano_parcelamento_response import PlanoParcelamentoResponse
from .models.plano_parcelamento_transferencia_credito_conta_bancaria_request import PlanoParcelamentoTransferenciaCreditoContaBancariaRequest
from .models.plano_parcelamento_transferencia_credito_conta_bancaria_response import PlanoParcelamentoTransferenciaCreditoContaBancariaResponse
from .models.plano_parcelamento_transferencia_response import PlanoParcelamentoTransferenciaResponse
from .models.plataforma_mobile_persist import PlataformaMobilePersist
from .models.plataforma_mobile_response import PlataformaMobileResponse
from .models.plataforma_mobile_update import PlataformaMobileUpdate
from .models.portador_response import PortadorResponse
from .models.produto_detalhes_response import ProdutoDetalhesResponse
from .models.produto_origem_response import ProdutoOrigemResponse
from .models.produto_response import ProdutoResponse
from .models.promotor_response import PromotorResponse
from .models.propriedade_documento_request import PropriedadeDocumentoRequest
from .models.push_apns import PushAPNS
from .models.push_fcm_e_gcm import PushFCMEGCM
from .models.refencia_comercial_aprovado_persist import RefenciaComercialAprovadoPersist
from .models.referencia_comercial_aprovado_response import ReferenciaComercialAprovadoResponse
from .models.referencia_id_persist import ReferenciaIdPersist
from .models.risco_fraude_detalhado_response import RiscoFraudeDetalhadoResponse
from .models.risco_fraude_response import RiscoFraudeResponse
from .models.socio_aprovado_response import SocioAprovadoResponse
from .models.status_cartao_response import StatusCartaoResponse
from .models.status_conta_response import StatusContaResponse
from .models.status_impressao_response import StatusImpressaoResponse
from .models.status_oportunidade import StatusOportunidade
from .models.status_oportunidade_aud_response import StatusOportunidadeAUDResponse
from .models.status_oportunidade_response import StatusOportunidadeResponse
from .models.taxa_antecipacao_request import TaxaAntecipacaoRequest
from .models.taxas_refinanciamento_response import TaxasRefinanciamentoResponse
from .models.telefone_adicional_persist import TelefoneAdicionalPersist
from .models.telefone_adicional_update import TelefoneAdicionalUpdate
from .models.telefone_estabelecimento_response import TelefoneEstabelecimentoResponse
from .models.telefone_pessoa_aprovada_persist import TelefonePessoaAprovadaPersist
from .models.telefone_pessoa_aprovada_response import TelefonePessoaAprovadaResponse
from .models.telefone_response import TelefoneResponse
from .models.template_notificacao_detalhe_response import TemplateNotificacaoDetalheResponse
from .models.template_notificacao_response import TemplateNotificacaoResponse
from .models.terminal_response import TerminalResponse
from .models.terminal_update import TerminalUpdate
from .models.tipo_ajuste_response import TipoAjusteResponse
from .models.tipo_boleto_response import TipoBoletoResponse
from .models.tipo_campanha_response import TipoCampanhaResponse
from .models.tipo_debito_recorrente_response import TipoDebitoRecorrenteResponse
from .models.tipo_endereco_response import TipoEnderecoResponse
from .models.tipo_operacao_response import TipoOperacaoResponse
from .models.tipo_oportunidade import TipoOportunidade
from .models.tipo_oportunidade_aud_response import TipoOportunidadeAUDResponse
from .models.tipo_oportunidade_response import TipoOportunidadeResponse
from .models.tipo_resolucao_response import TipoResolucaoResponse
from .models.tipo_telefone_response import TipoTelefoneResponse
from .models.tipo_template_request import TipoTemplateRequest
from .models.tipo_template_response import TipoTemplateResponse
from .models.token_response import TokenResponse
from .models.transacao_corrente_response import TransacaoCorrenteResponse
from .models.transacao_nao_processada_response import TransacaoNaoProcessadaResponse
from .models.transacao_on_us_por_id_cartao_request import TransacaoOnUsPorIdCartaoRequest
from .models.transacao_on_us_request import TransacaoOnUsRequest
from .models.transacao_on_us_response import TransacaoOnUsResponse
from .models.transacao_pay_query_request import TransacaoPayQueryRequest
from .models.transacao_pay_query_response import TransacaoPayQueryResponse
from .models.transacao_pay_secure_request import TransacaoPaySecureRequest
from .models.transacoes_correntes_response import TransacoesCorrentesResponse
from .models.transferencia_bancaria_persist import TransferenciaBancariaPersist
from .models.transferencia_bancaria_response import TransferenciaBancariaResponse
from .models.transferencia_credito_conta_bancaria_lista_response import TransferenciaCreditoContaBancariaListaResponse
from .models.transferencia_credito_conta_bancaria_persist import TransferenciaCreditoContaBancariaPersist
from .models.transferencia_credito_conta_bancaria_response import TransferenciaCreditoContaBancariaResponse
from .models.transferencia_detalhe_response import TransferenciaDetalheResponse
from .models.transferencia_response import TransferenciaResponse
from .models.usuario_persist import UsuarioPersist
from .models.usuario_response import UsuarioResponse
from .models.usuario_update import UsuarioUpdate
from .models.valida_cartao_response import ValidaCartaoResponse
from .models.valida_senha_cartao_response import ValidaSenhaCartaoResponse
from .models.web_hook_response import WebHookResponse

# import apis into sdk package
from .apis.ajuste_financeiro_api import AjusteFinanceiroApi
from .apis.antecipacao_api import AntecipacaoApi
from .apis.aplicacao_mobile_api import AplicacaoMobileApi
from .apis.arquivo_api import ArquivoApi
from .apis.autorizacao_api import AutorizacaoApi
from .apis.base_api import BaseApi
from .apis.boleto_api import BoletoApi
from .apis.cadastro_cliente_api import CadastroClienteApi
from .apis.cadastro_geral_api import CadastroGeralApi
from .apis.cartao_api import CartaoApi
from .apis.conductor_pay_api import ConductorPayApi
from .apis.conta_api import ContaApi
from .apis.debito_recorrente_api import DebitoRecorrenteApi
from .apis.dispositivo_api import DispositivoApi
from .apis.documento_api import DocumentoApi
from .apis.endereco_nacional_api import EnderecoNacionalApi
from .apis.estabelecimento_api import EstabelecimentoApi
from .apis.faq_api import FAQApi
from .apis.fatura_api import FaturaApi
from .apis.job_api import JobApi
from .apis.limite_api import LimiteApi
from .apis.limite_disponibilidade_api import LimiteDisponibilidadeApi
from .apis.notificacao_api import NotificacaoApi
from .apis.oportunidade_api import OportunidadeApi
from .apis.permissao_pais_api import PermissaoPaisApi
from .apis.plataforma_mobile_api import PlataformaMobileApi
from .apis.risco_fraude_api import RiscoFraudeApi
from .apis.servico_conta_api import ServicoContaApi
from .apis.status_parametro_api import StatusParametroApi
from .apis.token_api import TokenApi
from .apis.transferencia_bancaria_api import TransferenciaBancariaApi
from .apis.usuario_api import UsuarioApi
from .apis.webhook_api import WebhookApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
