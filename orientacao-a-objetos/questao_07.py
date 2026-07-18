from typing import Protocol

class Pagavel(Protocol):
    def pagar(self, valor: float) -> str:
        ...

class PagamentoPix:
    def pagar(self, valor: float) -> str:
        return f"Pagamento de R${valor:.2f} realizado via Pix."

class PagamentoCartao:
    def pagar(self, valor: float) -> str:
        return f"Pagamento de R${valor:.2f} realizado via Cartão."

def processar_pagamento(metodo: Pagavel, valor: float):
    print(metodo.pagar(valor))

def main():
    pix = PagamentoPix()
    cartao = PagamentoCartao()
    processar_pagamento(pix, 150.0)
    processar_pagamento(cartao, 200.0)

if __name__ == '__main__':
    main()
