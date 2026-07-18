class Matriz:
    def __init__(self, dados):
        self.dados = dados
        
    def somar(self, outra):
        if len(self.dados) != len(outra.dados) or len(self.dados[0]) != len(outra.dados[0]):
            raise ValueError("Matrizes devem ter as mesmas dimensões para soma")
            
        resultado = []
        for i in range(len(self.dados)):
            linha = []
            for j in range(len(self.dados[0])):
                linha.append(self.dados[i][j] + outra.dados[i][j])
            resultado.append(linha)
        return Matriz(resultado)
        
    def multiplicar(self, outra):
        if len(self.dados[0]) != len(outra.dados):
            raise ValueError("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda")
            
        resultado = []
        for i in range(len(self.dados)):
            linha = []
            for j in range(len(outra.dados[0])):
                soma = 0
                for k in range(len(self.dados[0])):
                    soma += self.dados[i][k] * outra.dados[k][j]
                linha.append(soma)
            resultado.append(linha)
        return Matriz(resultado)

def main():
    m1 = Matriz([[1, 2], [3, 4]])
    m2 = Matriz([[5, 6], [7, 8]])
    print("Soma:", m1.somar(m2).dados)
    print("Multiplicação:", m1.multiplicar(m2).dados)

if __name__ == '__main__':
    main()
