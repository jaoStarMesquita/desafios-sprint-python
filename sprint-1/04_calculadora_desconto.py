# ---------------------------------------------------------------
# Desafio 4 - Calculadora de desconto
# ---------------------------------------------------------------
print("\n=== Desafio 4: Calculadora de desconto ===")
preco_produto = ler_float("Preço do produto: R$ ")
percentual_desconto = ler_float("Percentual de desconto (%): ")

valor_desconto = preco_produto * percentual_desconto / 100
preco_final = preco_produto - valor_desconto

print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
