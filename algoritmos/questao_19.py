def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    esquerda = [x for x in lista if x < pivo]
    meio = [x for x in lista if x == pivo]
    direita = [x for x in lista if x > pivo]
    return quick_sort(esquerda) + meio + quick_sort(direita)

def main():
    print(quick_sort([5, 3, 8, 1, 9, 2]))

if __name__ == '__main__':
    main()
