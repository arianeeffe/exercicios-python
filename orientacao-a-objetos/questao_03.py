import math

class Forma:
    def area(self):
        raise NotImplementedError("Método não implementado")

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
        
    def area(self):
        return math.pi * self.raio ** 2

def main():
    r = Retangulo(2, 3)
    c = Circulo(2)
    print(r.area())
    print(c.area())

if __name__ == '__main__':
    main()
