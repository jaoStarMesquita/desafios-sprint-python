// Versão em Portugol do conversor de temperatura.
programa {

  funcao real celsius_para_fahrenheit(real celsius) {
    retorne celsius * 9.0 / 5.0 + 32.0
  }

  funcao real fahrenheit_para_celsius(real fahrenheit) {
    retorne (fahrenheit - 32.0) * 5.0 / 9.0
  }

  funcao real celsius_para_kelvin(real celsius) {
    retorne celsius + 273.15
  }

  funcao inicio() {
    escreva("25 °C = ", celsius_para_fahrenheit(25.0), " °F\n")
    escreva("77 °F = ", fahrenheit_para_celsius(77.0), " °C\n")
    escreva("25 °C = ", celsius_para_kelvin(25.0), " K\n")
  }
}
