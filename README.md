# Fiscaliza
> Scripts para baixar informações sobre inspeções no Sistema Fiscaliza da Anatel e atualizar inspeções por meio da API do Redmine.


```python
%load_ext autoreload
%autoreload 2
%config Completer.use_jedi = False
```

## Instalação

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
{% include note.html content='O escopo da terceira função `relatar_inspecao` possui escopo limitado. Atualmente somente é formatado e relatado Inspeções ( Issue ) to tipo "Uso do Espectro - Monitoração". Essa inspeção é a principal utilizada para as atividades de monitoração da Anatel e foi o que motivou a criação da presente biblioteca. Outras inspeções possuem campos distintos e assim exigem formatação distinta. Versões futuras poderão abarcar o relato de diferentes inspeções. ' %}

Vamos exemplificar a Inspeção de Teste `53689`

```python
login = getuser()
senha = getpass()
inspecao = '57689'
```

     ··········
    

```python
detalhes = detalhar_inspecao(inspecao, login, senha)
```

```python
for k,v in detalhes.items():
    console.print(f'[red]{k} [blue]-> [green]{v}')
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">id </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">57689</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">subject </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span><span style="color: #008000; text-decoration-color: #008000">INSP_GR01_2021_0508</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">status </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span><span style="color: #008000; text-decoration-color: #008000">Rascunho</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">priority </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span><span style="color: #008000; text-decoration-color: #008000">Normal</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">start_date </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">due_date </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">Classe da Inspeção </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">Tipo de inspeção </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">Ano </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">2021</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">Número Sei do Processo </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">"numero"</span><span style="color: #008000; text-decoration-color: #008000">=&gt;</span><span style="color: #008000; text-decoration-color: #008000">"53504.000007/2021-50"</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">"link_acesso"</span><span style="color: #008000; text-decoration-color: #008000">=&gt;</span><span style="color: #008000; text-decoration-color: #008000">"https://seihm.an</span>
<span style="color: #008000; text-decoration-color: #008000">atel.gov.br/sei/controlador.php?acao=procedimento_trabalhar&amp;id_procedimento=1962455"</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">Descrição da Inspeção </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">Fiscal Responsável </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">Fiscais </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">[]</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">Entidade da Inspeção </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">[]</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">UF/Município </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">[]</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">Serviços da Inspeção </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">[]</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">Horas de Preparação </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">Horas de Deslocamento </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">Horas de Execução </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">Horas de Conclusão </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">SAV </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">PCDP </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">Procedimentos </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">[]</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">Agrupamento </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">AppFiscaliza </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">0</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">id_ACAO </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">52876</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">nome_ACAO </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span><span style="color: #008000; text-decoration-color: #008000">ACAO_GR01_2021_0491</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">descrição_ACAO </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span><span style="color: #008000; text-decoration-color: #008000">Teste</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000">Users </span><span style="color: #000080; text-decoration-color: #000080">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'Alexandre Elias de Andrade Oliveira'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Alexandre Freitas de Lima'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Alexandre </span>
<span style="color: #008000; text-decoration-color: #008000">Inacio'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Alexandre Junzo Hamada'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Alfredo de Andrade Filho'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Ananias Pereira'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Antonio </span>
<span style="color: #008000; text-decoration-color: #008000">Carlos Cardoso de Mello'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Aparecido Sebastiao da Silva'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Arthur Pisaruk'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Carlos Augusto </span>
<span style="color: #008000; text-decoration-color: #008000">de Carvalho'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Carlos Eduardo Guimaraes Silveira'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Carlos da Paixao Filho'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Celio Yukio </span>
<span style="color: #008000; text-decoration-color: #008000">Takahashi'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Celso Luiz Maximino'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Diogo Caldeira'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Ediceu Beraldi'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Eduardo Narkevicius'</span><span style="color: #008000; text-decoration-color: #008000">,</span>
<span style="color: #008000; text-decoration-color: #008000">'Elcio Maehara'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Eustaquio Lages Duarte'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Fiscal UD'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Gauber Albuquerque'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Gilson Ponce </span>
<span style="color: #008000; text-decoration-color: #008000">Ayres Filho'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Helio Lopes de Carvalho Filho'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Higor Paz Melo'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Hugo Santana Lima'</span><span style="color: #008000; text-decoration-color: #008000">, </span>
<span style="color: #008000; text-decoration-color: #008000">'Humberto Barbosa Vinagre'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Jamilson Evangelista'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Joao Yokoyama'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Joaquim Miranda'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'José</span>
<span style="color: #008000; text-decoration-color: #008000">Antônio S. Sanches'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Julio Cesar de Assis Santos'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Kiyotomo Kawamura'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Laert Calil </span>
<span style="color: #008000; text-decoration-color: #008000">Junior'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Lannei Vilela Moraes'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Luis Lagomes'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Luiz Vinicios Mielniczuk Seelig'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Marcelo </span>
<span style="color: #008000; text-decoration-color: #008000">Augusto Scacabarozi'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Marcio Costa'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Marcio Rodrigues Maciel'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Marcos Antônio Rodrigues'</span><span style="color: #008000; text-decoration-color: #008000">, </span>
<span style="color: #008000; text-decoration-color: #008000">'Marcos Juliano Valim da Silva'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Maria Teresa Flosi Garrafa'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Mario Augusto Volpini'</span><span style="color: #008000; text-decoration-color: #008000">, </span>
<span style="color: #008000; text-decoration-color: #008000">'Murilo Amaro'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Osnir Lopes'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Paulo Diogo Costa'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Pedro Arai'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Renato Sadao Kushioyada'</span><span style="color: #008000; text-decoration-color: #008000">, </span>
<span style="color: #008000; text-decoration-color: #008000">'Ricardo Santos Marques'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Ricardo da Silva e Souza'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Roberto Carlos Soares Campos'</span><span style="color: #008000; text-decoration-color: #008000">, </span>
<span style="color: #008000; text-decoration-color: #008000">'Roberto Ferreira dos Santos'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Roberto Takata'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Rodrigo Barbosa de Paula'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Rogerio </span>
<span style="color: #008000; text-decoration-color: #008000">Zambotto'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Ronaldo da Silva Alves Batista'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Sergio Pereira'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Thiago Silva'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Thomaz Honma </span>
<span style="color: #008000; text-decoration-color: #008000">Ishida'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Vinicius Paiva de Oliveira'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Vitor Zelada'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Wellington Devechi Piauilino'</span><span style="color: #008000; text-decoration-color: #008000">, </span>
<span style="color: #008000; text-decoration-color: #008000">'Wladimir Senise'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'marcio colazingari'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">]</span>
</pre>



Agora vamos testar o retorno de informações para um Inspeção no Fiscaliza de produção `teste=False`.

```python
inspecao = '51804'
detalhes = detalhar_inspecao(inspecao, login, senha, teste=False)
```

```python
for k,v in detalhes.items():
    console.print(f'[blue]{k} [red]-> [green]{v}')
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">id </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">51804</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">subject </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000">INSP_GR01_2021_0449</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">status </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000">Conferida</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">priority </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000">Normal</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">start_date </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">2020</span><span style="color: #008000; text-decoration-color: #008000">-</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">10</span><span style="color: #008000; text-decoration-color: #008000">-</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">22</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">due_date </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">2021</span><span style="color: #008000; text-decoration-color: #008000">-</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">03</span><span style="color: #008000; text-decoration-color: #008000">-</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">31</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Classe da Inspeção </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000">Técnica</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Tipo de inspeção </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000">Uso do Espectro - Monitoração</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Ano </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">2021</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080; font-weight: bold">178</span><span style="color: #000080; text-decoration-color: #000080"> </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Número Sei do Processo </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">"numero"</span><span style="color: #008000; text-decoration-color: #008000">=&gt;</span><span style="color: #008000; text-decoration-color: #008000">"53504.006733/2020-03"</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">"link_acesso"</span><span style="color: #008000; text-decoration-color: #008000">=&gt;</span><span style="color: #008000; text-decoration-color: #008000">"https://sei.anat</span>
<span style="color: #008000; text-decoration-color: #008000">el.gov.br/sei/controlador.php?acao=procedimento_trabalhar&amp;id_procedimento=6892566"</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Descrição da Inspeção </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000">Atendimento da Denúncia AC202010213075425 </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">6104512</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">)</span><span style="color: #008000; text-decoration-color: #008000">, verificação da </span>
<span style="color: #008000; text-decoration-color: #008000">Potência e Intensidade de Campo Elétrico da Frequência </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">105.</span><span style="color: #008000; text-decoration-color: #008000">1MHz e seus harmônicos, além da </span>
<span style="color: #008000; text-decoration-color: #008000">checagem de Intermodulação e Espúrios nas frequências </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">450.</span><span style="color: #008000; text-decoration-color: #008000">3MHz e 750MHz.</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Fiscal Responsável </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000">Ronaldo da Silva Alves Batista</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Fiscais </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'Ronaldo da Silva Alves Batista'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">]</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Entidade da Inspeção </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'{"valor":"30913990000110","texto":"SISTEMA TRANSRIO DE COMUNICACAO </span>
<span style="color: #008000; text-decoration-color: #008000">LTDA  (30913990000110)"}'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">]</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">UF/Município </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'RJ/Rio de Janeiro'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">]</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Serviços da Inspeção </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'230 - COLETIVO - RADIODIFUSÃO SONORA EM FREQÜÊNCIA MODULADA'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">]</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Qnt. de emissões na faixa </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">1</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Emissões não autorizadas/desc </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">0</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Horas de Preparação </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">2</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Horas de Deslocamento </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">0</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Horas de Execução </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">32</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Horas de Conclusão </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">6</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">SAV </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">PCDP </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Procedimentos </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">[]</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Latitude </span><span style="color: #000080; text-decoration-color: #000080; font-weight: bold">(</span><span style="color: #000080; text-decoration-color: #000080">coordenadas</span><span style="color: #000080; text-decoration-color: #000080; font-weight: bold">)</span><span style="color: #000080; text-decoration-color: #000080"> </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">-22.94694</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Longitude </span><span style="color: #000080; text-decoration-color: #000080; font-weight: bold">(</span><span style="color: #000080; text-decoration-color: #000080">coordenadas</span><span style="color: #000080; text-decoration-color: #000080; font-weight: bold">)</span><span style="color: #000080; text-decoration-color: #000080"> </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">-43.21944</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Uso de PF </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000">Não se aplica PF - uso apenas de formulários</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Ação de risco à vida criada? </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000">Não</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Frequência Inicial </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">105.1</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Unidade da Frequência Inicial </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000">MHz</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Frequência Final </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">750</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Unidade da Frequência Final </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000">MHz</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Agrupamento </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">AppFiscaliza </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">0</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080; font-weight: bold">596</span><span style="color: #000080; text-decoration-color: #000080"> </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080; font-weight: bold">598</span><span style="color: #000080; text-decoration-color: #000080"> </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">id_ACAO </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">51803</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">nome_ACAO </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000">ACAO_GR01_2021_0456</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">descrição_ACAO </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000">Atendimento à Denúncia AC202010213075425 </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">6104512</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">)</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Users </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'Alexandre Elias de Andrade Oliveira'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Alexandre Freitas de Lima'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Alexandre </span>
<span style="color: #008000; text-decoration-color: #008000">Inacio'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Alexandre Junzo Hamada'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Alfredo de Andrade Filho'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Ananias Pereira'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Antonio </span>
<span style="color: #008000; text-decoration-color: #008000">Carlos Cardoso de Mello'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Aparecido Sebastiao da Silva'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Arthur Pisaruk'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Carlos Augusto </span>
<span style="color: #008000; text-decoration-color: #008000">de Carvalho'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Carlos Eduardo Guimaraes Silveira'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Carlos da Paixao Filho'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Celio Yukio </span>
<span style="color: #008000; text-decoration-color: #008000">Takahashi'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Celso Luiz Maximino'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Diogo Caldeira'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Ediceu Beraldi'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Eduardo Narkevicius'</span><span style="color: #008000; text-decoration-color: #008000">,</span>
<span style="color: #008000; text-decoration-color: #008000">'Elcio Maehara'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Eustaquio Lages Duarte'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Fiscal UD'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Gauber Albuquerque'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Gilson Ponce </span>
<span style="color: #008000; text-decoration-color: #008000">Ayres Filho'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Helio Lopes de Carvalho Filho'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Higor da Paz Melo'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Hugo Santana Lima'</span><span style="color: #008000; text-decoration-color: #008000">, </span>
<span style="color: #008000; text-decoration-color: #008000">'Humberto Barbosa Vinagre'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Jamilson Evangelista'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Joao Yokoyama'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Joaquim Miranda'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'José</span>
<span style="color: #008000; text-decoration-color: #008000">Antônio S. Sanches'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Julio Cesar de Assis Santos'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Kiyotomo Kawamura'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Laert Calil </span>
<span style="color: #008000; text-decoration-color: #008000">Junior'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Lannei Vilela Moraes'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Luis Lagomes'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Luiz Vinicios Mielniczuk Seelig'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Marcelo </span>
<span style="color: #008000; text-decoration-color: #008000">Augusto Scacabarozi'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Marcelo Vaz Netto'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Marcio Colazingari'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Marcio Costa'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Marcio </span>
<span style="color: #008000; text-decoration-color: #008000">Rodrigues Maciel'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Marcos Antônio Rodrigues'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Marcos Juliano Valim da Silva'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Maria Teresa</span>
<span style="color: #008000; text-decoration-color: #008000">Flosi Garrafa'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Mario Augusto Volpini'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Murilo Amaro'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Osnir Lopes'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Paulo Diogo Costa'</span><span style="color: #008000; text-decoration-color: #008000">, </span>
<span style="color: #008000; text-decoration-color: #008000">'Pedro Arai'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Renato Sadao Kushioyada'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Ricardo Santos Marques'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Ricardo da Silva e </span>
<span style="color: #008000; text-decoration-color: #008000">Souza'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Roberto Carlos Soares Campos'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Roberto Ferreira dos Santos'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Roberto Takata'</span><span style="color: #008000; text-decoration-color: #008000">, </span>
<span style="color: #008000; text-decoration-color: #008000">'Rodrigo Barbosa de Paula'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Rogerio Zambotto'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Ronaldo da Silva Alves Batista'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Sergio </span>
<span style="color: #008000; text-decoration-color: #008000">Pereira'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Thiago Silva'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Thomaz Honma Ishida'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Vinicius Paiva de Oliveira'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Vitor </span>
<span style="color: #008000; text-decoration-color: #008000">Zelada'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Wellington Devechi Piauilino'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Wladimir Senise'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">]</span>
</pre>



## Dicionário de Dados
A função anterior somente retorna as informações já constantes em dada Inspeção ( Issue ) do Fiscaliza. Para alterarmos ou atualizarmos dada inspeção, precisamos passar um dicionário de dados ou um caminho para um arquivo `.json` ou pickle `.pkl` onde conste esse dicionário de dados serializado. O exemplo seguinte mostra um dicionário de dados com as informações básicas constantes de uma monitoração e a formatação que elas são validadas:

```python
d = {}

d['Classe da Inspeção'] = 'Técnica' # str

d['Tipo de inspeção'] = 'Uso do Espectro - Monitoração' #str

d['Descrição da Inspeção'] = '''Atendimento da Denúncia AC202010213075425 (6104512), 
verificação da Potência e Intensidade de Campo Elétrico da Frequência 105.1MHz e seus harmônicos, 
além da checagem de Intermodulação e Espúrios nas frequências 450.3MHz e 750MHz.''' #str

d['Fiscal Responsável'] = 'Ronaldo da Silva Alves Batista' #str

d['Fiscais'] = ['Ronaldo da Silva Alves Batista', 'Paulo Diogo Costa', 'Mario Augusto Volpini'] #string ou lista de strings

# Windows
d['Html'] = 'D:\\OneDrive - ANATEL\\Monitoramento\\Processos\\53504.0005432021-55\\Guarulhos.html' #str

#ou 

#Unix d['Html'] = '/d/OneDrive - ANATEL/Monitoramento/53504.0005432021-55/Guarulhos.html' #str
            
d['Gerar Relatório'] = 1 # int 0 ou 1

d['Frequência Inicial']  = 54 #int ou float

d['Unidade da Frequência Inicial'] = 'MHz' #string

d['Frequência Final'] = 700 #int ou float

d['Unidade da Frequência Final'] = 'MHz' #string

d['Data de Início'] = '2021-03-19' #YYYY-MM-DD #string nesse formato

d['Data Limite'] = '2021-12-31'  #YYYY-MM-DD #string nesse formato

d['UF/Município'] = "SP/São Paulo" # string ou Lista de Strings: ["SP/São Paulo", "SP/Sorocaba"]

d['Serviços da Inspeção'] = ['230', '231', '800'] # String ou Lista de Strings

d['Qnt. de emissões na faixa'] = 12 # int

d['Emissões não autorizadas/desc'] = 70 # int

d['Horas de Preparação'] = 2 # int

d['Horas de Deslocamento'] = 0 # int

d['Horas de Execução'] = 32 # int

d['Horas de Conclusão'] = 6 # int

d['Latitude (coordenadas)'] = -22.94694 # float

d['Longitude (coordenadas)'] = -43.21944 # float

d['Uso de PF'] = 'Não se aplica PF - uso apenas de formulários' # string

d['Ação de risco à vida criada?'] = 'Não' # string Sim | Não

d['Impossibilidade acesso online?'] = '0' # string '0' | '1'

d['Reservar Instrumentos?'] = '0' #string '0' = Não | '1' = 'Sim'

d['Utilizou algum instrumento?'] = '0'

#d['Reserva de Instrumentos'] = '' 

d['Notes'] = "Não foi constatada irregularidade no Período monitorado" # string

# No caso de uma tabela, string formatada como csv

d['Notes'] = """Faixa, Classe Especial, Classe A, Classe B, Classe C
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
inspecao = '57689'
dados = validar_dicionario('files/data.json', inspecao, login, senha)
```

```python
for k,v in dados.items():
    if k == "Html":
        v = str(v)
        v = v[:100] + '\n...\n' + v[-100:]
    console.print(f'[blue]{k} [red]-> [green]{v}')
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Classe da Inspeção </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">89</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000">'{"valor":"Técnica","texto":"Técnica"}'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Tipo de inspeção </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">2</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000">'{"valor":"Uso do Espectro - Monitoração","texto":"Uso</span>
<span style="color: #008000; text-decoration-color: #008000">do Espectro - Monitoração"}'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Descrição da Inspeção </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">22</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000">'Atendimento da Denúncia AC202010213075425 </span>
<span style="color: #008000; text-decoration-color: #008000">(6104512), \nverificação da Potência e Intensidade de Campo Elétrico da Frequência 105.1MHz e</span>
<span style="color: #008000; text-decoration-color: #008000">seus harmônicos, \nalém da checagem de Intermodulação e Espúrios nas frequências 450.3MHz e </span>
<span style="color: #008000; text-decoration-color: #008000">750MHz.'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Fiscal Responsável </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">25</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000">'Ronaldo da Silva Alves Batista'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Fiscais </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">26</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'Ronaldo da Silva Alves Batista'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Paulo Diogo Costa'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'Mario</span>
<span style="color: #008000; text-decoration-color: #008000">Augusto Volpini'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">]}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Html </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">537</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: '&lt;!DOCTYPE html PUBLIC </span><span style="color: #008000; text-decoration-color: #008000">"-//W3C//DTD HTML 4.01//EN"</span><span style="color: #008000; text-decoration-color: #008000"> </span>
<span style="color: #008000; text-decoration-color: #008000">"</span><span style="color: #008000; text-decoration-color: #008000; text-decoration: underline">http://www.w3.org/TR/html4/</span>
<span style="color: #008000; text-decoration-color: #008000">...</span>
<span style="color: #008000; text-decoration-color: #008000">nte do exposto, conclui-se este relat&amp;oacute;rio </span>
<span style="color: #008000; text-decoration-color: #008000">de\n\t\tatividades.\n\t</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&lt;</span><span style="color: #008000; text-decoration-color: #008000">/p</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&gt;</span><span style="color: #008000; text-decoration-color: #008000">\n\n</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&lt;</span><span style="color: #008000; text-decoration-color: #008000">/body</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&gt;</span><span style="color: #008000; text-decoration-color: #008000">\n\n</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&lt;</span><span style="color: #008000; text-decoration-color: #008000">/html</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">&gt;</span><span style="color: #008000; text-decoration-color: #008000">'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Gerar Relatório </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">534</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">1</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Frequência Inicial </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">156</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">54</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Unidade da Frequência Inicial </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">157</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000">'MHz'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Frequência Final </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">158</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">700</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Unidade da Frequência Final </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">159</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000">'MHz'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Data de Início </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">2021</span><span style="color: #008000; text-decoration-color: #008000">-</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">03</span><span style="color: #008000; text-decoration-color: #008000">-</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">19</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Data Limite </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">2021</span><span style="color: #008000; text-decoration-color: #008000">-</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">12</span><span style="color: #008000; text-decoration-color: #008000">-</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">31</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">UF/Município </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">31</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'{"valor":"SP/São Paulo","texto":"SP/São Paulo"}'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">]}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Serviços da Inspeção </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">57</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'{"valor":"230 - COLETIVO - RADIODIFUSÃO SONORA </span>
<span style="color: #008000; text-decoration-color: #008000">EM FREQÜÊNCIA MODULADA","texto":"230 - COLETIVO - RADIODIFUSÃO SONORA EM FREQÜÊNCIA </span>
<span style="color: #008000; text-decoration-color: #008000">MODULADA"}'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'{"valor":"231 - COLETIVO - RADIODIFUSÃO COMUNITÁRIA","texto":"231 - COLETIVO - </span>
<span style="color: #008000; text-decoration-color: #008000">RADIODIFUSÃO COMUNITÁRIA"}'</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'{"valor":"800 - COLETIVO - RETRANSMISSAO DE T.V.","texto":"800 </span>
<span style="color: #008000; text-decoration-color: #008000">- COLETIVO - RETRANSMISSAO DE T.V."}'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">]}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Qnt. de emissões na faixa </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">69</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">12</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Emissões não autorizadas/desc </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">70</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">70</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Horas de Preparação </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">91</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">2</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Horas de Deslocamento </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">92</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">0</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Horas de Execução </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">93</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">32</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Horas de Conclusão </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">94</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">6</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Latitude </span><span style="color: #000080; text-decoration-color: #000080; font-weight: bold">(</span><span style="color: #000080; text-decoration-color: #000080">coordenadas</span><span style="color: #000080; text-decoration-color: #000080; font-weight: bold">)</span><span style="color: #000080; text-decoration-color: #000080"> </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">170</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">-22.94694</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Longitude </span><span style="color: #000080; text-decoration-color: #000080; font-weight: bold">(</span><span style="color: #000080; text-decoration-color: #000080">coordenadas</span><span style="color: #000080; text-decoration-color: #000080; font-weight: bold">)</span><span style="color: #000080; text-decoration-color: #000080"> </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">171</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">-43.21944</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Uso de PF </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">151</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000">'Não se aplica PF - uso apenas de formulários'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Ação de risco à vida criada? </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">154</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000">'Não'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Impossibilidade acesso online? </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">450</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000">'0'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Reservar Instrumentos? </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">658</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000">'0'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Utilizou algum instrumento? </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">660</span><span style="color: #008000; text-decoration-color: #008000">, </span><span style="color: #008000; text-decoration-color: #008000">'value'</span><span style="color: #008000; text-decoration-color: #008000">: </span><span style="color: #008000; text-decoration-color: #008000">'0'</span><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #000080; text-decoration-color: #000080">Notes </span><span style="color: #800000; text-decoration-color: #800000">-&gt; </span><span style="color: #008000; text-decoration-color: #008000">|_.  Faixa                                      |_.   Classe Especial |_.   Classe A</span>
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



## Relatar Inspeção
A função a seguir é a mais importante do módulo porque ela de fato altera os dados na plataforma Fiscaliza.

```python
inspecao = '57689'
relatar_inspecao(inspecao, login, senha, dados='files/dados.json', teste=True)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">Usuário Autenticado com Sucesso 👍</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Inspeção <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">57689</span> vinculada à Ação <span style="font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id_ACAO'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">52876</span>, <span style="color: #008000; text-decoration-color: #008000">'nome_ACAO'</span>: <span style="color: #008000; text-decoration-color: #008000">'ACAO_GR01_2021_0491'</span>, 
<span style="color: #008000; text-decoration-color: #008000">'descrição_ACAO'</span>: <span style="color: #008000; text-decoration-color: #008000">'Teste'</span><span style="font-weight: bold">}</span>
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




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Sucesso ✨
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">Estado Atual: Relatando ❗</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Assine o Relatório de Monitoramento: <span style="font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">"numero"</span>=&gt;<span style="color: #008000; text-decoration-color: #008000">"0190599"</span>, <span style="color: #008000; text-decoration-color: #008000">"link_acesso"</span>=&gt;<span style="color: #008000; text-decoration-color: #008000">"https://seihm.anat</span>
<span style="color: #008000; text-decoration-color: #008000">el.gov.br/sei/controlador.php?acao=procedimento_trabalhar&amp;id_procedimento=1962455&amp;id_document</span>
<span style="color: #008000; text-decoration-color: #008000">o=1962869"</span><span style="font-weight: bold">}</span> e chame a função novamente ❗
</pre>






    {'id': '57689',
     'subject': 'INSP_GR01_2021_0508',
     'status': 'Relatando',
     'priority': 'Normal',
     'start_date': '2021-03-19',
     'due_date': '2021-12-31',
     'Classe da Inspeção': 'Técnica',
     'Tipo de inspeção': 'Uso do Espectro - Monitoração',
     'Ano': '2021',
     'Número Sei do Processo': '{"numero"=>"53504.000007/2021-50", "link_acesso"=>"https://seihm.anatel.gov.br/sei/controlador.php?acao=procedimento_trabalhar&id_procedimento=1962455"}',
     'Descrição da Inspeção': 'Atendimento da Denúncia AC202010213075425 (6104512), \nverificação da Potência e Intensidade de Campo Elétrico da Frequência 105.1MHz e seus harmônicos, \nalém da checagem de Intermodulação e Espúrios nas frequências 450.3MHz e 750MHz.',
     'Fiscal Responsável': 'Ronaldo da Silva Alves Batista',
     'Fiscais': ['Mario Augusto Volpini',
      'Paulo Diogo Costa',
      'Ronaldo da Silva Alves Batista'],
     'Entidade da Inspeção': [],
     'UF/Município': [],
     'Serviços da Inspeção': [],
     'Qnt. de emissões na faixa': '',
     'Emissões não autorizadas/desc': '',
     'Horas de Preparação': '',
     'Horas de Deslocamento': '',
     'Horas de Execução': '',
     'Horas de Conclusão': '',
     'SAV': '',
     'PCDP': '',
     'Procedimentos': [],
     'Latitude (coordenadas)': '',
     'Longitude (coordenadas)': '',
     'Uso de PF': '',
     'Ação de risco à vida criada?': '',
     'Frequência Inicial': '54',
     'Unidade da Frequência Inicial': 'MHz',
     'Frequência Final': '700',
     'Unidade da Frequência Final': 'MHz',
     'Agrupamento': '',
     'AppFiscaliza': '0',
     'Relatório de Monitoramento': '{"numero"=>"0190599", "link_acesso"=>"https://seihm.anatel.gov.br/sei/controlador.php?acao=procedimento_trabalhar&id_procedimento=1962455&id_documento=1962869"}',
     'Reservar Instrumentos?': '0',
     'Utilizou algum instrumento?': '',
     'id_ACAO': 52876,
     'nome_ACAO': 'ACAO_GR01_2021_0491',
     'descrição_ACAO': 'Teste',
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
      'marcio colazingari']}



O dicionário de dados possui os dados completos obrigatórios para o relato, no entanto o relato é feito em algumas etapas, utilizando somente algumas das informações do dicionário:
* `Rascunho` para `Aguardando Execução`
* `Aguardando Execução` para `Em Andamento`
* `Em Andamento` para `Relatando`
* `Relatando` para `Relatada`

Na terceira etapa é gerado um relatório da monitoração no Sistema Eletrônico de Informações - SEI. Para executar a quarta etapa é preciso que esse relatório da terceira etapa esteja assinado. Por essa razão a função para na terceira etapa e informa da necessidade do relatório estar assinado.

Após o relatório ser assinado basta chamar a função com os mesmos argumentos para que a etapa final seja realizada.

```python
estado = relatar_inspecao(inspecao, login, senha, dados=dados, teste=True)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">Usuário Autenticado com Sucesso 👍</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Inspeção <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">57689</span> vinculada à Ação <span style="font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'id_ACAO'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">52876</span>, <span style="color: #008000; text-decoration-color: #008000">'nome_ACAO'</span>: <span style="color: #008000; text-decoration-color: #008000">'ACAO_GR01_2021_0491'</span>, 
<span style="color: #008000; text-decoration-color: #008000">'descrição_ACAO'</span>: <span style="color: #008000; text-decoration-color: #008000">'Teste'</span><span style="font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008000; text-decoration-color: #008000; font-weight: bold">Estado Atual: Relatando ❗</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Sucesso ✨
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'id'</span>: <span style="color: #008000; text-decoration-color: #008000">'57689'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'subject'</span>: <span style="color: #008000; text-decoration-color: #008000">'INSP_GR01_2021_0508'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'status'</span>: <span style="color: #008000; text-decoration-color: #008000">'Relatada'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'priority'</span>: <span style="color: #008000; text-decoration-color: #008000">'Normal'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'start_date'</span>: <span style="color: #008000; text-decoration-color: #008000">'2021-03-19'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'due_date'</span>: <span style="color: #008000; text-decoration-color: #008000">'2021-12-31'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Classe da Inspeção'</span>: <span style="color: #008000; text-decoration-color: #008000">'Técnica'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Tipo de inspeção'</span>: <span style="color: #008000; text-decoration-color: #008000">'Uso do Espectro - Monitoração'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Ano'</span>: <span style="color: #008000; text-decoration-color: #008000">'2021'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Número Sei do Processo'</span>: <span style="color: #008000; text-decoration-color: #008000">'{"numero"=&gt;"53504.000007/2021-50", "link_acesso"=&gt;"https://sei</span>
<span style="color: #008000; text-decoration-color: #008000">hm.anatel.gov.br/sei/controlador.php?acao=procedimento_trabalhar&amp;id_procedimento=1962455"}'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Descrição da Inspeção'</span>: <span style="color: #008000; text-decoration-color: #008000">'Atendimento da Denúncia AC202010213075425 (6104512), </span>
<span style="color: #008000; text-decoration-color: #008000">\nverificação da Potência e Intensidade de Campo Elétrico da Frequência 105.1MHz e seus </span>
<span style="color: #008000; text-decoration-color: #008000">harmônicos, \nalém da checagem de Intermodulação e Espúrios nas frequências 450.3MHz e </span>
<span style="color: #008000; text-decoration-color: #008000">750MHz.'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Fiscal Responsável'</span>: <span style="color: #008000; text-decoration-color: #008000">'Ronaldo da Silva Alves Batista'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Fiscais'</span>: <span style="font-weight: bold">[</span>
        <span style="color: #008000; text-decoration-color: #008000">'Ronaldo da Silva Alves Batista'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Mario Augusto Volpini'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'Paulo Diogo Costa'</span>
    <span style="font-weight: bold">]</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Entidade da Inspeção'</span>: <span style="font-weight: bold">[]</span>,
    <span style="color: #008000; text-decoration-color: #008000">'UF/Município'</span>: <span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'SP/São Paulo'</span><span style="font-weight: bold">]</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Serviços da Inspeção'</span>: <span style="font-weight: bold">[</span>
        <span style="color: #008000; text-decoration-color: #008000">'800 - COLETIVO - RETRANSMISSAO DE T.V.'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'231 - COLETIVO - RADIODIFUSÃO COMUNITÁRIA'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'230 - COLETIVO - RADIODIFUSÃO SONORA EM FREQÜÊNCIA MODULADA'</span>
    <span style="font-weight: bold">]</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Qnt. de emissões na faixa'</span>: <span style="color: #008000; text-decoration-color: #008000">'12'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Emissões não autorizadas/desc'</span>: <span style="color: #008000; text-decoration-color: #008000">'70'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Horas de Preparação'</span>: <span style="color: #008000; text-decoration-color: #008000">'2'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Horas de Deslocamento'</span>: <span style="color: #008000; text-decoration-color: #008000">'0'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Horas de Execução'</span>: <span style="color: #008000; text-decoration-color: #008000">'32'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Horas de Conclusão'</span>: <span style="color: #008000; text-decoration-color: #008000">'6'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'SAV'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'PCDP'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Procedimentos'</span>: <span style="font-weight: bold">[]</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Latitude (coordenadas)'</span>: <span style="color: #008000; text-decoration-color: #008000">'-22.94694'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Longitude (coordenadas)'</span>: <span style="color: #008000; text-decoration-color: #008000">'-43.21944'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Uso de PF'</span>: <span style="color: #008000; text-decoration-color: #008000">'Não se aplica PF - uso apenas de formulários'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Ação de risco à vida criada?'</span>: <span style="color: #008000; text-decoration-color: #008000">'Não'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Frequência Inicial'</span>: <span style="color: #008000; text-decoration-color: #008000">'54'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Unidade da Frequência Inicial'</span>: <span style="color: #008000; text-decoration-color: #008000">'MHz'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Frequência Final'</span>: <span style="color: #008000; text-decoration-color: #008000">'700'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Unidade da Frequência Final'</span>: <span style="color: #008000; text-decoration-color: #008000">'MHz'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Agrupamento'</span>: <span style="color: #008000; text-decoration-color: #008000">''</span>,
    <span style="color: #008000; text-decoration-color: #008000">'AppFiscaliza'</span>: <span style="color: #008000; text-decoration-color: #008000">'0'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Relatório de Monitoramento'</span>: <span style="color: #008000; text-decoration-color: #008000">'{"numero"=&gt;"0190599", "link_acesso"=&gt;"https://seihm.anatel</span>
<span style="color: #008000; text-decoration-color: #008000">.gov.br/sei/controlador.php?acao=procedimento_trabalhar&amp;id_procedimento=1962455&amp;id_documento=</span>
<span style="color: #008000; text-decoration-color: #008000">1962869"}'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Reservar Instrumentos?'</span>: <span style="color: #008000; text-decoration-color: #008000">'0'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'Utilizou algum instrumento?'</span>: <span style="color: #008000; text-decoration-color: #008000">'0'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'id_ACAO'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">52876</span>,
    <span style="color: #008000; text-decoration-color: #008000">'nome_ACAO'</span>: <span style="color: #008000; text-decoration-color: #008000">'ACAO_GR01_2021_0491'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'descrição_ACAO'</span>: <span style="color: #008000; text-decoration-color: #008000">'Teste'</span>,
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
    <span style="font-weight: bold">]</span>
<span style="font-weight: bold">}</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Inspeção Relatada 😎
</pre>


