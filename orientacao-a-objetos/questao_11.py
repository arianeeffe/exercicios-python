class Produto:
    def __init__(self, preco):
        self.preco = preco
        
    @property
    def preco(self):
        return self._preco
        
    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("Preço não pode ser negativo")
        self._preco = valor

def main():
    p = Produto(100)
    print(p.preco)
    try:
        p.preco = -10
    except ValueError as e:
        print(f"Erro esperado: {e}")

if __name__ == '__main__':
    main()
