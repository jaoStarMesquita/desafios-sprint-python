programa {
  funcao inicio() {
    const cadeia SENHA_CORRETA = "python123"
    const inteiro MAX_TENTATIVAS = 3

    cadeia senha_digitada
    inteiro tentativas = 0
    logico acesso_liberado = falso

    enquanto (tentativas < MAX_TENTATIVAS e nao acesso_liberado) {
      escreva("Digite a senha: ")
      leia(senha_digitada)
      tentativas = tentativas + 1

      se (senha_digitada == SENHA_CORRETA) {
        acesso_liberado = verdadeiro
      } senao {
        escreva("Senha incorreta! Tentativas restantes: ", MAX_TENTATIVAS - tentativas, "\n")
      }
    }

    se (acesso_liberado) {
      escreva("Acesso liberado após ", tentativas, " tentativa(s). Bem-vindo!\n")
    } senao {
      escreva("Acesso bloqueado: número máximo de tentativas excedido.\n")
    }
  }
}
