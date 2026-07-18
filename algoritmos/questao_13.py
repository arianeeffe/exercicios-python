def eh_armstrong(n):
    str_n = str(n)
    num_digitos = len(str_n)
    soma = sum(int(d) ** num_digitos for d in str_n)
    return soma == n

def main():
    print(eh_armstrong(153))
    print(eh_armstrong(123))

if __name__ == '__main__':
    main()
