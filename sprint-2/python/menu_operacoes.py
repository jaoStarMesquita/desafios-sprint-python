#Desafio 2 - Menu de Operações Matemáticas (match / case).
print("=== Menu de Operações ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Escolha uma opção: "))

if opcao in (1, 2, 3, 4):
    primeiro_numero = float(input("Primeiro número: ").replace(",", "."))
    segundo_numero = float(input("Segundo número: ").replace(",", "."))
    
    match opcao:
        case 1:
            print(f"{primeiro_numero} + {segundo_numero} = {primeiro_numero + segundo_numero}")
        case 2:
            print(f"{primeiro_numero} - {segundo_numero} = {primeiro_numero - segundo_numero}")
        case 3:
            print(f"{primeiro_numero} x {segundo_numero} = {primeiro_numero * segundo_numero}")
        case 4:
            if segundo_numero == 0:
                print("Erro: não é possível dividir por zero.")
            else:
                print(f"{primeiro_numero} / {segundo_numero} = {primeiro_numero / segundo_numero:.2f}")
else:
    print("Opção inválida! Escolha um número de 1 a 4.")

