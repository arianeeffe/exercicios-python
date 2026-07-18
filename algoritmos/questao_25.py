import re

def contar_palavras(texto):
    texto_limpo = re.sub(r'[^a-zA-Z\s]', '', texto).lower()
    palavras = texto_limpo.split()
    
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
        
    return contagem

def main():
    print(contar_palavras("O gato correu. O gato subiu."))

if __name__ == '__main__':
    main()
