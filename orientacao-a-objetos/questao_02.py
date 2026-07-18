class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def emitir_som(self):
        return "Som genérico"

class Cachorro(Animal):
    def emitir_som(self):
        return "Au au!"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"

def main():
    c = Cachorro("Rex")
    g = Gato("Mimi")
    print(c.emitir_som())
    print(g.emitir_som())

if __name__ == '__main__':
    main()
