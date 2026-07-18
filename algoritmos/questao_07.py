import re
import unicodedata

def eh_palindromo(s):
    # Remove acentos
    s = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
    # Mantem so caracteres alfanumericos e minusculos
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]

def main():
    print(eh_palindromo("Ame a ema"))

if __name__ == '__main__':
    main()
