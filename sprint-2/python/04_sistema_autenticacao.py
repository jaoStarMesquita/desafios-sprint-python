#Desafio 4 - Sistema de Autenticação (while).

SENHA_CORRETA = "python123"
MAX_TENTATIVAS = 3

tentativas = 0
acesso_liberado = False

while tentativas < MAX_TENTATIVAS and not acesso_liberado:
    senha_digitada = input("Digite a senha: ")
    tentativas += 1  # atualiza a variável de controle (evita loop infinito)

    if senha_digitada == SENHA_CORRETA:
        acesso_liberado = True
    else:
        restantes = MAX_TENTATIVAS - tentativas
        print(f"Senha incorreta! Tentativas restantes: {restantes}")

if acesso_liberado:
    print(f"Acesso liberado após {tentativas} tentativa(s). Bem-vindo!")
else:
    print("Acesso bloqueado: número máximo de tentativas excedido.")
