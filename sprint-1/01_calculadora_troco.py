# ---------------------------------------------------------------
# Desafio 1 - Calculadora de troco
# ---------------------------------------------------------------
valor_compra = float(
    input("Valor da compra: R$ ").replace(",", "."))
valor_pago = float(
    input("Valor pago: R$ ").replace(",", "."))

if valor_pago >= valor_compra:
    troco = valor_pago - valor_compra
    print(f"Troco: R$ {troco:.2f}")
else:
    falta_pagar = valor_compra - valor_pago
    print(f"Valor insuficiente. Faltam R$ {falta_pagar:.2f}.")
