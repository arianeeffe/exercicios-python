def maior_soma_subarray(lista):
    if not lista:
        return 0
        
    soma_atual = lista[0]
    soma_maxima = lista[0]
    
    for num in lista[1:]:
        soma_atual = max(num, soma_atual + num)
        soma_maxima = max(soma_maxima, soma_atual)
        
    return soma_maxima

def main():
    print(maior_soma_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

if __name__ == '__main__':
    main()
