# Lista de Exercícios de Python (Parte 2)

Continuação da lista de exercícios, com mais 15 exercícios de **Algoritmos** e 15 de **Orientação a Objetos** (questões 16 a 30).

## Regras

- O código completo de cada questão deve ficar somente em um único arquivo, sem depender de outros arquivos.

## Estrutura de Projeto

```
exercicios-python/
├── algoritmos/
│   ├── questao_16.py
│   ├── questao_17.py
│   ├── questao_18.py
│   ├── questao_19.py
│   ├── questao_20.py
│   ├── questao_21.py
│   ├── questao_22.py
│   ├── questao_23.py
│   ├── questao_24.py
│   ├── questao_25.py
│   ├── questao_26.py
│   ├── questao_27.py
│   ├── questao_28.py
│   ├── questao_29.py
│   └── questao_30.py
└── orientacao-a-objetos/
    ├── questao_16.py
    ├── questao_17.py
    ├── questao_18.py
    ├── questao_19.py
    ├── questao_20.py
    ├── questao_21.py
    ├── questao_22.py
    ├── questao_23.py
    ├── questao_24.py
    ├── questao_25.py
    ├── questao_26.py
    ├── questao_27.py
    ├── questao_28.py
    ├── questao_29.py
    └── questao_30.py
```

## Algoritmos

### 16. Selection Sort
**Arquivo:** `questao_16.py`

Implemente o algoritmo de ordenação Selection Sort para ordenar
uma lista de números em ordem crescente, sem usar sorted() ou
list.sort().

**Exemplo:**
```python
selection_sort([5, 3, 8, 1]) -> [1, 3, 5, 8]
```

### 17. Insertion Sort
**Arquivo:** `questao_17.py`

Implemente o algoritmo de ordenação Insertion Sort para ordenar
uma lista de números em ordem crescente, sem usar sorted() ou
list.sort().

**Exemplo:**
```python
insertion_sort([5, 3, 8, 1]) -> [1, 3, 5, 8]
```

### 18. Merge Sort
**Arquivo:** `questao_18.py`

Implemente o algoritmo de ordenação Merge Sort (divisão e
conquista) para ordenar uma lista de números em ordem crescente.

**Exemplo:**
```python
merge_sort([5, 3, 8, 1, 9, 2]) -> [1, 2, 3, 5, 8, 9]
```

### 19. Quick Sort
**Arquivo:** `questao_19.py`

Implemente o algoritmo de ordenação Quick Sort para ordenar
uma lista de números em ordem crescente.

**Exemplo:**
```python
quick_sort([5, 3, 8, 1, 9, 2]) -> [1, 2, 3, 5, 8, 9]
```

### 20. Anagramas
**Arquivo:** `questao_20.py`

Implemente uma função que verifique se duas strings são
anagramas uma da outra (contêm exatamente as mesmas letras, ignorando
espaços e diferenças entre maiúsculas/minúsculas).

**Exemplo:**
```python
sao_anagramas("roma", "amor") -> True
sao_anagramas("python", "java") -> False
```

### 21. Elementos únicos
**Arquivo:** `questao_21.py`

Implemente uma função que receba uma lista e retorne uma
nova lista contendo apenas os elementos que aparecem uma única vez,
mantendo a ordem original, sem utilizar set().

**Exemplo:**
```python
elementos_unicos([1, 2, 2, 3, 4, 4, 5]) -> [1, 3, 5]
```

### 22. Maior e menor elemento
**Arquivo:** `questao_22.py`

Implemente uma função que receba uma lista de números e
retorne uma tupla (maior, menor), sem utilizar as funções max() e
min().

**Exemplo:**
```python
maior_e_menor([4, 8, 1, 9, 3]) -> (9, 1)
```

### 23. Sequência de Collatz
**Arquivo:** `questao_23.py`

Implemente uma função que gere a sequência de Collatz a
partir de um número n: se n for par, divida por 2; se for ímpar,
multiplique por 3 e some 1. Repita até chegar a 1. Retorne a lista com
todos os valores da sequência, incluindo o número inicial e o 1 final.

**Exemplo:**
```python
collatz(6) -> [6, 3, 10, 5, 16, 8, 4, 2, 1]
```

### 24. Crivo de Eratóstenes
**Arquivo:** `questao_24.py`

Implemente o algoritmo do Crivo de Eratóstenes para retornar
uma lista com todos os números primos até um limite N.

**Exemplo:**
```python
crivo_eratostenes(20) -> [2, 3, 5, 7, 11, 13, 17, 19]
```

### 25. Contagem de palavras
**Arquivo:** `questao_25.py`

Implemente uma função que receba um texto e retorne um
dicionário com a contagem de ocorrências de cada palavra, ignorando
maiúsculas/minúsculas e pontuação básica.

**Exemplo:**
```python
contar_palavras("O gato correu. O gato subiu.")
-> {'o': 2, 'gato': 2, 'correu': 1, 'subiu': 1}
```

### 26. Rotação de lista
**Arquivo:** `questao_26.py`

Implemente uma função que rotacione os elementos de uma
lista em k posições para a direita, sem utilizar slicing (fatiamento
[:]).

**Exemplo:**
```python
rotacionar([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
```

### 27. Lista ordenada
**Arquivo:** `questao_27.py`

Implemente uma função que verifique se uma lista de números
está ordenada em ordem crescente, sem utilizar sorted().

**Exemplo:**
```python
esta_ordenada([1, 2, 3, 4]) -> True
esta_ordenada([1, 3, 2, 4]) -> False
```

### 28. Subarray de soma máxima (Kadane)
**Arquivo:** `questao_28.py`

Implemente o algoritmo de Kadane para encontrar a soma
máxima de um subarray contíguo dentro de uma lista de números
(que pode conter valores negativos).

**Exemplo:**
```python
maior_soma_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) -> 6
(subarray [4, -1, 2, 1])
```

### 29. Números romanos para inteiro
**Arquivo:** `questao_29.py`

Implemente uma função que converta um número romano
(string) para seu valor inteiro correspondente.

**Exemplo:**
```python
romano_para_inteiro("XIV") -> 14
romano_para_inteiro("MCMXCIV") -> 1994
```

### 30. Permutações
**Arquivo:** `questao_30.py`

Implemente uma função recursiva que gere e retorne todas as
permutações possíveis dos elementos de uma lista, sem utilizar o
módulo itertools.

**Exemplo:**
```python
permutacoes([1, 2, 3])
-> [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

## Orientação a Objetos

### 16. Fila (Queue)
**Arquivo:** `questao_16.py`

Implemente uma classe `Fila` que simule uma estrutura de
fila (FIFO), com os métodos `enfileirar(item)`, `desenfileirar()`
(removendo e retornando o primeiro item) e `esta_vazia()`.

### 17. Pilha (Stack)
**Arquivo:** `questao_17.py`

Implemente uma classe `Pilha` que simule uma estrutura de
pilha (LIFO), com os métodos `empilhar(item)`, `desempilhar()`
(removendo e retornando o último item) e `topo()` (consultando o
último item sem remover).

### 18. Lista encadeada
**Arquivo:** `questao_18.py`

Implemente uma classe `No` (com atributos `valor` e
`proximo`) e uma classe `ListaEncadeada` com os métodos
`adicionar(valor)` (insere no final) e `to_list()` (retorna os valores
da lista encadeada como uma lista Python).

### 19. Classe Matriz
**Arquivo:** `questao_19.py`

Crie uma classe `Matriz` que armazene uma matriz (lista de
listas) e implemente os métodos `somar(outra)` e `multiplicar(outra)`
para operações entre duas instâncias de `Matriz`.

### 20. Funcionários
**Arquivo:** `questao_20.py`

Crie uma classe base `Funcionario` com atributos `nome` e
`salario_base` e um método `calcular_salario()`. Crie as subclasses
`Gerente` (que recebe um bônus fixo) e `Vendedor` (que recebe comissão
sobre vendas), cada uma sobrescrevendo `calcular_salario()`.

### 21. Padrão Singleton
**Arquivo:** `questao_21.py`

Implemente uma classe `Configuracao` que siga o padrão
Singleton, garantindo que apenas uma única instância dessa classe
exista durante a execução do programa, independentemente de quantas
vezes seja instanciada.

### 22. Padrão Factory Method
**Arquivo:** `questao_22.py`

Implemente o padrão Factory Method para criação de
diferentes tipos de notificação (`NotificacaoEmail`,
`NotificacaoSMS`), todas seguindo uma interface comum `Notificacao`
com o método `enviar(mensagem)`. Crie uma classe `NotificacaoFactory`
com um método `criar(tipo)` que retorna a instância correta.

### 23. Classe Fração
**Arquivo:** `questao_23.py`

Crie uma classe `Fracao` com atributos `numerador` e
`denominador`. Implemente os métodos `somar(outra)`, `simplificar()`
(usando o MDC) e `__repr__` para exibir a fração no formato
"numerador/denominador".

### 24. Sistema de reserva de hotel
**Arquivo:** `questao_24.py`

Crie as classes `Quarto` (com `numero` e `disponivel`) e
`Hotel`, que gerencia uma lista de quartos e implementa os métodos
`reservar(numero)` e `liberar(numero)`, atualizando a disponibilidade
do quarto correspondente.

### 25. Árvore binária de busca
**Arquivo:** `questao_25.py`

Implemente uma classe `NoArvore` (com `valor`, `esquerda` e
`direita`) e uma classe `ArvoreBinariaBusca` com os métodos
`inserir(valor)` e `buscar(valor)` (retornando True/False).

### 26. Classe Temperatura
**Arquivo:** `questao_26.py`

Crie uma classe `Temperatura` que armazene um valor em
Celsius internamente e exponha properties `fahrenheit` e `kelvin`
(com getter e setter) para conversão automática entre as escalas.

### 27. Sistema de tarefas com Enum
**Arquivo:** `questao_27.py`

Utilizando `enum.Enum`, crie uma classe `StatusTarefa` com
os valores `PENDENTE`, `EM_ANDAMENTO` e `CONCLUIDA`. Crie uma classe
`Tarefa` com atributos `titulo` e `status`, e um método
`avancar_status()` que mova a tarefa para o próximo status da
sequência.

### 28. Iterador customizado
**Arquivo:** `questao_28.py`

Implemente uma classe `Contagem` que seja iterável,
implementando os métodos `__iter__` e `__next__`, permitindo iterar
sobre um intervalo de números de `inicio` até `fim` usando um laço
`for`.

### 29. Context manager customizado
**Arquivo:** `questao_29.py`

Implemente uma classe `CronometroContexto` que funcione
como um context manager (utilizando `__enter__` e `__exit__`),
medindo e imprimindo o tempo decorrido dentro de um bloco `with`.
Utilize o módulo `time` da biblioteca padrão.

### 30. Sistema de votação
**Arquivo:** `questao_30.py`

Crie as classes `Candidato` (com `nome` e `votos`) e `Urna`,
que gerencia uma lista de candidatos e implementa os métodos
`votar(nome_candidato)` e `resultado()` (retornando o nome do
candidato com mais votos).
