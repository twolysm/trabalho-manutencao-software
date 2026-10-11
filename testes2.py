import unittest

from loja.estoque import (
    adicionar_produto,
    adicionar_preco_produto,
    atualizar_quantidade,
    remover_produto,
    calcular_total_estoque,
    gerar_alerta_estoque_baixo,
)


class TestEstoque(unittest.TestCase):

    def setUp(self):
        self.produtos = {}

    def test_adicionar_produto(self):
        adicionar_produto(
            self.produtos,
            "Caderno",
            20.00,
            5
        )

        self.assertIn("Caderno", self.produtos)
        self.assertEqual(
            self.produtos["Caderno"]["quantidade"],
            5
        )

    def test_adicionar_preco(self):
        adicionar_produto(self.produtos, "Caneta")

        adicionar_preco_produto(
            self.produtos,
            "Caneta",
            5.00
        )

        self.assertEqual(
            self.produtos["Caneta"]["preco"],
            5.00
        )

    def test_atualizar_quantidade(self):
        adicionar_produto(
            self.produtos,
            "Lápis",
            2.00,
            5
        )

        atualizar_quantidade(
            self.produtos,
            "Lápis",
            10
        )

        self.assertEqual(
            self.produtos["Lápis"]["quantidade"],
            10
        )

    def test_remover_produto(self):
        adicionar_produto(
            self.produtos,
            "Borracha",
            3.00,
            2
        )

        remover_produto(
            self.produtos,
            "Borracha"
        )

        self.assertNotIn(
            "Borracha",
            self.produtos
        )

    def test_calcular_total_estoque(self):
        adicionar_produto(
            self.produtos,
            "Produto A",
            10.00,
            2
        )

        adicionar_produto(
            self.produtos,
            "Produto B",
            5.00,
            3
        )

        self.assertEqual(
            calcular_total_estoque(self.produtos),
            35.00
        )

    def test_alerta_estoque_baixo(self):
        adicionar_produto(
            self.produtos,
            "Produto A",
            10.00,
            2
        )

        alertas = gerar_alerta_estoque_baixo(
            self.produtos
        )

        self.assertIn("Produto A", alertas)
