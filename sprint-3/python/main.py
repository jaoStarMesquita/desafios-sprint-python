#Script principal: importa os módulos e demonstra o reaproveitamento de código.
import calculadora
import estatistica as est
from utilidades import (
    adicionar_item_seguro,
    caixa,
    celsius_para_fahrenheit,
    celsius_para_kelvin,
    fahrenheit_para_celsius,
    fatorial,
    ficha_aluno,
    relatorio,
    validar_senha,
)

print("=== Calculadora ===")
print(f"8 + 2 = {calculadora.somar(8, 2)}")
print(f"8 - 2 = {calculadora.subtrair(8, 2)}")
print(f"8 x 2 = {calculadora.multiplicar(8, 2)}")
print(f"8 / 2 = {calculadora.dividir(8, 2)}")
resultado_divisao = calculadora.dividir(8, 0)
print(f"8 / 0 = {resultado_divisao}")

print("\n=== Conversor de temperatura ===")
print(f"25 °C = {celsius_para_fahrenheit(25):.1f} °F")
print(f"77 °F = {fahrenheit_para_celsius(77):.1f} °C")
print(f"25 °C = {celsius_para_kelvin(25):.2f} K")

print("\n=== Validador de senha ===")
for senha in ["abc", "senhafraca1", "Python123"]:
    situacao = "válida" if validar_senha(senha) else "inválida"
    print(f"'{senha}': {situacao}")

print("\n=== Caixa (*precos) ===")
print(f"Total com 3 itens: R$ {caixa(10.5, 20, 5.25):.2f}")
print(f"Total com 1 item: R$ {caixa(7.9):.2f}")
print(f"Total sem itens: R$ {caixa():.2f}")

print("\n=== Ficha do aluno (**dados) ===")
print(ficha_aluno("Ana Souza", idade=20, curso="ADS", media=8.5))

print("\n=== Lista segura ===")
lista_original = [1, 2, 3]
lista_nova = adicionar_item_seguro(lista_original, 4)
print(f"Original: {lista_original}")
print(f"Nova:     {lista_nova}")

print("\n=== Bônus: estatística (alias est) ===")
notas = [7, 8, 8, 9, 10]
print(f"Média: {est.media(notas):.2f}")
print(f"Mediana: {est.mediana(notas)}")
print(f"Moda: {est.moda(notas)}")

print("\n=== Bônus: fatorial recursivo ===")
print(f"5! = {fatorial(5)}")

print("\n=== Bônus: relatório ===")
print(relatorio("Resumo da Turma", "Média: 8.40", "Aprovados: 4", largura=30, maiusculo=True))
