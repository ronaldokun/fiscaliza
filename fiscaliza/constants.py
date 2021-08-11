# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/constants.ipynb (unless otherwise specified).

__all__ = ['URL', 'URLHM', 'URLHM2', 'ACAO_DESCRIPTION', 'ACAO_TRACKER', 'FIELDS', 'CUSTOM_IDS', 'SITUACAO',
           'DICT_FIELDS', 'JSON_FIELDS', 'CLASSE', 'TIPO', 'STATUS', 'SERVICOS', 'PF', 'PROCEDIMENTOS', 'ID2FIELD',
           'FIELD2ID', 'ESTADOS', 'TABLECOLS']

# Cell
URL = "https://sistemas.anatel.gov.br/fiscaliza/"
URLHM = "https://sistemashm.anatel.gov.br/fiscaliza"
URLHM2 = "https://sistemasnethm/fiscaliza"
ACAO_DESCRIPTION = 54
ACAO_TRACKER = 2
from typing import *

# Cell
FIELDS = [
    "id",
    "subject",
    "status",
    "priority",
    "start_date",
    "due_date",
    "description",
]
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
    541,
    544,
    543,
    596,
    597,
    598,
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
    "description": str,
    "Fiscal_Responsavel": str,
    "Fiscais": list,
    "Html": str,
    "Gerar_Relatorio": (int, str),
    "Frequencia_Inicial": (int, float),
    "Unidade_da_Frequencia_Inicial": str,
    "Frequencia_Final": (int, float),
    "Unidade_da_Frequencia_Final": str,
    "start_date": str,
    "due_date": str,
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
    "notes": str,
    "Entidade_da_Inspecao": str,
    "Agrupamento": int,
    "SAV": str,
    "PCDP": str,
    "Procedimentos": list,
    "Reservar_Instrumentos": (int, str),
    "Utilizou_algum_instrumento": (int, str),
    "uploads": List[dict],
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
    ),
    "Em andamento": ("Html", "Gerar_Relatorio", "Reservar_Instrumentos"),
    "Relatando": (
        "Frequencia_Inicial",
        "Frequencia_Final",
        "Unidade_da_Frequencia_Inicial",
        "Unidade_da_Frequencia_Final",
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
    "000": "000 - Não Aplicável",
    "001": "001 - COLETIVO - SERVIÇO DE INTERESSE COLETIVO",
    "002": "002 - RESTRITO - SERVIÇO DE INTERESSE RESTRITO",
    "010": "010 - COLETIVO - SERVIÇO MOVEL PESSOAL",
    "011": "011 - RESTRITO - LIMITADO PRIVADO - PRESTAÇÃO A TERCEIROS",
    "012": "012 - RESTRITO - RADIOENLACES ASSOCIADOS AO SERVIÇO MÓVEL PRIVADO",
    "013": "013 - COLETIVO - RADIOENLACES ASSOCIADOS AO SERVIÇO ESPECIALIZADO RADIOCHAMADA",
    "014": "014 - RESTRITO - RADIOENLACES ASSOCIADOS AO SERVIÇO DE REDE ESPECIALIZADO",
    "015": "015 - COLETIVO - RADIOENLACES ASSOCIADOS A SISTEMA DE SATÉLITES",
    "016": "016 - COLETIVO - RADIOENLACES ASSOCIADOS AO SERVIÇO POR LINHA DEDICADA",
    "017": "017 - RESTRITO - LIMITADO ESPECIALIZADO",
    "019": "019 - RESTRITO - LIMITADO PRIVADO",
    "020": "020 - COLETIVO - SERVIÇO MOVEL ESPECIALIZADO",
    "021": "021 - RESTRITO - LIMITADO - FIBRAS ÓTICAS",
    "023": "023 - RESTRITO - SERVIÇO LIMITADO MOVEL PRIVATIVO",
    "024": "024 - COLETIVO - RADIOENLACES ASSOCIADOS AO SERVIÇO ESPECIALIZADO REPETIÇÃO SINAL ÁUDIO",
    "025": "025 - COLETIVO - RADIOENLACES ASSOCIADOS AO SERVIÇO ESPECIALIZADO REPETIÇÃO TV/VÍDEO",
    "026": "026 - RESTRITO - RADIOENLACES ASSOCIADOS AO SERVIÇO DE CIRCUITO ESPECIALIZADO",
    "027": "027 - COLETIVO - RADIOENLACES ASSOCIADOS AO SERVIÇO MÓVEL ESPECIALIZADO",
    "028": "028 - RESTRITO - LIMITADO PRIVADO ESTAÇÕES ITINERANTES",
    "029": "029 - COLETIVO - RADIOENLACES ASSOCIADOS AO SERVIÇO LIMITADO ESPECIALIZADO",
    "030": "030 - COLETIVO - SERVIÇO REDE DE TRANSPORTE TELECOMUNICAÇÕES - SRTT",
    "031": "031 - COLETIVO - SERV. REDE DE TRANSPORTE TELECOM-SRTT - SATELITE",
    "032": "032 - COLETIVO - RADIOENLACES ASSOCIADOS AO SERVIÇO REDE TRANSPORTE TELECOMUNICAÇÃO",
    "033": "033 - COLETIVO - RADIOENLACES ASSOCIADOS AO SERVIÇO DE RÁDIOTAXI",
    "034": "034 - RESTRITO - SERVIÇO SLMP PRESTADO A DETERMINADOS GRUPOS DE USUARIOS",
    "035": "035 - RESTRITO - ESPC. P/FINS CIENTIF.EXPERIMENTAIS",
    "036": "036 - RESTRITO - SERVIÇO DE MONITORAGEM DO ESPECTRO",
    "037": "037 - RESTRITO - SERVIÇO USO TEMPORÁRIO DO ESPECTRO",
    "038": "038 - COLETIVO - SERVIÇO ESPECIAL DE REPETIÇÃO DE SINAIS DE TV E VÍDEO",
    "039": "039 - COLETIVO - SERVIÇO ESPECIAL DE REPETIÇÃO DE SINAIS DE ÁUDIO",
    "040": "040 - COLETIVO - SERVIÇO POR LINHA DEDICADA (SLD)",
    "041": "041 - COLETIVO - SERVIÇO DE REDE COMUTADA POR PACOTE",
    "042": "042 - COLETIVO - SERVIÇO DE REDE COMUTADA POR CIRCUITO",
    "043": "043 - COLETIVO - ESPECIAL DE RADIORRECADO",
    "044": "044 - RESTRITO - ENLACES FÍSICOS ASSOCIADOS AO SERVIÇO LIMITADO PRIVADO",
    "045": "045 - COLETIVO - SERVIÇO DE COMUNICAÇÃO MULTIMÍDIA",
    "046": "046 - COLETIVO - RADIOENLACES ASSOCIADOS AO SCM",
    "047": "047 - COLETIVO - SERVIÇO DE COMUNICAÇÃO MULTIMÍDIA - EST. TERRENA",
    "048": "048 - RESTRITO - RÁDIO-ACESSO",
    "049": "049 - RESTRITO - SERVIÇO LIMITADO PRIVADO PARA PRESTAÇÃO DE SERVIÇO PELAS PREFEITURAS MUNICIPAIS",
    "050": "050 - RESTRITO - SERVIÇO LIMITADO PRIVADO PARA INCLUSÃO DIGITAL NAS FAIXAS DE 2,5GHZ E 3,5GHZ",
    "051": "051 - COLETIVO - SERVIÇO ESPECIAL DE RADIOCHAMADA",
    "053": "053 - COLETIVO - RADIOENLACES ASSOCIADOS AO SMP",
    "060": "060 - RESTRITO - SERVIÇO LIMITADO PRIVADO DE RADIOCHAMADA-SLPR",
    "064": "064 - COLETIVO - MÓVEL MARÍTIMO ESPECIALIZADO",
    "067": "067 - COLETIVO - SERVIÇO AVANÇADO DE MENSAGEM (SAM)",
    "069": "069 - RESTRITO - SERVIÇO DE CIRCUITO ESPECIALIZADO",
    "076": "076 - RESTRITO - SERVIÇO DE REDE PRIVADO",
    "077": "077 - RESTRITO - SERVIÇO DE REDE ESPECIALIZADO",
    "078": "078 - RESTRITO - SERVIÇO DE RADIOTÁXI PRIVADO",
    "079": "079 - COLETIVO - SERVIÇO DE RADIOTÁXI ESPECIALIZADO",
    "086": "086 - COLETIVO - ESPECIAL DE FREQÜÊNCIA PADRÃO",
    "094": "094 - COLETIVO - SERVIÇO ESPECIAL DE SINAIS HORÁRIOS",
    "099": "099 - RESTRITO - SERVIÇO DE RADIAÇÃO RESTRITA",
    "108": "108 - RESTRITO - SERVIÇO LIMITADO PRIVADO SUBMODALIDADE RADIODETERMINAÇÃO",
    "116": "116 - COLETIVO - TEL.PUBLICO MOVEL RODOVIARIO-TELESTRADA",
    "124": "124 - RESTRITO - ESPECIAL DE SUPERVISÃO E CONTROLE/USO PRÓPRIO",
    "125": "125 - RESTRITO - ESPECIAL DE SUPERVISÃO E CONTROLE/TERCEIROS",
    "132": "132 - RESTRITO - ESPECIAL DE RADIOAUTOCINE",
    "140": "140 - RESTRITO - LIMITADO - RADIOESTRADA",
    "159": "159 - COLETIVO - RADIOCOMUNICAÇÃO AERONÁUTICA PÚBLICO - RESTRITO",
    "163": "163 - COLETIVO - SERVIÇO DE COMUNICAÇÃO DE TEXTOS",
    "167": "167 - COLETIVO - ESPECIAL DE TELEVISAO POR ASSINATURA",
    "171": "171 - COLETIVO - SERVICO TELEFONICO FIXO COMUTADO",
    "175": "175 - COLETIVO - STFC/RADIOTELEFONICO - ESTACOES TERRESTRES",
    "176": "176 - COLETIVO - STFC/RADIOTELEFONICO - ESTACOES TERRENAS",
    "181": "181 - RESTRITO - LIMITADO PRIVADO POR SATELITE",
    "182": "182 - RESTRITO - LIMITADO ESPECIALIZADO POR SATELITE",
    "183": "183 - COLETIVO - ESPECIAL DE BOLETINS METEOROLOGICOS",
    "185": "185 - RESTRITO - EXPLORACAO DE SATELITE E ESTACOES DE ACESSO",
    "186": "186 - RESTRITO - EXPLORAÇÃO DE SATÉLITE NÃO-GEOESTACIONÁRIO E ESTAÇÃO DE ACESSO",
    "187": "187 - RESTRITO - SERVICO DE REDE ESPECIALIZADO P/SATELITE",
    "188": "188 - RESTRITO - SERVICO DE CIRCUITO ESPECIALIZADO P/SATELITE",
    "189": "189 - COLETIVO - SERVICO MOVEL GLOBAL POR SATELITE(SMGS)",
    "191": "191 - COLETIVO - SERVIÇO DE COMUNICAÇÃO DE DADOS COMUTADO",
    "205": "205 - COLETIVO - RADIODIFUSÃO SONORA EM ONDA MÉDIA",
    "213": "213 - COLETIVO - RADIODIFUSÃO SONORA EM ONDAS CURTAS",
    "221": "221 - COLETIVO - RADIODIFUSÃO SONORA EM ONDA TROPICAL",
    "230": "230 - COLETIVO - RADIODIFUSÃO SONORA EM FREQÜÊNCIA MODULADA",
    "231": "231 - COLETIVO - RADIODIFUSÃO COMUNITÁRIA",
    "247": "247 - COLETIVO - GERADORA DE RADIODIFUSÃO DE SONS E IMAGENS - DIGITAL",
    "248": "248 - COLETIVO - RADIODIFUSÃO DE SONS E IMAGENS",
    "251": "251 - RESTRITO - AUXILIAR RADIODIF.- TRANSMISS. DE PROGRAMAS",
    "252": "252 - RESTRITO - AUXILIAR RADIODIF.- REPORTAGEM EXTERNA",
    "253": "253 - RESTRITO - AUXILIAR RADIODIF.- COM. DE ORDENS INTERNAS",
    "254": "254 - RESTRITO - AUX. DE RADIODIFUSAO - TELECOMANDO",
    "255": "255 - RESTRITO - AUX. DE RADIODIFUSAO - TELEMEDICAO",
    "256": "256 - RESTRITO - AUXILIAR DE RADIODIFUSAO E CORRELATOS",
    "264": "264 - RESTRITO - ESPECIAL CANAL SECUNDARIO DE SONS E IMAGENS",
    "302": "302 - RESTRITO - RADIOAMADOR",
    "400": "400 - RESTRITO - RÁDIO DO CIDADÃO",
    "450": "450 - COLETIVO - COMUNICAÇÃO MULTIMÍDIA - DISPENSA DE AUTORIZAÇÃO",
    "507": "507 - RESTRITO - MÓVEL AERONÁUTICO",
    "604": "604 - RESTRITO - MÓVEL MARÍTIMO",
    "701": "701 - RESTRITO - ESPECIAL DE MUSICA FUNCIONAL",
    "710": "710 - RESTRITO - ESPECIAL EM CANAL SECUNDARIO DE FM",
    "728": "728 - RESTRITO - ESPECIAL DE REPETICAO DE TELEVISAO",
    "729": "729 - COLETIVO - TV A CABO",
    "730": "730 - COLETIVO - ESPECIAL DE REPETICAO DE TV - SATELITE",
    "735": "735 - COLETIVO - DISTRIB. SINAIS TV/AUDIO P/ASSINATURA VIA SATELITE",
    "740": "740 - COLETIVO - ESPEC.DISTRIB.SINAIS MULTIPONTO/MULTICANAL",
    "750": "750 - COLETIVO - SERVIÇO DE ACESSO CONDICIONADO",
    "800": "800 - COLETIVO - RETRANSMISSAO DE T.V.",
    "801": "801 - COLETIVO - RETRANSMISSÃO DE RADIODIFUSÃO DE SONS E IMAGENS - DIGITAL",
    "802": "802 - COLETIVO - PLANO BÁSICO DE RADIODIFUSÃO DE SONS E IMAGENS - DIGITAL",
    "810": "810 - COLETIVO - DISTRIBUICAO DE SINAIS DE TELEVISAO - DISTV",
    "820": "820 - RESTRITO - DE TELEV. EM CIRCUITO FECHADO (RADIOENLACE)",
    "900": "900 - COLETIVO - FUST",
    "901": "901 - COLETIVO - FUNTTEL",
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
    541: "Gerar_Relatorio",
    544: "Relatorio_de_Monitoramento",
    543: "Html",
    596: "Reservar_Instrumentos",
    597: "Reserva_de_Instrumentos",
    598: "Utilizou_algum_instrumento",
}

FIELD2ID = {
    "Tipo_de_Inspecao": 2,
    "Ano": 5,
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
    "Gerar_Relatorio": 541,
    "Relatorio_de_Monitoramento": 544,
    "Html": 543,
    "Reservar_Instrumentos": 596,
    "Reserva_de_Instrumentos": 597,
    "Utilizou_algum_instrumento": 598,
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

TABLECOLS = {
    "NaoLicenciados": "Não Licenciados",
    "NaoLicenciaveis": "Não Licenciáveis",
    "NaoDefinido": "Não Definido",
    "Servico": "Serviço",
    "Classe_Especial": "Classe Especial",
    "Classe_A": "Classe A",
    "Classe_B": "Classe B",
    "Classe_C": "Classe C",
}