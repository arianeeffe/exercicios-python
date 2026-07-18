class Vetor2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, outro):
        return Vetor2D(self.x + outro.x, self.y + outro.y)
        
    def __sub__(self, outro):
        return Vetor2D(self.x - outro.x, self.y - outro.y)
        
    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y
        
    def __repr__(self):
        return f"Vetor2D({self.x}, {self.y})"

def main():
    v1 = Vetor2D(1, 2)
    v2 = Vetor2D(3, 4)
    print(v1 + v2)
    print(v1 == Vetor2D(1, 2))

if __name__ == '__main__':
    main()
