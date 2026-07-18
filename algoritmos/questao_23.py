def collatz(n):
    sequencia = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequencia.append(n)
    return sequencia

def main():
    print(collatz(6))

if __name__ == '__main__':
    main()
