# Paradigma Funcional: Conceitos e Exemplos

O paradigma funcional pode ser aplicado em várias linguagens, tanto em linguagens puramente funcionais (como Haskell) quanto em linguagens multi-paradigma (como Python e JavaScript). Vamos explorar alguns conceitos com exemplos em diferentes linguagens.

---

## **1. Funções Puras**

Uma **função pura** sempre retorna o mesmo resultado para os mesmos argumentos e não altera estados externos.

### **Exemplo em Haskell** (linguagem puramente funcional)

```haskell
soma :: Int -> Int -> Int
soma x y = x + y
```

📌 A função `soma` sempre retorna o mesmo valor para os mesmos parâmetros.

### **Exemplo em JavaScript**

```javascript
const soma = (x, y) => x + y;
console.log(soma(2, 3)); // 5
```

---

## **2. Imutabilidade**

No paradigma funcional, os dados são imutáveis, ou seja, não são modificados após a criação.

### **Exemplo em Python**

```python
from typing import List

def adicionar_elemento(lista: List[int], elemento: int) -> List[int]:
    return lista + [elemento]

lista_original = [1, 2, 3]
nova_lista = adicionar_elemento(lista_original, 4)

print(lista_original)  # [1, 2, 3] (permanece inalterada)
print(nova_lista)      # [1, 2, 3, 4]
```

📌 `adicionar_elemento` não altera `lista_original`, mas retorna uma nova lista.

---

## **3. Funções de Alta Ordem**

Funções de alta ordem são aquelas que recebem ou retornam outras funções.

### **Exemplo em JavaScript**

```javascript
const dobrar = (x) => x * 2;
const mapear = (fn, lista) => lista.map(fn);

console.log(mapear(dobrar, [1, 2, 3])); // [2, 4, 6]
```

📌 `mapear` recebe uma função `dobrar` como argumento e a aplica em todos os elementos da lista.

### **Exemplo em Scala**

```scala
val dobrar = (x: Int) => x * 2
val numeros = List(1, 2, 3)
val resultado = numeros.map(dobrar)

println(resultado) // List(2, 4, 6)
```

---

## **4. Recursão**

O paradigma funcional evita loops e usa recursão.

### **Exemplo em Haskell**

```haskell
fatorial :: Int -> Int
fatorial 0 = 1
fatorial n = n * fatorial (n - 1)

print (fatorial 5) -- 120
```

### **Exemplo em Python**

```python
def fatorial(n):
    return 1 if n == 0 else n * fatorial(n - 1)

print(fatorial(5))  # 120
```

---

## **5. Avaliação Preguiçosa**

Algumas linguagens funcionais avaliam expressões apenas quando necessário.

### **Exemplo em Haskell**

```haskell
numeros = [1..]  -- Lista infinita
pares = filter even numeros
print (take 5 pares)  -- [2, 4, 6, 8, 10]
```

📌 A lista `numeros` é infinita, mas apenas os primeiros 5 números pares são avaliados.

### **Exemplo em Python (com geradores)**

```python
def numeros_pares():
    n = 2
    while True:
        yield n
        n += 2

pares = numeros_pares()
print([next(pares) for _ in range(5)])  # [2, 4, 6, 8, 10]
```

📌 O gerador `numeros_pares` cria números conforme necessário, sem armazenar todos na memória.

---

## **6. Composição de Funções**

No paradigma funcional, várias funções podem ser combinadas.

### **Exemplo em JavaScript**

```javascript
const dobrar = (x) => x * 2;
const incrementar = (x) => x + 1;

const dobrarEIncrementar = (x) => incrementar(dobrar(x));

console.log(dobrarEIncrementar(3)); // (3 * 2) + 1 = 7
```

### **Exemplo em F#**

```fsharp
let dobrar x = x * 2
let incrementar x = x + 1

let resultado = (dobrar >> incrementar) 3
printfn "%d" resultado  // 7
```

📌 O operador `>>` compõe funções, aplicando `dobrar` e depois `incrementar`.

---

## **Conclusão**

O paradigma funcional foca em **funções puras**, **imutabilidade** e **composição de funções**, o que ajuda a escrever código mais previsível e seguro. Embora algumas linguagens como **Haskell, F# e Clojure** sejam totalmente funcionais, linguagens como **Python, JavaScript e Scala** permitem a adoção de conceitos funcionais.

Se quiser mais exemplos em uma linguagem específica, posso aprofundar! 🚀

---

### 🚀 [ricardotecpro.github.io](https://ricardotecpro.github.io/)
