def fatorial(n):
    if n == 0 or n == 1:
        return 1
    fat = 1
    for i in range(2, n + 1):
        fat *= i
    return fat

def main():
    print(fatorial(5))

if __name__ == '__main__':
    main()
