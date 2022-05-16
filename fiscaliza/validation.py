# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/validation.ipynb (unless otherwise specified).

__all__ = ['date_pattern', 'issue2users', 'auth_user', 'valida_fiscaliza', 'parse_dict', 'validar_dados', 'DICT_FIELDS']

# Cell
import re
from typing import Iterable, Union
from pathlib import Path
import json

from redminelib import Redmine
from fastcore.xtras import is_listy, listify
from rich.console import Console

from .constants import *
from .format import check_update, journal2table

date_pattern = re.compile("([2]\d{3})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])")

# Cell
def issue2users(insp: str, fiscaliza: Redmine) -> tuple:
    """Recebe objeto Redmine `fiscaliza` e string `insp` e retorna um dicionário com os usuários do grupo Inspeção-Execução"""
    fiscaliza = valida_fiscaliza(fiscaliza=fiscaliza)
    proj = fiscaliza.issue.get(insp).project.name.lower()
    members = fiscaliza.project_membership.filter(project_id=proj)
    id2name = {}
    name2id = {}
    names = []
    for member in members:
        for role in getattr(member, "roles", []):
            if str(role) == "Inspeção-Execução":
                if user := getattr(member, "user", None):
                    if (id_ := getattr(user, "id", None)) and (
                        name := getattr(user, "name", None)
                    ):
                        names.append((id_, name))

    names.sort(key=lambda x: x[1])
    id2name = dict(names)
    name2id = {v: k for k, v in id2name.items()}
    return id2name, name2id

# Cell
def auth_user(username=None, password=None, api=None, teste=True):
    """Autentica o usuário e retorna um objeto Redmine logado"""
    url = URLHM if teste else URL
    fiscaliza = Redmine(
        url, key=api, username=username, password=password, requests={"verify": True}
    )
    try:
        fiscaliza.auth()
        return fiscaliza

    except ConnectionError:
        Console().print(
            "[bold red] Sem resposta do Servidor. Verifique: Conexão com a Internet | VPN  | Fiscaliza fora do ar"
        )


def valida_fiscaliza(
    login: str = None,
    senha: str = None,
    api: str = None,
    fiscaliza: Redmine = None,
    teste: bool = True,
) -> Redmine:
    """Checa se `fiscaliza` é um objeto do tipo `Redmine` ou autentica o usuário e retorna um objeto Redmine"""
    if isinstance(fiscaliza, Redmine):
        return fiscaliza
    if api is not None:
        return auth_user(api=api, teste=teste)
    if login and senha:
        return auth_user(username=login, password=senha, teste=teste)
    raise ValueError(
        "Não foi fornecida uma das 3 opções: Chave api | login e senha | objeto Redmine"
    )


def parse_dict(data_dict: Union[dict, str, Path]) -> dict:
    if not isinstance(data_dict, dict):
        try:
            path = Path(data_dict)
            assert path.exists(), f"O caminho retornado não existe: {path}!"
            assert (
                path.is_file()
            ), f"O caminho retornado {path} não corresponde a um arquivo!"
        except TypeError as e:
            raise ValueError(
                f"O caminho de arquivo inserido {data_dict} é inválido"
            ) from e
        if path.suffix != ".json":
            raise TypeError(f"Formato de Arquivo Desconhecido {path.suffix}")
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            return json.loads(path.read_text(encoding="cp1252"))

    return data_dict.copy()


def _validar_relatorio(dados, key="Gerar_Relatorio"):
    """Valida se o arquivo do relatório existe e está legível"""
    if (relatorio := dados.get(key)) in (1, "1"):
        if (html := dados.get("Html")) is None:
            raise ValueError(
                f"Foi solicitado a criação de um relatório no entanto o arquivo html não é válido: {html}"
            )
        html = Path(html)
        if not html.exists():
            raise ValueError(f"Arquivo {html} não existe")
        if not html.is_file():
            raise ValueError(f"Arquivo {html} não é um arquivo")
        try:
            html_text = html.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            html_text = html.read_text(encoding="cp1252")
        dados["Html"] = check_update("Html", html_text, DICT_FIELDS["Html"]["type"])
    dados[key] = check_update(
        key,
        relatorio,
        DICT_FIELDS[key].get("type"),
        DICT_FIELDS[key].get("set"),
        DICT_FIELDS[key].get("format"),
    )


def _validar_data(dados, key):
    """Valida se as datas são válidas"""
    assert re.match(
        date_pattern, dados[key]
    ), f"A data informada é inválida {dados[key]}, informe o formato yyyy-mm-dd"


def _validar_uf_municipio(dados, key):
    if municipio := dados.get(key):
        municipio = listify(municipio)
        lista_municipios = []
        for m in municipio:
            match = re.match(f'({"|".join(ESTADOS)})/(\w+[\s|\w]+)', m)
            if not match:
                raise ValueError(f"Verifique o formato da string UF/Municipio: {m}")
            lista_municipios.append(
                check_update(
                    key,
                    m,
                    DICT_FIELDS[key]["type"],
                    DICT_FIELDS[key]["set"],
                    DICT_FIELDS[key]["format"],
                )["value"]
            )
        dados[key] = {"id": FIELD2ID[key], "value": lista_municipios}


def _validar_servico(dados, key):
    if servicos := dados.get(key):
        servicos = listify(servicos)
        lista_servicos = []
        for s in servicos:
            s = SERVICOS[s]
            lista_servicos.append(
                check_update(
                    key,
                    s,
                    DICT_FIELDS[key]["type"],
                    DICT_FIELDS[key]["set"],
                    DICT_FIELDS[key]["format"],
                )["value"]
            )
        dados[key] = {"id": FIELD2ID[key], "value": lista_servicos}


def _validar_coordenadas(dados, key):
    if key == "Latitude":
        max_coord = 5.2666664  # Monte Caburaí RR
        min_coord = -33.7017531  # Arroio Chuy RS
    elif key == "Longitude":
        min_coord = -75.3709938
        max_coord = -32.423786
    if (coord := dados.get(key, "")) != "":
        if not min_coord <= coord <= max_coord:
            raise ValueError(
                f"O valor de coordenada {key} inserido está fora dos extremos do Brasil: ({min_coord}, {max_coord})"
            )
        try:
            coord = float(coord)
        except ValueError as e:
            raise ValueError(
                f"O valor de coordenada {key} inserido não é um número: {coord}"
            ) from e

    dados[key] = coord


def _validar_notas(dados, key):
    if notes := dados.get(key):
        dados[key] = (
            "\n".join(journal2table(note) for note in notes)
            if is_listy(notes)
            else notes
        )


def _validar_anexos(dados, key):
    if (anexos := dados.get(key)) is None:
        return
    dados[key] = []
    if not is_listy(anexos):
        anexos = [anexos]
    for item in anexos:
        if not isinstance(item, dict):
            raise TypeError(
                f"Para cada item da chave {key} é esperado um dicionário, foi retornado {type(item)}"
            )
        if not {"path", "filename"}.issubset(item.keys()):
            raise ValueError(
                "É obrigatório que cada dicionário de anexos contenha no mínimo as chaves path e filename!"
            )

        dados[key].append(item)


def validar_dados(
    data_dict: Union[dict, Path, str],
    inspecao: Union[int, str],
    login: str = None,
    senha: str = None,
    fiscaliza: Redmine = None,
    teste: bool = True,
) -> dict:
    """Valida as informações de data_dict e as formata como exigido pela API do Redmine.
    Returns: dicionário com os dados formatados
    """

    dados = parse_dict(data_dict)

    if not set(dados.keys()).issubset(DICT_FIELDS.keys()):
        raise ValueError(
            f"As chaves seguintes são desconhecidas ou estão com o nome diferente do esperado: \
                         {set(dados.keys()).difference(DICT_FIELDS.keys())}"
        )

    if not login or not senha:
        assert (
            fiscaliza is not None
        ), "Para logar no Fiscaliza é preciso login e senha ou o objeto fiscaliza"

        fiscaliza = valida_fiscaliza(fiscaliza=fiscaliza)
    else:
        fiscaliza = auth_user(login, senha, teste)

    issue = fiscaliza.issue.get(inspecao, include=["relations", "attachments"])
    dados = {k: v for k, v in dados.items() if k in DICT_FIELDS.keys()}
    _, name2id = issue2users(issue.id, fiscaliza)

    cache_dict = dados.copy()

    for key in KWARGS[-3:]:
        if key not in dados:
            raise ValueError(f"O campo {key} não pode ficar vazio")
        cache_dict.pop(key, None)

    cache_dict.pop("Html", None)

    key = "Fiscal_Responsavel"
    if fiscal := cache_dict.pop(key, None):
        fiscal = check_update(
            key,
            fiscal,
            DICT_FIELDS[key].get("type"),
            name2id.keys(),
            DICT_FIELDS[key].get("format"),
        )
        fiscal["value"] = name2id[fiscal["value"]]
        dados[key] = fiscal

    key = "Fiscais"
    if fiscais := listify(cache_dict.pop(key, None)):
        fiscais = check_update(
            key,
            fiscais,
            DICT_FIELDS[key].get("type"),
            name2id.keys(),
            DICT_FIELDS[key].get("format"),
        )
        dados[key] = fiscais
        dados[key]["value"] = [name2id[v] for v in fiscais["value"]]

    for key, value in cache_dict.items():  # O Dicionário original é alterado no loop
        if custom := DICT_FIELDS[key].get("custom"):
            custom(dados, key)
        else:
            dados[key] = check_update(
                key,
                value,
                DICT_FIELDS[key].get("type"),
                DICT_FIELDS[key].get("set"),
                DICT_FIELDS[key].get("format"),
            )

    dados["Coordenadas_Geograficas"] = {
        "id": 717,
        "value": '{"latitude"=>"'
        + str(dados.get("Latitude", ""))
        + '", "longitude"=>"'
        + str(dados.get("Longitude", ""))
        + '"}',
    }
    dados.pop("Latitude", None)
    dados.pop("Longitude", None)

    return dados


DICT_FIELDS = {
    "Classe_da_Inspecao": {"type": str, "set": CLASSE, "format": True},
    "Tipo_de_Inspecao": {"type": str, "set": TIPO, "format": True},
    "description": {"type": str},
    "Fiscal_Responsavel": {"type": str},
    "Fiscais": {"type": Iterable},
    "Html": {"type": str},
    "Gerar_Relatorio": {
        "type": (int, str),
        "set": (0, "0", 1, "1"),
        "custom": _validar_relatorio,
    },
    "Frequencia_Inicial": {"type": (int, float)},
    "Unidade_da_Frequencia_Inicial": {"type": str, "set": ("kHz", "MHz", "GHz")},
    "Frequencia_Final": {"type": (int, float)},
    "Unidade_da_Frequencia_Final": {"type": str, "set": ("kHz", "MHz", "GHz")},
    "start_date": {"type": str, "custom": _validar_data},
    "due_date": {"type": str, "custom": _validar_data},
    "UF_Municipio": {
        "type": str,
        "custom": _validar_uf_municipio,
        "set": MUNICIPIOS,
        "format": True,
    },
    "Servicos_da_Inspecao": {
        "type": (str, list),
        "custom": _validar_servico,
        "set": SERVICOS.values(),
        "format": True,
    },
    "Qtd_Emissoes": {"type": int},
    "Emissoes_nao_autorizadas": {"type": int},
    "Horas_de_Preparacao": {"type": int},
    "Horas_de_Deslocamento": {"type": int},
    "Horas_de_Execucao": {"type": int},
    "Horas_de_Conclusao": {"type": int},
    "Latitude": {"type": float, "custom": _validar_coordenadas},
    "Longitude": {"type": float, "custom": _validar_coordenadas},
    "Uso_de_PF": {"type": str, "set": PF},
    "Acao_de_risco_a_vida_criada": {"type": str, "set": ("Sim", "Não")},
    "Impossibilidade_acesso_online": {"type": str, "set": ("1", "0")},
    "notes": {"type": str, "custom": _validar_notas},
    "Entidade_da_Inspecao": {"type": str},
    "Agrupamento": {"type": int},
    "SAV": {"type": str},
    "PCDP": {"type": str},
    "Procedimentos": {"type": list},
    "Reservar_Instrumentos": {"type": (int, str), "set": (0, 1, "0", "1")},
    "Utilizou_algum_instrumento": {"type": (int, str), "set": (0, 1, "0", "1")},
    "uploads": {"type": list, "custom": _validar_anexos},
    "Relatorio_de_Monitoramento": {"type": (str, int)},
    "Qtd_Licenciadas": {"type": int},
    "Qtd_Identificadas": {"type": int},
    "Coordenadas_Geograficas": {"type": str},
}