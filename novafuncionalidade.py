def registrar_venda(historico_vendas, carrinho, total_final):
    """
    Registra uma compra concluída no histórico de vendas.
    """
    venda = {
        "itens": [item.copy() for item in carrinho],
        "total": total_final,
    }

    historico_vendas.append(venda)


def exibir_historico_vendas(historico_vendas):
    """
    Exibe as vendas realizadas durante a execução do sistema.
    """
    if not historico_vendas:
        print("\nNenhuma venda registrada.")
        return

    print("\n==== HISTÓRICO DE VENDAS ====")

    for numero, venda in enumerate(historico_vendas, start=1):
        print(f"\nVenda {numero}")

        for item in venda["itens"]:
            print(
                f"- {item['nome']} | "
                f"Quantidade: {item['quantidade']} | "
                f"Preço: R$ {item['preco']:.2f}"
            )

        print(f"Total: R$ {venda['total']:.2f}")
