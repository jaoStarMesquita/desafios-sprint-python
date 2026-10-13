#Desafio 3 - Análise de Números (for).
soma = 0
maior = 0
menor = 0

for posicao in range(1, 6):  # 1, 2, 3, 4, 5
    numero = float(input(f"Digite o {posicao}º número: ").replace(",", "."))
    soma += numero
    if posicao == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

media = soma / 5

print(f"Soma: {soma:.2f}")
print(f"Média: {media:.2f}")
print(f"Maior: {maior:.2f}")
print(f"Menor: {menor:.2f}")
