# Lista de Exercícios de Python

Lista de exercícios dividida em dois tópicos principais: **Algoritmos** e **Orientação a Objetos**, com 15 exercícios cada.

## Regras

- O código completo de cada questão deve ficar somente em um único arquivo, sem depender de outros arquivos.

## Estrutura de Projeto

```
exercicios-python/
├── algoritmos/
│   ├── questao_01.py
│   ├── questao_02.py
│   ├── questao_03.py
│   ├── questao_04.py
│   ├── questao_05.py
│   ├── questao_06.py
│   ├── questao_07.py
│   ├── questao_08.py
│   ├── questao_09.py
│   ├── questao_10.py
│   ├── questao_11.py
│   ├── questao_12.py
│   ├── questao_13.py
│   ├── questao_14.py
│   └── questao_15.py
└── orientacao-a-objetos/
    ├── questao_01.py
    ├── questao_02.py
    ├── questao_03.py
    ├── questao_04.py
    ├── questao_05.py
    ├── questao_06.py
    ├── questao_07.py
    ├── questao_08.py
    ├── questao_09.py
    ├── questao_10.py
    ├── questao_11.py
    ├── questao_12.py
    ├── questao_13.py
    ├── questao_14.py
    └── questao_15.py
```

## Algoritmos

### 1. Sequência de Fibonacci
**Arquivo:** `questao_01.py`

Implemente uma função que retorne o n-ésimo termo da sequência de
Fibonacci (0, 1, 1, 2, 3, 5, 8, ...), onde fib(0) = 0 e fib(1) = 1.

**Exemplo:**
```python
fibonacci(6) -> 8
```

### 2. Fatorial
**Arquivo:** `questao_02.py`

Implemente uma função que calcule o fatorial de um número inteiro
não-negativo n (n!).

**Exemplo:**
```python
fatorial(5) -> 120
```

### 3. Números primos
**Arquivo:** `questao_03.py`

Implemente uma função que verifique se um número inteiro é primo.
Um número primo é maior que 1 e divisível apenas por 1 e por ele mesmo.

**Exemplo:**
```python
eh_primo(7)  -> True
eh_primo(10) -> False
```

### 4. Bubble Sort
**Arquivo:** `questao_04.py`

Implemente o algoritmo de ordenação Bubble Sort para ordenar uma
lista de números em ordem crescente, sem usar sorted() ou list.sort().

**Exemplo:**
```python
bubble_sort([5, 3, 8, 1]) -> [1, 3, 5, 8]
```

### 5. Busca binária
**Arquivo:** `questao_05.py`

Implemente o algoritmo de busca binária, que recebe uma lista
JÁ ORDENADA e um valor alvo, retornando o índice do valor na lista
ou -1 caso não seja encontrado.

**Exemplo:**
```python
busca_binaria([1, 3, 5, 7, 9], 7) -> 3
```

### 6. MDC e MMC
**Arquivo:** `questao_06.py`

Implemente duas funções: uma para calcular o Máximo Divisor Comum
(MDC) e outra para o Mínimo Múltiplo Comum (MMC) entre dois números
inteiros positivos.

**Exemplo:**
```python
mdc(12, 18) -> 6
mmc(4, 6)   -> 12
```

### 7. Palíndromo
**Arquivo:** `questao_07.py`

Implemente uma função que verifique se uma string é um palíndromo,
ou seja, se ela é lida da mesma forma de trás para frente.
Ignore espaços, pontuação e diferenças entre maiúsculas/minúsculas.

**Exemplo:**
```python
eh_palindromo("Ame a ema") -> True
```

### 8. Contagem de vogais
**Arquivo:** `questao_08.py`

Implemente uma função que receba uma string e retorne um
dicionário com a contagem de cada vogal presente no texto (a, e, i, o, u),
ignorando maiúsculas/minúsculas.

**Exemplo:**
```python
contar_vogais("Programacao em Python") -> {'a': 3, 'e': 1, 'i': 0, 'o': 3, 'u': 0}
```

### 9. Inversão de string
**Arquivo:** `questao_09.py`

Implemente uma função que inverta uma string SEM utilizar
slicing reverso ([::-1]) nem a função reversed().

**Exemplo:**
```python
inverter("python") -> "nohtyp"
```

### 10. Soma dos dígitos
**Arquivo:** `questao_10.py`

Implemente uma função que retorne a soma dos dígitos de um
número inteiro positivo.

**Exemplo:**
```python
soma_digitos(1234) -> 10  (1+2+3+4)
```

### 11. Torre de Hanoi
**Arquivo:** `questao_11.py`

Implemente a solução recursiva para o problema da Torre de
Hanoi. A função deve imprimir os passos necessários para mover N discos
da torre de origem para a torre de destino, usando uma torre auxiliar.

**Exemplo:**
```python
hanoi(2, 'A', 'C', 'B') deve imprimir os movimentos necessários
para mover 2 discos de A para C usando B como auxiliar.
```

### 12. Números perfeitos
**Arquivo:** `questao_12.py`

Um número perfeito é aquele que é igual à soma de seus
divisores próprios (excluindo ele mesmo). Implemente uma função que
retorne uma lista com todos os números perfeitos entre 1 e um limite N.

**Exemplo:**
```python
numeros_perfeitos(30) -> [6, 28]
```

### 13. Número de Armstrong
**Arquivo:** `questao_13.py`

Um número de Armstrong (ou número narcisista) é aquele em
que a soma de seus dígitos, cada um elevado à quantidade de dígitos do
número, é igual ao próprio número. Implemente uma função que verifique
se um número é de Armstrong.

**Exemplo:**
```python
eh_armstrong(153) -> True   (1**3 + 5**3 + 3**3 = 153)
eh_armstrong(123) -> False
```

### 14. Matriz transposta
**Arquivo:** `questao_14.py`

Implemente uma função que receba uma matriz (lista de listas)
e retorne sua transposta, sem utilizar bibliotecas externas como numpy.

**Exemplo:**
```python
transposta([[1, 2, 3], [4, 5, 6]]) -> [[1, 4], [2, 5], [3, 6]]
```

### 15. Conversão de bases numéricas
**Arquivo:** `questao_15.py`

Implemente uma função que converta um número inteiro
decimal para sua representação em uma base numérica arbitrária
(entre 2 e 16), retornando o resultado como string. Não utilize as
funções bin(), oct() ou hex().

**Exemplo:**
```python
converter_base(10, 2)  -> "1010"
converter_base(255, 16) -> "FF"
```

## Orientação a Objetos

### 1. Classe Pessoa
**Arquivo:** `questao_01.py`

Crie uma classe `Pessoa` com atributos `nome` e `idade`.
Implemente um método `apresentar()` que retorne uma string no formato:
"Olá, meu nome é {nome} e tenho {idade} anos."

### 2. Herança - Animais
**Arquivo:** `questao_02.py`

Crie uma classe base `Animal` com o atributo `nome` e um método
`emitir_som()` que retorne "Som genérico". Crie as classes `Cachorro` e
`Gato`, que herdam de `Animal` e sobrescrevem `emitir_som()` retornando
"Au au!" e "Miau!" respectivamente.

### 3. Polimorfismo - Formas geométricas
**Arquivo:** `questao_03.py`

Crie uma classe base `Forma` com um método `area()` que
levante `NotImplementedError`. Crie as classes `Retangulo` (com `largura`
e `altura`) e `Circulo` (com `raio`), cada uma implementando seu próprio
cálculo de área. Utilize `math.pi` para o círculo (biblioteca padrão).

### 4. Encapsulamento - Conta bancária
**Arquivo:** `questao_04.py`

Crie uma classe `ContaBancaria` com um atributo privado
`_saldo`. Implemente os métodos `depositar(valor)`, `sacar(valor)`
(que deve impedir saque maior que o saldo, lançando uma exceção
`ValueError`) e uma property `saldo` para leitura do saldo atual.

### 5. Classe abstrata - Veículo
**Arquivo:** `questao_05.py`

Utilizando o módulo `abc`, crie uma classe abstrata
`Veiculo` com um método abstrato `acelerar()`. Crie as classes concretas
`Carro` e `Moto` que implementam esse método retornando mensagens
diferentes. Tente instanciar `Veiculo` diretamente e observe o erro.

### 6. Composição - Carro e Motor
**Arquivo:** `questao_06.py`

Crie uma classe `Motor` com atributo `potencia` e método
`ligar()` que retorna "Motor de {potencia}cv ligado.". Crie uma classe
`Carro` que POSSUI um `Motor` (composição, não herança) e um método
`ligar_carro()` que utiliza o motor internamente.

### 7. Interfaces com Protocol
**Arquivo:** `questao_07.py`

Utilizando `typing.Protocol`, defina uma interface
`Pagavel` que exige um método `pagar(valor: float) -> str`. Implemente
as classes `PagamentoPix` e `PagamentoCartao`, cada uma seguindo o
protocolo com sua própria implementação de `pagar`.

### 8. Sobrecarga de operadores - Vetor2D
**Arquivo:** `questao_08.py`

Crie uma classe `Vetor2D` com atributos `x` e `y`.
Sobrecarregue os operadores `+`, `-` e `==` utilizando os métodos
mágicos `__add__`, `__sub__` e `__eq__`. Implemente também `__repr__`
para facilitar a visualização.

### 9. Métodos estáticos e de classe - Contador
**Arquivo:** `questao_09.py`

Crie uma classe `Contador` que mantenha, através de um
atributo de classe, a quantidade de instâncias criadas. Implemente um
`classmethod` `total_instancias()` que retorne essa contagem e um
`staticmethod` `eh_par(numero)` que verifique se um número é par.

### 10. Herança múltipla - Pato
**Arquivo:** `questao_10.py`

Crie as classes `Voador` (com método `voar()`) e `Nadador`
(com método `nadar()`). Crie a classe `Pato`, que herda de AMBAS as
classes (herança múltipla), somando as duas capacidades.

### 11. Propriedades - Produto
**Arquivo:** `questao_11.py`

Crie uma classe `Produto` com um atributo privado `_preco`.
Utilize `@property` e `@preco.setter` para garantir que o preço nunca
possa ser definido como um valor negativo (deve lançar `ValueError`
nesse caso).

### 12. Padrão Observer
**Arquivo:** `questao_12.py`

Implemente uma versão simples do padrão Observer. Crie uma
classe `Publicador` que mantém uma lista de observadores (funções ou
objetos com método `atualizar(dado)`), permite `inscrever(observador)`
e `notificar(dado)`, chamando `atualizar` em todos os inscritos.

### 13. Padrão Strategy
**Arquivo:** `questao_13.py`

Implemente o padrão Strategy para cálculo de frete. Crie uma
interface `EstrategiaFrete` (pode usar `Protocol` ou classe abstrata)
com o método `calcular(peso: float) -> float`. Implemente duas
estratégias concretas: `FreteExpresso` e `FreteEconomico`, cada uma com
uma fórmula diferente. Crie uma classe `Pedido` que recebe a estratégia
e delega o cálculo do frete a ela.

### 14. Sistema de biblioteca
**Arquivo:** `questao_14.py`

Crie três classes: `Livro` (com `titulo` e `disponivel`),
`Usuario` (com `nome` e lista de `livros_emprestados`) e `Biblioteca`
(com lista de livros). A `Biblioteca` deve ter os métodos
`emprestar(usuario, titulo)` e `devolver(usuario, titulo)`, atualizando
a disponibilidade do livro e a lista do usuário.

### 15. Sistema de estoque
**Arquivo:** `questao_15.py`

Crie uma classe `Produto` (com `nome`, `preco` e
`quantidade`) e uma classe `Estoque` que gerencia uma lista de produtos.
Implemente na `Estoque` os métodos `adicionar_produto(produto)`,
`remover_quantidade(nome, quantidade)` (lançando `ValueError` se não
houver quantidade suficiente) e `valor_total()`, que retorna a soma de
`preco * quantidade` de todos os produtos.
