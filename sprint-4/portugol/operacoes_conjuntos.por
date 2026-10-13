programa {

  // Verifica se "valor" já está nas primeiras "quantidade" posições
  funcao logico contem(cadeia conjunto[], inteiro quantidade, cadeia valor) {
    para (inteiro i = 0; i < quantidade; i++) {
      se (conjunto[i] == valor) {
        retorne verdadeiro
      }
    }
    retorne falso
  }

  funcao exibir_conjunto(cadeia titulo, cadeia conjunto[], inteiro quantidade) {
    escreva(titulo)
    para (inteiro i = 0; i < quantidade; i++) {
      escreva(conjunto[i], " ")
    }
    escreva("\n")
  }

  inteiro quantidade_a = 4
  inteiro quantidade_b = 3

  funcao inicio() {
    cadeia conjunto_a[4] = {"Eletronicos", "Livros", "Casa", "Games"}
    cadeia conjunto_b[3] = {"Livros", "Games", "Moda"}

    cadeia resultado[7]
    inteiro quantidade

    exibir_conjunto("A: ", conjunto_a, quantidade_a)
    exibir_conjunto("B: ", conjunto_b, quantidade_b)

    // UNIÃO (A | B): tudo de A + o que de B ainda não está no resultado
    quantidade = 0
    para (inteiro i = 0; i < quantidade_a; i++) {
      resultado[quantidade] = conjunto_a[i]
      quantidade++
    }
    para (inteiro i = 0; i < quantidade_b; i++) {
      se (nao contem(resultado, quantidade, conjunto_b[i])) {
        resultado[quantidade] = conjunto_b[i]
        quantidade++
      }
    }
    exibir_conjunto("União (|):          ", resultado, quantidade)

    // INTERSEÇÃO (A & B): itens de A que também estão em B
    quantidade = 0
    para (inteiro i = 0; i < quantidade_a; i++) {
      se (contem(conjunto_b, quantidade_b, conjunto_a[i])) {
        resultado[quantidade] = conjunto_a[i]
        quantidade++
      }
    }
    exibir_conjunto("Interseção (&):     ", resultado, quantidade)

    // DIFERENÇA (A - B): itens de A que NÃO estão em B
    quantidade = 0
    para (inteiro i = 0; i < quantidade_a; i++) {
      se (nao contem(conjunto_b, quantidade_b, conjunto_a[i])) {
        resultado[quantidade] = conjunto_a[i]
        quantidade++
      }
    }
    exibir_conjunto("Diferença (-):      ", resultado, quantidade)

    // DIFERENÇA SIMÉTRICA (A ^ B): (A - B) + (B - A)
    quantidade = 0
    para (inteiro i = 0; i < quantidade_a; i++) {
      se (nao contem(conjunto_b, quantidade_b, conjunto_a[i])) {
        resultado[quantidade] = conjunto_a[i]
        quantidade++
      }
    }
    para (inteiro i = 0; i < quantidade_b; i++) {
      se (nao contem(conjunto_a, quantidade_a, conjunto_b[i])) {
        resultado[quantidade] = conjunto_b[i]
        quantidade++
      }
    }
    exibir_conjunto("Dif. simétrica (^): ", resultado, quantidade)
  }
}
