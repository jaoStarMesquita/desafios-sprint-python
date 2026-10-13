programa {

  funcao exibir_ficha(cadeia nome, inteiro idade, cadeia curso, real media) {
    escreva("Aluno: ", nome, "\n")
    escreva("  Idade: ", idade, "\n")
    escreva("  Curso: ", curso, "\n")
    escreva("  Media: ", media, "\n")
    // Sem "retorne": é uma função "vazio" (em Python, devolveria None).
  }

  funcao inicio() {
    exibir_ficha("Ana Souza", 20, "ADS", 8.5)
  }
}
