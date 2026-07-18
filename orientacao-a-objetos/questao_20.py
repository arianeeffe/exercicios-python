class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base
        
    def calcular_salario(self):
        return self.salario_base

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus_fixo):
        super().__init__(nome, salario_base)
        self.bonus_fixo = bonus_fixo
        
    def calcular_salario(self):
        return self.salario_base + self.bonus_fixo

class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, total_vendas, percentual_comissao):
        super().__init__(nome, salario_base)
        self.total_vendas = total_vendas
        self.percentual_comissao = percentual_comissao
        
    def calcular_salario(self):
        return self.salario_base + (self.total_vendas * self.percentual_comissao)

def main():
    g = Gerente("Carlos", 5000, 2000)
    v = Vendedor("Ana", 3000, 10000, 0.05)
    print("Gerente:", g.calcular_salario())
    print("Vendedor:", v.calcular_salario())

if __name__ == '__main__':
    main()
