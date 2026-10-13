#Sistema de produtos - Sprint 4.
#Estruturas de dados praticadas:
#- lista (mutável, ordenada): armazena os produtos;
#- tupla (imutável): cada produto e as estatísticas finais;
#- conjunto/set (únicos, sem ordem): categorias sem repetição.
def ler_float(mensagem):
    #Lê um número decimal aceitando vírgula ou ponto como separador.
    return float(input(mensagem).replace(",", "."))

# 1) Cadastro de produtos (input + append)
def cadastrar_produtos():
    #Lê nome, preço e categoria até o nome ficar vazio. Cada produto é uma tupla (nome, preco, categoria) guardada na lista.
    produtos = []
    print("=== Cadastro de produtos (deixe o nome vazio para encerrar) ===")

    while True:
        nome = input("Nome do produto: ").strip()
        if nome == "":
            break

        preco = ler_float("Preço (R$): ")
        while preco < 0:  # validação: preço não pode ser negativo
            print("Preço inválido! Digite um valor maior ou igual a zero.")
            preco = ler_float("Preço (R$): ")

        categoria = input("Categoria: ").strip().capitalize()
        produtos.append((nome, preco, categoria))
        print(f"-> '{nome}' cadastrado!\n")
      
    return produtos

# 2) Filtragem por preço
def filtrar_por_preco(produtos, valor_referencia, acima=True):
    #Retorna os produtos acima (acima=True) ou abaixo (acima=False) do valor de referência. Produtos com preço igual não entram.
    filtrados = []
    for produto in produtos:
        preco = produto[1]
        if acima and preco > valor_referencia:
            filtrados.append(produto)
        elif not acima and preco < valor_referencia:
            filtrados.append(produto)
    return filtrados

# 3) Ordenação
def obter_preco(produto):
    #Devolve o preço de um produto (usado como chave de ordenação).
    return produto[1]
def ordenar_crescente(produtos):
    #Retorna uma cópia dos produtos em ordem crescente de preço.
    #sort() altera a própria lista; por isso ele é aplicado em uma CÓPIA, preservando a ordem de cadastro da lista original.
    copia = list(produtos)
    copia.sort(key=obter_preco)
    return copia
def ordenar_decrescente(produtos):
    #Retorna uma NOVA lista em ordem decrescente de preço (sorted).
    return sorted(produtos, key=obter_preco, reverse=True)

# 4) Conjunto de categorias únicas
def obter_categorias_unicas(produtos):
    #Retorna um set com as categorias, sem duplicatas.
    categorias = []
    for produto in produtos:
        categorias.append(produto[2])
    return set(categorias)  # set() elimina as repetições

# 5) Tupla de estatísticas
def calcular_estatisticas(produtos):
    #Retorna a tupla imutável (menor_preco, maior_preco, media_precos).
    precos = []
    for produto in produtos:
        precos.append(produto[1])
    return (min(precos), max(precos), sum(precos) / len(precos))

# 6) Relatório final (f-strings)
def exibir_lista(titulo, produtos):
    #Imprime uma lista de produtos em formato de tabela.
    print(f"\n{titulo}")
    if not produtos:
        print("  (nenhum produto)")
        return
    for nome, preco, categoria in produtos:
        print(f"  {nome:<20} R$ {preco:>10.2f}  [{categoria}]")
      
def exibir_relatorio(produtos, valor_referencia, acima):
    #Imprime o relatório final com todos os resultados.
    sentido = "acima" if acima else "abaixo"
    menor, maior, media = calcular_estatisticas(produtos)
    categorias = obter_categorias_unicas(produtos)

    print("\n" + "=" * 50)
    print(f"{'RELATÓRIO FINAL DE PRODUTOS':^50}")
    print("=" * 50)

    exibir_lista(f"Todos os produtos ({len(produtos)}):", produtos)
    exibir_lista(
        f"Produtos {sentido} de R$ {valor_referencia:.2f}:",
        filtrar_por_preco(produtos, valor_referencia, acima),
    )
    exibir_lista("Preço crescente:", ordenar_crescente(produtos))
    exibir_lista("Preço decrescente:", ordenar_decrescente(produtos))

    print(f"\nCategorias únicas ({len(categorias)}): {', '.join(sorted(categorias))}")

    print("\nEstatísticas (tupla):")
    print(f"  Menor preço: R$ {menor:.2f}")
    print(f"  Maior preço: R$ {maior:.2f}")
    print(f"  Preço médio: R$ {media:.2f}")

    # Bônus: operações de conjuntos entre categorias caras e baratas
    categorias_acima = obter_categorias_unicas(
        filtrar_por_preco(produtos, valor_referencia, True)
    )
    categorias_abaixo = obter_categorias_unicas(
        filtrar_por_preco(produtos, valor_referencia, False)
    )
    print(f"\nOperações de conjuntos (acima x abaixo de R$ {valor_referencia:.2f}):")
    print(f"  Acima:                {sorted(categorias_acima)}")
    print(f"  Abaixo:               {sorted(categorias_abaixo)}")
    print(f"  União (|):            {sorted(categorias_acima | categorias_abaixo)}")
    print(f"  Interseção (&):       {sorted(categorias_acima & categorias_abaixo)}")
    print(f"  Diferença (-):        {sorted(categorias_acima - categorias_abaixo)}")
    print(f"  Dif. simétrica (^):   {sorted(categorias_acima ^ categorias_abaixo)}")
    print("=" * 50)

def main():
    """Executa o fluxo completo do sistema."""
    produtos = cadastrar_produtos()
    if not produtos:
        print("Nenhum produto cadastrado. Encerrando.")
        return
      
    valor_referencia = ler_float("\nValor de referência para o filtro: R$ ")
    sentido = input("Listar produtos acima (A) ou abaixo (B)? ").strip().upper()
    acima = sentido != "B"  # qualquer resposta diferente de B vale como "acima"

    exibir_relatorio(produtos, valor_referencia, acima)

if __name__ == "__main__":
    main()
