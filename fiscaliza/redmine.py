# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/redmine.ipynb (unless otherwise specified).

__all__ = ['journal2table', 'value_text_string', 'check_update', 'view_string', 'valida_fiscaliza', 'issue_type',
           'hm2prod', 'validar_dicionario', 'auth_user', 'issue2users', 'insp2acao', 'detalhar_inspecao',
           'atualiza_fiscaliza', 'relatar_inspecao']

# Cell
import json
import re
import logging
import pkg_resources
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Iterable, Union
from redminelib import Redmine
from rich.console import Console
from tabulate import tabulate
from fastcore.test import *
from fastcore.basics import listify, str_enum
from fastcore.script import Param, call_parse, bool_arg
from fastcore.xtras import is_listy
from .constants import *

# Cell
def journal2table(journal):
    """Recebe a string journal, caso a formatação seja compatível com um csv, retorna este formato como markdown
    Do contrário simplesmente retorna a string inalterada"""
    table = [
        [r.strip() for r in j.strip().split(",")]
        for j in journal.split("\n")
        if j.strip() != ""
    ]
    if not len(set([len(t) for t in table])) == 1:
        print("A tabela não possui todas as linhas com o mesmo número de colunas")
        print("As notas serão salvas como texto somente")
        return table
    return tabulate(table[1:], headers=table[0], tablefmt="textile")


def value_text_string(input_value):
    """Formata `input_value` como string json contendo chaves `texto` e `valor` com o mesmo valor de `input_value`"""
    return "{" + '"valor":"{0}","texto":"{0}"'.format(input_value) + "}"


def check_update(
    field: str, value, dtype, values_set: Iterable = None, val_text_string: bool = False
) -> dict:
    """checa se `value` é do tipo `dtype`. Opcionalmente checa se `value` pertence ao conjunto `values_set`
    Opcionalmente formata `value` com a função `value_text_string`
    Returns: Dicionário no formato compatível com a API do Redmine {"id" : ... , "value" : ...}
    """
    if not isinstance(value, dtype):
        raise TypeError(
            f"É esperado que o campo {value} seja do tipo {str}, o fornecido foi {type(value)}"
        )

    if values_set is not None and not set(listify(value)).issubset(set(values_set)):
        raise ValueError(
            f"O valor para {field} : {value} deve pertencer ao conjunto: {values_set}"
        )

    if val_text_string:
        value = value_text_string(value)

    return {"id": FIELD2ID[field], "value": value}


def view_string(s):
    """Recebe uma string formatada como json e retorna somente o valor 'value' da string"""
    try:
        d = json.loads(s)
        return d.get("valor", s)
    except json.JSONDecodeError:
        return s


def valida_fiscaliza(fiscaliza_obj: Redmine) -> None:
    """Checa se `fiscaliza_obj` é do tipo `Redmine`"""
    if not isinstance(fiscaliza_obj, Redmine):
        raise TypeError(
            f"O Objeto Fiscaliza deve ser uma instância autenticada "
            "(logada) da classe Redmine, o typo do objeto fornecido é {type(fiscaliza_obj)}"
        )


def issue_type(insp, fiscaliza):
    """Checa se a Issue de nº `insp` do Redmine é de um dos tipos válidos: `Inspeção | Ação`"""
    if (tipo := fiscaliza.issue.get(insp).tracker["id"]) == 1:
        return "Inspeção"
    elif tipo == 2:
        return "Ação"
    return "Desconhecido"


def hm2prod():
    """Esta função substitui os ids de homologação pelos de produção, quando distintos"""
    global CUSTOM_IDS, FIELD2ID, ID2FIELD
    CUSTOM_IDS = [HM2PROD.get(i, i) for i in CUSTOM_IDS]
    FIELD2ID = {k: HM2PROD.get(v, v) for k, v in FIELD2ID.items()}
    ID2FIELD = {HM2PROD.get(k, k): v for k, v in ID2FIELD.items()}

# Cell
@call_parse
def validar_dicionario(
    data_dict: Param("Dicionário de Dados ou Caminho para o arquivo .json"),
    inspecao: Param("Número da Inspeção a ser relatada", str),
    login: Param("Login Anatel do Usuário", str) = None,
    senha: Param("Senha Utilizada nos Sistemas Interativos da Anatel", str) = None,
    fiscaliza: Param(
        "Objeto Redmine logado, opcional ao login e senha", Redmine
    ) = None,
    teste: Param(
        "Caso verdadeiro o Fiscaliza de Teste ( Homologação ) é utilizado", bool_arg
    ) = True,
    save_path: Param("Caminho para salvar o dicionário formatado", str) = None,
) -> dict:
    """Valida as informações de data_dict e as formata como exigido pela API do Redmine.
    Opcionalmente salva o dicionário serializado como .json caso seja passado um `save_path` válido
    Returns: dicionário com os dados formatados
    """

    keys = list(DICT_FIELDS.keys())
    if not isinstance(data_dict, dict):
        try:
            path = Path(data_dict)
            assert path.exists(), f"O caminho retornado não existe: {path}!"
            assert (
                path.is_file()
            ), f"O caminho retornado {path} não corresponde a um arquivo!"
        except TypeError as e:
            raise e(f"O caminho de arquivo inserido {data_dict} é inválido")
        if path.suffix == ".json":
            data_dict = json.loads(path.read_text())
        else:
            raise TypeError(f"Formato de Arquivo Desconhecido {path.suffix}")

    if not set(data_dict.keys()).issubset(keys):
        raise ValueError(
            f"As chaves seguintes são desconhecidas ou estão com o nome diferente do esperado: \
                         {set(data_dict.keys()).difference(keys)}"
        )

    if not login or not senha:
        assert (
            fiscaliza is not None
        ), "Para logar no Fiscaliza é preciso login e senha ou o objeto fiscaliza"
        valida_fiscaliza(fiscaliza)
    else:
        fiscaliza = auth_user(login, senha, teste)

    issue = fiscaliza.issue.get(inspecao, include=["relations", "attachments"])
    issue_id = issue.id
    date_pattern = "([2]\d{3})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])"
    d = data_dict.copy()
    key = keys[0]
    if classe := d.get(key):
        d[key] = check_update(key, classe, DICT_FIELDS[key], CLASSE, True)

    key = keys[1]
    if tipo := d.get(key):
        d[key] = check_update(key, tipo, DICT_FIELDS[key], TIPO, True)

    key = keys[2]
    if description := d.get(key):
        d[key] = check_update(key, description, DICT_FIELDS[key])

    key = keys[3]
    if fiscal := d.get(key):
        _, name2id = issue2users(issue_id, fiscaliza)
        d[key] = check_update(key, fiscal, DICT_FIELDS[key], name2id.keys())

    key = keys[4]
    if fiscais := d.get(key):
        _, name2id = issue2users(issue_id, fiscaliza)
        fiscais = listify(fiscais)
        d[key] = check_update(key, fiscais, DICT_FIELDS[key], name2id.keys())

    key = keys[5]
    if (html := d.get(key, None)) is not None:
        html = Path(html)
        assert (
            html.exists() and html.is_file()
        ), f"O caminho para o arquivo html informado não existe ou não é um arquivo: {html}"
        criar = keys[6]
        if (relatorio := d.get(criar, None)) is not None:
            d[key] = check_update(key, html.read_text(), str)
            d[criar] = check_update(criar, relatorio, DICT_FIELDS[criar], (0, 1))

    key = keys[7]
    if freq_init := d.get(key):
        d[key] = check_update(key, freq_init, DICT_FIELDS[key])

    key = keys[8]
    if init_unit := d.get(key):
        d[key] = check_update(key, init_unit, DICT_FIELDS[key], ("kHz", "MHz", "GHz"))

    key = keys[9]
    if freq_final := d.get(key):
        d[key] = check_update(key, freq_final, DICT_FIELDS[key])

    key = keys[10]
    if final_unit := d.get(key):
        d[key] = check_update(key, final_unit, DICT_FIELDS[key], ("kHz", "MHz", "GHz"))

    key = keys[11]
    if start_date := d.get(key):
        assert re.match(
            date_pattern, start_date
        ), f"A data informada é inválida {start_date}, informe o formato yyyy-mm-dd"
        d[key] = start_date
    else:
        raise ValueError(f'O campo "Data_de_Inicio" não pode ficar vazio!')

    key = keys[12]
    if due_date := d.get(key):
        assert re.match(
            date_pattern, due_date
        ), f"A data informada é inválida {due_date}, informe o formato yyyy-mm-dd"
        d[key] = due_date
    else:
        raise ValueError(f'O campo "Data_Limite" não poder ficar vazio!')

    key = keys[13]
    if municipio := d.get(key):
        stream = pkg_resources.resource_stream(__name__, "files/municipios.json")
        #stream = Path("files/municipios.json").open()
        municipios = set(json.load(stream))
        municipio = listify(municipio)
        lista_municipios = []
        for m in municipio:
            match = re.match(f'({"|".join(ESTADOS)})/(\w+[\s|\w]+)', m)
            if not match:
                raise ValueError(f"Verifique o formato da string UF/Municipio: {m}")
            lista_municipios.append(
                check_update(key, m, str, municipios, True)["value"]
            )
        d[key] = {"id": FIELD2ID[key], "value": lista_municipios}
        del municipios

    key = keys[14]
    if servicos := d.get(key):
        servicos = listify(servicos)
        lista_servicos = []
        for s in servicos:
            s = SERVICOS[s]
            lista_servicos.append(
                check_update(key, s, str, SERVICOS.values(), True)["value"]
            )
        d[key] = {"id": FIELD2ID[key], "value": lista_servicos}

    key = keys[15]
    if (qnt := d.get(key)) is not None:  # 0 não deve ser interpretado como False
        d[key] = check_update(key, qnt, DICT_FIELDS[key])

    key = keys[16]
    if (nauto := d.get(key)) is not None:
        d[key] = check_update(key, nauto, DICT_FIELDS[key])

    key = keys[17]
    if (hprep := d.get(key)) is not None:
        d[key] = check_update(key, hprep, DICT_FIELDS[key])

    key = keys[18]
    if (hdesl := d.get(key)) is not None:
        d[key] = check_update(key, hdesl, DICT_FIELDS[key])

    key = keys[19]
    if (hexec := d.get(key)) is not None:
        d[key] = check_update(key, hexec, DICT_FIELDS[key])

    key = keys[20]
    if (hconc := d.get(key)) is not None:
        d[key] = check_update(key, hconc, DICT_FIELDS[key])

    key = keys[21]
    if (lat := d.get(key)) is not None:
        max_lat = 5.2666664  # Monte Caburaí RR
        min_lat = -33.7017531  # Arroio Chuy RS
        if not min_lat <= lat <= max_lat:
            raise ValueError(
                f"O valor de latitude inserido está fora dos extremos do Brasil: ({min_lat}, {max_lat})"
            )
        d[key] = check_update(key, lat, DICT_FIELDS[key])

    key = keys[22]
    if long := d.get(key):  # Não pode ser 0
        min_long = -75.3709938
        max_long = -32.423786
        if not min_long <= long <= max_long:
            raise ValueError(
                f"O valor de longitude inserido está fora dos extremos do Brasil: ({min_long}, {max_long})"
            )
        d[key] = check_update(key, long, DICT_FIELDS[key])

    key = keys[23]
    if pf := d.get(key):
        d[key] = check_update(key, pf, DICT_FIELDS[key], PF)

    key = keys[24]
    if risco := d.get(key):
        d[key] = check_update(key, risco, DICT_FIELDS[key], ("Sim", "Não"))

    key = keys[25]
    if online := d.get(key):
        d[key] = check_update(key, online, DICT_FIELDS[key], ("0", "1"))

    key = keys[26]
    if Notes := d.get(key):
        d[key] = journal2table(Notes)

    key = keys[27]
    if entidade := d.get(key):
        # raise NotImplementedError("Não foi implementada a validação de Entidades")
        console.print(
            f":exclamation: Não foi implementada a validação de Entidades, o valor será repassado diretamente para o Fiscaliza :exclamation:"
        )

    key = keys[28]
    if agrup := d.get(key):
        d[key] = check_update(key, agrup, DICT_FIELDS[key])

    key = keys[29]
    if sav := d.get(key):
        d[key] = check_update(key, sav, DICT_FIELDS[key])

    key = keys[30]
    if pcdp := d.get(key):
        d[key] = check_update(key, pcdp, DICT_FIELDS[key])

    key = keys[31]
    if proc := d.get(key):
        d[key] = check_update(key, listify(proc), DICT_FIELDS[key])

    key = keys[32]
    if (reserva := d.get(key)) is not None:
        d[key] = check_update(key, reserva, DICT_FIELDS[key], ("0", "1"))

    key = keys[34]
    if (utilizou := d.get(key)) is not None:
        d[key] = check_update(key, utilizou, DICT_FIELDS[key], ("0", "1"))

    if save_path is not None:
        json.dump(d, Path(save_path).open("w", encoding="utf-8"))

    return d

# Cell
def auth_user(username, password, teste=True, verify=True):
    url = URLHM if teste else URL
    fiscaliza = Redmine(
        url, username=username, password=password, requests={"verify": verify}
    )
    fiscaliza.auth()
    return fiscaliza


def issue2users(insp: str, fiscaliza: Redmine) -> dict:
    """Recebe objeto Redmine `fiscaliza` e string `insp` e retorna um dicionário com os usuários do grupo Inspeção-Execução"""
    valida_fiscaliza(fiscaliza)
    proj = fiscaliza.issue.get(insp).project.name.lower()
    members = fiscaliza.project_membership.filter(project_id=proj)
    id2name = {}
    name2id = {}
    names = []
    for member in members:
        if roles := getattr(member, "roles", []):
            for role in roles:
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


def insp2acao(insp: str, fiscaliza: Redmine) -> dict:
    """Recebe o objeto `fiscaliza` e a string referente à inspeção `insp` e retorna um dicionário resumo da Ação atrelada à inspeção

    Args:
        redmineObj (Redmine): Objeto Redmine autenticado
        insp (str): string com o número da inspeção

    Returns:
        dict: Dicionário com o id, nome e descrição da Ação associada à inspeção
    >>>fiscaliza = Redmine(URL, username=USR, password=PWD)
       fiscaliza.auth()
       detalhar_inspecao(fiscaliza, '51804')
    {'id': 51803,
    'name': 'ACAO_GR01_2021_0456',
    'description': 'Atendimento à Denúncia AC202010213075425 (6104512)'}
    """
    valida_fiscaliza(fiscaliza)
    issue = fiscaliza.issue.get(insp, include=["relations", "attachments"])
    if relations := getattr(issue, "relations", []):
        if relations := getattr(relations, "values", []):
            relations = relations()
    for relation in relations:
        if issue_to_id := relation.get("issue_to_id", None):
            if issue_to_id := fiscaliza.issue.get(issue_to_id):
                if "ACAO" in str(issue_to_id) or (
                    (tracker := getattr(issue_to_id, "tracker", None))
                    and (getattr(tracker, "id", None) == 2)
                ):
                    if (
                        description := getattr(issue_to_id, "custom_fields", None)
                    ) is not None:
                        if description := description.get(ACAO_DESCRIPTION, None):
                            description = getattr(description, "value", "")
                        else:
                            description = ""
                    else:
                        description = ""

                    return {
                        "id_ACAO": getattr(issue_to_id, "id", ""),
                        "nome_ACAO": str(issue_to_id),
                        "descricao_ACAO": description,
                    }
    else:
        return {"id_ACAO": "", "nome_ACAO": "", "descricao_ACAO": ""}


def detalhar_inspecao(
    inspecao: Param("Número da Inspeção a ser relatada", str),
    login: Param("Login Anatel do Usuário", str) = None,
    senha: Param("Senha Utilizada nos Sistemas Interativos da Anatel", str) = None,
    fiscaliza: Param(
        "Objeto Redmine logado, opcional ao login e senha", Redmine
    ) = None,
    teste: Param("Indica se o relato será de teste", bool_arg) = True,
) -> dict:
    """Recebe número da inspeção `inspecao`, o login e senha ou opcionalmente objeto Redmine logado `fiscaliza`
    inspecao: str - Número da Inspeção a ser relatada
    login: str - Login Anatel do Usuário
    senha: str - Senha Utilizada nos Sistemas Interativos da
    fiscaliza: Redmine - Objeto Redmine logado, opcional ao login e senha
    teste: bool - Caso verdadeiro o Fiscaliza de Teste ( Homologação ) é utilizado

    Returns:
        dict: Retorna um dicionário com a Situação Atual e campos preenchidos da Inspeção

    """
    if not login or not senha:
        assert (
            fiscaliza is not None
        ), "Para logar no Fiscaliza é preciso login e senha ou o objeto fiscaliza"
        valida_fiscaliza(fiscaliza)
    else:
        fiscaliza = auth_user(login, senha, teste)

    if not teste:
        hm2prod()

    result = {k: "" for k in FIELDS}
    issue = fiscaliza.issue.get(inspecao, include=["relations", "attachments"])
    result.update({k: str(getattr(issue, k, "")) for k in FIELDS})
    if custom_fields := getattr(issue, "custom_fields", None):
        custom_fields = list(custom_fields)
        for field in custom_fields:
            key = field.id
            result[ID2FIELD.get(key, key)] = getattr(field, "value")
    result.update(insp2acao(inspecao, fiscaliza))
    id2users, users2id = issue2users(inspecao, fiscaliza)
    if value := result["Fiscal_Responsavel"]:
        try:
            result["Fiscal_Responsavel"] = id2users.get(int(value), value)
        except ValueError:
            pass
    if value := result["Fiscais"]:
        try:
            result["Fiscais"] = [id2users.get(int(v), v) for v in result["Fiscais"]]
        except ValueError:
            pass
    users = list(users2id.keys())
    result["Users"] = users
    for f in JSON_FIELDS:
        if (field := result.get(f)) is None:
            result[f] = ''
            continue
        if is_listy(field):
            result[f] = [view_string(s) for s in field]
        else:
            result[f] = view_string(field)

    if journal := list(issue.journals):
        journal = dict(list(issue.journals)[-1])
        key = 'user'
    else:
        journal = dict(issue)
        key = 'author'

    user = journal[key]['name']
    date = datetime.strptime(journal['created_on'], '%Y-%m-%dT%H:%M:%SZ') - timedelta(hours=3)
    result['Modificado'] = f"Atualizado por {user} em {date.date()} às {date.time()}"

    return result

# Cell
def atualiza_fiscaliza(
    insp: str, fields: dict, fiscaliza: Redmine, status: str, Notes=None
):
    """Atualiza a Inspeção `insp` para a Situação `status` com os dados do dicionário `fields`"""
    assert (
        status in STATUS
    ), f"Digite uma das mudanças de lituação válidas: {STATUS.keys()}"
    valida_fiscaliza(fiscaliza)
    issue = fiscaliza.issue.get(insp, include=["relations", "attachments"])
    issue_status = str(getattr(issue, "status", ""))
    if issue_status == status:
        logging.info(f"A inspeção atual já está no status desejado: {status}.")
    custom_fields = [fields.get(field, "") for field in STATUS[status]]
    if status in ("Relatando", "Relatada"):
        start_date = fields.get("Data_de_Inicio", "")
        due_date = fields.get("Data_Limite", "")
    else:
        start_date, due_date = None, None
    Notes = fields.get("Notes") if status == "Relatada" else None
    fiscaliza.issue.update(
        issue.id,
        status_id=SITUACAO[status],
        custom_fields=custom_fields,
        start_date=start_date,
        due_date=due_date,
        Notes=Notes,
    )

# Cell
@call_parse
def relatar_inspecao(
    inspecao: Param("Número da Inspeção a ser relatada", str),
    login: Param("Login Anatel do Usuário", str),
    senha: Param("Senha Utilizada nos Sistemas Interativos da Anatel", str),
    dados: Param("Dicionário já validado com os Dados a serem relatados"),
    teste: Param("Indica se o relato será de teste", bool_arg) = True,
):
    """Relata a inspeção `inspecao` com os dados constantes no dicionário `dados`"""
    console = Console()
    if not isinstance(dados, dict):
        try:
            path = Path(dados)
            assert path.exists(), f"O caminho retornado não existe: {path}!"
            assert (
                path.is_file()
            ), f"O caminho retornado {path} não corresponde a um arquivo!"
        except TypeError as e:
            raise e(f"O caminho de arquivo inserido {dados} é inválido")
        if path.suffix == ".json":
            dados = json.loads(path.read_text())
        else:
            raise TypeError(f"Formato de Arquivo Desconhecido {path.suffix}")

    fiscaliza = auth_user(login, senha, teste)
    if not teste:
        hm2prod()
    console.print("Usuário Autenticado com Sucesso :thumbs_up:", style="bold green")

    if issue_type(inspecao, fiscaliza) == "Ação":
        console.print(
            f":exclamation: O número de inspeção inserido {inspecao} corresponde a uma [bold red]Ação[/bold red] :exclamation:"
        )
        return

    acao = insp2acao(inspecao, fiscaliza)
    console.print(f"Inspeção {inspecao} vinculada à Ação {acao}")

    with console.status("Resgatando Situação Atual da Inspeção...", spinner="pong"):
        status_atual = detalhar_inspecao(
            inspecao=inspecao, fiscaliza=fiscaliza, teste=teste
        )
        console.print(
            f"[bold green]Estado Atual: {status_atual['status']} :exclamation:"
        )

    antes = status_atual["status"]
    lista_status = list(SITUACAO.keys())

    index = lista_status.index(antes) + 1
    if index >= len(lista_status):
        index = len(lista_status) - 1

    for status in lista_status[index:]:
        with console.status(
            f"Atualizando {antes} para {status}",
            spinner="runner",
        ):
            atualiza_fiscaliza(inspecao, dados, fiscaliza, status)
            console.print("Sucesso :sparkles:")

        with console.status("Resgatando Situação Atual da Inspeção...", spinner="pong"):
            status_atual = detalhar_inspecao(inspecao, fiscaliza=fiscaliza)
            console.print(
                f"[bold green]Estado Atual: {status_atual['status']} :exclamation:"
            )

        if antes == "Em andamento" and status == "Relatando":
            console.print(
                f"Assine o Relatorio_de_Monitoramento: {status_atual.get('Relatorio_de_Monitoramento', '')} e chame a função novamente :exclamation:"
            )
            break
        antes = status

    if status_atual["status"] == "Relatada":
        console.print(status_atual)
        console.print("Inspeção Relatada :sunglasses:")

    return status_atual