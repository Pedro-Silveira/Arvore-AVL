# Árvore Binária AVL

Árvore Binária AVL, desenvolvida para a disciplina de Complexidade de Algoritmos e Análise de Desempenho da Universidade La Salle em Canoas - RS.

### 📋 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:
* Você instalou o interpretador [`Python`](https://www.python.org/);

## ⚙️ Funcionamento

Este código implementa uma Árvore AVL (Árvore de Busca Binária Balanceada) em Python.

### 🔩 Classe NodoAVL()

Essa classe representa um nó na árvore AVL. Cada nó contém uma chave (valor), uma altura, uma referência para o nó à esquerda e uma referência para o nó à direita.

### 🔩 Classe ArvoreAVL()

Essa classe representa a árvore AVL em si. Ela tem um atributo _"raiz"_, que aponta para o nó raiz da árvore ou é _"None"_ se a árvore estiver vazia.

### 🔩 Função _altura(nodo)

Função para obter a altura de um nó da árvore. Se o nó for _"None"_, a altura é 0; caso contrário, é a altura armazenada no próprio nó.

### 🔩 Função _atualizar_altura(nodo)

Função para atualizar a altura de um nó com base nas alturas de seus filhos.

### 🔩 Função _balanco(nodo)

Função para calcular o fator de equilíbrio de um nó, que é a diferença entre a altura da subárvore esquerda e a altura da subárvore direita.

### 🔩 Funções _rodar_esquerda(y) e _rodar_direita(x)

Funções para realizar rotações à esquerda e à direita, respectivamente, em torno de um nó específico na árvore. Essas operações são usadas para reequilibrar a árvore durante as inserções e exclusões.

### 🔩 Função _nodo_balanco(nodo)

Função para verificar e ajustar o equilíbrio de um nó da árvore. Ela chama as funções "**_rodar_esquerda**" e "**_rodar_direita**" quando necessário.

### 🔩 Função inserir(chave)

Função para inserir um valor (chave) na árvore AVL. Ela chama a função "**_inserir_recursivamente**" para realizar a inserção de forma recursiva.

### 🔩 Função _inserir_recursivamente(raiz, chave)

Função interna para inserir uma chave recursivamente na árvore AVL.

### 🔩 Função deletar(chave)

Função para excluir um valor (chave) da árvore AVL. Ela chama a função "**_deletar_recursivamente**" para realizar a exclusão de forma recursiva.

### 🔩 Função _deletar_recursivamente(raiz, chave)

Função para excluir uma chave recursivamente na árvore AVL.

### 🔩 Função _encontrar_chave_min(nodo)

Função para encontrar a chave mínima em uma subárvore (utilizada durante a exclusão).

### 🔩 Função procurar(chave)

Função para procurar uma chave na árvore AVL. Ela chama a função "**_procurar_recursivamente**" para realizar a pesquisa de forma recursiva.

### 🔩 Função _procurar_recursivamente(raiz, chave)

Função para realizar uma pesquisa recursiva por uma chave na árvore AVL.

### 🔩 Função ordenacao_travessia()

Função para realizar uma travessia em ordem na árvore AVL. Ela chama a função "**_ordenacao_recursiva**" para construir uma lista ordenada.

### 🔩 Função _ordenacao_recursiva(raiz, resultado)

Função para realizar uma travessia em ordem recursivamente e construir uma lista ordenada com os valores da árvore.

### 🔩 Função main()

Função principal que permite ao usuário interagir com a árvore AVL. Ela oferece opções para imprimir a árvore, inserir, excluir e pesquisar elementos na árvore até que o usuário escolha sair.
