#Módulo calculadora: operações matemáticas básicas.
def somar(primeiro_numero, segundo_numero):
    """Retorna a soma de dois números."""
    return primeiro_numero + segundo_numero
def subtrair(primeiro_numero, segundo_numero):
    """Retorna a subtração do segundo número pelo primeiro."""
    return primeiro_numero - segundo_numero
def multiplicar(primeiro_numero, segundo_numero):
    """Retorna o produto de dois números."""
    return primeiro_numero * segundo_numero
def dividir(dividendo, divisor):
    """Retorna a divisão de dois números.
    Se o divisor for zero, exibe uma mensagem de erro e retorna None,
    sem quebrar o programa.
    """
    if divisor == 0:
        print("Erro: não é possível dividir por zero.")
        return None
    return dividendo / divisor
if __name__ == "__main__":
    # Bloco de teste: só roda quando o arquivo é executado diretamente.
    print(somar(2, 3))        # 5
    print(subtrair(10, 4))    # 6
    print(multiplicar(3, 4))  # 12
    print(dividir(10, 4))     # 2.5
    print(dividir(1, 0))      # mensagem de erro e None
