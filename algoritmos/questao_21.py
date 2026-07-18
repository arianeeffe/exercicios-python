def elementos_unicos(lista):
    contagem = {}
    for item in lista:
        contagem[item] = contagem.get(item, 0) + 1
        
    resultado = []
    for item in lista:
        if contagem[item] == 1:
            resultado.append(item)
    return resultado

def main():
    print(elementos_unicos([1, 2, 2, 3, 4, 4, 5]))

if __name__ == '__main__':
    main()
