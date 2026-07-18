def hanoi(n, origem, destino, auxiliar):
    if n > 0:
        hanoi(n - 1, origem, auxiliar, destino)
        print(f"Mover disco de {origem} para {destino}")
        hanoi(n - 1, auxiliar, destino, origem)

def main():
    hanoi(2, 'A', 'C', 'B')

if __name__ == '__main__':
    main()
