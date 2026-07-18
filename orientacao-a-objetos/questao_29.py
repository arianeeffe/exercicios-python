import time

class CronometroContexto:
    def __enter__(self):
        self.inicio = time.time()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fim = time.time()
        print(f"Tempo decorrido: {self.fim - self.inicio:.4f} segundos")

def main():
    with CronometroContexto():
        # simulando uma operação que leva algum tempo
        soma = sum(range(1000000))
        print("Soma finalizada.")

if __name__ == '__main__':
    main()
