#Desafio 1 - Classificador de Cliente (if / elif / else).

idade = int(input("Digite a idade do cliente: "))
renda = float(input("Digite a renda mensal (R$): ").replace(",", "."))

if idade >= 30 and renda >= 10000:
    categoria = "Diamante"
elif idade >= 25 and renda >= 5000:
    categoria = "Ouro"
elif idade >= 18 and renda >= 2500:
    categoria = "Prata"
else:
    categoria = "Bronze"

print(f"Cliente de {idade} anos com renda de R$ {renda:.2f}: categoria {categoria}.")
