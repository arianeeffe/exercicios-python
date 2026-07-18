def maior_e_menor(lista):
    if not lista:
        return None, None
    maior = lista[0]
    menor = lista[0]
    for num in lista[1:]:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    return maior, menor

def main():
    print(maior_e_menor([4, 8, 1, 9, 3]))

if __name__ == '__main__':
    main()
