# Sprint 3 — Funções e Modularização em Python

## Objetivo

Desenvolver programas modulares utilizando funções, importação de módulos, parâmetros variáveis, tratamento de listas e recursividade.

## Funcionalidades

- **Calculadora:** realiza operações matemáticas por meio de funções reutilizáveis.
- **Utilidades:** reúne funções para conversão de temperatura, validação de senha, cálculo de caixa e montagem de ficha de aluno.
- **Programa principal:** importa e utiliza funções de diferentes módulos para demonstrar a reutilização de código.
- **Lista segura:** adiciona elementos sem modificar a lista original.
- **Estatísticas:** calcula medidas como média, mediana e moda.
- **Fatorial recursivo:** calcula o fatorial utilizando uma função que chama a si mesma.
- **Relatório:** gera um relatório de texto com parâmetros variáveis e configurações opcionais.

## Conceitos praticados

- Definição e chamada de funções com `def`.
- Parâmetros e valores de retorno com `return`.
- Documentação de funções com docstrings.
- Importação e reutilização de módulos com `import`.
- Argumentos variáveis com `*args` e `**kwargs`.
- Cópia defensiva de listas.
- Recursividade.
- Organização do código em módulos.
- Boas práticas de nomenclatura com `snake_case`.
- Uso de `if __name__ == "__main__":`.

## Organização dos arquivos

```text
sprint-3/
├── python/
│   ├── calculadora.py
│   ├── utilidades.py
│   ├── main.py
│   ├── lista_segura.py
│   └── estatistica.py
└── portugol/
    └── exercícios equivalentes em arquivos separados
```

## Como executar

Na raiz do repositório, execute:

```bash
python sprint-3/python/main.py
```

O programa principal importa os módulos e demonstra o funcionamento das funções implementadas.

## Objetivo de aprendizagem

Aprender a dividir um programa em partes menores, facilitar a manutenção do código e reutilizar funções em diferentes situações.

---

Projeto desenvolvido como parte das atividades práticas de programação da Sprint 3.
