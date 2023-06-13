import unittest

from main.models.avaliacao import Avaliacao
from main.models.filme import Filme
from main.models.usuario import Usuario
from main.persistence.AvaliacaoDAO import AvaliacaoDAO


class AvaliacaoDAOTest(unittest.TestCase):
    ad = None
    a1 = None
    a2 = None
    u = None
    f = None

    def setUp(self) -> None:
        self.ad = AvaliacaoDAO()
        self.u = Usuario(nickname="nick")
        self.f = Filme(id="tt00000")
        self.a1 = Avaliacao(id=1, upvotes=100, downvotes=50,
                            data_hora="15/07/2023 17:00",
                            texto="Um filme muito bom...",
                            usuario=self.u, filme=self.f)

    def testa_sucesso_insercao(self):
        self.assertTrue(self.ad.insert(self.a1))

    def testa_erro_insercao(self):
        self.assertFalse(self.ad.insert(self.a2))

    def testa_sucesso_delecao(self):
        self.assertTrue(self.ad.delete(self.a1))

    def testa_erro_delecao(self):
        self.assertFalse(self.ad.delete(self.a2))

    def testa_sucesso_atualizacao(self):
        self.assertTrue(self.ad.update(self.a1))

    def testa_erro_atualizacao(self):
        self.assertFalse(self.ad.update(self.a2))

    def testa_sucesso_selecao(self):
        self.assertIsNotNone(self.ad.select(self.a1.id))

    def testa_erro_selecao(self):
        self.assertIsNone(self.ad.select(id_aval=0))


if __name__ == '__main__':
    unittest.main()
