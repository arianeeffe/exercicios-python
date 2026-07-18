import unicodedata

def contar_vogais(texto):
    texto = ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
    texto = texto.lower()
    contagem = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for char in texto:
        if char in contagem:
            contagem[char] += 1
    return contagem

def main():
    print(contar_vogais("Programacao em Python"))

if __name__ == '__main__':
    main()
