class Temperatura:
    def __init__(self, celsius=0.0):
        self.celsius = celsius
        
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32
        
    @fahrenheit.setter
    def fahrenheit(self, valor):
        self.celsius = (valor - 32) * 5/9
        
    @property
    def kelvin(self):
        return self.celsius + 273.15
        
    @kelvin.setter
    def kelvin(self, valor):
        self.celsius = valor - 273.15

def main():
    t = Temperatura(25)
    print("Celsius:", t.celsius)
    print("Fahrenheit:", t.fahrenheit)
    print("Kelvin:", t.kelvin)
    
    t.fahrenheit = 100
    print("Novo Celsius:", round(t.celsius, 2))

if __name__ == '__main__':
    main()
