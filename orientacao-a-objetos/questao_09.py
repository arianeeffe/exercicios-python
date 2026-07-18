class Contador:
    _instancias = 0
    
    def __init__(self):
        Contador._instancias += 1
        
    @classmethod
    def total_instancias(cls):
        return cls._instancias
        
    @staticmethod
    def eh_par(numero):
        return numero % 2 == 0

def main():
    c1 = Contador()
    c2 = Contador()
    print(Contador.total_instancias())
    print(Contador.eh_par(4))

if __name__ == '__main__':
    main()
