# Dados_Escolar.py

## Descrição
Um sistema de gerenciamento de notas de alunos que permite adicionar, mostrar, calcular médias, alterar semestres e excluir alunos. O sistema armazena os dados em um arquivo de texto chamado "dicionario.txt" e utiliza um dicionário em Python para armazenar os nomes dos alunos e suas respectivas notas.

## Métodos e Propriedades

- **novoAluno(nome)**:
    - **Descrição:** Função para adicionar um novo aluno ao dicionário de notas.
    - **Parâmetros:**
        - `nome`: Nome do aluno a ser adicionado.

- **arquivo = open("dicionario.txt", "r")**:
    - **Descrição:** Abre o arquivo "dicionario.txt" em modo de leitura.
    - **Método:**
        - `read()`: Lê o conteúdo do arquivo.

- **ast.literal_eval()**:
    - **Descrição:** Função do módulo `ast` que avalia uma expressão Python em formato de string.
    - **Retorno:** Converte o conteúdo do arquivo de texto em um dicionário Python.

- **while True:** 
    - **Descrição:** Loop infinito para manter a execução do programa até que seja interrompido.

- **statistics.mean()**:
    - **Descrição:** Função do módulo `statistics` que calcula a média de um conjunto de números.
    - **Parâmetros:**
        - Lista de notas do aluno.

## Lógica do Código

1. **Inicialização:**
    - O código lê os dados previamente armazenados no arquivo "dicionario.txt" e carrega-os em um dicionário `notas`.

2. **Menu de Opções:**
    - Um menu é exibido para o usuário com opções para adicionar aluno, mostrar notas, alterar semestre, calcular médias, excluir aluno ou sair do programa.

3. **Opções do Menu:**
    #### Adicionar Aluno (Opção 1):
     - **Descrição:** Esta opção permite ao usuário adicionar um novo aluno ao sistema, inserindo o nome do aluno e suas respectivas notas.
     - **Funcionamento:**
        - O usuário fornece o nome do aluno.
        - Em seguida, são solicitadas as notas do aluno, que são adicionadas ao dicionário de notas do sistema.
        - O aluno é registrado no sistema com suas notas associadas.

    #### Mostrar Notas (Opção 2):
    - **Descrição:** Esta opção permite visualizar as notas dos alunos armazenadas no sistema.
    - **Funcionamento:**
        - O usuário pode optar por ver as notas de todos os alunos cadastrados ou inserir o nome de um aluno específico para visualizar suas notas.
        - As notas do aluno são exibidas na saída do sistema.

    #### Alterar Semestre (Opção 3):
    - **Descrição:** Essa opção permite ao usuário alterar o semestre em curso e recalcular as médias ponderadas das notas dos alunos.
    - **Funcionamento:**
        - O usuário informa o novo semestre em que está sendo registrada as notas.
        - O sistema recalcula as médias das notas dos alunos com base na nova ponderação do semestre.
        - As novas médias são exibidas ou atualizadas no sistema.

    #### Calcular Média (Opção 4):
    - **Descrição:** Esta opção permite calcular a média das notas dos alunos, podendo ser feito para todos os alunos cadastrados ou para um aluno específico.
    - **Funcionamento:**
        - O usuário escolhe se deseja calcular a média de todos os alunos ou de um aluno específico.
        - O sistema realiza o cálculo da média das notas de acordo com a ponderação do semestre vigente.
        - A média calculada é exibida na saída do sistema.

    #### Excluir Aluno (Opção 5):
    - **Descrição:** Permite ao usuário excluir um aluno e suas respectivas notas do sistema.
    - **Funcionamento:**
        - O usuário fornece o nome do aluno que deseja excluir.
        - O sistema remove o aluno e suas notas do dicionário de notas.
        - Uma confirmação é exibida ao usuário indicando que o aluno foi removido com sucesso.

    #### Sair (Opção 0):
    - **Descrição:** Encerra o programa de gerenciamento de notas de alunos e salva os dados no arquivo "dicionario.txt".
    - **Funcionamento:**
        - Ao selecionar esta opção, o programa é encerrado.
        - Antes de finalizar, os dados são salvos no arquivo "dicionario.txt" para preservar as informações dos alunos.

## Funcionamento do Código
- Os dados do arquivo "dicionario.txt" são carregados como um dicionário Python.
- O menu interativo permite ao usuário executar diversas operações como adicionar, visualizar, calcular médias, alterar semestre e excluir alunos.
- Ao finalizar, os dados são salvos no arquivo "dicionario.txt" antes de encerrar o programa.

Esta documentação detalhada explica os métodos, propriedades e a lógica por trás do código de gerenciamento de notas de alunos, fornecendo uma visão abrangente de seu funcionamento e capacidades.
