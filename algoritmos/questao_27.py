def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

def main():
    print(esta_ordenada([1, 2, 3, 4]))
    print(esta_ordenada([1, 3, 2, 4]))

if __name__ == '__main__':
    main()
