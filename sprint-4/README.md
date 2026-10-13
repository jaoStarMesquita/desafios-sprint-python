# Sprint 4 — Sistema de Análise de Produtos

## Objetivo

Desenvolver um sistema de cadastro e análise de produtos, utilizando listas, tuplas, conjuntos e operações de ordenação e filtragem em Python.

## Funcionalidades

- **Cadastro de produtos:** recebe nome, preço e categoria e armazena os dados em uma lista.
- **Filtragem por preço:** identifica produtos acima ou abaixo de um valor de referência.
- **Ordenação crescente:** organiza os produtos do menor para o maior preço.
- **Ordenação decrescente:** organiza os produtos do maior para o menor preço.
- **Categorias únicas:** utiliza conjuntos para eliminar categorias repetidas.
- **Estatísticas:** calcula o menor preço, o maior preço e a média dos preços.
- **Relatório final:** apresenta os produtos, os filtros, as categorias e as estatísticas.
- **Operações com conjuntos:** demonstra união, interseção, diferença e diferença simétrica entre categorias.

## Conceitos praticados

- Listas para armazenar coleções de produtos.
- Tuplas para representar produtos e agrupar estatísticas.
- Conjuntos (`set`) para eliminar duplicatas.
- Métodos `append()` e `sort()`.
- Função `sorted()` com `reverse=True`.
- Funções e parâmetros.
- Laços de repetição.
- Filtragem de dados.
- Operações de conjuntos: `|`, `&`, `-` e `^`.
- Formatação de relatórios com f-strings.
- Validação de preços.

## Organização dos arquivos

```text
sprint-4/
├── python/
│   └── sistema_produtos.py
└── portugol/
    └── sistema_produtos.por
```

## Como executar

Na raiz do repositório, execute:

```bash
python sprint-4/python/sistema_produtos.py
```

O programa solicitará os produtos, seus preços e suas categorias. Depois, solicitará um valor de referência e apresentará o relatório de análise.

## Objetivo de aprendizagem

Compreender como diferentes estruturas de dados podem ser combinadas para organizar, filtrar, ordenar e analisar informações.

---

Projeto desenvolvido como parte das atividades práticas de programação da Sprint 4.
