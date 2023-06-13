import unittest

from main.models.ator import Ator
from main.models.filme import Filme
from main.models.imagem import Imagem
from main.persistence.AtorDAO import AtorDAO


class AtorDAOTest(unittest.TestCase):
    ad = None
    a1 = None
    a2 = None
    foto = None
    participacoes = None

    def setUp(self) -> None:
        self.ad = AtorDAO()
        self.foto = Imagem(url="url")
        self.participacoes = [Filme(id="A"), Filme(id="B"), Filme(id="C")]
        self.a1 = Ator(id="nm00000", nome="Fulano", bio="Um ator muito famoso...",
                       data_nasc="20/02/1995", local_nasc="Sao Paulo, Brasil", altura=175,
                       foto=self.foto, participacoes=self.participacoes)

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
        self.assertIsNone(self.ad.select(id_ator=""))

    def testa_sucesso_selecao_todos(self):
        self.assertIsNotNone(self.ad.select_all())


if __name__ == '__main__':
    unittest.main()
