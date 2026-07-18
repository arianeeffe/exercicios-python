class ContaBancaria:
    def __init__(self):
        self._saldo = 0.0
        
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            
    def sacar(self, valor):
        if valor > self._saldo:
            raise ValueError("Saque maior que o saldo disponível")
        self._saldo -= valor
        
    @property
    def saldo(self):
        return self._saldo

def main():
    c = ContaBancaria()
    c.depositar(100)
    print(c.saldo)
    c.sacar(50)
    print(c.saldo)

if __name__ == '__main__':
    main()
