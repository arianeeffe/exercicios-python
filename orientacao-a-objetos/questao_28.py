class Contagem:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        self.atual = inicio
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.atual <= self.fim:
            valor = self.atual
            self.atual += 1
            return valor
        else:
            raise StopIteration

def main():
    contador = Contagem(1, 5)
    for n in contador:
        print(n)

if __name__ == '__main__':
    main()
