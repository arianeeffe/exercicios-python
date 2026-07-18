def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

def main():
    print(busca_binaria([1, 3, 5, 7, 9], 7))

if __name__ == '__main__':
    main()
