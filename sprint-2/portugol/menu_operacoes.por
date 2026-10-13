programa {
  funcao inicio() {
    inteiro opcao
    real primeiro_numero, segundo_numero

    escreva("=== Menu de Operações ===\n")
    escreva("1 - Soma\n")
    escreva("2 - Subtração\n")
    escreva("3 - Multiplicação\n")
    escreva("4 - Divisão\n")

    escreva("Escolha uma opção: ")
    leia(opcao)

    se (opcao >= 1 e opcao <= 4) {
      escreva("Primeiro número: ")
      leia(primeiro_numero)

      escreva("Segundo número: ")
      leia(segundo_numero)

      escolha (opcao) {
        caso 1:
          escreva(primeiro_numero, " + ", segundo_numero, " = ",
            primeiro_numero + segundo_numero, "\n")
          pare

        caso 2:
          escreva(primeiro_numero, " - ", segundo_numero, " = ",
            primeiro_numero - segundo_numero, "\n")
          pare

        caso 3:
          escreva(primeiro_numero, " x ", segundo_numero, " = ",
            primeiro_numero * segundo_numero, "\n")
          pare

        caso 4:
          se (segundo_numero == 0.0) {
            escreva("Erro: não é possível dividir por zero.\n")
          } senao {
            escreva(primeiro_numero, " / ", segundo_numero, " = ",
              primeiro_numero / segundo_numero, "\n")
          }
          pare
      }
    } senao {
      escreva("Opção inválida! Escolha um número de 1 a 4.\n")
    }
  }
}
