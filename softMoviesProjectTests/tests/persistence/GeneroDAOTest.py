import unittest

from main.models.genero import Genero
from main.persistence.GeneroDAO import GeneroDAO


class GeneroDAOTest(unittest.TestCase):

    gd = None
    g1 = None
    g2 = None

    def setUp(self) -> None:
        self.gd = GeneroDAO()
        self.g1 = Genero(id=1, nome="Genero")

    def testa_sucesso_insercao(self):
        self.assertTrue(self.gd.insert(self.g1))

    def testa_erro_insercao(self):
        self.assertFalse(self.gd.insert(self.g2))

    def testa_sucesso_delecao(self):
        self.assertTrue(self.gd.delete(self.g1))

    def testa_erro_delecao(self):
        self.assertFalse(self.gd.delete(self.g2))

    def testa_sucesso_atualizacao(self):
        self.assertTrue(self.gd.update(self.g1))

    def testa_erro_atualizacao(self):
        self.assertFalse(self.gd.update(self.g2))

    def testa_sucesso_selecao(self):
        self.assertIsNotNone(self.gd.select(id_genero=1))

    def testa_erro_selecao(self):
        self.assertIsNone(self.gd.select(id_genero=0))

    def testa_sucesso_selecao_todos(self):
        self.assertIsNotNone(self.gd.select_all())


if __name__ == '__main__':
    unittest.main()
