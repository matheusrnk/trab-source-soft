import unittest

from main.models.imagem import Imagem
from main.persistence.ImagemDAO import ImagemDAO


class ImagemDAOTest(unittest.TestCase):

    imgd = None
    i1 = None
    i2 = None

    def setUp(self) -> None:
        self.imgd = ImagemDAO()
        self.i1 = Imagem(id=1, imagem=bytearray(), url="url.com",
                         altura=800, largura=600)

    def testa_sucesso_insercao(self):
        self.assertTrue(self.imgd.insert(self.i1))

    def testa_erro_insercao(self):
        self.assertFalse(self.imgd.insert(self.i2))

    def testa_sucesso_delecao(self):
        self.assertTrue(self.imgd.delete(self.i1))

    def testa_erro_delecao(self):
        self.assertFalse(self.imgd.delete(self.i2))

    def testa_sucesso_atualizacao(self):
        self.assertTrue(self.imgd.update(self.i1))

    def testa_erro_atualizacao(self):
        self.assertFalse(self.imgd.update(self.i2))

    def testa_sucesso_selecao(self):
        self.assertIsNotNone(self.imgd.select(id_imagem=1))

    def testa_erro_selecao(self):
        self.assertIsNone(self.imgd.select(id_imagem=0))


if __name__ == '__main__':
    unittest.main()
