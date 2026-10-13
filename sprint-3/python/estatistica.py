#Módulo estatistica: média, mediana e moda de uma lista de números.
def _validar(numeros):
    """Garante que a lista não está vazia."""
    if not numeros:
        raise ValueError("A lista não pode estar vazia.")
      
def media(numeros):
    """Retorna a média aritmética."""
    _validar(numeros)
    return sum(numeros) / len(numeros)
  
def mediana(numeros):
    """Retorna a mediana (valor central da lista ordenada)."""
    _validar(numeros)
    ordenados = sorted(numeros)  # sorted() não altera a lista original
    meio = len(ordenados) // 2
    if len(ordenados) % 2 == 1:
        return ordenados[meio]
    return (ordenados[meio - 1] + ordenados[meio]) / 2
  
def moda(numeros):
    """Retorna uma lista com o(s) valor(es) mais frequente(s)."""
    _validar(numeros)
    frequencias = {}
    for numero in numeros:
        frequencias[numero] = frequencias.get(numero, 0) + 1
    maior_frequencia = max(frequencias.values())
    return sorted(n for n, freq in frequencias.items() if freq == maior_frequencia)
  
if __name__ == "__main__":
    dados = [1, 2, 2, 3, 4]
    print(media(dados), mediana(dados), moda(dados))  # 2.4 2 [2]
