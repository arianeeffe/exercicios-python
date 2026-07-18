class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
        
    def ligar(self):
        return f"Motor de {self.potencia}cv ligado."

class Carro:
    def __init__(self, motor):
        self.motor = motor
        
    def ligar_carro(self):
        return self.motor.ligar()

def main():
    m = Motor(150)
    c = Carro(m)
    print(c.ligar_carro())

if __name__ == '__main__':
    main()
