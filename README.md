# Fiscaliza
> Scripts para baixar informações sobre issues ( Ação, Inspeção, Reserva de Instrumentos etc..) no Sistema Fiscaliza da Anatel e atualizar inspeções por meio da API do Redmine.


```python
from nbdev.showdoc import show_doc
from getpass import getuser, getpass
from fiscaliza.redmine import detalhar_inspecao, validar_dicionario, relatar_inspecao
from rich.console import Console
console = Console()
```

## Instalação
Como boa prática é sugerido a criação de um ambiente virtual para encapsular o ambiente python no qual você irá instalar a biblioteca

Utilizando o `conda`:
```bash
conda create -n fiscaliza python=3.8
conda activate fiscaliza
python -m pip install fiscaliza
```
Utilizando somente python:

Windows
```bash
python -m venv <pasta onde criar o ambiente virtual>
<pasta onde criou o ambiente virtual>\Scripts\activate.bat
python -m pip install fiscaliza
```
Linux:
```bash
python -m venv <pasta onde criar o ambiente virtual>
source <pasta onde criou o ambiente virtual>/Scripts/activate
python -m pip install fiscaliza
```

Caso não desejar utilizar um ambiente virtual basta rodar:
`pip install fiscaliza`

## Como utilizar

O `Fiscaliza` da Anatel é um sistema web que utiliza a plataforma Redmine. É basicamente um softaware de gerenciamento e atividades.

O Fiscaliza possui 2 módulos para os fiscais utilizarem:
* Módulo de Teste ( Homologação ) : "https://sistemashm.anatel.gov.br/fiscaliza"
* Módulo de Produção: "https://sistemas.anatel.gov.br/fiscaliza/"

Ambos módulos precisam de um usuário e senha com acesso autorizado, em geral somente servidores da Anatel.

O Escopo desse módulo basicamente está encapsulado em 3 funções básicas:
* detalhar_inspecao - **Retorna as informações do estado atual da Issue ( Inspeção )**
* validar_dicionario - **Para dado dicionário de dados, formata-o para a API do Redmine**
* relatar_inspecao - **Atualiza e Issue com o dicionário de dados passado**

_O escopo da terceira função `relatar_inspecao` possui escopo limitado. Atualmente somente é formatado e relatado Inspeções ( Issue ) to tipo "Uso do Espectro - Monitoração". Essa inspeção é a principal utilizada para as atividades de monitoração da Anatel e foi o que motivou a criação da presente biblioteca. Outras inspeções possuem campos distintos e assim exigem formatação distinta. Versões futuras poderão abarcar o relato de diferentes inspeções._

### Detalhar Inspeção

```python
show_doc(detalhar_inspecao)
```



<h4 id="detalhar_inspecao" class="doc_header"><code>detalhar_inspecao</code><a href="https://github.com/ronaldokun/fiscaliza/tree/master/fiscaliza/redmine.py#L435" class="source_link" style="float:right">[source]</a></h4>
> <code>detalhar_inspecao</code>(**`inspecao`**:"Número da Inspeção a ser relatada", **`login`**:"Login Anatel do Usuário"=*`None`*, **`senha`**:"Senha Utilizada nos Sistemas Interativos da Anatel"=*`None`*, **`fiscaliza`**:"Objeto Redmine logado, opcional ao login e senha"=*`None`*, **`teste`**:"Indica se o relato será de teste"=*`True`*)
Recebe número da inspeção `inspecao`, o login e senha ou opcionalmente objeto Redmine logado `fiscaliza`
inspecao: str - Número da Inspeção a ser relatada
login: str - Login Anatel do Usuário
senha: str - Senha Utilizada nos Sistemas Interativos da
fiscaliza: Redmine - Objeto Redmine logado, opcional ao login e senha
teste: bool - Caso verdadeiro o Fiscaliza de Teste ( Homologação ) é utilizado

Returns:
    dict: Retorna um dicionário com a Situação Atual e campos preenchidos da Inspeção



Vamos exemplificar a Inspeção de Teste `57824`

```python
login = getuser()
senha = getpass()
```

     ··········

```python
inspecao = '57824'
detalhes = detalhar_inspecao(inspecao, login, senha)
console.print(detalhes)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'id'</span>: <span style="color: #008000; text-decoration-color: #008000">'57824'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'subject'</span>: <span style="color: #008000; text-decoration-color: #008000">'INSP_GR01_2021_0518'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'status'</span>: <span style="color: #008000; text-decoration-color: #008000">'Rascunho'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'priority'</span>: <span style="color: #008000; text-decoration-color: #008000">'Normal'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'start_date'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'due_date'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Classe_da_Inspecao'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Tipo_de_Inspecao'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Ano'</span>: <span style="color: #008000; text-decoration-color: #008000">'2021'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Numero_Sei_do_Processo'</span>: <span style="color: #008000; text-decoration-color: #008000">'{"numero"=&gt;"53504.000007/2021-50", "link_acesso"=&gt;"https://sei</span>
<span style="color: #008000; text-decoration-color: #008000">hm.anatel.gov.br/sei/controlador.php?acao=procedimento_trabalhar&amp;id_procedimento=1962455"}'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Descricao_da_Inspecao'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Fiscal_Responsavel'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Fiscais'</span>: <span style="font-weight: bold">[]</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Entidade_da_Inspecao'</span>: <span style="font-weight: bold">[]</span>,
    <span style="color: #008000; text-decoration-color: #008000">'UF_Municipio'</span>: <span style="font-weight: bold">[]</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Servicos_da_Inspecao'</span>: <span style="font-weight: bold">[]</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Horas_de_Preparacao'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Horas_de_Deslocamento'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Horas_de_Execucao'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Horas_de_Conclusao'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'SAV'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'PCDP'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Procedimentos'</span>: <span style="font-weight: bold">[]</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Agrupamento'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'AppFiscaliza'</span>: <span style="color: #008000; text-decoration-color: #008000">'0'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'id_ACAO'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">52876</span>,
    <span style="color: #008000; text-decoration-color: #008000">'nome_ACAO'</span>: <span style="color: #008000; text-decoration-color: #008000">'ACAO_GR01_2021_0491'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'descricao_ACAO'</span>: <span style="color: #008000; text-decoration-color: #008000">'Teste'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Users'</span>: <span style="font-weight: bold">[</span>
        <span style="color: #008000; text-decoration-color: #008000">'Alexandre Elias de Andrade Oliveira'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Alexandre Freitas de Lima'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Alexandre Inacio'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Alexandre Junzo Hamada'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Alfredo de Andrade Filho'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Ananias Pereira'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Antonio Carlos Cardoso de Mello'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Aparecido Sebastiao da Silva'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Arthur Pisaruk'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Carlos Augusto de Carvalho'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Carlos Eduardo Guimaraes Silveira'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Carlos da Paixao Filho'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Celio Yukio Takahashi'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Celso Luiz Maximino'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Diogo Caldeira'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Ediceu Beraldi'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Eduardo Narkevicius'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Elcio Maehara'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Eustaquio Lages Duarte'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Fiscal UD'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Gauber Albuquerque'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Gilson Ponce Ayres Filho'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Helio Lopes de Carvalho Filho'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Higor Paz Melo'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Hugo Santana Lima'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Humberto Barbosa Vinagre'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Jamilson Evangelista'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Joao Yokoyama'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Joaquim Miranda'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'José Antônio S. Sanches'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Julio Cesar de Assis Santos'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Kiyotomo Kawamura'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Laert Calil Junior'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Lannei Vilela Moraes'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Luis Lagomes'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Luiz Vinicios Mielniczuk Seelig'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Marcelo Augusto Scacabarozi'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Marcio Costa'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Marcio Rodrigues Maciel'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Marcos Antônio Rodrigues'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Marcos Juliano Valim da Silva'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Maria Teresa Flosi Garrafa'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Mario Augusto Volpini'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Murilo Amaro'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Osnir Lopes'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Paulo Diogo Costa'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Pedro Arai'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Renato Sadao Kushioyada'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Ricardo Santos Marques'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Ricardo da Silva e Souza'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Roberto Carlos Soares Campos'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Roberto Ferreira dos Santos'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Roberto Takata'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Rodrigo Barbosa de Paula'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Rogerio Zambotto'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Ronaldo da Silva Alves Batista'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Sergio Pereira'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Thiago Silva'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Thomaz Honma Ishida'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Vinicius Paiva de Oliveira'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Vitor Zelada'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Wellington Devechi Piauilino'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Wladimir Senise'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'marcio colazingari'</span>
    <span style="font-weight: bold">]</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Modificado'</span>: <span style="color: #008000; text-decoration-color: #008000">'Atualizado por Ronaldo da Silva Alves Batista em 2021-05-25 às 18:16:42'</span>
<span style="font-weight: bold">}</span>
</pre>

### Validação de Dados e Formatação para submeter à API
A função anterior somente retorna as informações já constantes em dada Inspeção ( Issue ) do Fiscaliza. Para alterarmos ou atualizarmos dada inspeção, precisamos passar um dicionário de dados ou um caminho para um arquivo `.json` onde conste esse dicionário de dados serializado. O exemplo seguinte mostra um dicionário de dados com as informações básicas constantes de uma monitoração e a formatação que elas são validadas:


```python
d = {}

d['Classe_da_Inspecao'] = 'Técnica' # str

d['Tipo_de_Inspecao'] = 'Uso do Espectro - Monitoração' #str

d['Descricao_da_Inspecao'] = '''Atendimento da Denúncia AC202010213075425 (6104512), 
verificação da Potência e Intensidade de Campo Elétrico da Frequência 105.1MHz e seus harmônicos, 
além da checagem de Intermodulação e Espúrios nas frequências 450.3MHz e 750MHz.''' #str

d['Fiscal_Responsavel'] = 'Ronaldo da Silva Alves Batista' #str

d['Fiscais'] = ['Ronaldo da Silva Alves Batista', 'Paulo Diogo Costa', 'Mario Augusto Volpini'] #string ou lista de strings

# Windows
d['Html'] = 'D:\\OneDrive - ANATEL\\Monitoramento\\Processos\\53504.0005432021-55\\Guarulhos.html' #str
          
d['Gerar_Relatorio'] = 1 # int 0 ou 1

d['Frequencia_Inicial']  = 54 #int ou float

d['Unidade_da_Frequencia_Inicial'] = 'MHz' #string

d['Frequencia_Final'] = 700 #int ou float

d['Unidade_da_Frequencia_Final'] = 'MHz' #string

d['start_date'] = '2021-03-19' #YYYY-MM-DD #string nesse formato

d['due_date'] = '2021-12-31'  #YYYY-MM-DD #string nesse formato

d['UF_Municipio'] = "SP/São Paulo" # string ou Lista de Strings: ["SP/São Paulo", "SP/Sorocaba"]

d['Servicos_da_Inspecao'] = ['230', '231', '800'] # String ou Lista de Strings

d['Qnt_de_emissoes_na_faixa'] = 12 # int

d['Emissoes_nao_autorizadas'] = 70 # int

d['Horas_de_Preparacao'] = 2 # int

d['Horas_de_Deslocamento'] = 0 # int

d['Horas_de_Execucao'] = 32 # int

d['Horas_de_Conclusao'] = 6 # int

d['Latitude'] = -22.94694 # float

d['Longitude'] = -43.21944 # float

d['Uso_de_PF'] = 'Não se aplica PF - uso apenas de formulários' # string

d['Acao_de_risco_a_vida_criada'] = 'Não' # string Sim | Não

d['Impossibilidade_acesso_online'] = '0' # string '0' | '1'

d['Reservar_Instrumentos'] = 0 #string '0' = Não | '1' = 'Sim'

d['Utilizou_algum_instrumento'] = 0

d['notes'] = "Não foi constatada irregularidade no Período monitorado" # string

# No caso de uma tabela, string formatada como csv
d['notes'] = """Faixa, Classe Especial, Classe A, Classe B, Classe C
                VHF-L,0,5,7,5
                VHF-H,0,12,1,0
                UHF,1,1,2,4
                FM,5,1,0,0
                RADCOM,0,0,0,0
                Outorgadas com indícios de irregularidades,1,2,3,4
            """
```


A API do Redmine possui formatos específicos de como esses campos devem ser submetidos, validar os formatos acima e fazer essa formatação exigida pela API do Redmine é o papel da função `validar_dicionario`.

```python
show_doc(validar_dicionario)
```

<h4 id="validar_dicionario" class="doc_header"><code>validar_dicionario</code><a href="https://github.com/ronaldokun/fiscaliza/tree/master/fiscaliza/redmine.py#L104" class="source_link" style="float:right">[source]</a></h4>
> <code>validar_dicionario</code>(**`data_dict`**:"Dicionário de Dados ou Caminho para o arquivo .json", **`inspecao`**:"Número da Inspeção a ser relatada", **`login`**:"Login Anatel do Usuário"=*`None`*, **`senha`**:"Senha Utilizada nos Sistemas Interativos da Anatel"=*`None`*, **`fiscaliza`**:"Objeto Redmine logado, opcional ao login e senha"=*`None`*, **`teste`**:"Caso verdadeiro o Fiscaliza de Teste ( Homologação ) é utilizado"=*`True`*, **`save_path`**:"Caminho para salvar o dicionário formatado"=*`None`*)
Valida as informações de data_dict e as formata como exigido pela API do Redmine.
Opcionalmente salva o dicionário serializado como .json caso seja passado um `save_path` válido
Returns: dicionário com os dados formatados


```python
dados = validar_dicionario(d, inspecao, login, senha)
```


```python
for k,v in dados.items():
    if k == "Html":
        v = str(v)
        v = v[:100] + '\n...\n' + v[-100:]
    console.print(f'[blue]{k} [red]-> [green]{v}')
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Classe_da_Inspecao </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">89</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000">'{"valor":"Técnica","texto":"Técnica"}'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Tipo_de_Inspecao </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">2</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000">'{"valor":"Uso do Espectro - Monitoração","texto":"Uso</span>
<span style="color: #008000; text-decoration-color: #008000">do Espectro - Monitoração"}'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Descricao_da_Inspecao </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">22</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000">'Atendimento da Denúncia AC202010213075425 </span>
<span style="color: #008000; text-decoration-color: #008000">(6104512), \nverificação da Potência e Intensidade de Campo Elétrico da Frequência 105.1MHz e</span>
<span style="color: #008000; text-decoration-color: #008000">seus harmônicos, \nalém da checagem de Intermodulação e Espúrios nas frequências 450.3MHz e </span>
<span style="color: #008000; text-decoration-color: #008000">750MHz.'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Fiscal_Responsavel </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">25</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">887</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Fiscais </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">26</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">887</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">607</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">165</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">]}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Html </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">537</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: '&lt;!DOCTYPE html PUBLIC </span><span style="color: #008000; text-decoration-color: #008000">"-//W3C//DTD HTML 4.01//EN"</span><span style="color: #008000; text-decoration-color: #008000"> </span>
<span style="color: #008000; text-decoration-color: #008000">"</span><span style="color: #008000; text-decoration-color: #008000; text-decoration: underline">http://www.w3.org/TR/html4/</span>
<span style="color: #008000; text-decoration-color: #008000">...</span>
<span style="color: #008000; text-decoration-color: #008000">nte do exposto, conclui-se este relat&amp;oacute;rio </span>
<span style="color: #008000; text-decoration-color: #008000">de\n\t\tatividades.\n\t</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&lt;</span><span style="color: #008000; text-decoration-color: #008000">/p</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&gt;</span><span style="color: #008000; text-decoration-color: #008000">\n\n</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&lt;</span><span style="color: #008000; text-decoration-color: #008000">/body</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&gt;</span><span style="color: #008000; text-decoration-color: #008000">\n\n</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&lt;</span><span style="color: #008000; text-decoration-color: #008000">/html</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&gt;</span><span style="color: #008000; text-decoration-color: #008000">'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Gerar_Relatorio </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">534</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">1</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Frequencia_Inicial </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">156</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">54</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Unidade_da_Frequencia_Inicial </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">157</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000">'MHz'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Frequencia_Final </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">158</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">700</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Unidade_da_Frequencia_Final </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">159</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000">'MHz'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">start_date </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">2021</span><span style="color: #008000; text-decoration-color: #008000">-</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">03</span><span style="color: #008000; text-decoration-color: #008000">-</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">19</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">due_date </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">2021</span><span style="color: #008000; text-decoration-color: #008000">-</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">12</span><span style="color: #008000; text-decoration-color: #008000">-</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">31</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">UF_Municipio </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">31</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'{"valor":"SP/São Paulo","texto":"SP/São Paulo"}'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">]}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Servicos_da_Inspecao </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">57</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'{"valor":"230 - COLETIVO - RADIODIFUSÃO SONORA </span>
<span style="color: #008000; text-decoration-color: #008000">EM FREQÜÊNCIA MODULADA","texto":"230 - COLETIVO - RADIODIFUSÃO SONORA EM FREQÜÊNCIA </span>
<span style="color: #008000; text-decoration-color: #008000">MODULADA"}'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'{"valor":"231 - COLETIVO - RADIODIFUSÃO COMUNITÁRIA","texto":"231 - COLETIVO - </span>
<span style="color: #008000; text-decoration-color: #008000">RADIODIFUSÃO COMUNITÁRIA"}'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'{"valor":"800 - COLETIVO - RETRANSMISSAO DE T.V.","texto":"800 </span>
<span style="color: #008000; text-decoration-color: #008000">- COLETIVO - RETRANSMISSAO DE T.V."}'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">]}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Qnt_de_emissoes_na_faixa </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">69</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">12</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Emissoes_nao_autorizadas </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">70</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">70</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Horas_de_Preparacao </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">91</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">2</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Horas_de_Deslocamento </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">92</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">0</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Horas_de_Execucao </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">93</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">32</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Horas_de_Conclusao </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">94</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">6</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Latitude </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">170</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">-22.94694</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Longitude </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">171</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">-43.21944</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Uso_de_PF </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">151</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000">'Não se aplica PF - uso apenas de formulários'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Acao_de_risco_a_vida_criada </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">154</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000">'Não'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Impossibilidade_acesso_online </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">450</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000">'0'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Reservar_Instrumentos </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">658</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">0</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Utilizou_algum_instrumento </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">660</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">0</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">notes </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000">|_.  Faixa                                      |_.   Classe Especial |_.   Classe A</span>
<span style="color: #008000; text-decoration-color: #008000">|_.   Classe B |_.   Classe C |</span>
<span style="color: #008000; text-decoration-color: #008000">|</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&lt;.</span><span style="color: #008000; text-decoration-color: #008000"> VHF-L                                       |</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&gt;</span><span style="color: #008000; text-decoration-color: #008000">.                 </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">0</span><span style="color: #008000; text-decoration-color: #008000"> |&gt;.          </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">5</span><span style="color: #008000; text-decoration-color: #008000"> |&gt;.     </span>
<span style="color: #008000; text-decoration-color: #008000; font-weight: bold">7</span><span style="color: #008000; text-decoration-color: #008000"> |&gt;.          </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">5</span><span style="color: #008000; text-decoration-color: #008000"> |</span>
<span style="color: #008000; text-decoration-color: #008000">|</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&lt;.</span><span style="color: #008000; text-decoration-color: #008000"> VHF-H                                       |</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&gt;</span><span style="color: #008000; text-decoration-color: #008000">.                 </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">0</span><span style="color: #008000; text-decoration-color: #008000"> |&gt;.         </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">12</span><span style="color: #008000; text-decoration-color: #008000"> |&gt;.     </span>
<span style="color: #008000; text-decoration-color: #008000; font-weight: bold">1</span><span style="color: #008000; text-decoration-color: #008000"> |&gt;.          </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">0</span><span style="color: #008000; text-decoration-color: #008000"> |</span>
<span style="color: #008000; text-decoration-color: #008000">|</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&lt;.</span><span style="color: #008000; text-decoration-color: #008000"> UHF                                         |</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&gt;</span><span style="color: #008000; text-decoration-color: #008000">.                 </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">1</span><span style="color: #008000; text-decoration-color: #008000"> |&gt;.          </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">1</span><span style="color: #008000; text-decoration-color: #008000"> |&gt;.     </span>
<span style="color: #008000; text-decoration-color: #008000; font-weight: bold">2</span><span style="color: #008000; text-decoration-color: #008000"> |&gt;.          </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">4</span><span style="color: #008000; text-decoration-color: #008000"> |</span>
<span style="color: #008000; text-decoration-color: #008000">|</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&lt;.</span><span style="color: #008000; text-decoration-color: #008000"> FM                                          |</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&gt;</span><span style="color: #008000; text-decoration-color: #008000">.                 </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">5</span><span style="color: #008000; text-decoration-color: #008000"> |&gt;.          </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">1</span><span style="color: #008000; text-decoration-color: #008000"> |&gt;.     </span>
<span style="color: #008000; text-decoration-color: #008000; font-weight: bold">0</span><span style="color: #008000; text-decoration-color: #008000"> |&gt;.          </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">0</span><span style="color: #008000; text-decoration-color: #008000"> |</span>
<span style="color: #008000; text-decoration-color: #008000">|</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&lt;.</span><span style="color: #008000; text-decoration-color: #008000"> RADCOM                                      |</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&gt;</span><span style="color: #008000; text-decoration-color: #008000">.                 </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">0</span><span style="color: #008000; text-decoration-color: #008000"> |&gt;.          </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">0</span><span style="color: #008000; text-decoration-color: #008000"> |&gt;.     </span>
<span style="color: #008000; text-decoration-color: #008000; font-weight: bold">0</span><span style="color: #008000; text-decoration-color: #008000"> |&gt;.          </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">0</span><span style="color: #008000; text-decoration-color: #008000"> |</span>
<span style="color: #008000; text-decoration-color: #008000">|</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&lt;.</span><span style="color: #008000; text-decoration-color: #008000"> Outorgadas com indícios de irregularidades  |</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&gt;</span><span style="color: #008000; text-decoration-color: #008000">.                 </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">1</span><span style="color: #008000; text-decoration-color: #008000"> |&gt;.          </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">2</span><span style="color: #008000; text-decoration-color: #008000"> |&gt;.     </span>
<span style="color: #008000; text-decoration-color: #008000; font-weight: bold">3</span><span style="color: #008000; text-decoration-color: #008000"> |&gt;.          </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">4</span><span style="color: #008000; text-decoration-color: #008000"> |</span>
</pre>


### Relatar Inspeção
A função a seguir é a mais importante do módulo porque ela de fato altera os dados na plataforma Fiscaliza.

```python
show_doc(relatar_inspecao)
```


<h4 id="relatar_inspecao" class="doc_header"><code>relatar_inspecao</code><a href="https://github.com/ronaldokun/fiscaliza/tree/master/fiscaliza/redmine.py#L540" class="source_link" style="float:right">[source]</a></h4>
> <code>relatar_inspecao</code>(**`inspecao`**:"Número da Inspeção a ser relatada", **`login`**:"Login Anatel do Usuário", **`senha`**:"Senha Utilizada nos Sistemas Interativos da Anatel", **`dados`**:"Dicionário já validado com os Dados a serem relatados", **`teste`**:"Indica se o relato será de teste"=*`True`*)
Relata a inspeção `inspecao` com os dados constantes no dicionário `dados`

```python
relatar_inspecao(login, senha, inspecao, dados=dados, teste=True)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">Usuário Autenticado com Sucesso 👍</span>
</pre>
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Inspeção <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">57824</span> vinculada à Ação <span style="font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id_ACAO'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">52876</span>, <span style="color: #008000; text-decoration-color: #008000">'nome_ACAO'</span>: <span style="color: #008000; text-decoration-color: #008000">'ACAO_GR01_2021_0491'</span>, 
<span style="color: #008000; text-decoration-color: #008000">'descricao_ACAO'</span>: <span style="color: #008000; text-decoration-color: #008000">'Teste'</span><span style="font-weight: bold">}</span>
</pre>
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">Estado Atual: Rascunho ❗</span>
</pre>
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Sucesso ✨
</pre>
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">Estado Atual: Aguardando Execução ❗</span>
</pre>
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Sucesso ✨
</pre>
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">Estado Atual: Em andamento ❗</span>
</pre>
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Sucesso ✨
</pre>
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">Estado Atual: Relatando ❗</span>
</pre>
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">✒ Assine o Relatorio_de_Monitoramento: <span style="font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">"numero"</span>=&gt;<span style="color: #008000; text-decoration-color: #008000">"0190660"</span>, <span style="color: #008000; text-decoration-color: #008000">"link_acesso"</span>=&gt;<span style="color: #008000; text-decoration-color: #008000">"https://seihm.an</span>
<span style="color: #008000; text-decoration-color: #008000">atel.gov.br/sei/controlador.php?acao=procedimento_trabalhar&amp;id_procedimento=1962455&amp;id_docume</span>
<span style="color: #008000; text-decoration-color: #008000">nto=1962947"</span><span style="font-weight: bold">}</span> e chame a função novamente ❗
</pre>
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>
    {'id': '57824',
     'subject': 'INSP_GR01_2021_0518',
     'status': 'Relatando',
     'priority': 'Normal',
     'start_date': '2021-03-19',
     'due_date': '2021-12-31',
     'Classe_da_Inspecao': 'Técnica',
     'Tipo_de_Inspecao': 'Uso do Espectro - Monitoração',
     'Ano': '2021',
     'Numero_Sei_do_Processo': '{"numero"=>"53504.000007/2021-50", "link_acesso"=>"https://seihm.anatel.gov.br/sei/controlador.php?acao=procedimento_trabalhar&id_procedimento=1962455"}',
     'Descricao_da_Inspecao': 'Atendimento da Denúncia AC202010213075425 (6104512), \nverificação da Potência e Intensidade de Campo Elétrico da Frequência 105.1MHz e seus harmônicos, \nalém da checagem de Intermodulação e Espúrios nas frequências 450.3MHz e 750MHz.',
     'Fiscal_Responsavel': 'Ronaldo da Silva Alves Batista',
     'Fiscais': ['Ronaldo da Silva Alves Batista',
      'Paulo Diogo Costa',
      'Mario Augusto Volpini'],
     'Entidade_da_Inspecao': [],
     'UF_Municipio': ['SP/São Paulo'],
     'Servicos_da_Inspecao': ['800 - COLETIVO - RETRANSMISSAO DE T.V.',
      '231 - COLETIVO - RADIODIFUSÃO COMUNITÁRIA',
      '230 - COLETIVO - RADIODIFUSÃO SONORA EM FREQÜÊNCIA MODULADA'],
     'Qnt_de_emissoes_na_faixa': '12',
     'Emissoes_nao_autorizadas': '70',
     'Horas_de_Preparacao': '2',
     'Horas_de_Deslocamento': '0',
     'Horas_de_Execucao': '32',
     'Horas_de_Conclusao': '6',
     'SAV': '',
     'PCDP': '',
     'Procedimentos': [],
     'Latitude': '-22.94694',
     'Longitude': '-43.21944',
     'Uso_de_PF': 'Não se aplica PF - uso apenas de formulários',
     'Acao_de_risco_a_vida_criada': 'Não',
     'Frequencia_Inicial': '54',
     'Unidade_da_Frequencia_Inicial': 'MHz',
     'Frequencia_Final': '700',
     'Unidade_da_Frequencia_Final': 'MHz',
     'Agrupamento': '',
     'AppFiscaliza': '0',
     'Relatorio_de_Monitoramento': '{"numero"=>"0190660", "link_acesso"=>"https://seihm.anatel.gov.br/sei/controlador.php?acao=procedimento_trabalhar&id_procedimento=1962455&id_documento=1962947"}',
     'Reservar_Instrumentos': '0',
     'Utilizou_algum_instrumento': '0',
     'id_ACAO': 52876,
     'nome_ACAO': 'ACAO_GR01_2021_0491',
     'descricao_ACAO': 'Teste',
     'Users': ['Alexandre Elias de Andrade Oliveira',
      'Alexandre Freitas de Lima',
      'Alexandre Inacio',
      'Alexandre Junzo Hamada',
      'Alfredo de Andrade Filho',
      'Ananias Pereira',
      'Antonio Carlos Cardoso de Mello',
      'Aparecido Sebastiao da Silva',
      'Arthur Pisaruk',
      'Carlos Augusto de Carvalho',
      'Carlos Eduardo Guimaraes Silveira',
      'Carlos da Paixao Filho',
      'Celio Yukio Takahashi',
      'Celso Luiz Maximino',
      'Diogo Caldeira',
      'Ediceu Beraldi',
      'Eduardo Narkevicius',
      'Elcio Maehara',
      'Eustaquio Lages Duarte',
      'Fiscal UD',
      'Gauber Albuquerque',
      'Gilson Ponce Ayres Filho',
      'Helio Lopes de Carvalho Filho',
      'Higor Paz Melo',
      'Hugo Santana Lima',
      'Humberto Barbosa Vinagre',
      'Jamilson Evangelista',
      'Joao Yokoyama',
      'Joaquim Miranda',
      'José Antônio S. Sanches',
      'Julio Cesar de Assis Santos',
      'Kiyotomo Kawamura',
      'Laert Calil Junior',
      'Lannei Vilela Moraes',
      'Luis Lagomes',
      'Luiz Vinicios Mielniczuk Seelig',
      'Marcelo Augusto Scacabarozi',
      'Marcio Costa',
      'Marcio Rodrigues Maciel',
      'Marcos Antônio Rodrigues',
      'Marcos Juliano Valim da Silva',
      'Maria Teresa Flosi Garrafa',
      'Mario Augusto Volpini',
      'Murilo Amaro',
      'Osnir Lopes',
      'Paulo Diogo Costa',
      'Pedro Arai',
      'Renato Sadao Kushioyada',
      'Ricardo Santos Marques',
      'Ricardo da Silva e Souza',
      'Roberto Carlos Soares Campos',
      'Roberto Ferreira dos Santos',
      'Roberto Takata',
      'Rodrigo Barbosa de Paula',
      'Rogerio Zambotto',
      'Ronaldo da Silva Alves Batista',
      'Sergio Pereira',
      'Thiago Silva',
      'Thomaz Honma Ishida',
      'Vinicius Paiva de Oliveira',
      'Vitor Zelada',
      'Wellington Devechi Piauilino',
      'Wladimir Senise',
      'marcio colazingari'],
     'Modificado': 'Atualizado por Ronaldo da Silva Alves Batista em 2021-05-25 às 19:01:49'}



O dicionário de dados possui os dados completos obrigatórios para o relato, no entanto o relato é feito em algumas etapas, utilizando somente algumas das informações do dicionário:
* `Rascunho` para `Aguardando Execução`
* `Aguardando Execução` para `Em Andamento`
* `Em Andamento` para `Relatando`
* `Relatando` para `Relatada`

Na terceira etapa é gerado um relatório da monitoração no Sistema Eletrônico de Informações - SEI. Para executar a quarta etapa é preciso que esse relatório da terceira etapa esteja assinado. Por essa razão a função para na terceira etapa e informa da necessidade do relatório estar assinado.

Após o relatório ser assinado basta chamar a função com os mesmos argumentos para que a etapa final seja realizada.


```python
estado = relatar_inspecao(login, senha, inspecao, dados=dados, teste=True)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">Usuário Autenticado com Sucesso 👍</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Inspeção <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">57824</span> vinculada à Ação <span style="font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id_ACAO'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">52876</span>, <span style="color: #008000; text-decoration-color: #008000">'nome_ACAO'</span>: <span style="color: #008000; text-decoration-color: #008000">'ACAO_GR01_2021_0491'</span>, 
<span style="color: #008000; text-decoration-color: #008000">'descricao_ACAO'</span>: <span style="color: #008000; text-decoration-color: #008000">'Teste'</span><span style="font-weight: bold">}</span>
</pre>







<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">Estado Atual: Relatando ❗</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>







<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Sucesso ✨
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>







<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">Estado Atual: Relatada ❗</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Inspeção Relatada 😎
</pre>

Os mesmos passos acima podem ser efetuados no **Fiscaliza** de produção, bastando passar o argumento `teste=False` nas funções acima

```python
inspecao = '51849'
detalhes = detalhar_inspecao(inspecao, login, senha, teste=False)
console.print(detalhes)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'id'</span>: <span style="color: #008000; text-decoration-color: #008000">'51849'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'subject'</span>: <span style="color: #008000; text-decoration-color: #008000">'INSP_GR01_2021_0456'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'status'</span>: <span style="color: #008000; text-decoration-color: #008000">'Rascunho'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'priority'</span>: <span style="color: #008000; text-decoration-color: #008000">'Normal'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'start_date'</span>: <span style="color: #008000; text-decoration-color: #008000">'2021-03-09'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'due_date'</span>: <span style="color: #008000; text-decoration-color: #008000">'2021-06-30'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Classe_da_Inspecao'</span>: <span style="color: #008000; text-decoration-color: #008000">'Técnica'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Tipo_de_Inspecao'</span>: <span style="color: #008000; text-decoration-color: #008000">'Uso do Espectro - Monitoração'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Ano'</span>: <span style="color: #008000; text-decoration-color: #008000">'2021'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Coordenacao'</span>: <span style="color: #008000; text-decoration-color: #008000">'FI3'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Numero_Sei_do_Processo'</span>: <span style="color: #008000; text-decoration-color: #008000">'{"numero"=&gt;"53504.001879/2021-35", "link_acesso"=&gt;"https://sei</span>
<span style="color: #008000; text-decoration-color: #008000">.anatel.gov.br/sei/controlador.php?acao=procedimento_trabalhar&amp;id_procedimento=7542104"}'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Descricao_da_Inspecao'</span>: <span style="color: #008000; text-decoration-color: #008000">'[PMEC 2021] GR01. Etapa 1.'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Fiscal_Responsavel'</span>: <span style="color: #008000; text-decoration-color: #008000">'Arthur Pisaruk'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Fiscais'</span>: <span style="font-weight: bold">[]</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Entidade_da_Inspecao'</span>: <span style="font-weight: bold">[]</span>,
    <span style="color: #008000; text-decoration-color: #008000">'UF_Municipio'</span>: <span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'SP/São Paulo'</span><span style="font-weight: bold">]</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Servicos_da_Inspecao'</span>: <span style="font-weight: bold">[]</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Qnt_de_emissoes_na_faixa'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Emissoes_nao_autorizadas'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Horas_de_Preparacao'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Horas_de_Deslocamento'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Horas_de_Execucao'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Horas_de_Conclusao'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'SAV'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'PCDP'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Procedimentos'</span>: <span style="font-weight: bold">[]</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Latitude'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Longitude'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Uso_de_PF'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Acao_de_risco_a_vida_criada'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Frequencia_Inicial'</span>: <span style="color: #008000; text-decoration-color: #008000">'12.29'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Unidade_da_Frequencia_Inicial'</span>: <span style="color: #008000; text-decoration-color: #008000">'MHz'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Frequencia_Final'</span>: <span style="color: #008000; text-decoration-color: #008000">'5460'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Unidade_da_Frequencia_Final'</span>: <span style="color: #008000; text-decoration-color: #008000">'MHz'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Agrupamento'</span>: <span style="color: #008000; text-decoration-color: #008000">'[PMEC 2021] GR01. Etapa 1.'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'AppFiscaliza'</span>: <span style="color: #008000; text-decoration-color: #008000">'0'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Reservar_Instrumentos'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Utilizou_algum_instrumento'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'id_ACAO'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">47823</span>,
    <span style="color: #008000; text-decoration-color: #008000">'nome_ACAO'</span>: <span style="color: #008000; text-decoration-color: #008000">'ACAO_GR01_2021_0338'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'descricao_ACAO'</span>: <span style="color: #008000; text-decoration-color: #008000">'[PMEC 2021] Monitorar canais e faixas de frequências relacionados às </span>
<span style="color: #008000; text-decoration-color: #008000">aplicações críticas (como, por exemplo, radionavegação e radiocomunicação aeronáutica e </span>
<span style="color: #008000; text-decoration-color: #008000">canais de emergência) na forma a ser estabelecida no Plano de Ação de Fiscalização GR08FI2 </span>
<span style="color: #008000; text-decoration-color: #008000">(SEI nº 6383328).'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Users'</span>: <span style="font-weight: bold">[</span>
        <span style="color: #008000; text-decoration-color: #008000">'Alexandre Elias de Andrade Oliveira'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Alexandre Freitas de Lima'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Alexandre Inacio'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Alexandre Junzo Hamada'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Alfredo de Andrade Filho'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Ananias Pereira'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Antonio Carlos Cardoso de Mello'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Aparecido Sebastiao da Silva'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Arthur Pisaruk'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Carlos Augusto de Carvalho'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Carlos Eduardo Guimaraes Silveira'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Carlos da Paixao Filho'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Celio Yukio Takahashi'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Celso Luiz Maximino'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Diogo Caldeira'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Ediceu Beraldi'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Eduardo Narkevicius'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Elcio Maehara'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Eustaquio Lages Duarte'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Fiscal UD'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Gauber Albuquerque'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Gilson Ponce Ayres Filho'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Helio Lopes de Carvalho Filho'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Higor da Paz Melo'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Hugo Santana Lima'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Humberto Barbosa Vinagre'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Jamilson Evangelista'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Joao Yokoyama'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Joaquim Miranda'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'José Antônio S. Sanches'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Julio Cesar de Assis Santos'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Kiyotomo Kawamura'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Laert Calil Junior'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Lannei Vilela Moraes'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Luis Lagomes'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Luiz Vinicios Mielniczuk Seelig'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Marcelo Augusto Scacabarozi'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Marcelo Vaz Netto'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Marcio Colazingari'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Marcio Costa'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Marcio Rodrigues Maciel'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Marcos Antônio Rodrigues'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Marcos Juliano Valim da Silva'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Maria Teresa Flosi Garrafa'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Mario Augusto Volpini'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Murilo Amaro'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Osnir Lopes'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Paulo Diogo Costa'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Pedro Arai'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Renato Sadao Kushioyada'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Ricardo Santos Marques'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Ricardo da Silva e Souza'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Roberto Carlos Soares Campos'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Roberto Ferreira dos Santos'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Roberto Takata'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Rodrigo Barbosa de Paula'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Rogerio Zambotto'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Ronaldo da Silva Alves Batista'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Sergio Pereira'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Thiago Silva'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Thomaz Honma Ishida'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Vinicius Paiva de Oliveira'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Vitor Zelada'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Wellington Devechi Piauilino'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Wladimir Senise'</span>
    <span style="font-weight: bold">]</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Modificado'</span>: <span style="color: #008000; text-decoration-color: #008000">'Atualizado por Ronaldo da Silva Alves Batista em 2021-05-24 às 13:12:32'</span>
<span style="font-weight: bold">}</span>
</pre>
