class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
        
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = NoArvore(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)
            
    def _inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = NoArvore(valor)
            else:
                self._inserir_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = NoArvore(valor)
            else:
                self._inserir_recursivo(no_atual.direita, valor)
                
    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)
        
    def _buscar_recursivo(self, no_atual, valor):
        if no_atual is None:
            return False
        if no_atual.valor == valor:
            return True
        elif valor < no_atual.valor:
            return self._buscar_recursivo(no_atual.esquerda, valor)
        else:
            return self._buscar_recursivo(no_atual.direita, valor)

def main():
    arvore = ArvoreBinariaBusca()
    arvore.inserir(10)
    arvore.inserir(5)
    arvore.inserir(15)
    print(arvore.buscar(5))
    print(arvore.buscar(12))

if __name__ == '__main__':
    main()
