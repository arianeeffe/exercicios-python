# Exercícios Python

Este repositório contém a resolução de 30 exercícios práticos em Python, divididos em dois tópicos principais: **Algoritmos** e **Orientação a Objetos**. 

Cada exercício foi implementado em um arquivo Python autossuficiente, sem dependências de outras bibliotecas externas não nativas.

## Estrutura do Projeto

```text
exercicios-python/
├── algoritmos/
│   ├── questao_01.py (Sequência de Fibonacci)
│   ├── questao_02.py (Fatorial)
│   └── ... (até questao_15.py)
└── orientacao-a-objetos/
    ├── questao_01.py (Classe Pessoa)
    ├── questao_02.py (Herança - Animais)
    └── ... (até questao_15.py)
```

## Tópicos Abordados

### Algoritmos
- Lógica de programação geral
- Recursão (Fibonacci, Fatorial, Torre de Hanoi)
- Algoritmos de Ordenação e Busca (Bubble Sort, Busca Binária)
- Manipulação de Strings (Palíndromo, Inversão, Contagem de Vogais)
- Cálculos matemáticos (Números Primos, MDC, MMC, Números de Armstrong, Números Perfeitos)
- Operações com Matrizes e Conversão de Bases Numéricas

### Orientação a Objetos (POO)
- Classes, Atributos e Métodos
- Herança (Simples e Múltipla)
- Polimorfismo e Classes Abstratas (módulo `abc`)
- Encapsulamento (uso de `@property`)
- Composição de Objetos
- Interfaces (uso de `typing.Protocol`)
- Sobrecarga de Operadores (métodos mágicos como `__add__`, `__eq__`)
- Padrões de Projeto (Design Patterns): Observer e Strategy

## Como Executar

Todos os arquivos foram programados para serem executados de forma independente. Cada questão possui uma função `main()` que roda testes básicos do que foi implementado. Para testar qualquer um dos exercícios, basta rodar o arquivo no terminal utilizando o Python:

Exemplos:

```bash
python3 algoritmos/questao_01.py
python3 orientacao-a-objetos/questao_14.py
```