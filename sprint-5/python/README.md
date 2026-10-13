
# Sprint 5 - Analisador de Dados

## Objetivo

Desenvolver um programa em Python para ler arquivos CSV, validar informações utilizando expressões regulares e tratar exceções.

## Funcionalidades

- Leitura de arquivos CSV utilizando `csv.DictReader`.
- Validação de e-mail, CPF, telefone e data com Regex.
- Tratamento de exceções nativas e personalizadas.
- Separação dos registros válidos e inválidos.
- Geração de relatório utilizando f-strings.
- Salvamento do relatório em arquivo TXT.

## Validações

- E-mail: verifica a estrutura básica do endereço.
- CPF: verifica o formato `000.000.000-00`.
- Telefone: verifica o formato com DDD.
- Data: verifica o formato `DD/MM/AAAA` e se a data existe.

A validação do CPF verifica apenas o formato, não os dígitos verificadores.

## Exceções utilizadas

- `FileNotFoundError`: arquivo não encontrado.
- `ValueError`: arquivo sem cabeçalho ou erro de valor.
- `KeyError`: coluna obrigatória ausente.
- `OSError`: erro de acesso ou gravação.
- `FormatoInvalidoError`: exceção personalizada para dados inválidos.

O programa utiliza `try`, `except`, `else` e `finally` para controlar os erros durante o processamento.

## Como executar

Entre na pasta `python` e execute:

```bash
python analisador_dados.py
```

O programa lê `dados.csv`, exibe o relatório no terminal e gera `relatorio.txt`.

## Arquivos

- `python/analisador_dados.py`: código principal.
- `python/dados.csv`: dados de exemplo.
- `python/relatorio.txt`: relatório gerado durante a execução.
