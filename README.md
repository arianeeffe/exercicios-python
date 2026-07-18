# Exercícios Python

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge)

Este repositório contém a resolução de **60 exercícios práticos** em Python, divididos em dois tópicos principais: **Algoritmos** (30 exercícios) e **Orientação a Objetos** (30 exercícios). 

Cada exercício foi implementado em um arquivo Python autossuficiente, sem dependências de outras bibliotecas externas não nativas.

## Estrutura do Projeto

```text
exercicios-python/
├── algoritmos/
│   ├── questao_01.py (Sequência de Fibonacci)
│   ├── questao_02.py (Fatorial)
│   └── ... (até questao_30.py)
└── orientacao-a-objetos/
    ├── questao_01.py (Classe Pessoa)
    ├── questao_02.py (Herança - Animais)
    └── ... (até questao_30.py)
```

## Tópicos Abordados

### Algoritmos
- Lógica de programação geral
- Recursão (Fibonacci, Fatorial, Torre de Hanoi, Permutações)
- Algoritmos de Ordenação e Busca (Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, Busca Binária)
- Manipulação de Strings (Palíndromo, Inversão, Contagem de Vogais, Anagramas, Numerais Romanos)
- Cálculos matemáticos (Números Primos, MDC, MMC, Números de Armstrong, Números Perfeitos, Crivo de Eratóstenes, Sequência de Collatz)
- Operações com Matrizes e Conversão de Bases Numéricas
- Estruturas Lineares e Subarrays (Soma máxima/Algoritmo de Kadane, Rotação de Listas)

### Orientação a Objetos (POO)
- Classes, Atributos e Métodos
- Herança (Simples e Múltipla)
- Polimorfismo e Classes Abstratas (módulo `abc`)
- Encapsulamento (uso de `@property`)
- Composição de Objetos
- Interfaces (uso de `typing.Protocol`)
- Sobrecarga de Operadores (métodos mágicos como `__add__`, `__eq__`)
- Estruturas de Dados Customizadas (Fila, Pilha, Lista Encadeada, Árvore Binária de Busca)
- Tópicos Avançados (Iteradores `__iter__`/`__next__`, Context Managers `__enter__`/`__exit__`, `enum.Enum`)
- Padrões de Projeto (Design Patterns): Observer, Strategy, Singleton e Factory Method

## Como Executar

Todos os arquivos foram programados para serem executados de forma independente. Cada questão possui uma função `main()` que roda testes básicos do que foi implementado. Para testar qualquer um dos exercícios, basta rodar o arquivo no terminal utilizando o Python:

Exemplos:

```bash
python3 algoritmos/questao_28.py
python3 orientacao-a-objetos/questao_21.py
```