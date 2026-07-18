import math

class Fracao:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("Denominador não pode ser zero")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()
        
    def simplificar(self):
        mdc = math.gcd(self.numerador, self.denominador)
        self.numerador //= mdc
        self.denominador //= mdc
        
    def somar(self, outra):
        novo_num = (self.numerador * outra.denominador) + (outra.numerador * self.denominador)
        novo_den = self.denominador * outra.denominador
        return Fracao(novo_num, novo_den)
        
    def __repr__(self):
        return f"{self.numerador}/{self.denominador}"

def main():
    f1 = Fracao(1, 2)
    f2 = Fracao(1, 4)
    print("Soma:", f1.somar(f2))

if __name__ == '__main__':
    main()
