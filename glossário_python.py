Este é um glossário focado no que você aprendeu até agora, com especial atenção à manipulação de dados e à sua estrutura de trabalho no Windows.

### 1. Navegação e Ambiente (Terminal/CMD)

Esses comandos são a base para você chegar até os seus dados e preparar o terreno para o Python.

`dir`: Lista todos os arquivos e pastas no diretório atual (Equivalente ao `ls` do Mac/Linux).
`cd <nome>`: Entra em uma pasta específica. Use aspas se o nome tiver espaços, como `cd "Análise de Dados"`.
`cd ..`: Volta para a pasta anterior (sobe um nível na hierarquia).
`mkdir <nome>`: Cria uma nova pasta (diretório) para organizar seus projetos.
`python -m venv venv`: Cria um ambiente virtual (venv) para isolar as bibliotecas do seu projeto.
`venv\Scripts\activate`: Ativa o ambiente virtual no Windows, permitindo que você trabalhe de forma isolada.
`deactivate` ou `path\to\venv\Scripts\deactivate`: Desativa o ambiente virtual atual.

### 2. Fundamentos Básicos (Lógica e Dados)

O essencial para processar informações e interagir com o usuário.

`input()`: Captura dados digitados pelo usuário no terminal.
`int()` / `float()`: Converte textos (strings) em números inteiros ou decimais para cálculos.
`print()`: Exibe informações, resultados ou mensagens no console.
`if` / `else` / `elif`: Estruturas condicionais que decidem qual parte do código executar com base em critérios.
`%` (Módulo)**: Retorna o resto da divisão. Muito usado para identificar números pares (`n % 2 == 0`).
`range(inicio, fim)`: Gera uma sequência de números, útil para repetições controladas.
`for ... in ...`: Laço de repetição que percorre listas ou intervalos de números.

### 3. Estruturas de Dados (Coleções)

Como o Python organiza volumes de dados na memória.

Listas (`[]`): Coleções ordenadas de itens.
`.append()`: Adiciona um item ao final da lista (Lógica de Pilha).
`.insert(posição, item)`: Insere um item em uma posição específica (pode ser usado para Lógica de Fila).
`.remove()`: Exclui um item específico da lista pelo seu valor.


Dicionários (`{}`): Coleções de pares "Chave: Valor", ideais para buscas rápidas.
`dict(lista)`: Tenta converter uma coleção em dicionário (requer pares chave-valor).
`dicionario[chave]`: Acessa o valor associado a uma chave específica.

### 4. POO (Programação Orientada a Objetos)

Conceitos para organizar códigos complexos em "Objetos" que possuem características e ações.

`class NomeDaClasse:`: Define um novo tipo de objeto (como um "molde" para Criar Alunos ou Carros).
`def __init__(self, ...):`: O "Construtor". Define quais dados o objeto terá assim que for criado.
`self`: Refere-se à instância específica do objeto que está sendo manipulada no momento.
Métodos: Funções criadas dentro da classe que representam as ações que o objeto pode realizar.

### 5. Bibliotecas para Dados (Próximos Passos)

Ferramentas que você usará dentro do seu `venv` para análise profissional.

`pip install <nome>`: Instala bibliotecas externas no seu ambiente virtual.
`pandas`: A biblioteca principal para manipulação de tabelas (DataFrames).
`numpy`: Focada em cálculos matemáticos avançados e matrizes numéricas.
`matplotlib`: Utilizada para gerar gráficos a partir dos dados processados.

Este glossário pode ser salvo como um arquivo `.txt` ou `.py` dentro da sua pasta `primeiro_projeto_python` para consulta rápida!