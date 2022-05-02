# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/info.ipynb (unless otherwise specified).

__all__ = ['insp2acao', 'issue_type', 'utf2ascii', 'detalhar_issue', 'download']

# Cell
import re
from typing import Iterable, Union
from unidecode import unidecode
from datetime import datetime, timedelta
import contextlib
from pathlib import Path
import json


from redminelib import Redmine
from redminelib.exceptions import ResourceAttrError
from fastcore.xtras import is_listy, listify
from fastcore.script import Param, call_parse, bool_arg, store_false, store_true


from .constants import ACAO_DESCRIPTION, KWARGS, IDS, FIELDS, JSON_FIELDS
from .validation import auth_user, valida_fiscaliza, issue2users
from .format import view_string

# Cell
def insp2acao(insp: str, fiscaliza: Redmine) -> dict:
    """Recebe o objeto `fiscaliza` e a string referente à inspeção `insp` e retorna um dicionário resumo da Ação atrelada à inspeção

    Args:
        redmineObj (Redmine): Objeto Redmine autenticado
        insp (str): string com o número da inspeção

    Returns:
        dict: Dicionário com o id, nome e descrição da Ação associada à inspeção

    s"""
    valida_fiscaliza(fiscaliza)
    issue = fiscaliza.issue.get(insp, include=["relations", "attachments"])

    if "INSP" not in str(issue.subject):
        return {}
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
                    ) is None:
                        description = ""

                    elif description := description.get(ACAO_DESCRIPTION, None):
                        description = getattr(description, "value", "")
                    else:
                        description = ""
                    return {
                        "id_ACAO": getattr(issue_to_id, "id", ""),
                        "nome_ACAO": str(issue_to_id),
                        "descricao_ACAO": description,
                    }
    return {"id_ACAO": "", "nome_ACAO": "", "descricao_ACAO": ""}

# Cell
def issue_type(insp, fiscaliza):
    """Checa se a Issue de nº `insp` do Redmine é de um dos tipos válidos: `Inspeção | Ação`"""
    if (tipo := fiscaliza.issue.get(insp).tracker["id"]) == 1:
        return "Inspeção"
    elif tipo == 2:
        return "Ação"
    return "Desconhecido"

# Cell
def utf2ascii(s):
    """Recebe uma string e retorna a mesma em formato ASCII"""
    s = re.sub("[!\"#$%&'()*+\,\-\.\/:;<=>\?@[\\]\^`_\{\|\}~]", "", s)
    return unidecode(s.replace(" ", "_"))


def detalhar_issue(
    issue: str,
    login: str = None,
    senha: str = None,
    fiscaliza: Redmine = None,
    teste: bool = True,
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

    issue_data = {}
    i = fiscaliza.issue.get(issue, include=["relations", "attachments"])

    if (attachments := getattr(i, "attachments")) is not None:
        issue_data["Anexos"] = {d["filename"]: d["content_url"] for d in attachments}

    issue_data |= {k: f'{getattr(i, k, "")}' for k in KWARGS}

    id2field = dict(zip(IDS, FIELDS))

    if custom_fields := listify(getattr(i, "custom_fields", None)):
        for field in custom_fields:
            try:
                issue_data[id2field.get(field.id, utf2ascii(field.name))] = getattr(
                    field, "value", ""
                )
            except ResourceAttrError as e:
                raise ValueError(
                    f"O atributo 'value' não existe na Issue mencionada: key {field.id}, name: {field.name}"
                ) from e

    issue_data |= insp2acao(issue, fiscaliza)
    id2users, users2id = issue2users(issue, fiscaliza)

    if (value := issue_data.get("Fiscal_Responsavel", None)) is not None:
        with contextlib.suppress(ValueError):
            issue_data["Fiscal_Responsavel"] = id2users.get(int(value), value)

    if (value := issue_data.get("Fiscais", None)) is not None:
        with contextlib.suppress(ValueError):
            issue_data["Fiscais"] = [
                id2users.get(int(v), v) for v in issue_data["Fiscais"]
            ]

    users = list(users2id.keys())
    issue_data["Users"] = users

    for f in JSON_FIELDS:
        if (field := issue_data.get(f)) is None:
            issue_data[f] = ""
            continue
        if is_listy(field):
            issue_data[f] = [view_string(s) for s in field]
        else:
            issue_data[f] = view_string(field)

    if journal := list(i.journals):
        journal = dict(journal[-1])
        key = "user"
    else:
        journal = dict(i)
        key = "author"

    user = journal[key]["name"]
    date = datetime.strptime(journal["created_on"], "%Y-%m-%dT%H:%M:%SZ") - timedelta(
        hours=3
    )

    issue_data[
        "Atualizado"
    ] = f"Atualizado por {user} em {datetime.strftime(date, '%d/%m/%Y')} às {date.time()}"

    return issue_data


@call_parse
def download(
    issue: Param("Inspeção na qual o anexo está contido", str),
    login: Param("Login Anatel do Usuário", str),
    senha: Param("Senha Utilizada nos Sistemas Interativos da Anatel", str),
    teste: Param("Indica se o relato será de teste", bool_arg) = True,
    savepath: Param("Pasta onde serão salvos os arquivos", str) = None,
    attach: Param("Indica se os anexos devem ser baixados", bool_arg) = False,
) -> dict:
    """Recebe número da inspeção `inspecao`, o login e senha ou opcionalmente objeto Redmine logado `fiscaliza`
    inspecao: str - Número da Inspeção a ser relatada
    login: str - Login Anatel do Usuário
    senha: str - Senha Utilizada nos Sistemas Interativos da
    fiscaliza: Redmine - Objeto Redmine logado, opcional ao login e senha
    teste: bool - Caso verdadeiro o Fiscaliza de Teste ( Homologação ) é utilizado
    info: bool - Caso verdadeiro, o arquivo .json com os dados da inspeção é baixado
    savepath: str - Caminho para salvar o arquivo .json

    Returns:
        None: Somente salva os arquivos desejados.
    """

    if not login or not senha:
        ValueError("Para logar no Fiscaliza é preciso login e senha")

    fiscaliza = auth_user(login, senha, teste)

    i = fiscaliza.issue.get(issue, include=["relations", "attachments"])

    issue_data = detalhar_issue(issue, fiscaliza=fiscaliza, teste=teste)

    issue_data["Data_de_inicio_efetivo"] = datetime.strftime(
        issue_data["Data_de_inicio_efetivo"], "%d/%m/%Y"
    )
    if not savepath:
        savepath = Path.cwd()
    with open(f"{savepath}/{issue}.json", "w") as f:
        json.dump(issue_data, f, indent=4)

    if attach:
        attachments = getattr(i, "attachments", [])
        for attach in attachments:
            url = getattr(attach, "content_url").replace("http://", "https://")
            fiscaliza.download(
                url,
                savepath=savepath,
                filename=f"{issue}_{attach.id}_{attach.filename}",
            )