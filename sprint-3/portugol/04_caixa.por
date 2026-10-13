programa {
  inclua biblioteca Util --> ut

  funcao real caixa(real precos[]) {
    real total = 0.0
    inteiro quantidade = ut.numero_elementos(precos)

    para (inteiro i = 0; i < quantidade; i++) {
      total = total + precos[i]
    }
    retorne total
  }

  funcao inicio() {
    real precos_compra[3] = {10.5, 20.0, 5.25}
    escreva("Total da compra: R$ ", caixa(precos_compra), "\n")
  }
}
