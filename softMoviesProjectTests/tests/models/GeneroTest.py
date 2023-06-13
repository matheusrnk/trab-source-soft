import unittest

from main.models.genero import Genero


class GeneroTest(unittest.TestCase):

    g = None

    def setUp(self) -> None:
        self.g = Genero(id=1, nome="Um genero")

    def testa_busca_id(self):
        self.assertEqual(1, self.g.id)

    def testa_busca_nome(self):
        self.assertEqual("Um genero", self.g.nome)


if __name__ == '__main__':
    unittest.main()
