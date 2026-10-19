import unittest
from io import StringIO
from contextlib import redirect_stdout

from loja.loja import (
    registrar_venda,
    exibir_historico_vendas,
)


class TestHistoricoVendas(unittest.TestCase):

    def test_registrar_venda(self):
        historico = []

        carrinho = [
            {
                "nome": "Caderno",
                "preco": 20.00,
                "quantidade": 2,
            }
        ]

        registrar_venda(
            historico,
            carrinho,
            40.00
        )

        self.assertEqual(
            len(historico),
            1
        )

        self.assertEqual(
            historico[0]["total"],
            40.00
        )

        self.assertEqual(
            historico[0]["itens"][0]["nome"],
            "Caderno"
        )


    def test_registrar_duas_vendas(self):
        historico = []

        registrar_venda(
            historico,
            [
                {
                    "nome": "Caneta",
                    "preco": 5.00,
                    "quantidade": 2,
                }
            ],
            10.00
        )

        registrar_venda(
            historico,
            [
                {
                    "nome": "Caderno",
                    "preco": 20.00,
                    "quantidade": 1,
                }
            ],
            20.00
        )

        self.assertEqual(
            len(historico),
            2
        )


    def test_historico_vazio(self):
        historico = []

        saida = StringIO()

        with redirect_stdout(saida):

            exibir_historico_vendas(
                historico
            )

        self.assertIn(
            "Nenhuma venda registrada",
            saida.getvalue()
        )


    def test_exibir_historico(self):
        historico = [
            {
                "itens": [
                    {
                        "nome": "Caderno",
                        "preco": 20.00,
                        "quantidade": 2,
                    }
                ],
                "total": 40.00,
            }
        ]

        saida = StringIO()

        with redirect_stdout(saida):

            exibir_historico_vendas(
                historico
            )

        resultado = saida.getvalue()

        self.assertIn(
            "Venda 1",
            resultado
        )

        self.assertIn(
            "Caderno",
            resultado
        )

        self.assertIn(
            "40.00",
            resultado
        )


if __name__ == "__main__":
    unittest.main()
