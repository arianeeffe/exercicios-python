class Pilha:
    def __init__(self):
        self.itens = []
        
    def empilhar(self, item):
        self.itens.append(item)
        
    def desempilhar(self):
        if len(self.itens) > 0:
            return self.itens.pop()
        raise IndexError("A pilha está vazia")
        
    def topo(self):
        if len(self.itens) > 0:
            return self.itens[-1]
        raise IndexError("A pilha está vazia")

def main():
    p = Pilha()
    p.empilhar(10)
    p.empilhar(20)
    print(p.topo())
    print(p.desempilhar())
    print(p.desempilhar())

if __name__ == '__main__':
    main()
