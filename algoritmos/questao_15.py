def converter_base(numero, base):
    if numero == 0:
        return "0"
    
    digitos = "0123456789ABCDEF"
    resultado = ""
    
    while numero > 0:
        resto = numero % base
        resultado = digitos[resto] + resultado
        numero //= base
        
    return resultado

def main():
    print(converter_base(10, 2))
    print(converter_base(255, 16))

if __name__ == '__main__':
    main()
