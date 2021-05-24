# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/constants.ipynb (unless otherwise specified).

__all__ = ['URL', 'URLHM', 'URLHM2', 'ACAO_DESCRIPTION', 'ACAO_TRACKER', 'FIELDS', 'CUSTOM_IDS', 'SITUACAO',
           'DICT_FIELDS', 'JSON_FIELDS', 'CLASSE', 'TIPO', 'STATUS', 'SERVICOS', 'PF', 'PROCEDIMENTOS', 'ID2FIELD',
           'HM2PROD', 'FIELD2ID', 'ESTADOS']

# Cell
URL = "https://sistemas.anatel.gov.br/fiscaliza/"
URLHM = "https://sistemashm.anatel.gov.br/fiscaliza"
URLHM2 = "https://sistemasnethm/fiscaliza"
ACAO_DESCRIPTION = 54
ACAO_TRACKER = 2

# Cell
FIELDS = ["id", "subject", "status", "priority", "start_date", "due_date"]
CUSTOM_IDS = [
    2,
    5,
    22,
    25,
    26,
    30,
    31,
    57,
    69,
    70,
    71,
    89,
    91,
    92,
    93,
    94,
    111,
    112,
    151,
    154,
    156,
    157,
    158,
    159,
    170,
    171,
    178,
    213,
    280,
    422,
    450,
    463,
    534,
    535,
    537,
    658,
    659,
    660,
]

SITUACAO = {
    "Rascunho": 1,
    "Aguardando Execução": 11,
    "Em andamento": 13,
    "Relatando": 14,
    "Relatada": 15,
}

#'Cancelada': 19}

DICT_FIELDS = {
    "Classe_da_Inspecao": str,
    "Tipo_de_Inspecao": str,
    "Descricao_da_Inspecao": str,
    "Fiscal_Responsavel": str,
    "Fiscais": list,
    "Html": str,
    "Gerar_Relatorio": int,
    "Frequencia_Inicial": (int, float),
    "Unidade_da_Frequencia_Inicial": str,
    "Frequencia_Final": (int, float),
    "Unidade_da_Frequencia_Final": str,
    "Data_de_Inicio": str,
    "Data_Limite": str,
    "UF_Municipio": (str, list),
    "Servicos_da_Inspecao": (str, list),
    "Qnt_de_emissoes_na_faixa": int,
    "Emissoes_nao_autorizadas": int,
    "Horas_de_Preparacao": int,
    "Horas_de_Deslocamento": int,
    "Horas_de_Execucao": int,
    "Horas_de_Conclusao": int,
    "Latitude": float,
    "Longitude": float,
    "Uso_de_PF": str,
    "Acao_de_risco_a_vida_criada": str,
    "Impossibilidade_acesso_online": str,
    "Notes": str,
    "Entidade_da_Inspecao": str,
    "Agrupamento": int,
    "SAV": str,
    "PCDP": str,
    "Procedimentos": list,
    "Reservar_Instrumentos": str,
    "Reserva_de_Instrumentos": list,
    "Utilizou_algum_instrumento": str,
    "Coordenacao": str,
}

JSON_FIELDS = (
    "Classe_da_Inspecao",
    "Tipo_de_Inspecao",
    "UF_Municipio",
    "Servicos_da_Inspecao",
)


CLASSE = ("Tributária", "Técnica", "Serviço")

TIPO = (
    "Outorga - Aspectos não Técnicos",
    "Medição de CEMRF (RNI)",
    "Outorga - Aspectos Técnicos",
    "TV Digital",
    "Uso do Espectro - Monitoração",
    "Uso do Espectro - Não Outorgado",
    "Certificação",
)

STATUS = {
    "Aguardando Execução": (
        "Classe_da_Inspecao",
        "Tipo_de_Inspecao",
        "Descricao_da_Inspecao",
        "Fiscal_Responsavel",
        "Fiscais",
        "Entidade_da_Inspecao",
    ),
    "Em andamento": (
        "Html",
        "Gerar_Relatorio",
        "Reservar_Instrumentos",
        "Reserva_de_Instrumentos",
    ),
    "Relatando": (
        "Frequencia_Inicial",
        "Frequencia_Final",
        "Unidade_da_Frequencia_Inicial",
        "Unidade_da_Frequencia_Final",
    ),
    "Relatada": (
        "UF_Municipio",
        "Servicos_da_Inspecao",
        "Qnt_de_emissoes_na_faixa",
        "Emissoes_nao_autorizadas",
        "Horas_de_Preparacao",
        "Horas_de_Deslocamento",
        "Horas_de_Execucao",
        "Horas_de_Conclusao",
        "SAV",
        "PCDP",
        "Procedimentos",
        "Latitude",
        "Longitude",
        "Uso_de_PF",
        "Acao_de_risco_a_vida_criada",
        "Impossibilidade_acesso_online",
        "Utilizou_algum_instrumento",
    ),
}


SERVICOS = {
    "230": "230 - COLETIVO - RADIODIFUSÃO SONORA EM FREQÜÊNCIA MODULADA",
    "231": "231 - COLETIVO - RADIODIFUSÃO COMUNITÁRIA",
    "507": "507 - RESTRITO - MÓVEL AERONÁUTICO",
    "019": "019 - RESTRITO - LIMITADO PRIVADO",
    "800": "800 - COLETIVO - RETRANSMISSAO DE T.V.",
    "205": "205 - COLETIVO - RADIODIFUSÃO SONORA EM ONDA MÉDIA",
    "248": "248 - COLETIVO - RADIODIFUSÃO DE SONS E IMAGENS",
    "167": "167 - COLETIVO - ESPECIAL DE TELEVISAO POR ASSINATURA",
    "801": "801 - COLETIVO - RETRANSMISSÃO DE RADIODIFUSÃO DE SONS E IMAGENS - DIGITAL",
    "247": "247 - COLETIVO - GERADORA DE RADIODIFUSÃO DE SONS E IMAGENS - DIGITAL",
    "035": "035 - RESTRITO - ESPC. P/FINS CIENTIF.EXPERIMENTAIS",
    "078": "078 - RESTRITO - SERVIÇO DE RADIOTÁXI PRIVADO",
    "079": "079 - COLETIVO - SERVIÇO DE RADIOTÁXI ESPECIALIZADO",
    "033": "033 - COLETIVO - RADIOENLACES ASSOCIADOS AO SERVIÇO DE RÁDIOTAXI",
    "108": "108 - RESTRITO - SERVIÇO LIMITADO PRIVADO SUBMODALIDADE RADIODETERMINAÇÃO",
    "132": "108 - RESTRITO - ESPECIAL DE RADIOAUTOCINE",
    "017": "017 - RESTRITO - LIMITADO ESPECIALIZADO",
    "011": "011 - RESTRITO - LIMITADO PRIVADO - PRESTAÇÃO A TERCEIROS",
    "124": "124 - RESTRITO - ESPECIAL DE SUPERVISÃO E CONTROLE/USO PRÓPRIO",
    "125": "125 - RESTRITO - ESPECIAL DE SUPERVISÃO E CONTROLE/TERCEIROS",
    "604": "604 - RESTRITO - MÓVEL MARÍTIMO",
    "064": "064 - COLETIVO - MÓVEL MARÍTIMO ESPECIALIZADO",
    "046": "046 - COLETIVO - RADIOENLACES ASSOCIADOS AO SCM",
    "053": "053 - COLETIVO - RADIOENLACES ASSOCIADOS AO SMP",
    "099": "099 - RESTRITO - SERVIÇO DE RADIAÇÃO RESTRITA",
    "012": "012 - RESTRITO - RADIOENLACES ASSOCIADOS AO SERVIÇO MÓVEL PRIVADO",
}

PF = (
    "Utilização integral",
    "Utilização parcial",
    "Não utilização de PF existente",
    "Não se aplica PF - demanda específica",
    "Não se aplica PF - uso apenas de formulários",
    "Não se aplica PF - PF inexistente",
    "Não se aplica PF - necessidade de elaborar PF",
    "Não se aplica PF - outros",
)

PROCEDIMENTOS = (
    "Nenhum",
    "Lacração",
    "Apreensão",
    "Interrupção",
    "Não Cadastrado",
    "Notificado",
    "A Notificar",
    "Liberação/Desinterrupção",
    "Orientação ao Usuário",
    "Comunicado",
    "Deslacrado",
    "Vistoriado",
    "Emissão Termo Violação de Lacre",
    "Apoio a busca e apreensão",
    "Investigação/Pesquisa",
    "Não Lacrado - Impedimento",
    "Não Lacrado - Amparo Judicial",
    "Não Lacrado - Responsável Ausente",
    "Não Lacrado - Local Fechado",
    "Constatação Violação Lacre/Relacrado",
    "Constatação Violação Lacre/Impedimento",
    "Notícia Crime",
    "Monitorado alterado",
    "Constatação Encerramento - Informe",
    "Levantamento de Dados",
    "Análise/coleta de Dados",
    "Monitorado",
    "Não Lacrado - Desativado",
    "Devolução de Produto(s)",
)

ID2FIELD = {
    2: "Tipo_de_Inspecao",
    5: "Ano",
    22: "Descricao_da_Inspecao",
    25: "Fiscal_Responsavel",
    26: "Fiscais",
    30: "Entidade_da_Inspecao",
    31: "UF_Municipio",
    57: "Servicos_da_Inspecao",
    69: "Qnt_de_emissoes_na_faixa",
    70: "Emissoes_nao_autorizadas",
    71: "Procedimentos",
    89: "Classe_da_Inspecao",
    91: "Horas_de_Preparacao",
    92: "Horas_de_Deslocamento",
    93: "Horas_de_Execucao",
    94: "Horas_de_Conclusao",
    111: "SAV",
    112: "PCDP",
    151: "Uso_de_PF",
    154: "Acao_de_risco_a_vida_criada",
    156: "Frequencia_Inicial",
    157: "Unidade_da_Frequencia_Inicial",
    158: "Frequencia_Final",
    159: "Unidade_da_Frequencia_Final",
    170: "Latitude",
    171: "Longitude",
    178: "Coordenacao",
    213: "Agrupamento",
    280: "Utilizou_algum_instrumento",
    422: "Numero_Sei_do_Processo",
    450: "Impossibilidade_acesso_online",
    463: "AppFiscaliza",
    534: "Gerar_Relatorio",
    535: "Relatorio_de_Monitoramento",
    537: "Html",
    658: "Reservar_Instrumentos",
    659: "Reserva_de_Instrumentos",
    660: "Utilizou_algum_instrumento",
}

HM2PROD = {537: 543, 534: 541, 535: 544, 658: 596, 659: 597, 660: 598}

FIELD2ID = {
    "Tipo_de_Inspecao": 2,
    "Ano": 5,
    "Descricao_da_Inspecao": 22,
    "Fiscal_Responsavel": 25,
    "Fiscais": 26,
    "Entidade_da_Inspecao": 30,
    "UF_Municipio": 31,
    "Servicos_da_Inspecao": 57,
    "Qnt_de_emissoes_na_faixa": 69,
    "Emissoes_nao_autorizadas": 70,
    "Procedimentos": 71,
    "Classe_da_Inspecao": 89,
    "Horas_de_Preparacao": 91,
    "Horas_de_Deslocamento": 92,
    "Horas_de_Execucao": 93,
    "Horas_de_Conclusao": 94,
    "SAV": 111,
    "PCDP": 112,
    "Uso_de_PF": 151,
    "Acao_de_risco_a_vida_criada": 154,
    "Frequencia_Inicial": 156,
    "Unidade_da_Frequencia_Inicial": 157,
    "Frequencia_Final": 158,
    "Unidade_da_Frequencia_Final": 159,
    "Latitude": 170,
    "Longitude": 171,
    "Coordenacao": 178,
    "Agrupamento": 213,
    "Utilizou_algum_instrumento": 280,
    "Numero_Sei_do_Processo": 422,
    "Impossibilidade_acesso_online": 450,
    "AppFiscaliza": 463,
    "Gerar_Relatorio": 534,
    "Relatorio_de_Monitoramento": 535,
    "Html": 537,
    "Reservar_Instrumentos": 658,
    "Reserva_de_Instrumentos": 659,
    "Utilizou_algum_instrumento": 660,
}

ESTADOS = [
    "AC",
    "AL",
    "AP",
    "AM",
    "BA",
    "CE",
    "ES",
    "GO",
    "MA",
    "MT",
    "MS",
    "MG",
    "PA",
    "PB",
    "PR",
    "PE",
    "PI",
    "RJ",
    "RN",
    "RS",
    "RO",
    "RR",
    "SC",
    "SP",
    "SE",
    "TO",
    "DF",
]