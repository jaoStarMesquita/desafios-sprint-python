programa {
  funcao inicio() {
    real numero, soma = 0.0, media, maior = 0.0, menor = 0.0

    para (inteiro posicao = 1; posicao <= 5; posicao++) {
      escreva("Digite o ", posicao, "º número: ")
      leia(numero)
      soma = soma + numero

      se (posicao == 1) {
        maior = numero
        menor = numero
      } senao {
        se (numero > maior) {
          maior = numero
        }
        se (numero < menor) {
          menor = numero
        }
      }
    }

    media = soma / 5.0

    escreva("Soma: ", soma, "\n")
    escreva("Média: ", media, "\n")
    escreva("Maior: ", maior, "\n")
    escreva("Menor: ", menor, "\n")
  }
}
