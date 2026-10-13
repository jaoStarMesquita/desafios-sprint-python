
"""Sprint 5 - Sistema de Análise de Dados."""

import csv
import re
from datetime import datetime


class FormatoInvalidoError(Exception):
    """Exceção para formatos de dados inválidos."""
    pass


def validar_email(email):
    """Valida o formato do e-mail."""
    padrao = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

    if not re.fullmatch(padrao, email):
        raise FormatoInvalidoError("E-mail inválido.")


def validar_cpf(cpf):
    """Valida o formato do CPF."""
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"

    if not re.fullmatch(padrao, cpf):
        raise FormatoInvalidoError("CPF inválido.")


def validar_telefone(telefone):
    """Valida o formato do telefone."""
    padrao = r"^\(?\d{2}\)?\s?9?\d{4}-?\d{4}$"

    if not re.fullmatch(padrao, telefone):
        raise FormatoInvalidoError("Telefone inválido.")


def validar_data(data):
    """Valida o formato e a existência da data."""
    if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", data):
        raise FormatoInvalidoError("Formato de data inválido.")

    try:
        datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        raise FormatoInvalidoError("Data inexistente.")


def validar_registro(registro):
    """Valida os dados de um registro."""
    erros = []

    try:
        nome = registro["nome"].strip()
        email = registro["email"].strip()
        cpf = registro["cpf"].strip()
        telefone = registro["telefone"].strip()
        data = registro["data"].strip()

        if not nome:
            erros.append("Nome vazio.")

        validacoes = [
            ("E-mail", validar_email, email),
            ("CPF", validar_cpf, cpf),
            ("Telefone", validar_telefone, telefone),
            ("Data", validar_data, data)
        ]

        for campo, funcao, valor in validacoes:
            try:
                funcao(valor)
            except FormatoInvalidoError as erro:
                erros.append(f"{campo}: {erro}")

    except KeyError as erro:
        raise KeyError(f"Coluna ausente: {erro.args[0]}")

    return erros


def analisar_arquivo(nome_arquivo):
    """Lê o CSV e separa os registros válidos e inválidos."""
    validos = []
    invalidos = []
    mensagens = []

    try:
        with open(nome_arquivo, "r", encoding="utf-8", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)

            colunas = {"nome", "email", "cpf", "telefone", "data"}

            if leitor.fieldnames is None:
                raise ValueError("Arquivo vazio ou sem cabeçalho.")

            faltantes = colunas - set(leitor.fieldnames)

            if faltantes:
                raise KeyError(f"Colunas ausentes: {', '.join(sorted(faltantes))}")

            for numero, registro in enumerate(leitor, start=2):
                erros = validar_registro(registro)

                resultado = {
                    "linha": numero,
                    "dados": registro,
                    "erros": erros
                }

                if erros:
                    invalidos.append(resultado)
                else:
                    validos.append(resultado)

    except FileNotFoundError:
        mensagens.append("Erro: arquivo não encontrado.")

    except ValueError as erro:
        mensagens.append(f"Erro de valor: {erro}")

    except KeyError as erro:
        mensagens.append(f"Erro no arquivo CSV: {erro}")

    except OSError as erro:
        mensagens.append(f"Erro ao acessar o arquivo: {erro}")

    else:
        mensagens.append("Arquivo processado com sucesso.")

    finally:
        mensagens.append("Leitura do arquivo finalizada.")

    return validos, invalidos, mensagens


def gerar_relatorio(validos, invalidos, mensagens):
    """Gera o relatório final da análise."""
    total = len(validos) + len(invalidos)

    if total > 0:
        percentual = len(validos) / total * 100
    else:
        percentual = 0

    linhas = [
        "=" * 50,
        f"{'RELATÓRIO DE ANÁLISE DE DADOS':^50}",
        "=" * 50,
        f"Total de registros: {total}",
        f"Registros válidos: {len(validos)}",
        f"Registros inválidos: {len(invalidos)}",
        f"Percentual válido: {percentual:.1f}%",
        "",
        "REGISTROS VÁLIDOS",
        "-" * 50
    ]

    if validos:
        for registro in validos:
            linhas.append(
                f"Linha {registro['linha']}: {registro['dados']['nome']}"
            )
    else:
        linhas.append("Nenhum registro válido.")

    linhas.extend(["", "REGISTROS INVÁLIDOS", "-" * 50])

    if invalidos:
        for registro in invalidos:
            linhas.append(f"Linha {registro['linha']}:")

            for erro in registro["erros"]:
                linhas.append(f"  - {erro}")
    else:
        linhas.append("Nenhum registro inválido.")

    linhas.extend(["", "MENSAGENS", "-" * 50])
    linhas.extend(mensagens)
    linhas.append("=" * 50)

    return "\n".join(linhas)


def main():
    """Executa o programa."""
    validos, invalidos, mensagens = analisar_arquivo("dados.csv")

    relatorio = gerar_relatorio(validos, invalidos, mensagens)
    print(relatorio)

    try:
        with open("relatorio.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(relatorio)

    except OSError as erro:
        print(f"Erro ao salvar relatório: {erro}")

    else:
        print("Relatório salvo com sucesso.")

    finally:
        print("Programa finalizado.")


if __name__ == "__main__":
    main()
