from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        return "Carro acelerando..."

class Moto(Veiculo):
    def acelerar(self):
        return "Moto acelerando..."

def main():
    c = Carro()
    print(c.acelerar())
    try:
        v = Veiculo()
    except TypeError as e:
        print(f"Erro esperado: {e}")

if __name__ == '__main__':
    main()
