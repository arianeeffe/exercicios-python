def rotacionar(lista, k):
    if not lista:
        return []
    k = k % len(lista)
    if k == 0:
        return lista[:]
        
    n = len(lista)
    nova_lista = [0] * n
    for i in range(n):
        nova_posicao = (i + k) % n
        nova_lista[nova_posicao] = lista[i]
        
    return nova_lista

def main():
    print(rotacionar([1, 2, 3, 4, 5], 2))

if __name__ == '__main__':
    main()
