def soma_digitos(n):
    return sum(int(d) for d in str(n))

def main():
    print(soma_digitos(1234))

if __name__ == '__main__':
    main()
