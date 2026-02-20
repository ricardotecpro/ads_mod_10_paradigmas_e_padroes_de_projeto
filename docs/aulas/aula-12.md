# Aula 12: Padrões Estruturais 🔗

## 🎯 Objetivos da Aula
- [x] Conhecer os padrões Adapter, Composite, Decorator e Facade.
- [x] Aprender a harmonizar interfaces incompatíveis.
- [x] Representar hierarquias de objetos "parte-todo".
- [x] Adicionar responsabilidades a objetos dinamicamente.

---

## 💡 O que são Padrões Estruturais?

Eles lidam com a composição de classes e objetos para formar estruturas maiores e mais complexas. Eles ajudam a garantir que, quando uma parte muda, a estrutura inteira não precise ser alterada.

---

## 🧱 Destaques Estruturais

### 1. Adapter (Adaptador) 🔌
Converte a interface de uma classe em outra interface que os clientes esperam.
*Exemplo: Conectar um sistema novo em um banco de dados legado.*

### 2. Composite (Composição) 🌳
Compõe objetos em estruturas de árvore para representar hierarquias. Permite tratar objetos individuais e composições de forma uniforme.

### 3. Decorator (Decorador) 🎀
Adiciona comportamento a um objeto individual, estaticamente ou dinamicamente, sem afetar o comportamento de outros objetos da mesma classe.

---

## 📊 Diagrama: Adapter

```mermaid
graph LR
    Client[Cliente] --> ITarget[Interface Alvo]
    ITarget --> Adapter[Adapter]
    Adapter --> Adaptee[Sistema Legado]
```

---

## 💻 Exemplo: Decorator em Python

```python
class Cafe:
    def custo(self):
        return 5

class LeiteDecorator:
    def __init__(self, cafe):
        self._cafe = cafe
    
    def custo(self):
        return self._cafe.custo() + 2

meu_cafe = Cafe()
meu_cafe_com_leite = LeiteDecorator(meu_cafe)

print(f"Custo total: {meu_cafe_com_leite.custo()}")
```

```termynal-exec
python aula-12-decorator.py
Custo total: 7
```

---

## 🧠 Blocos de Destaque

!!! concept "Facade (Fachada)"
    Fornece uma interface simplificada para um conjunto complexo de classes em um subsistema. É como o painel de um carro: você vira a chave (facade) e muitos sistemas complexos funcionam por trás sem você ver.

!!! info "Proxy"
    Atua como um substituto ou porta-voz de outro objeto para controlar o acesso a ele.

---

## 🚀 Mini-projeto: Sistema de Arquivos
Use o padrão **Composite** para criar uma estrutura de Pastas e Arquivos, onde uma Pasta pode conter tanto Arquivos quanto outras Pastas, e todos podem ser "listados" da mesma forma.

---

## 🎯 Próximos Passos

<div class="grid cards" markdown>

-   :material-presentation: **Slides**
    -   [Ver Slides da Aula](../slides/slide-12.md)

-   :material-school: **Quiz**
    -   [Responder Quiz](../quizzes/quiz-12.md)

-   :material-dumbbell: **Exercícios**
    -   [Lista de Exercícios](../exercicios/exercicio-12.md)

-   :material-rocket: **Projeto**
    -   [Detalhamento do Projeto](../projetos/projeto-12.md)

</div>
