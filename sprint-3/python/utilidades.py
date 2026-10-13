#Módulo utilidades: funções dos desafios da Prática Independente.
# Conversor de temperatura
def celsius_para_fahrenheit(celsius):
    """Converte graus Celsius para Fahrenheit."""
    return celsius * 9 / 5 + 32
def fahrenheit_para_celsius(fahrenheit):
    """Converte graus Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5 / 9
def celsius_para_kelvin(celsius):
    """Converte graus Celsius para Kelvin."""
    return celsius + 273.15

# Validador de senha
def validar_senha(senha, tamanho_minimo=8):
    """Valida uma senha.

    Regras: tamanho mínimo (padrão 8), ao menos uma letra maiúscula,
    uma minúscula e um dígito. Retorna True se válida, False se não.
    """
    tem_tamanho = len(senha) >= tamanho_minimo
    tem_maiuscula = any(caractere.isupper() for caractere in senha)
    tem_minuscula = any(caractere.islower() for caractere in senha)
    tem_digito = any(caractere.isdigit() for caractere in senha)
    return tem_tamanho and tem_maiuscula and tem_minuscula and tem_digito

# Caixa
def caixa(*precos):
    """Soma um número variável de preços (recebidos como tupla).

    Sem argumentos, retorna 0.
    """
    return sum(precos)

# Ficha do aluno
def ficha_aluno(nome, **dados):
    """Monta a ficha de um aluno com os dados extras recebidos (dicionário)."""
    linhas = [f"Aluno: {nome}"]
    for campo, valor in dados.items():
        linhas.append(f"  {campo.capitalize()}: {valor}")
    return "\n".join(linhas)

# Lista segura (cópia defensiva)
def adicionar_item_seguro(lista_original, novo_item):
    """Retorna uma NOVA lista com o item adicionado.

    A lista original não é alterada (cópia defensiva).
    """
    nova_lista = list(lista_original)  # cópia: outra lista na memória
    nova_lista.append(novo_item)
    return nova_lista

# Fatorial recursivo
def fatorial(numero):
    """Calcula o fatorial de um inteiro não negativo de forma recursiva."""
    if numero < 0:
        raise ValueError("O fatorial não é definido para números negativos.")
    if numero <= 1:  
        return 1
    return numero * fatorial(numero - 1)
  
#Relatório
def relatorio(titulo, *linhas, **config):
    """Monta um relatório de texto.

    Configurações opcionais (**config):
      largura (int, padrão 40), borda (str, padrão "="),
      numerar (bool, padrão True), maiusculo (bool, padrão False).
    """
    largura = config.get("largura", 40)
    borda = config.get("borda", "=")
    numerar = config.get("numerar", True)
    if config.get("maiusculo", False):
        titulo = titulo.upper()

    partes = [borda * largura, titulo.center(largura), borda * largura]
    for numero, linha in enumerate(linhas, start=1):
        partes.append(f"{numero}. {linha}" if numerar else linha)
    partes.append(borda * largura)
    return "\n".join(partes)

if __name__ == "__main__":
    print(celsius_para_fahrenheit(100))      # 212.0
    print(validar_senha("Python123"))        # True
    print(caixa(10.5, 20, 5.25))             # 35.75
    print(ficha_aluno("Ana", idade=20, curso="ADS"))
    original = [1, 2, 3]
    print(adicionar_item_seguro(original, 4), original)  # [1,2,3,4] [1,2,3]
    print(fatorial(5))                       # 120
