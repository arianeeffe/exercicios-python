class Quarto:
    def __init__(self, numero):
        self.numero = numero
        self.disponivel = True

class Hotel:
    def __init__(self):
        self.quartos = {}
        
    def adicionar_quarto(self, quarto):
        self.quartos[quarto.numero] = quarto
        
    def reservar(self, numero):
        if numero in self.quartos:
            quarto = self.quartos[numero]
            if quarto.disponivel:
                quarto.disponivel = False
                return True
        return False
        
    def liberar(self, numero):
        if numero in self.quartos:
            quarto = self.quartos[numero]
            if not quarto.disponivel:
                quarto.disponivel = True
                return True
        return False

def main():
    h = Hotel()
    h.adicionar_quarto(Quarto(101))
    h.adicionar_quarto(Quarto(102))
    
    print("Reserva 101:", h.reservar(101))
    print("Reserva 101 novamente:", h.reservar(101))
    print("Libera 101:", h.liberar(101))

if __name__ == '__main__':
    main()
