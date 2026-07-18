from enum import Enum

class StatusTarefa(Enum):
    PENDENTE = 1
    EM_ANDAMENTO = 2
    CONCLUIDA = 3

class Tarefa:
    def __init__(self, titulo):
        self.titulo = titulo
        self.status = StatusTarefa.PENDENTE
        
    def avancar_status(self):
        if self.status == StatusTarefa.PENDENTE:
            self.status = StatusTarefa.EM_ANDAMENTO
        elif self.status == StatusTarefa.EM_ANDAMENTO:
            self.status = StatusTarefa.CONCLUIDA
        else:
            print("Tarefa já está concluída.")

def main():
    t = Tarefa("Estudar Python")
    print(t.status)
    t.avancar_status()
    print(t.status)
    t.avancar_status()
    print(t.status)

if __name__ == '__main__':
    main()
