def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def mmc(a, b):
    return abs(a * b) // mdc(a, b)

def main():
    print(mdc(12, 18))
    print(mmc(4, 6))

if __name__ == '__main__':
    main()
