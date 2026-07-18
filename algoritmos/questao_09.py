def inverter(s):
    resultado = ""
    for char in s:
        resultado = char + resultado
    return resultado

def main():
    print(inverter("python"))

if __name__ == '__main__':
    main()
