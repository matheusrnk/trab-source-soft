import unittest

from main.models.imagem import Imagem


class ImagemTest(unittest.TestCase):

    i = None
    img_byte = None

    def setUp(self) -> None:
        self.img_byte = bytearray(b'')
        self.i = Imagem(id=1, url="www.url.com/imagem",
                        altura=800, largura=600, imagem=self.img_byte)

    def testa_busca_id(self):
        self.assertEqual(1, self.i.id)

    def testa_busca_url(self):
        self.assertEqual("www.url.com/imagem", self.i.url)

    def testa_busca_altura(self):
        self.assertEqual(800, self.i.altura)

    def testa_busca_largura(self):
        self.assertEqual(600, self.i.largura)

    def testa_busca_img_byte(self):
        self.assertEqual(self.img_byte, self.i.imagem)


if __name__ == '__main__':
    unittest.main()
