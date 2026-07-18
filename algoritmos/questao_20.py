import re
import unicodedata

def sao_anagramas(s1, s2):
    def limpar(s):
        s = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
        return re.sub(r'\s+', '', s).lower()
        
    s1_limpo = limpar(s1)
    s2_limpo = limpar(s2)
    
    if len(s1_limpo) != len(s2_limpo):
        return False
        
    contagem = {}
    for char in s1_limpo:
        contagem[char] = contagem.get(char, 0) + 1
    for char in s2_limpo:
        if char not in contagem:
            return False
        contagem[char] -= 1
        if contagem[char] < 0:
            return False
            
    return all(v == 0 for v in contagem.values())

def main():
    print(sao_anagramas("roma", "amor"))
    print(sao_anagramas("python", "java"))

if __name__ == '__main__':
    main()
