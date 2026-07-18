def numeros_perfeitos(limite):
    perfeitos = []
    for n in range(2, limite + 1):
        soma_divisores = sum(i for i in range(1, n) if n % i == 0)
        if soma_divisores == n:
            perfeitos.append(n)
    return perfeitos

def main():
    print(numeros_perfeitos(30))

if __name__ == '__main__':
    main()
