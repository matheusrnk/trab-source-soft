import unittest

from main.models.avaliacao import Avaliacao
from main.models.filme import Filme
from main.models.usuario import Usuario


class AvaliacaoTest(unittest.TestCase):

    a = None
    u = None
    f = None

    def setUp(self) -> None:
        self.u = Usuario(nickname="nick")
        self.f = Filme(id="tt00000")
        self.a = Avaliacao(id=1, upvotes=100, downvotes=50,
                           data_hora="15/07/2023 17:00",
                           texto="Um filme muito bom...",
                           usuario=self.u, filme=self.f)

    def testa_busca_id(self):
        self.assertEqual(1, self.a.id)

    def testa_busca_upvotes(self):
        self.assertEqual(100, self.a.upvotes)

    def testa_busca_downvotes(self):
        self.assertEqual(50, self.a.downvotes)

    def testa_busca_data_hora(self):
        self.assertEqual("15/07/2023 17:00", self.a.data_hora)

    def testa_busca_texto(self):
        self.assertEqual("Um filme muito bom...", self.a.texto)

    def testa_busca_usuario(self):
        self.assertEqual(self.u, self.a.usuario)

    def testa_busca_filme(self):
        self.assertEqual(self.f, self.a.filme)


if __name__ == '__main__':
    unittest.main()
