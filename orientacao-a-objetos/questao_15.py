class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Estoque:
    def __init__(self):
        self.produtos = []
        
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        
    def remover_quantidade(self, nome, quantidade):
        for prod in self.produtos:
            if prod.nome == nome:
                if prod.quantidade >= quantidade:
                    prod.quantidade -= quantidade
                    return
                else:
                    raise ValueError(f"Quantidade insuficiente para {nome}")
        raise ValueError("Produto não encontrado")
        
    def valor_total(self):
        return sum(p.preco * p.quantidade for p in self.produtos)

def main():
    est = Estoque()
    p1 = Produto("Arroz", 20.0, 5)
    p2 = Produto("Feijão", 10.0, 10)
    est.adicionar_produto(p1)
    est.adicionar_produto(p2)
    
    print("Total:", est.valor_total())
    est.remover_quantidade("Arroz", 2)
    print("Total após remover:", est.valor_total())

if __name__ == '__main__':
    main()
