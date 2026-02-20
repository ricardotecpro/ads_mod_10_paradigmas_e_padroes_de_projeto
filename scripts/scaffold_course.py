import os
from pathlib import Path

# --- Configuration ---
SYLLABUS = [
    # Módulo 1 – Fundamentos dos Paradigmas
    {"id": 1, "module": "Módulo 1 – Fundamentos", "title": "Introdução aos Paradigmas de Programação"},
    {"id": 2, "module": "Módulo 1 – Fundamentos", "title": "Paradigma Imperativo e Estruturado"},
    {"id": 3, "module": "Módulo 1 – Fundamentos", "title": "Paradigma Orientado a Objetos (POO)"},
    {"id": 4, "module": "Módulo 1 – Fundamentos", "title": "Paradigma Funcional"},
    
    # Módulo 2 – Comparação e Aplicação de Paradigmas
    {"id": 5, "module": "Módulo 2 – Comparação e Aplicação", "title": "Comparando Paradigmas na Prática"},
    {"id": 6, "module": "Módulo 2 – Comparação e Aplicação", "title": "Paradigmas Modernos e Multi-Paradigma"},
    {"id": 7, "module": "Módulo 2 – Comparação e Aplicação", "title": "Princípios de Projeto de Software"},
    {"id": 8, "module": "Módulo 2 – Comparação e Aplicação", "title": "Problemas Comuns de Design"},
    
    # Módulo 3 – Padrões Criacionais
    {"id": 9, "module": "Módulo 3 – Padrões Criacionais", "title": "Introdução aos Padrões de Projeto"},
    {"id": 10, "module": "Módulo 3 – Padrões Criacionais", "title": "Padrões Criacionais"},
    {"id": 11, "module": "Módulo 3 – Padrões Criacionais", "title": "Aplicando Padrões Criacionais em Projeto"},
    
    # Módulo 4 – Padrões Estruturais e Comportamentais
    {"id": 12, "module": "Módulo 4 – Estruturais e Comportamentais", "title": "Padrões Estruturais"},
    {"id": 13, "module": "Módulo 4 – Estruturais e Comportamentais", "title": "Padrões Comportamentais"},
    {"id": 14, "module": "Módulo 4 – Estruturais e Comportamentais", "title": "MVC e Arquitetura"},
    {"id": 15, "module": "Módulo 4 – Estruturais e Comportamentais", "title": "Refatoração com Padrões"},
    
    # Módulo 5 – Projeto Final
    {"id": 16, "module": "Módulo 5 – Projeto Final", "title": "Desenvolvimento de Mini Projeto"},
]

DIRS = [
    "docs/aulas",
    "docs/slides",
    "docs/quizzes",
    "docs/exercicios",
    "docs/projetos",
    "docs/assets/images"
]

# --- Templates ---

TEMPLATE_AULA = """# {title}

## 🎯 Objetivos da Aula
- [ ] Compreender os conceitos de {title}
- [ ] Aplicar exemplos práticos
- [ ] Desenvolver pensamento crítico sobre design de software

---

## 💡 Conceito
{title} é fundamental para...

!!! info "Definição"
    Breve explicação do conceito central da aula.

---

## 📊 Arquitetura e Fluxo

```mermaid
graph TD
    A[Início] --> B[Conceito]
    B --> C{{Decisão}}
    C -->|Sim| D[Aplicação]
    C -->|Não| E[Teoria]
```

---

## 💻 Exemplo Prático

```python
# Exemplo de código demonstrativo
def exemplo():
    pass
```

```termynal-exec
python aula-{id:02d}.py
Rodando exemplo da aula {id:02d}...
[OK] Sucesso!
```

!!! tip "Dica"
    Use este padrão para melhorar a manutenibilidade do seu código.

---

## 🚀 Mini-projeto
Nesta aula, iniciaremos...

---

## 📝 Exercícios
1. Explique como {title} resolve problemas de acoplamento.
2. Implemente um exemplo simplificado.

---

## 🎯 Próximos Passos

<div class="grid cards" markdown>

-   :material-presentation: **Slides**
    -   [Ver Slides da Aula](../slides/slide-{id:02d}.md)

-   :material-school: **Quiz**
    -   [Responder Quiz](../quizzes/quiz-{id:02d}.md)

-   :material-dumbbell: **Exercícios**
    -   [Lista de Exercícios](../exercicios/exercicio-{id:02d}.md)

-   :material-rocket: **Projeto**
    -   [Detalhamento do Projeto](../projetos/projeto-{id:02d}.md)

</div>
"""

TEMPLATE_SLIDE = """---
theme: material
---

# {title}
## Aula {id:02d} 🚀

---

## 🎯 Objetivos
- Entender o paradigma/padrão
- Ver aplicações reais
- Exercitar a modelagem

---

## 🧠 Introdução
{title} nos permite...

---

## 📊 Visualização

```mermaid
graph LR
    P[Problema] --> S[Solução via {title}]
```

---

## 💻 Código

```python
# Trecho de exemplo
class Exemplo:
    pass
```

---

## 💡 Conclusão
- Ponto 1
- Ponto 2

---

<!-- _class: lead -->
# Próxima Aula: ...
"""

TEMPLATE_QUIZ = """# Quiz {id:02d}: {title}

**Teste seus conhecimentos sobre {title}.**

1. O que define {title}?
    - ( ) Opção A
    - (x) Opção B (Correta)
    - ( ) Opção C
    - ( ) Opção D

    !!! success "Explicação"
        A opção B é a correta porque...

(Repetir até 10 perguntas)
"""

TEMPLATE_EXERCICIO = """# Exercícios Aula {id:02d}: {title}

---

### 🟢 Básico
1. Defina o conceito de {title}.
2. Dê um exemplo do dia a dia.

### 🟡 Intermediário
3. Compare {title} com outra abordagem.
4. Refatore um código simples usando {title}.

### 🔴 Desafio
5. Projete um sistema pequeno que utilize {title} de forma eficiente.
"""

TEMPLATE_PROJETO = """# Projeto Aula {id:02d}: {title}

## 📝 Descrição
Neste projeto, você deve...

## 🎯 Requisitos
- [ ] Aplicar o conceito de {title}
- [ ] Código limpo e comentado

## 💡 Sugestão
Tente integrar com o que aprendemos na aula anterior.
"""

TEMPLATE_INDEX = """# 📘 Paradigmas de Programação e Padrões de Projeto

Bem-vindo ao curso avançado de arquitetura e design de software.

## 🚀 Comece por aqui
Este curso é focado em transformar sua forma de pensar sobre código.

<div class="grid cards" markdown>

-   :material-rocket: **Módulo 1: Fundamentos**
    -   [Aula 01: Introdução](aulas/aula-01.md)
    -   [Aula 02: Imperativo](aulas/aula-02.md)
    -   [Aula 03: POO](aulas/aula-03.md)
    -   [Aula 04: Funcional](aulas/aula-04.md)

-   :material-school: **Materiais**
    -   [Plano de Ensino](plano-ensino.md)
    -   [Sobre o Curso](sobre.md)

</div>
"""

# --- Execution ---

def create_files():
    # 1. Ensure Directories
    for d in DIRS:
        Path(d).mkdir(parents=True, exist_ok=True)
    
    # 2. Create Index if missing
    if not Path("docs/index.md").exists():
        Path("docs/index.md").write_text(TEMPLATE_INDEX, encoding="utf-8")
        print("Created index.md")

    # 3. Generate Content
    for lesson in SYLLABUS:
        lid = lesson["id"]
        title = lesson["title"]
        
        # Paths
        p_aula = Path(f"docs/aulas/aula-{lid:02d}.md")
        p_slide = Path(f"docs/slides/slide-{lid:02d}.md")
        p_quiz = Path(f"docs/quizzes/quiz-{lid:02d}.md")
        p_exerc = Path(f"docs/exercicios/exercicio-{lid:02d}.md")
        p_proj = Path(f"docs/projetos/projeto-{lid:02d}.md")
        
        # Write Files
        p_aula.write_text(TEMPLATE_AULA.format(id=lid, title=title), encoding="utf-8")
        p_slide.write_text(TEMPLATE_SLIDE.format(id=lid, title=title), encoding="utf-8")
        p_quiz.write_text(TEMPLATE_QUIZ.format(id=lid, title=title), encoding="utf-8")
        p_exerc.write_text(TEMPLATE_EXERCICIO.format(id=lid, title=title), encoding="utf-8")
        p_proj.write_text(TEMPLATE_PROJETO.format(id=lid, title=title), encoding="utf-8")
            
        print(f"Generated Lesson {lid:02d}: {title}")

def generate_nav_yaml():
    nav = ["nav:", "  - Início: index.md"]
    
    nav.append("  - Aulas:")
    nav.append("      - aulas/index.md")
    
    current_module = None
    
    for lesson in SYLLABUS:
        module = lesson["module"]
        title = lesson["title"]
        lid = lesson["id"]
        filename = f"aulas/aula-{lid:02d}.md"
        
        if module != current_module:
            nav.append(f"      - {module}:")
            current_module = module
        
        nav.append(f"        - 'Aula {lid:02d} - {title}': {filename}")
    
    nav.append("  - Materiais:")
    nav.append("      - materiais.md")
    nav.append("      - Slides: slides/index.md")
    nav.append("      - Exercícios: exercicios/index.md")
    nav.append("      - Quizzes: quizzes/")
    nav.append("      - Projetos: projetos/")
    nav.append("      - Setups: setups/index.md")
    nav.append("  - Impressão: print_page.md")
    
    return "\n".join(nav)

def update_mkdocs():
    mkdocs_path = Path("mkdocs.yml")
    content = mkdocs_path.read_text(encoding="utf-8")
    
    # Remove existing 'nav:' if present (simplistic approach, assumes nav is at end or distinct)
    # We will append the new nav
    # Better: finding where nav starts
    
    if "nav:" in content:
        content = content.split("nav:")[0] # Truncate everything after nav:
    
    new_nav = generate_nav_yaml()
    
    final_content = content.strip() + "\n\n" + new_nav + "\n"
    mkdocs_path.write_text(final_content, encoding="utf-8")
    print("Updated mkdocs.yml navigation")

if __name__ == "__main__":
    create_files()
    update_mkdocs()
