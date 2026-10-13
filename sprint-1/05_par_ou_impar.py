# ---------------------------------------------------------------
# Desafio 5 - Par ou ímpar
# ---------------------------------------------------------------
print("\n=== Desafio 5: Par ou ímpar ===")
numero = int(input("Digite um número inteiro: "))

resto = numero % 2
resultado = "par" if resto == 0 else "ímpar"

print(f"O número {numero} é {resultado}.")
