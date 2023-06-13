import unittest

from main.models.ator import Ator
from main.models.filme import Filme
from main.models.imagem import Imagem


class AtorTest(unittest.TestCase):
    a = None
    foto = None
    participacoes = None

    def setUp(self):
        self.foto = Imagem(url="url")
        self.participacoes = [Filme(id="A"), Filme(id="B"), Filme(id="C")]
        self.a = Ator(id="nm00000", nome="Fulano", bio="Um ator muito famoso...",
                      data_nasc="20/02/1995", local_nasc="Sao Paulo, Brasil", altura=175,
                      foto=self.foto, participacoes=self.participacoes)

    def testa_busca_id(self):
        self.assertEqual("nm00000", self.a.id)

    def testa_busca_nome(self):
        self.assertEqual("Fulano", self.a.nome)

    def testa_busca_bio(self):
        self.assertEqual("Um ator muito famoso...", self.a.bio)

    def testa_busca_data_nasc(self):
        self.assertEqual("20/02/1995", self.a.data_nasc)

    def testa_busca_local_nasc(self):
        self.assertEqual("Sao Paulo, Brasil", self.a.local_nasc)

    def testa_busca_altura(self):
        self.assertEqual(175, self.a.altura)

    def testa_busca_foto(self):
        self.assertEqual(self.foto, self.a.foto)

    def testa_busca_participacoes(self):
        self.assertListEqual(self.participacoes, self.a.participacoes)


if __name__ == '__main__':
    unittest.main()
