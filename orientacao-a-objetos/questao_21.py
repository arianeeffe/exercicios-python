class Configuracao:
    _instancia = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super(Configuracao, cls).__new__(cls)
            cls._instancia.config_data = {}
        return cls._instancia
        
    def set(self, chave, valor):
        self.config_data[chave] = valor
        
    def get(self, chave):
        return self.config_data.get(chave)

def main():
    c1 = Configuracao()
    c2 = Configuracao()
    c1.set("theme", "dark")
    
    print(c2.get("theme"))
    print("É a mesma instância?", c1 is c2)

if __name__ == '__main__':
    main()
