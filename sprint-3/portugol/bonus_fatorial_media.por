programa {
  inclua biblioteca Util --> ut

  funcao inteiro fatorial(inteiro numero) {
    se (numero <= 1) {
      retorne 1 // caso base
    }
    retorne numero * fatorial(numero - 1)
  }

  funcao real media(real numeros[]) {
    real soma = 0.0
    inteiro quantidade = ut.numero_elementos(numeros)

    para (inteiro i = 0; i < quantidade; i++) {
      soma = soma + numeros[i]
    }
    retorne soma / quantidade
  }

  funcao inicio() {
    real notas[5] = {7.0, 8.0, 8.0, 9.0, 10.0}

    escreva("5! = ", fatorial(5), "\n")
    escreva("Média: ", media(notas), "\n")
  }
}
