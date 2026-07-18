class Candidato:
    def __init__(self, nome):
        self.nome = nome
        self.votos = 0

class Urna:
    def __init__(self):
        self.candidatos = {}
        
    def adicionar_candidato(self, nome):
        if nome not in self.candidatos:
            self.candidatos[nome] = Candidato(nome)
            
    def votar(self, nome_candidato):
        if nome_candidato in self.candidatos:
            self.candidatos[nome_candidato].votos += 1
            return True
        return False
        
    def resultado(self):
        if not self.candidatos:
            return None
        
        vencedor = max(self.candidatos.values(), key=lambda c: c.votos)
        return vencedor.nome

def main():
    u = Urna()
    u.adicionar_candidato("Alice")
    u.adicionar_candidato("Bob")
    
    u.votar("Alice")
    u.votar("Alice")
    u.votar("Bob")
    
    print("Vencedor:", u.resultado())

if __name__ == '__main__':
    main()
