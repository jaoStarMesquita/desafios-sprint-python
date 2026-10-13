programa {

  funcao real somar(real a, real b) {
    retorne a + b
  }

  funcao real subtrair(real a, real b) {
    retorne a - b
  }

  funcao real multiplicar(real a, real b) {
    retorne a * b
  }

  funcao real dividir(real dividendo, real divisor) {
    se (divisor == 0.0) {
      escreva("Erro: não é possível dividir por zero.\n")
      retorne 0.0
    }
    retorne dividendo / divisor
  }

  funcao inicio() {
    escreva("8 + 2 = ", somar(8.0, 2.0), "\n")
    escreva("8 - 2 = ", subtrair(8.0, 2.0), "\n")
    escreva("8 x 2 = ", multiplicar(8.0, 2.0), "\n")
    escreva("8 / 2 = ", dividir(8.0, 2.0), "\n")
    escreva("8 / 0 = ", dividir(8.0, 0.0), "\n")
  }
}
