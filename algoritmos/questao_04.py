def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista

def main():
    print(bubble_sort([5, 3, 8, 1]))

if __name__ == '__main__':
    main()
