from __future__ import absolute_import

# import models into model package
from .adicional_detalhe_response import AdicionalDetalheResponse
from .adicional_persist import AdicionalPersist
from .adicional_response import AdicionalResponse
from .adicional_update import AdicionalUpdate
from .ajuste_financeiro_response import AjusteFinanceiroResponse
from .alterar_produto_request import AlterarProdutoRequest
from .anexo_notificacao_email_request import AnexoNotificacaoEmailRequest
from .antecipacao_response import AntecipacaoResponse
from .antecipacao_simulada_detalhes_response import AntecipacaoSimuladaDetalhesResponse
from .antecipacao_simulada_lote_response import AntecipacaoSimuladaLoteResponse
from .antecipacao_simulada_response import AntecipacaoSimuladaResponse
from .anuidade_response import AnuidadeResponse
from .aplicacao_mobile_persist import AplicacaoMobilePersist
from .aplicacao_mobile_response import AplicacaoMobileResponse
from .aplicacao_mobile_update import AplicacaoMobileUpdate
from .arquivo_aud_response import ArquivoAUDResponse
from .arquivo_detalhe_response import ArquivoDetalheResponse
from .arquivo_detalhes_persist import ArquivoDetalhesPersist
from .arquivo_parametro_aud_response import ArquivoParametroAUDResponse
from .arquivo_parametro_response import ArquivoParametroResponse
from .arquivo_persist import ArquivoPersist
from .arquivo_response import ArquivoResponse
from .atendimento_cliente_response import AtendimentoClienteResponse
from .atribuir_assinatura_cliente_persist import AtribuirAssinaturaClientePersist
from .auth_token import AuthToken
from .autorizacao_on_us_request import AutorizacaoOnUsRequest
from .aviso_viagem_response import AvisoViagemResponse
from .banco_response import BancoResponse
from .base_response import BaseResponse
from .beneficio_pagamento_atraso_response import BeneficioPagamentoAtrasoResponse
from .body_access_token import BodyAccessToken
from .boleto_response import BoletoResponse
from .campanha_persist import CampanhaPersist
from .campanha_response import CampanhaResponse
from .campanha_update import CampanhaUpdate
from .campo_codificado_descricao_response import CampoCodificadoDescricaoResponse
from .cancelamento_transacao_on_us_request import CancelamentoTransacaoOnUsRequest
from .cancelamento_transacao_por_id_cartao_request import CancelamentoTransacaoPorIdCartaoRequest
from .cartao_detalhe_response import CartaoDetalheResponse
from .cartao_embossing_request import CartaoEmbossingRequest
from .cartao_embossing_response import CartaoEmbossingResponse
from .cartao_impressao_provisorio_response import CartaoImpressaoProvisorioResponse
from .cartao_impressao_response import CartaoImpressaoResponse
from .cartao_pay_atualizar_chave_response import CartaoPayAtualizarChaveResponse
from .cartao_pay_cadastro_response import CartaoPayCadastroResponse
from .cartao_pay_confirmar_chave_response import CartaoPayConfirmarChaveResponse
from .cartao_pay_detalhe_response import CartaoPayDetalheResponse
from .cartao_pay_key_update import CartaoPayKeyUpdate
from .cartao_pay_persist import CartaoPayPersist
from .cartao_pay_response import CartaoPayResponse
from .cartao_pay_update import CartaoPayUpdate
from .cartao_response import CartaoResponse
from .cdt_detalhe_oportunidade_aud import CdtDetalheOportunidadeAUD
from .codigo_seguranca_email_persist import CodigoSegurancaEMAILPersist
from .codigo_seguranca_response import CodigoSegurancaResponse
from .codigo_seguranca_sms_persist import CodigoSegurancaSMSPersist
from .codigo_seguranca_sms_request import CodigoSegurancaSMSRequest
from .compra_response import CompraResponse
from .configuracao_email_persist import ConfiguracaoEmailPersist
from .configuracao_email_response import ConfiguracaoEmailResponse
from .configuracao_registro_cobranca_persist import ConfiguracaoRegistroCobrancaPersist
from .configuracao_registro_cobranca_response import ConfiguracaoRegistroCobrancaResponse
from .configuracao_rotativo_detalhe_response import ConfiguracaoRotativoDetalheResponse
from .configuracao_rotativo_persist import ConfiguracaoRotativoPersist
from .consulta_cadastro_estabelecimento_dto import ConsultaCadastroEstabelecimentoDTO
from .conta_bancaria_portador_persist import ContaBancariaPortadorPersist
from .conta_bancaria_portador_response import ContaBancariaPortadorResponse
from .conta_bancaria_portador_update import ContaBancariaPortadorUpdate
from .conta_detalhe_response import ContaDetalheResponse
from .conta_historico_pagamento_response import ContaHistoricoPagamentoResponse
from .conta_response import ContaResponse
from .controle_vencimento_response import ControleVencimentoResponse
from .dados_cartao_impressao_response import DadosCartaoImpressaoResponse
from .dados_cartao_response import DadosCartaoResponse
from .desfazimento_transacao_on_us_request import DesfazimentoTransacaoOnUsRequest
from .detalhe_operacao_response import DetalheOperacaoResponse
from .detalhe_oportunidade_persist import DetalheOportunidadePersist
from .detalhe_oportunidade_response import DetalheOportunidadeResponse
from .detalhe_oportunidade_update import DetalheOportunidadeUpdate
from .detalhes_fatura_consignada_response import DetalhesFaturaConsignadaResponse
from .detalhes_fatura_response import DetalhesFaturaResponse
from .dispositivo_persist import DispositivoPersist
from .dispositivo_response import DispositivoResponse
from .divida_cliente_response import DividaClienteResponse
from .documento_detalhado_response import DocumentoDetalhadoResponse
from .documento_detalhe_response import DocumentoDetalheResponse
from .documento_integracao_response import DocumentoIntegracaoResponse
from .documento_parametros_request import DocumentoParametrosRequest
from .documento_response import DocumentoResponse
from .documento_template_persist import DocumentoTemplatePersist
from .documento_template_response import DocumentoTemplateResponse
from .emprestimo_pessoal_request import EmprestimoPessoalRequest
from .emprestimo_pessoal_response import EmprestimoPessoalResponse
from .endereco_aprovado_persist import EnderecoAprovadoPersist
from .endereco_aprovado_response import EnderecoAprovadoResponse
from .endereco_response import EnderecoResponse
from .entidade_response import EntidadeResponse
from .estabelecimento_persist import EstabelecimentoPersist
from .estabelecimento_response import EstabelecimentoResponse
from .estabelecimento_update import EstabelecimentoUpdate
from .estagio_cartao_response import EstagioCartaoResponse
from .extra_info import ExtraInfo
from .fantasia_basica_response import FantasiaBasicaResponse
from .faq_response import FaqResponse
from .fatura_consignada_detalhe_response import FaturaConsignadaDetalheResponse
from .fatura_consignada_response import FaturaConsignadaResponse
from .fatura_detalhe_response import FaturaDetalheResponse
from .fatura_fechada_response import FaturaFechadaResponse
from .fatura_response import FaturaResponse
from .grade_pendente_request import GradePendenteRequest
from .grupo_economico_dto import GrupoEconomicoDTO
from .grupo_economico_response import GrupoEconomicoResponse
from .historico_assessoria_response import HistoricoAssessoriaResponse
from .historico_atraso_fatura_response import HistoricoAtrasoFaturaResponse
from .historico_eventos_response import HistoricoEventosResponse
from .historico_impressao_cartao_response import HistoricoImpressaoCartaoResponse
from .historico_pagamento_response import HistoricoPagamentoResponse
from .historico_telefone_response import HistoricoTelefoneResponse
from .integracao_emissor_persist import IntegracaoEmissorPersist
from .integracao_emissor_response import IntegracaoEmissorResponse
from .integrar_arquivo_request import IntegrarArquivoRequest
from .integrar_documento_request import IntegrarDocumentoRequest
from .job_response import JobResponse
from .lancamento_fatura_response import LancamentoFaturaResponse
from .limite_disponibilidade_response import LimiteDisponibilidadeResponse
from .lote_cartoes_pre_pagos_response import LoteCartoesPrePagosResponse
from .mcc_response import MCCResponse
from .map_ofstring_andstring import MapOfstringAndstring
from .maquineta_persist import MaquinetaPersist
from .maquineta_response import MaquinetaResponse
from .maquineta_update import MaquinetaUpdate
from .moeda_response import MoedaResponse
from .notificacao_email_request import NotificacaoEmailRequest
from .notificacao_push_response import NotificacaoPushResponse
from .notificacao_response import NotificacaoResponse
from .notificacao_sms_body import NotificacaoSMSBody
from .notificacao_sms_response import NotificacaoSMSResponse
from .operacao_credor_persist import OperacaoCredorPersist
from .operacao_credor_response import OperacaoCredorResponse
from .operacao_credor_update import OperacaoCredorUpdate
from .operacao_response import OperacaoResponse
from .operadora_response import OperadoraResponse
from .oportunidade_aud_response import OportunidadeAUDResponse
from .oportunidade_persist import OportunidadePersist
from .oportunidade_response import OportunidadeResponse
from .oportunidade_update import OportunidadeUpdate
from .origem_comercial_persist import OrigemComercialPersist
from .origem_comercial_response import OrigemComercialResponse
from .origem_comercial_update import OrigemComercialUpdate
from .page_ajuste_response import PageAjusteResponse
from .page_anuidade_response import PageAnuidadeResponse
from .page_aplicacao_mobile_response import PageAplicacaoMobileResponse
from .page_arquivo_aud_response import PageArquivoAUDResponse
from .page_arquivo_response import PageArquivoResponse
from .page_atendimento_cliente_response import PageAtendimentoClienteResponse
from .page_aviso_viagem_response import PageAvisoViagemResponse
from .page_banco_response import PageBancoResponse
from .page_base_response import PageBaseResponse
from .page_campanha_response import PageCampanhaResponse
from .page_campo_codificado_descricao_response import PageCampoCodificadoDescricaoResponse
from .page_cartao_pay_response import PageCartaoPayResponse
from .page_cartao_response import PageCartaoResponse
from .page_codigo_seguranca_response import PageCodigoSegurancaResponse
from .page_compra_response import PageCompraResponse
from .page_configuracao_email_response import PageConfiguracaoEmailResponse
from .page_configuracao_rotativo_response import PageConfiguracaoRotativoResponse
from .page_conta_bancaria_portador_response import PageContaBancariaPortadorResponse
from .page_conta_detalhe_response import PageContaDetalheResponse
from .page_conta_historico_pagamento_response import PageContaHistoricoPagamentoResponse
from .page_conta_response import PageContaResponse
from .page_controle_vencimento_response import PageControleVencimentoResponse
from .page_dispositivo_response import PageDispositivoResponse
from .page_documento_response import PageDocumentoResponse
from .page_documento_template_response import PageDocumentoTemplateResponse
from .page_endereco_response import PageEnderecoResponse
from .page_entidade_response import PageEntidadeResponse
from .page_estabelecimento_response import PageEstabelecimentoResponse
from .page_estagio_cartao_response import PageEstagioCartaoResponse
from .page_fantasia_basica_response import PageFantasiaBasicaResponse
from .page_faq_response import PageFaqResponse
from .page_fatura_consignada_response import PageFaturaConsignadaResponse
from .page_fatura_fechada_response import PageFaturaFechadaResponse
from .page_fatura_response import PageFaturaResponse
from .page_grupo_economico_response import PageGrupoEconomicoResponse
from .page_historico_assessoria_response import PageHistoricoAssessoriaResponse
from .page_historico_atraso_fatura_response import PageHistoricoAtrasoFaturaResponse
from .page_historico_eventos_response import PageHistoricoEventosResponse
from .page_historico_pagamento_response import PageHistoricoPagamentoResponse
from .page_job_response import PageJobResponse
from .page_lote_cartoes_pre_pagos_response import PageLoteCartoesPrePagosResponse
from .page_mcc_response import PageMCCResponse
from .page_maquineta_response import PageMaquinetaResponse
from .page_moeda_response import PageMoedaResponse
from .page_operacao_credor_response import PageOperacaoCredorResponse
from .page_operacao_response import PageOperacaoResponse
from .page_operadora_response import PageOperadoraResponse
from .page_oportunidade_aud_response import PageOportunidadeAUDResponse
from .page_oportunidade_response import PageOportunidadeResponse
from .page_origem_comercial_response import PageOrigemComercialResponse
from .page_pais_response import PagePaisResponse
from .page_pessoa_detalhe_response import PagePessoaDetalheResponse
from .page_pessoa_response import PagePessoaResponse
from .page_plano_parcelamento_response import PagePlanoParcelamentoResponse
from .page_plataforma_mobile_response import PagePlataformaMobileResponse
from .page_portador_response import PagePortadorResponse
from .page_produto_response import PageProdutoResponse
from .page_promotor_response import PagePromotorResponse
from .page_push_response import PagePushResponse
from .page_risco_fraude_response import PageRiscoFraudeResponse
from .page_sms_response import PageSMSResponse
from .page_status_cartao_response import PageStatusCartaoResponse
from .page_status_conta_response import PageStatusContaResponse
from .page_status_impressao_response import PageStatusImpressaoResponse
from .page_status_oportunidade_aud_response import PageStatusOportunidadeAUDResponse
from .page_status_oportunidade_response import PageStatusOportunidadeResponse
from .page_taxas_refinanciamento_response import PageTaxasRefinanciamentoResponse
from .page_telefone_estabelecimento_response import PageTelefoneEstabelecimentoResponse
from .page_telefone_response import PageTelefoneResponse
from .page_template_notificacao_response import PageTemplateNotificacaoResponse
from .page_terminal_response import PageTerminalResponse
from .page_tipo_ajuste_response import PageTipoAjusteResponse
from .page_tipo_boleto_response import PageTipoBoletoResponse
from .page_tipo_campanha_response import PageTipoCampanhaResponse
from .page_tipo_debito_recorrente_response import PageTipoDebitoRecorrenteResponse
from .page_tipo_endereco_response import PageTipoEnderecoResponse
from .page_tipo_faturamento_por_conta_response import PageTipoFaturamentoPorContaResponse
from .page_tipo_faturamento_response import PageTipoFaturamentoResponse
from .page_tipo_oportunidade_aud_response import PageTipoOportunidadeAUDResponse
from .page_tipo_oportunidade_response import PageTipoOportunidadeResponse
from .page_tipo_telefone_response import PageTipoTelefoneResponse
from .page_tipo_template_response import PageTipoTemplateResponse
from .page_tipo_terminal_response import PageTipoTerminalResponse
from .page_transacao_nao_processada_response import PageTransacaoNaoProcessadaResponse
from .page_transacao_response import PageTransacaoResponse
from .page_transacoes_correntes_response import PageTransacoesCorrentesResponse
from .page_transferencia_bancaria_response import PageTransferenciaBancariaResponse
from .page_transferencia_credito_conta_bancaria_response import PageTransferenciaCreditoContaBancariaResponse
from .page_transferencia_response import PageTransferenciaResponse
from .page_usuario_response import PageUsuarioResponse
from .page_vinculo_estabelecimento_adquirente_response import PageVinculoEstabelecimentoAdquirenteResponse
from .page_vinculo_operacao_response import PageVinculoOperacaoResponse
from .page_web_hook_response import PageWebHookResponse
from .pais_response import PaisResponse
from .parametro_produto_response import ParametroProdutoResponse
from .parcelamento_transferencia_response import ParcelamentoTransferenciaResponse
from .pessoa_detalhe_response import PessoaDetalheResponse
from .pessoa_fisica_aprovada_persist import PessoaFisicaAprovadaPersist
from .pessoa_fisica_aprovada_response import PessoaFisicaAprovadaResponse
from .pessoa_juridica_aprovada_persist import PessoaJuridicaAprovadaPersist
from .pessoa_juridica_aprovada_response import PessoaJuridicaAprovadaResponse
from .pessoa_persist import PessoaPersist
from .pessoa_response import PessoaResponse
from .plano_campanha_persist import PlanoCampanhaPersist
from .plano_campanha_response import PlanoCampanhaResponse
from .plano_campanha_update import PlanoCampanhaUpdate
from .plano_parcelamento_emprestimo_response import PlanoParcelamentoEmprestimoResponse
from .plano_parcelamento_response import PlanoParcelamentoResponse
from .plano_parcelamento_transferencia_credito_conta_bancaria_request import PlanoParcelamentoTransferenciaCreditoContaBancariaRequest
from .plano_parcelamento_transferencia_credito_conta_bancaria_response import PlanoParcelamentoTransferenciaCreditoContaBancariaResponse
from .plataforma_mobile_persist import PlataformaMobilePersist
from .plataforma_mobile_response import PlataformaMobileResponse
from .plataforma_mobile_update import PlataformaMobileUpdate
from .portador_response import PortadorResponse
from .produto_detalhes_response import ProdutoDetalhesResponse
from .produto_origem_response import ProdutoOrigemResponse
from .produto_response import ProdutoResponse
from .promotor_response import PromotorResponse
from .propriedade_documento_request import PropriedadeDocumentoRequest
from .push_apns import PushAPNS
from .push_fcm_e_gcm import PushFCMEGCM
from .refencia_comercial_aprovado_persist import RefenciaComercialAprovadoPersist
from .referencia_comercial_aprovado_response import ReferenciaComercialAprovadoResponse
from .referencia_id_persist import ReferenciaIdPersist
from .risco_fraude_detalhado_response import RiscoFraudeDetalhadoResponse
from .risco_fraude_response import RiscoFraudeResponse
from .socio_aprovado_response import SocioAprovadoResponse
from .status_cartao_response import StatusCartaoResponse
from .status_conta_response import StatusContaResponse
from .status_impressao_response import StatusImpressaoResponse
from .status_oportunidade import StatusOportunidade
from .status_oportunidade_aud_response import StatusOportunidadeAUDResponse
from .status_oportunidade_response import StatusOportunidadeResponse
from .taxa_antecipacao_request import TaxaAntecipacaoRequest
from .taxas_refinanciamento_response import TaxasRefinanciamentoResponse
from .telefone_adicional_persist import TelefoneAdicionalPersist
from .telefone_adicional_update import TelefoneAdicionalUpdate
from .telefone_estabelecimento_response import TelefoneEstabelecimentoResponse
from .telefone_pessoa_aprovada_persist import TelefonePessoaAprovadaPersist
from .telefone_pessoa_aprovada_response import TelefonePessoaAprovadaResponse
from .telefone_response import TelefoneResponse
from .template_notificacao_detalhe_response import TemplateNotificacaoDetalheResponse
from .template_notificacao_response import TemplateNotificacaoResponse
from .terminal_persist import TerminalPersist
from .terminal_response import TerminalResponse
from .terminal_update import TerminalUpdate
from .tipo_ajuste_response import TipoAjusteResponse
from .tipo_boleto_response import TipoBoletoResponse
from .tipo_campanha_response import TipoCampanhaResponse
from .tipo_debito_recorrente_response import TipoDebitoRecorrenteResponse
from .tipo_endereco_response import TipoEnderecoResponse
from .tipo_faturamento_persist import TipoFaturamentoPersist
from .tipo_faturamento_por_conta_persist import TipoFaturamentoPorContaPersist
from .tipo_faturamento_por_conta_response import TipoFaturamentoPorContaResponse
from .tipo_faturamento_response import TipoFaturamentoResponse
from .tipo_operacao_response import TipoOperacaoResponse
from .tipo_oportunidade import TipoOportunidade
from .tipo_oportunidade_aud_response import TipoOportunidadeAUDResponse
from .tipo_oportunidade_response import TipoOportunidadeResponse
from .tipo_resolucao_response import TipoResolucaoResponse
from .tipo_telefone_response import TipoTelefoneResponse
from .tipo_template_request import TipoTemplateRequest
from .tipo_template_response import TipoTemplateResponse
from .tipo_terminal_response import TipoTerminalResponse
from .token_response import TokenResponse
from .transacao_corrente_response import TransacaoCorrenteResponse
from .transacao_nao_processada_response import TransacaoNaoProcessadaResponse
from .transacao_on_us_por_id_cartao_request import TransacaoOnUsPorIdCartaoRequest
from .transacao_on_us_request import TransacaoOnUsRequest
from .transacao_on_us_response import TransacaoOnUsResponse
from .transacao_pay_query_request import TransacaoPayQueryRequest
from .transacao_pay_query_response import TransacaoPayQueryResponse
from .transacao_pay_secure_request import TransacaoPaySecureRequest
from .transacoes_correntes_response import TransacoesCorrentesResponse
from .transferencia_bancaria_persist import TransferenciaBancariaPersist
from .transferencia_bancaria_response import TransferenciaBancariaResponse
from .transferencia_credito_conta_bancaria_lista_response import TransferenciaCreditoContaBancariaListaResponse
from .transferencia_credito_conta_bancaria_persist import TransferenciaCreditoContaBancariaPersist
from .transferencia_credito_conta_bancaria_response import TransferenciaCreditoContaBancariaResponse
from .transferencia_detalhe_response import TransferenciaDetalheResponse
from .transferencia_response import TransferenciaResponse
from .usuario_persist import UsuarioPersist
from .usuario_response import UsuarioResponse
from .usuario_update import UsuarioUpdate
from .valida_cvv_request import ValidaCVVRequest
from .valida_cartao_response import ValidaCartaoResponse
from .valida_senha_cartao_response import ValidaSenhaCartaoResponse
from .vinculo_estabelecimento_adquirente_persist import VinculoEstabelecimentoAdquirentePersist
from .vinculo_estabelecimento_adquirente_response import VinculoEstabelecimentoAdquirenteResponse
from .vinculo_operacao_persist import VinculoOperacaoPersist
from .vinculo_operacao_response import VinculoOperacaoResponse
from .web_hook import WebHook
from .web_hook_response import WebHookResponse
