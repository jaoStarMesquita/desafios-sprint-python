programa {
  inclua biblioteca Util --> ut
  inclua biblioteca Matematica --> mat

  // -----------------------------------------------------------------
  // 1) CADASTRO: laço "para" preenche os vetores (equivale a input+append)
  // -----------------------------------------------------------------
  funcao cadastrar_produtos(cadeia nomes[], real precos[], cadeia categorias[]) {
    inteiro total = ut.numero_elementos(nomes)

    escreva("=== Cadastro de produtos ===\n")
    para (inteiro i = 0; i < total; i++) {
      escreva("Produto ", i + 1, " - nome: ")
      leia(nomes[i])

      escreva("Preço (R$): ")
      leia(precos[i])
      // validação: repete enquanto o preço for negativo
      enquanto (precos[i] < 0.0) {
        escreva("Preço inválido! Digite um valor maior ou igual a zero: ")
        leia(precos[i])
      }

      escreva("Categoria: ")
      leia(categorias[i])
      escreva("\n")
    }
  }

  // -----------------------------------------------------------------
  // Auxiliar: exibe os produtos (percorre os 3 vetores juntos)
  // -----------------------------------------------------------------
  funcao exibir_produtos(cadeia titulo, cadeia nomes[], real precos[], cadeia categorias[]) {
    inteiro total = ut.numero_elementos(nomes)

    escreva("\n", titulo, "\n")
    para (inteiro i = 0; i < total; i++) {
      escreva("  ", nomes[i], " | R$ ", mat.arredondar(precos[i], 2), " | ", categorias[i], "\n")
    }
  }

  // -----------------------------------------------------------------
  // 2) FILTRAGEM: laço + condição (igual ao "if" dentro do "for" do Python)
  //    acima = verdadeiro -> preço > limite; falso -> preço < limite
  // -----------------------------------------------------------------
  funcao filtrar_por_preco(cadeia nomes[], real precos[], cadeia categorias[], real limite, logico acima) {
    inteiro total = ut.numero_elementos(nomes)
    inteiro encontrados = 0

    para (inteiro i = 0; i < total; i++) {
      logico atende = falso

      se (acima e precos[i] > limite) {
        atende = verdadeiro
      }
      se (nao acima e precos[i] < limite) {
        atende = verdadeiro
      }

      se (atende) {
        escreva("  ", nomes[i], " | R$ ", mat.arredondar(precos[i], 2), " | ", categorias[i], "\n")
        encontrados++
      }
    }

    se (encontrados == 0) {
      escreva("  (nenhum produto)\n")
    }
  }

  // -----------------------------------------------------------------
  // 3) ORDENAÇÃO: método da BOLHA (substitui sort()/sorted()).
  //    Compara pares vizinhos e troca se estiverem fora de ordem.
  //    A cada passada, o maior valor "sobe" para o fim do vetor.
  //    Os 3 vetores são trocados JUNTOS para o produto não se misturar.
  //    crescente = verdadeiro -> menor para maior; falso -> decrescente.
  // -----------------------------------------------------------------
  funcao ordenar_bolha(cadeia nomes[], real precos[], cadeia categorias[], logico crescente) {
    inteiro total = ut.numero_elementos(nomes)
    real aux_preco
    cadeia aux_nome
    cadeia aux_categoria
    logico trocar

    para (inteiro passada = 0; passada < total - 1; passada++) {
      para (inteiro j = 0; j < total - 1 - passada; j++) {
        trocar = falso

        se (crescente e precos[j] > precos[j + 1]) {
          trocar = verdadeiro
        }
        se (nao crescente e precos[j] < precos[j + 1]) {
          trocar = verdadeiro
        }

        se (trocar) {
          aux_preco = precos[j]
          precos[j] = precos[j + 1]
          precos[j + 1] = aux_preco

          aux_nome = nomes[j]
          nomes[j] = nomes[j + 1]
          nomes[j + 1] = aux_nome

          aux_categoria = categorias[j]
          categorias[j] = categorias[j + 1]
          categorias[j + 1] = aux_categoria
        }
      }
    }
  }

  // Copia os 3 vetores (cópia defensiva: preserva a ordem de cadastro)
  funcao copiar_produtos(cadeia nomes[], real precos[], cadeia categorias[],
                         cadeia nomes_copia[], real precos_copia[], cadeia categorias_copia[]) {
    inteiro total = ut.numero_elementos(nomes)

    para (inteiro i = 0; i < total; i++) {
      nomes_copia[i] = nomes[i]
      precos_copia[i] = precos[i]
      categorias_copia[i] = categorias[i]
    }
  }

  // -----------------------------------------------------------------
  // 4) CONJUNTO DE CATEGORIAS ÚNICAS (simula set())
  //    Para cada categoria, procura em "unicas"; se já existe, IGNORA;
  //    se não existe, ADICIONA. Retorna quantas categorias únicas há.
  // -----------------------------------------------------------------
  funcao inteiro montar_conjunto_categorias(cadeia categorias[], cadeia unicas[]) {
    inteiro total = ut.numero_elementos(categorias)
    inteiro quantidade_unicas = 0

    para (inteiro i = 0; i < total; i++) {
      logico ja_existe = falso

      para (inteiro j = 0; j < quantidade_unicas; j++) {
        se (categorias[i] == unicas[j]) {
          ja_existe = verdadeiro
        }
      }

      se (nao ja_existe) {
        unicas[quantidade_unicas] = categorias[i]
        quantidade_unicas++
      }
    }

    retorne quantidade_unicas
  }

  // -----------------------------------------------------------------
  // 5) ESTATÍSTICAS: sem tupla nem min()/max()/sum(); cada valor é
  //    calculado percorrendo o vetor com "para".
  // -----------------------------------------------------------------
  funcao real menor_preco(real precos[]) {
    real menor = precos[0]

    para (inteiro i = 1; i < ut.numero_elementos(precos); i++) {
      se (precos[i] < menor) {
        menor = precos[i]
      }
    }
    retorne menor
  }

  funcao real maior_preco(real precos[]) {
    real maior = precos[0]

    para (inteiro i = 1; i < ut.numero_elementos(precos); i++) {
      se (precos[i] > maior) {
        maior = precos[i]
      }
    }
    retorne maior
  }

  funcao real media_precos(real precos[]) {
    real soma = 0.0
    inteiro total = ut.numero_elementos(precos)

    para (inteiro i = 0; i < total; i++) {
      soma = soma + precos[i]
    }
    retorne soma / total
  }

  // -----------------------------------------------------------------
  // 6) PROGRAMA PRINCIPAL + RELATÓRIO FINAL
  // -----------------------------------------------------------------
  funcao inicio() {
    cadeia nomes[5]
    real precos[5]
    cadeia categorias[5]

    cadastrar_produtos(nomes, precos, categorias)

    real valor_referencia
    inteiro opcao
    escreva("Valor de referência para o filtro: R$ ")
    leia(valor_referencia)
    escreva("Listar produtos acima (1) ou abaixo (2)? ")
    leia(opcao)

    escreva("\n==================================================\n")
    escreva("              RELATÓRIO FINAL DE PRODUTOS\n")
    escreva("==================================================\n")

    exibir_produtos("Todos os produtos:", nomes, precos, categorias)

    // Filtragem
    se (opcao == 2) {
      escreva("\nProdutos abaixo de R$ ", valor_referencia, ":\n")
      filtrar_por_preco(nomes, precos, categorias, valor_referencia, falso)
    } senao {
      escreva("\nProdutos acima de R$ ", valor_referencia, ":\n")
      filtrar_por_preco(nomes, precos, categorias, valor_referencia, verdadeiro)
    }

    // Ordenação (sempre em CÓPIAS, para não alterar a ordem de cadastro)
    cadeia nomes_ord[5]
    real precos_ord[5]
    cadeia categorias_ord[5]

    copiar_produtos(nomes, precos, categorias, nomes_ord, precos_ord, categorias_ord)
    ordenar_bolha(nomes_ord, precos_ord, categorias_ord, verdadeiro)
    exibir_produtos("Preço crescente:", nomes_ord, precos_ord, categorias_ord)

    copiar_produtos(nomes, precos, categorias, nomes_ord, precos_ord, categorias_ord)
    ordenar_bolha(nomes_ord, precos_ord, categorias_ord, falso)
    exibir_produtos("Preço decrescente:", nomes_ord, precos_ord, categorias_ord)

    // Conjunto de categorias únicas
    cadeia categorias_unicas[5]
    inteiro quantidade_unicas = montar_conjunto_categorias(categorias, categorias_unicas)

    escreva("\nCategorias únicas (", quantidade_unicas, "): ")
    para (inteiro i = 0; i < quantidade_unicas; i++) {
      escreva(categorias_unicas[i], " ")
    }
    escreva("\n")

    // Estatísticas
    escreva("\nEstatísticas:\n")
    escreva("  Menor preço: R$ ", mat.arredondar(menor_preco(precos), 2), "\n")
    escreva("  Maior preço: R$ ", mat.arredondar(maior_preco(precos), 2), "\n")
    escreva("  Preço médio: R$ ", mat.arredondar(media_precos(precos), 2), "\n")
    escreva("==================================================\n")
  }
}
