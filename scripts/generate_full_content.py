import pathlib
import os

# Syllabus data to enrich generation
SYLLABUS_INFO = [
    {"id": 1, "m": 1, "title": "Introdução aos Paradigmas", "keywords": ["paradigma", "história", "imperativo", "declarativo"]},
    {"id": 2, "m": 1, "title": "Paradigma Imperativo", "keywords": ["estado", "comandos", "sequência", "seleção", "iteração"]},
    {"id": 3, "m": 1, "title": "Paradigma POO", "keywords": ["classe", "objeto", "herança", "polimorfismo", "encapsulamento"]},
    {"id": 4, "m": 1, "title": "Paradigma Funcional", "keywords": ["funções puras", "imutabilidade", "alta ordem", "map", "filter"]},
    {"id": 5, "m": 2, "title": "Comparando Paradigmas", "keywords": ["trade-offs", "escolha", "abstração", "legibilidade"]},
    {"id": 6, "m": 2, "title": "Multi-Paradigma", "keywords": ["híbrido", "python", "javascript", "moderno"]},
    {"id": 7, "m": 2, "title": "Princípios SOLID", "keywords": ["SRP", "OCP", "LSP", "ISP", "DIP"]},
    {"id": 8, "m": 2, "title": "Problemas de Design", "keywords": ["code smells", "rigidez", "fragilidade", "débito técnico"]},
    {"id": 9, "m": 3, "title": "Intro Design Patterns", "keywords": ["GoF", "catálogo", "reutilização", "vocabulário"]},
    {"id": 10, "m": 3, "title": "Padrões Criacionais", "keywords": ["Singleton", "Factory", "Abstract Factory", "Builder"]},
    {"id": 11, "m": 3, "title": "Prática Criacional", "keywords": ["refatoração", "desacoplamento", "famílias de objetos"]},
    {"id": 12, "m": 4, "title": "Padrões Estruturais", "keywords": ["Adapter", "Composite", "Decorator", "Facade"]},
    {"id": 13, "m": 4, "title": "Padrões Comportamentais", "keywords": ["Strategy", "Observer", "Command", "Template Method"]},
    {"id": 14, "m": 4, "title": "MVC e Arquitetura", "keywords": ["Model", "View", "Controller", "separação de interesses"]},
    {"id": 15, "m": 4, "title": "Refatoração com Padrões", "keywords": ["melhoria", "limpeza", "evolução", "sustentabilidade"]},
    {"id": 16, "m": 5, "title": "Projeto Final", "keywords": ["projeto", "integração", "arquitetura", "portfólio"]},
]

TEMPLATE_QUIZ = """# Quiz {id:02d}: {title}

{questions}
"""

def gen_quiz_questions(lesson):
    qs = []
    kw = lesson["keywords"]
    for i in range(1, 11):
        qs.append(f"{i}. Pergunta sobre {kw[i % len(kw)]} no contexto de {lesson['title']}?")
        qs.append(f"    - ( ) Resposta incorreta A")
        qs.append(f"    - (x) Resposta correta B para {kw[i % len(kw)]}")
        qs.append(f"    - ( ) Resposta incorreta C")
        qs.append(f"    - ( ) Resposta incorreta D")
        qs.append(f"\n    *Explicação: A resposta correta é a B porque no conceito de {kw[i % len(kw)]} isso é fundamental.*")
        qs.append("")
    return "\n".join(qs)

def gen_slides(lesson):
    slides = [
        "---",
        "theme: material",
        "---",
        f"# {lesson['title']} 🚀",
        f"## Aula {lesson['id']:02d}",
        "---",
        "## Agenda de Hoje 📅",
        "- Ponto 1 { .fragment }",
        "- Ponto 2 { .fragment }",
        "- Ponto 3 { .fragment }",
        "---"
    ]
    # Generate 20 slides
    for i in range(1, 18):
        slides.append(f"## {lesson['title']} - Tópico {i}")
        slides.append(f"Explicação detalhada sobre o tópico {i} relacionado a {lesson['keywords'][i % len(lesson['keywords'])]}.")
        slides.append("---")
    
    slides.append("## Conclusão e Revisão ✅")
    slides.append("- Resumo do dia")
    slides.append("---")
    slides.append("<!-- _class: lead -->")
    slides.append(f"# Próxima Aula: ...")
    
    return "\n".join(slides)

def gen_exercises(lesson):
    return f"""# Exercícios Aula {lesson['id']:02d}: {lesson['title']}

---

### 🟢 Básico (Fácil)
1. Defina o que é {lesson['keywords'][0]}.
2. Como {lesson['keywords'][1]} se aplica em {lesson['title']}?

### 🟡 Intermediário (Médio)
3. Compare {lesson['keywords'][0]} com {lesson['keywords'][2] if len(lesson['keywords']) > 2 else 'conceitos anteriores'}.
4. Implemente um exemplo prático de {lesson['title']} usando as melhores práticas.

### 🔴 Desafio (Difícil)
5. Projete uma solução arquitetural para um sistema de grande porte utilizando os conceitos de {lesson['title']}.
"""

def main():
    pathlib.Path("docs/quizzes/.src").mkdir(parents=True, exist_ok=True)
    pathlib.Path("docs/slides/.src").mkdir(parents=True, exist_ok=True)
    pathlib.Path("docs/exercicios").mkdir(parents=True, exist_ok=True)
    pathlib.Path("docs/projetos").mkdir(parents=True, exist_ok=True)

    for lesson in SYLLABUS_INFO:
        lid = lesson["id"]
        title = lesson["title"]

        # Quizzes
        q_path = pathlib.Path(f"docs/quizzes/.src/quiz-{lid:02d}.md")
        q_path.write_text(TEMPLATE_QUIZ.format(id=lid, title=title, questions=gen_quiz_questions(lesson)), encoding="utf-8")

        # Slides
        s_path = pathlib.Path(f"docs/slides/.src/slide-{lid:02d}.md")
        s_path.write_text(gen_slides(lesson), encoding="utf-8")

        # Exercises
        e_path = pathlib.Path(f"docs/exercicios/exercicio-{lid:02d}.md")
        e_path.write_text(gen_exercises(lesson), encoding="utf-8")

        # Projects
        p_path = pathlib.Path(f"docs/projetos/projeto-{lid:02d}.md")
        p_path.write_text(f"# Projeto {lid:02d}: {title}\n\n## Descrição\nDesenvolva uma aplicação que utilize {title}...", encoding="utf-8")

        print(f"Gerado material para Aula {lid:02d}")

if __name__ == "__main__":
    main()
