def montar_carrinho():
    """
    Monta o carrinho com os produtos escolhidos pelo usuário.
    """
    disponiveis = listar_produtos_disponiveis()

    if not disponiveis:
        print("Não há produtos disponíveis para venda.")
        return None

    print("\nProdutos disponíveis:")
    for nome, dados in disponiveis.items():
        print(
            f"- {nome} | R$ {dados['preco']:.2f} | "
            f"Estoque: {dados['quantidade']}"
        )

    carrinho = []

    while True:
        nome = input(
            "\nDigite o nome do produto (Enter para finalizar): "
        ).strip()

        if nome == "":
            break

        produto = consultar_produto(produtos, nome)

        if (
            produto is None
            or produto["preco"] is None
            or produto["quantidade"] <= 0
        ):
            print("Produto não encontrado ou indisponível.")
            continue

        try:
            quantidade = int(input("Digite a quantidade: "))
        except ValueError:
            print("Quantidade inválida.")
            continue

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            continue

        if quantidade > produto["quantidade"]:
            print(
                f"Estoque insuficiente. "
                f"Disponível: {produto['quantidade']}"
            )
            continue

        carrinho.append(
            {
                "nome": nome.strip().title(),
                "preco": produto["preco"],
                "quantidade": quantidade,
            }
        )

    return carrinho


def calcular_valores_compra(carrinho):
    """
    Calcula subtotal, desconto, imposto, frete e total final.
    """
    subtotal = calcular_total(carrinho)
    print(f"\nSubtotal: R$ {subtotal:.2f}")

    try:
        desconto = float(
            input(
                "Digite a porcentagem de desconto "
                "(0 para nenhum): "
            )
        )
        subtotal = aplicar_desconto(subtotal, desconto)

    except Exception:
        print("Desconto inválido. Seguindo sem desconto.")

    imposto = calcular_imposto(subtotal)
    frete = calcular_frete(subtotal)

    total_final = round(
        subtotal + imposto + frete,
        2
    )

    print(f"Total com desconto: R$ {subtotal:.2f}")
    print(f"Imposto: R$ {imposto:.2f}")
    print(f"Frete: R$ {frete:.2f}")
    print(f"Total final: R$ {total_final:.2f}")

    return total_final


def solicitar_cpf():
    """
    Pergunta se o cliente deseja CPF na nota.
    """
    cpf_opcao = input(
        "Deseja colocar CPF na nota? (s/n): "
    ).strip().lower()

    if cpf_opcao == "s":
        cpf = input("Digite o CPF: ")

        if validar_cpf_cliente(cpf):
            print("CPF válido.")
        else:
            print("CPF inválido.")


def processar_pagamento(total_final):
    """
    Processa pagamento parcelado ou à vista.
    """
    forma = input(
        "Deseja parcelar? (s/n): "
    ).strip().lower()

    if forma == "s":
        try:
            parcelas = int(
                input("Digite a quantidade de parcelas: ")
            )

            valor_parcela = calcular_parcelamento(
                total_final,
                parcelas
            )

            print(
                f"{parcelas}x de "
                f"R$ {valor_parcela:.2f}"
            )

        except Exception as erro:
            print(
                f"Erro no parcelamento: {erro}"
            )

    else:
        try:
            valor_pago = float(
                input("Digite o valor pago: ")
            )

            troco = calcular_troco(
                valor_pago,
                total_final
            )

            print(f"Troco: R$ {troco:.2f}")

        except Exception as erro:
            print(
                f"Erro no pagamento: {erro}"
            )
            return False

    return True


def atualizar_estoque_compra(carrinho):
    """
    Faz a baixa dos itens comprados no estoque.
    """
    for item in carrinho:
        produtos[item["nome"]]["quantidade"] -= (
            item["quantidade"]
        )


def registrar_compra(historico_vendas)::
    """
    Registra uma compra utilizando funções menores
    para cada responsabilidade.
    """
    carrinho = montar_carrinho()

    if carrinho is None:
        return

    if not carrinho:
        print(
            "Nenhum item foi adicionado ao carrinho."
        )
        return

    total_final = calcular_valores_compra(carrinho)

    solicitar_cpf()

    pagamento_realizado = processar_pagamento(
        total_final
    )

    if not pagamento_realizado:
        return

    atualizar_estoque_compra(carrinho)

    registrar_venda(
        historico_vendas,
        carrinho,
        total_final
    )

    print("Compra finalizada com sucesso.")
