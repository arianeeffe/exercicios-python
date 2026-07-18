class Publicador:
    def __init__(self):
        self._observadores = []
        
    def inscrever(self, observador):
        self._observadores.append(observador)
        
    def notificar(self, dado):
        for obs in self._observadores:
            if hasattr(obs, 'atualizar'):
                obs.atualizar(dado)
            elif callable(obs):
                obs(dado)

class Observador:
    def atualizar(self, dado):
        print(f"Observador recebeu: {dado}")

def main():
    pub = Publicador()
    obs = Observador()
    pub.inscrever(obs)
    pub.inscrever(lambda x: print(f"Função recebeu: {x}"))
    pub.notificar("Nova atualização!")

if __name__ == '__main__':
    main()
