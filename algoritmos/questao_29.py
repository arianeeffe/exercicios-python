def romano_para_inteiro(s):
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    anterior = 0
    
    for char in reversed(s):
        atual = valores[char]
        if atual < anterior:
            total -= atual
        else:
            total += atual
        anterior = atual
        
    return total

def main():
    print(romano_para_inteiro("XIV"))
    print(romano_para_inteiro("MCMXCIV"))

if __name__ == '__main__':
    main()
