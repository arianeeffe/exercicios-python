def transposta(matriz):
    if not matriz:
        return []
    linhas = len(matriz)
    colunas = len(matriz[0])
    resultado = [[0] * linhas for _ in range(colunas)]
    
    for i in range(linhas):
        for j in range(colunas):
            resultado[j][i] = matriz[i][j]
            
    return resultado

def main():
    print(transposta([[1, 2, 3], [4, 5, 6]]))

if __name__ == '__main__':
    main()
