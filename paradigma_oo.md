# **Tutorial: Estudo de Orientação a Objetos em Java**

## **1. O que é Orientação a Objetos (OO)?**

A **Orientação a Objetos** (OO) é um paradigma de programação que organiza o software em torno de **objetos**, que são instâncias de **classes**. Cada objeto pode conter **dados** (também conhecidos como atributos ou propriedades) e **comportamentos** (também conhecidos como métodos ou funções).

Em OO, os principais conceitos incluem:

- **Classe**: Um molde ou template que define as propriedades e comportamentos de um objeto.
- **Objeto**: Uma instância de uma classe.
- **Atributo**: Propriedade ou dado que pertence a um objeto.
- **Método**: Função ou comportamento que pode ser chamado em um objeto.
- **Encapsulamento**: O processo de esconder a implementação interna de um objeto e expor apenas o necessário.
- **Herança**: Mecanismo que permite criar uma nova classe com base em uma classe existente.
- **Polimorfismo**: Capacidade de um objeto assumir muitas formas, permitindo que diferentes classes respondam de maneira diferente ao mesmo método.
- **Abstração**: O processo de ocultar os detalhes complexos e exibir apenas a funcionalidade essencial.

---

## **2. Conceitos Fundamentais em Java**

### **2.1. Classes e Objetos**

Uma **classe** em Java é definida com a palavra-chave `class` e é onde você define os atributos e métodos que um objeto da classe terá.

**Objeto** é uma instância de uma classe. Quando você cria um objeto, você está instanciando a classe.

#### Exemplo de Classe e Objeto em Java:


No vsCode abrir barra de comando
Crtl +Shift + P
depois digitar > Create Java Projeto na barra e indicar o local
Vamos escolher a pasta Carro

```java
class Carro {
    String modelo;  // Atributo
    String cor;     // Atributo
    int ano;        // Atributo

    // Método (Comportamento)
    void ligar() {
        System.out.println("O carro " + modelo + " está ligado.");
    }

    void desligar() {
        System.out.println("O carro " + modelo + " está desligado.");
    }
}

public class Main {
    public static void main(String[] args) {
        // Criando um objeto da classe Carro
        Carro meuCarro = new Carro();
        meuCarro.modelo = "Fusca";
        meuCarro.cor = "azul";
        meuCarro.ano = 1975;

        // Chamando métodos do objeto
        meuCarro.ligar();
        meuCarro.desligar();
    }
}
```

---

### **2.2. Encapsulamento**

**Encapsulamento** em Java é o processo de esconder a implementação interna de um objeto e expor apenas a interface pública necessária para interagir com o objeto. Isso é feito utilizando **modificadores de acesso** como `private`, `public`, `protected`.

#### Exemplo de Encapsulamento em Java:

```java
class ContaBancaria {
    private double saldo;  // Atributo privado

    public ContaBancaria(double saldoInicial) {
        saldo = saldoInicial;
    }

    // Método público para depositar
    public void depositar(double valor) {
        if (valor > 0) {
            saldo += valor;
            System.out.println("Depósito de R$" + valor + " realizado com sucesso.");
        } else {
            System.out.println("Valor de depósito inválido.");
        }
    }

    // Método público para sacar
    public void sacar(double valor) {
        if (valor > 0 && valor <= saldo) {
            saldo -= valor;
            System.out.println("Saque de R$" + valor + " realizado com sucesso.");
        } else {
            System.out.println("Saldo insuficiente ou valor inválido.");
        }
    }

    // Método público para mostrar o saldo
    public void mostrarSaldo() {
        System.out.println("Saldo atual: R$" + saldo);
    }
}

public class Main {
    public static void main(String[] args) {
        ContaBancaria minhaConta = new ContaBancaria(1000);
        minhaConta.depositar(500);
        minhaConta.sacar(300);
        minhaConta.mostrarSaldo();
    }
}
```

---

### **2.3. Herança**

**Herança** permite que uma classe herde atributos e métodos de outra classe. A classe que herda é chamada de **subclasse** e a classe que é herdada é chamada de **superclasse**. Em Java, a herança é feita utilizando a palavra-chave `extends`.

#### Exemplo de Herança em Java:

```java
class Animal {
    String nome;

    public Animal(String nome) {
        this.nome = nome;
    }

    public void fazerSom() {
        System.out.println("Som de animal.");
    }
}

class Cachorro extends Animal {  // Herança
    public Cachorro(String nome) {
        super(nome);
    }

    @Override
    public void fazerSom() {
        System.out.println(nome + " faz: Au Au!");
    }
}

class Gato extends Animal {  // Herança
    public Gato(String nome) {
        super(nome);
    }

    @Override
    public void fazerSom() {
        System.out.println(nome + " faz: Miau!");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal cachorro = new Cachorro("Rex");
        Animal gato = new Gato("Mimi");

        cachorro.fazerSom();  // Saída: Rex faz: Au Au!
        gato.fazerSom();      // Saída: Mimi faz: Miau!
    }
}
```

---

### **2.4. Polimorfismo**

**Polimorfismo** é a capacidade de uma classe derivada substituir ou redefinir um método de sua classe base. Em Java, isso pode ser feito usando **override**. Isso permite que diferentes tipos de objetos respondam de maneira diferente ao mesmo método.

#### Exemplo de Polimorfismo em Java:

```java
class Ave {
    public void voar() {
        System.out.println("A ave está voando.");
    }
}

class Pato extends Ave {
    @Override
    public void voar() {
        System.out.println("O pato está voando.");
    }
}

class Galinha extends Ave {
    @Override
    public void voar() {
        System.out.println("A galinha não pode voar.");
    }
}

public class Main {
    public static void main(String[] args) {
        Ave ave = new Ave();
        Pato pato = new Pato();
        Galinha galinha = new Galinha();

        ave.voar();       // Saída: A ave está voando.
        pato.voar();      // Saída: O pato está voando.
        galinha.voar();   // Saída: A galinha não pode voar.
    }
}
```

---

### **2.5. Abstração**

**Abstração** em Java é implementada com o uso de **classes abstratas** ou **interfaces**. Uma **classe abstrata** pode ter métodos abstratos (sem implementação) e métodos concretos (com implementação). Uma **interface** define apenas os métodos, sem implementar nenhum comportamento.

#### Exemplo de Abstração com Classe Abstrata:

```java
abstract class Forma {
    public abstract double calcularArea();  // Método abstrato
}

class Circulo extends Forma {
    private double raio;

    public Circulo(double raio) {
        this.raio = raio;
    }

    @Override
    public double calcularArea() {
        return Math.PI * raio * raio;
    }
}

class Retangulo extends Forma {
    private double largura;
    private double altura;

    public Retangulo(double largura, double altura) {
        this.largura = largura;
        this.altura = altura;
    }

    @Override
    public double calcularArea() {
        return largura * altura;
    }
}

public class Main {
    public static void main(String[] args) {
        Forma circulo = new Circulo(5);
        Forma retangulo = new Retangulo(4, 6);

        System.out.println("Área do círculo: " + circulo.calcularArea());
        System.out.println("Área do retângulo: " + retangulo.calcularArea());
    }
}
```

---

## **3. Melhores Práticas de OO em Java**

- **Use nomes claros e significativos** para classes, objetos, atributos e métodos.
- **Aplique os princípios SOLID** para garantir que seu código seja modular, reutilizável e fácil de manter.
- **Evite a duplicação de código** utilizando herança, interfaces e composição.
- **Gerencie a complexidade** dividindo o código em classes menores e mais especializadas.

---

## **4. Prática e Exercícios**

Agora que você tem a teoria e os exemplos prontos, é hora de praticar! Aqui estão alguns exercícios para você:

1. **Crie um sistema bancário simples** com as classes `ContaBancaria`, `Cliente` e `Transacao`.
2. **Modelar um sistema de zoológico** com as classes `Animal`, `Mamifero`, `Reptil`, e implementando o método `fazerSom()` para cada tipo de animal.
3. **Implemente um sistema de loja online** com as classes `Produto`, `CarrinhoDeCompras` e `Pedido`, onde o carrinho pode adicionar e remover produtos.

---

Este tutorial deve ajudá-lo a entender os principais conceitos de **Orientação a Objetos em Java**. A chave para dominar OO é **praticar** e aplicar os conceitos em projetos reais. Boa sorte nos estudos! 

---

### 🚀 [ricardotecpro.github.io](https://ricardotecpro.github.io/)
