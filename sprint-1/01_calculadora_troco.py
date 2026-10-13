
valor_compra = float(input("Digite o valor da compra: R$ "))
valor_pago = float(input("Digite o valor pago: R$ "))

troco = valor_pago - valor_compra

if troco >= 0:
    print(f"Troco: R$ {troco:.2f}")
else:
    print(f"Faltam R$ {abs(troco):.2f} para pagar a compra.")
