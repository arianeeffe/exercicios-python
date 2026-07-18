def crivo_eratostenes(n):
    if n < 2:
        return []
    
    primos = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if primos[p]:
            for i in range(p * p, n + 1, p):
                primos[i] = False
        p += 1
        
    resultado = []
    for p in range(2, n + 1):
        if primos[p]:
            resultado.append(p)
    return resultado

def main():
    print(crivo_eratostenes(20))

if __name__ == '__main__':
    main()
