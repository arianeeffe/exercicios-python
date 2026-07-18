class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        
    def adicionar(self, valor):
        novo_no = No(valor)
        if self.cabeca is None:
            self.cabeca = novo_no
            return
            
        atual = self.cabeca
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo_no
        
    def to_list(self):
        resultado = []
        atual = self.cabeca
        while atual is not None:
            resultado.append(atual.valor)
            atual = atual.proximo
        return resultado

def main():
    lista = ListaEncadeada()
    lista.adicionar(1)
    lista.adicionar(2)
    lista.adicionar(3)
    print(lista.to_list())

if __name__ == '__main__':
    main()
