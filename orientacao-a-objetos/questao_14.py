class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponivel = True

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

class Biblioteca:
    def __init__(self):
        self.livros = []
        
    def adicionar_livro(self, livro):
        self.livros.append(livro)
        
    def emprestar(self, usuario, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and livro.disponivel:
                livro.disponivel = False
                usuario.livros_emprestados.append(livro)
                return True
        return False
        
    def devolver(self, usuario, titulo):
        for livro in usuario.livros_emprestados:
            if livro.titulo == titulo:
                livro.disponivel = True
                usuario.livros_emprestados.remove(livro)
                return True
        return False

def main():
    bib = Biblioteca()
    l1 = Livro("Python Fluente")
    bib.adicionar_livro(l1)
    
    u = Usuario("Ana")
    print("Emprestar:", bib.emprestar(u, "Python Fluente"))
    print("Disponível:", l1.disponivel)
    print("Devolver:", bib.devolver(u, "Python Fluente"))
    print("Disponível:", l1.disponivel)

if __name__ == '__main__':
    main()
