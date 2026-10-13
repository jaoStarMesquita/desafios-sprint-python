programa {
  inclua biblioteca Util --> ut

  funcao adicionar_item_seguro(inteiro original[], inteiro novo[], inteiro item) {
    inteiro quantidade = ut.numero_elementos(original)

    para (inteiro i = 0; i < quantidade; i++) {
      novo[i] = original[i]
    }
    novo[quantidade] = item
  }

  funcao exibir(cadeia titulo, inteiro vetor[]) {
    escreva(titulo)
    para (inteiro i = 0; i < ut.numero_elementos(vetor); i++) {
      escreva(vetor[i], " ")
    }
    escreva("\n")
  }

  funcao inicio() {
    inteiro lista_original[3] = {1, 2, 3}
    inteiro lista_nova[4] = {0, 0, 0, 0}

    adicionar_item_seguro(lista_original, lista_nova, 4)

    exibir("Original: ", lista_original)
    exibir("Nova:     ", lista_nova)
  }
}
