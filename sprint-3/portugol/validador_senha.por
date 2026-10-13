programa {
  inclua biblioteca Texto --> tx

  funcao logico validar_senha(cadeia senha) {
    inteiro tamanho = tx.numero_caracteres(senha)
    logico tem_maiuscula = falso
    logico tem_minuscula = falso
    logico tem_digito = falso

    para (inteiro i = 0; i < tamanho; i++) {
      caracter letra = tx.obter_caracter(senha, i)

      se (letra >= 'A' e letra <= 'Z') {
        tem_maiuscula = verdadeiro
      } senao se (letra >= 'a' e letra <= 'z') {
        tem_minuscula = verdadeiro
      } senao se (letra >= '0' e letra <= '9') {
        tem_digito = verdadeiro
      }
    }

    retorne tamanho >= 8 e tem_maiuscula e tem_minuscula e tem_digito
  }

  funcao inicio() {
    cadeia senha
    escreva("Digite uma senha: ")
    leia(senha)

    se (validar_senha(senha)) {
      escreva("Senha válida.\n")
    } senao {
      escreva("Senha inválida.\n")
    }
  }
}
