programa {
  funcao inicio() {
    inteiro idade
    real renda
    cadeia categoria

    escreva("Digite a idade do cliente: ")
    leia(idade)

    escreva("Digite a renda mensal (R$): ")
    leia(renda)

    se (idade >= 30 e renda >= 10000.0) {
      categoria = "Diamante"
    } senao se (idade >= 25 e renda >= 5000.0) {
      categoria = "Ouro"
    } senao se (idade >= 18 e renda >= 2500.0) {
      categoria = "Prata"
    } senao {
      categoria = "Bronze"
    }

    escreva("Cliente de ", idade, " anos com renda de R$ ",
      renda, ": categoria ", categoria, ".\n")
  }
}
