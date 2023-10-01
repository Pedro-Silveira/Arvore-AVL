class NodoAVL:
    def __init__(self, chave):
        self.chave = chave
        self.altura = 1
        self.esquerda = None
        self.direita = None

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    # Função para obter a altura de um nó
    def _altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    # Função para atualizar a altura de um nó
    def _atualizar_altura(self, nodo):
        if nodo is None:
            return
        nodo.altura = 1 + max(self._altura(nodo.esquerda), self._altura(nodo.direita))

    # Função para calcular o fator de equilíbrio de um nó
    def _balanco(self, nodo):
        if nodo is None:
            return 0
        return self._altura(nodo.esquerda) - self._altura(nodo.direita)

    # Função para rodar um nó para a esquerda
    def _rodar_esquerda(self, y):
        x = y.direita
        T2 = x.esquerda

        x.esquerda = y
        y.direita = T2

        self._atualizar_altura(y)
        self._atualizar_altura(x)

        return x

    # Função para rodar um nó para a direita
    def _rodar_direita(self, x):
        y = x.esquerda
        T2 = y.direita

        y.direita = x
        x.esquerda = T2

        self._atualizar_altura(x)
        self._atualizar_altura(y)

        return y

    # Função para balancear um nó
    def _nodo_balanco(self, nodo):
        balanco = self._balanco(nodo)

        if balanco > 1:
            if self._balanco(nodo.esquerda) < 0:
                nodo.esquerda = self._rodar_esquerda(nodo.esquerda)
            return self._rodar_direita(nodo)

        if balanco < -1:
            if self._balanco(nodo.direita) > 0:
                nodo.direita = self._rodar_direita(nodo.direita)
            return self._rodar_esquerda(nodo)

        return nodo

    # Função para inserir um valor na árvore
    def inserir(self, chave):
        self.raiz = self._inserir_recursivamente(self.raiz, chave)

    # Função para inserir um valor recursivamente
    def _inserir_recursivamente(self, raiz, chave):
        if raiz is None:
            return NodoAVL(chave)

        if chave < raiz.chave:
            raiz.esquerda = self._inserir_recursivamente(raiz.esquerda, chave)
        else:
            raiz.direita = self._inserir_recursivamente(raiz.direita, chave)

        self._atualizar_altura(raiz)
        return self._nodo_balanco(raiz)

    # Função para deletar um valor da árvore
    def deletar(self, chave):
        self.raiz = self._deletar_recursivamente(self.raiz, chave)

    # Função para deletar um valor recursivamente
    def _deletar_recursivamente(self, raiz, chave):
        if raiz is None:
            return raiz

        if chave < raiz.chave:
            raiz.esquerda = self._deletar_recursivamente(raiz.esquerda, chave)
        elif chave > raiz.chave:
            raiz.direita = self._deletar_recursivamente(raiz.direita, chave)
        else:
            if raiz.esquerda is None:
                return raiz.direita
            elif raiz.direita is None:
                return raiz.esquerda

            chave_min = self._encontrar_chave_min(raiz.direita)
            raiz.chave = chave_min
            raiz.direita = self._deletar_recursivamente(raiz.direita, chave_min)

        self._atualizar_altura(raiz)
        return self._nodo_balanco(raiz)

    # Função para encontrar a chave mínima na árvore
    def _encontrar_chave_min(self, nodo):
        while nodo.esquerda is not None:
            nodo = nodo.esquerda
        return nodo.chave

    # Função para procurar um valor na árvore
    def procurar(self, chave):
        return self._procurar_recursivamente(self.raiz, chave)

    # Função para procurar um valor recursivamente
    def _procurar_recursivamente(self, raiz, chave):
        if raiz is None:
            return "não encontrado!"

        if chave == raiz.chave:
            return "encontrado!"
        elif chave < raiz.chave:
            return self._procurar_recursivamente(raiz.esquerda, chave)
        else:
            return self._procurar_recursivamente(raiz.direita, chave)

    # Função para realizar uma travessia em ordem na árvore
    def ordenacao_travessia(self):
        resultado = []
        self._ordenacao_recursiva(self.raiz, resultado)
        return resultado

    # Função para realizar uma travessia em ordem recursivamente
    def _ordenacao_recursiva(self, raiz, resultado):
        if raiz is not None:
            self._ordenacao_recursiva(raiz.esquerda, resultado)
            resultado.append(raiz.chave)
            self._ordenacao_recursiva(raiz.direita, resultado)

# Função principal
def main():
    arvore = ArvoreAVL()
    flag = "0"

    while flag != "5":
        flag = input("\nDigite \"1\" para imprimir a árvore, \"2\" para inserir um elemento, \"3\" para excluir, \"4\" para pesquisar ou \"5\" para sair:\n")

        if flag == "1":
            print("\nÁrvore AVL:", arvore.ordenacao_travessia())
        elif flag == "2":
            arvore.inserir(input("\nDigite o elemento a ser inserido: \n"))
            print("\nÁrvore AVL, após inserção:", arvore.ordenacao_travessia())
        elif flag == "3":
            arvore.deletar(input("\nDigite o elemento a ser excluído: \n"))
            print("\nÁrvore AVL, após exclusão:", arvore.ordenacao_travessia())
        elif flag == "4":
            x = input("\nDigite o elemento a ser pesquisado: \n")
            print("\nResultado da pesquisa do elemento \"", x, "\" na árvore AVL: ", arvore.procurar(x))
        else:
            print("\nObrigado por testar minha implementação de uma Árvore AVL!\n")

if __name__ == "__main__":
    main()
