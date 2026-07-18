class Voador:
    def voar(self):
        return "Voando..."

class Nadador:
    def nadar(self):
        return "Nadando..."

class Pato(Voador, Nadador):
    pass

def main():
    p = Pato()
    print(p.voar())
    print(p.nadar())

if __name__ == '__main__':
    main()
