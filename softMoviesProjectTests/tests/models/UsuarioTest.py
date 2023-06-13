import unittest

from main.models.ator import Ator
from main.models.filme import Filme
from main.models.usuario import Usuario


class UsuarioTest(unittest.TestCase):

    ats = None
    fs = None
    u = None

    def setUp(self) -> None:
        self.ats = [Ator(id="nm00000"), Ator(id="nm00001")]
        self.fs = [Filme(id="tt00000"), Filme(id="tt00001")]
        self.u = Usuario(nickname="nick", email="email@email.com",
                         nome="nome", senha="12345",
                         atores_salvos=self.ats,
                         filmes_salvos=self.fs)

    def testa_busca_nickname(self):
        self.assertEqual("nick", self.u.nickname)

    def testa_busca_email(self):
        self.assertEqual("email@email.com", self.u.email)

    def testa_busca_nome(self):
        self.assertEqual("nome", self.u.nome)

    def testa_busca_senha(self):
        self.assertEqual("12345", self.u.senha)

    def testa_busca_atores_salvos(self):
        self.assertListEqual(self.ats, self.u.atores_salvos)

    def testa_busca_filmes_salvos(self):
        self.assertListEqual(self.fs, self.u.filmes_salvos)


if __name__ == '__main__':
    unittest.main()
