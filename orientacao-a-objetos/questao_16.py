class Fila:
    def __init__(self):
        self.itens = []
        
    def enfileirar(self, item):
        self.itens.append(item)
        
    def desenfileirar(self):
        if not self.esta_vazia():
            return self.itens.pop(0)
        raise IndexError("A fila está vazia")
        
    def esta_vazia(self):
        return len(self.itens) == 0

def main():
    f = Fila()
    f.enfileirar(1)
    f.enfileirar(2)
    print(f.desenfileirar())
    print(f.esta_vazia())
    print(f.desenfileirar())
    print(f.esta_vazia())

if __name__ == '__main__':
    main()
