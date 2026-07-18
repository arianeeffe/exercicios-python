from typing import Protocol

class EstrategiaFrete(Protocol):
    def calcular(self, peso: float) -> float:
        ...

class FreteExpresso:
    def calcular(self, peso: float) -> float:
        return peso * 15.0

class FreteEconomico:
    def calcular(self, peso: float) -> float:
        return peso * 5.0

class Pedido:
    def __init__(self, estrategia: EstrategiaFrete):
        self.estrategia = estrategia
        
    def calcular_frete(self, peso: float) -> float:
        return self.estrategia.calcular(peso)

def main():
    pedido1 = Pedido(FreteExpresso())
    print(pedido1.calcular_frete(2))
    
    pedido2 = Pedido(FreteEconomico())
    print(pedido2.calcular_frete(2))

if __name__ == '__main__':
    main()
