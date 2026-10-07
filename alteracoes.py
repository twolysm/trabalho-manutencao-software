def registrar_compra():
    carrinho = montar_carrinho()

    if not carrinho:
        return

    total = calcular_valores_compra(carrinho)

    solicitar_cpf()
    processar_pagamento(total)
    atualizar_estoque(carrinho)
