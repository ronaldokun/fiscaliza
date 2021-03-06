# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/update.ipynb (unless otherwise specified).

__all__ = ['atualiza_fiscaliza', 'del_attach', 'excluir_relatorio', 'gerar_relatorio', 'relatar_inspecao']

# Cell
import json
from pathlib import Path
from redminelib import Redmine
from rich.console import Console
from rich.progress import track
from fastcore.test import *
from fastcore.script import Param, call_parse, bool_arg
from fastcore.xtras import listify

from .constants import SITUACAO, STATUS, FIELD2ID
from .validation import valida_fiscaliza, validar_dados, auth_user
from .info import detalhar_issue, insp2acao, issue_type, extract_attachments

# Cell
def atualiza_fiscaliza(insp: str, fields: dict, fiscaliza: Redmine, status: str):
    """Atualiza a Inspeção `insp` para a Situação `status` com os dados do dicionário `fields`"""
    assert (
        status in SITUACAO
    ), f"Digite uma das mudanças de situação válidas: {SITUACAO.keys()}"

    fiscaliza = valida_fiscaliza(fiscaliza=fiscaliza)

    issue = fiscaliza.issue.get(insp, include=["relations", "attachments"])

    custom_fields = []
    for field in STATUS[status]:
        if f := fields.get(field, None):
            custom_fields.append(f)
    if not len(custom_fields):
        custom_fields = None
    start_date = fields.get("start_date")
    due_date = fields.get("due_date")
    description = fields.get("description")
    notes = None
    uploads = None
    if status == "Relatando":
        notes = fields.get("notes")
        uploads = fields.get("uploads")
        for journal in issue.journals:
            if notes == getattr(journal, "notes", None):
                notes = None
                break

    kwargs = dict(
        description=description,
        status_id=SITUACAO[status],
        custom_fields=custom_fields,
        start_date=start_date,
        due_date=due_date,
    )

    if notes is not None:
        kwargs["notes"] = notes

    if uploads is not None:
        kwargs["uploads"] = uploads

    kwargs = {k: v for k, v in kwargs.items() if v is not None}

    fiscaliza.issue.update(issue.id, **kwargs)


def del_attach(issue, fiscaliza, filenames="Info.json"):
    filenames = listify(filenames)
    attachments = extract_attachments(issue, fiscaliza=fiscaliza)
    for attach in attachments:
        if attach.filename in filenames:
            attach.delete()


def excluir_relatorio(
    inspecao: str,
    data: dict,
    fiscaliza: Redmine,
    status_atual: dict,
    teste: bool = False,
):  # sourcery skip: hoist-if-from-if
    if status_atual.get("Relatorio_de_Monitoramento"):
        temp = data.copy()
        temp["Gerar_Relatorio"] = {"id": FIELD2ID["Gerar_Relatorio"], "value": 0}
        temp.pop("uploads", None)
        temp["Relatorio_de_Monitoramento"] = {
            "id": FIELD2ID["Relatorio_de_Monitoramento"],
            "value": "",
        }
        temp["Html"] = {"id": FIELD2ID["Html"], "value": ""}
        atualiza_fiscaliza(
            inspecao, temp, fiscaliza, status=status_atual["status"]
        )
        status_atual = detalhar_issue(inspecao, fiscaliza=fiscaliza, teste=teste)
        if status_atual.get("Relatorio_de_Monitoramento"):
            raise ValueError("Não foi possível excluir o Relatório de Monitoramento")


def gerar_relatorio(
    inspecao: str,
    data: dict,
    fiscaliza: Redmine,
    status_atual: dict,
    teste: bool = False,
    substituir_relatorio: bool = False,
):
    """Gera o Relatório da Inspeção `inspecao` caso não existir ou seja substituído"""
    if substituir_relatorio:
        excluir_relatorio(inspecao, data, fiscaliza, status_atual)
    if "Gerar_Relatorio" in data and data["Gerar_Relatorio"]["value"] in (1, "1"):
        del_attach(inspecao, fiscaliza)
    atualiza_fiscaliza(inspecao, data, fiscaliza, status="Relatando")
    return detalhar_issue(inspecao, fiscaliza=fiscaliza, teste=teste)

# Cell
def _parse_data_dict(dados, inspecao, fiscaliza):
    if not isinstance(dados, dict):
        try:
            path = Path(dados)
            assert path.exists(), f"O caminho retornado não existe: {path}!"
            assert (
                path.is_file()
            ), f"O caminho retornado {path} não corresponde a um arquivo!"
        except TypeError as e:
            raise ValueError(f"O caminho de arquivo inserido {dados} é inválido") from e
        if path.suffix != ".json":
            raise TypeError(f"Formato de Arquivo Desconhecido {path.suffix}")
        try:
            dados = json.loads(path.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            dados = json.loads(path.read_text(encoding="cp1252"))

    return validar_dados(
        dados, inspecao, fiscaliza=fiscaliza
    )  # Não altera o dicionário original


@call_parse
def relatar_inspecao(
    inspecao: Param("Número da Inspeção a ser relatada", str),
    login: Param("Login Anatel do Usuário", str),
    senha: Param("Senha Utilizada nos Sistemas Interativos da Anatel", str),
    dados: Param("Dicionário já validado com os Dados a serem relatados"),
    teste: Param("Indica se o relato será de teste", bool_arg) = True,
    parar_em: Param(
        "String indicando até onde o relato deve ser avançado", str
    ) = "Relatada",
    substituir_relatorio: Param(
        "Substituir o relatório criado caso houver?", bool_arg
    ) = False,
):
    """Relata a inspeção `inspecao` com os dados constantes no dicionário `dados`"""
    assert (
        parar_em in SITUACAO.keys()
    ), f"Valor inválido do parâmetro `parar_em`. Forneça um dos valores {SITUACAO.keys()}"

    console = Console()
    fiscaliza = auth_user(login, senha, teste=teste)
    console.print("Usuário Autenticado com Sucesso :thumbs_up:", style="bold green")
    # Deprecate in future
    if not teste:
        FIELD2ID["Qtd_Licenciadas"] = 730
        FIELD2ID["Qtd_Identificadas"] = 731

    data = _parse_data_dict(dados, inspecao, fiscaliza)

    if issue_type(inspecao, fiscaliza) == "Ação":
        console.print(
            f":exclamation: O número de inspeção inserido {inspecao} corresponde a uma [bold red]Ação[/bold red] :exclamation:"
        )
        return

    acao = insp2acao(inspecao, fiscaliza)
    console.print(f"Inspeção {inspecao} vinculada à Ação {acao['id_ACAO']}")

    with console.status("Resgatando Situação Atual da Inspeção...", spinner="pong"):
        status_atual = detalhar_issue(inspecao, fiscaliza=fiscaliza, teste=teste)

    atual = status_atual["status"]

    console.print(f":white_check_mark: [cyan]Estado Atual: [bold green]{atual}")

    lista_status = list(SITUACAO.keys())

    if lista_status.index(atual) > lista_status.index(
        parar_em
    ):  # Não é possível retornar para uma situação anterior
        raise ValueError(
            f"A inspeção está na situação: {atual}. Não é possível retornar para uma situação anterior: {parar_em}."
        )

    index = min(lista_status.index(atual), len(lista_status) - 1)
    lista_status = lista_status[index : lista_status.index(parar_em) + 1]

    console.print(
        f":woman_technologist: [cyan] A inspeção será atualizada até a situação [bold green]{parar_em}"
    )

    for status in track(lista_status, description="Efetuado o relato...", total=len(lista_status)):
        if status == "Relatando":
            status_atual = gerar_relatorio(
                inspecao, data, fiscaliza, status_atual, teste, substituir_relatorio
            )
        else:
            atualiza_fiscaliza(inspecao, data, fiscaliza, status=status)
            status_atual = detalhar_issue(
                inspecao, fiscaliza=fiscaliza, teste=teste
            )
    console.print(
        f":sunglasses: [cyan]Inspeção {inspecao} atualizada para [bold green]{status_atual['status']}"
    )

    return status_atual