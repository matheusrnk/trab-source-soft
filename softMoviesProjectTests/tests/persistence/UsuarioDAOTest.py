import unittest

from main.models.ator import Ator
from main.models.filme import Filme
from main.models.usuario import Usuario
from main.persistence.UsuarioDAO import UsuarioDAO


class UsuarioDAOTest(unittest.TestCase):
    ats = None
    fs = None
    u1 = None
    u2 = None

    def setUp(self) -> None:
        self.ud = UsuarioDAO()
        self.ats = [Ator(id="nm00000"), Ator(id="nm00001")]
        self.fs = [Filme(id="tt00000"), Filme(id="tt00001")]
        self.u1 = Usuario(nickname="nick", email="email@email.com",
                          nome="nome", senha="12345",
                          atores_salvos=self.ats,
                          filmes_salvos=self.fs)

    def testa_sucesso_insercao(self):
        self.assertTrue(self.ud.insert(self.u1))

    def testa_erro_insercao(self):
        self.assertFalse(self.ud.insert(self.u2))

    def testa_sucesso_delecao(self):
        self.assertTrue(self.ud.delete(self.u1))

    def testa_erro_delecao(self):
        self.assertFalse(self.ud.delete(self.u2))

    def testa_sucesso_atualizacao(self):
        self.assertTrue(self.ud.update(self.u1))

    def testa_erro_atualizacao(self):
        self.assertFalse(self.ud.update(self.u2))

    def testa_sucesso_selecao(self):
        self.assertIsNotNone(self.ud.select(self.u1.nickname))

    def testa_erro_selecao(self):
        self.assertIsNone(self.ud.select(nickname=""))

    def testa_sucesso_login(self):
        self.assertTrue(self.ud.login(self.u1.nickname, self.u1.senha))

    def testa_erro_login(self):
        self.assertFalse(self.ud.login(nickname="", senha=""))

    def testa_sucesso_inserir_ator(self):
        self.assertTrue(self.ud.insert_ator_usuario(self.u1, Ator()))

    def testa_erro_inserir_ator(self):
        self.assertFalse(self.ud.insert_ator_usuario(self.u2, Ator()))

    def testa_sucesso_delecao_ator(self):
        self.assertTrue(self.ud.delete_ator_usuario(self.u1, Ator()))

    def testa_erro_delecao_ator(self):
        self.assertFalse(self.ud.delete_ator_usuario(self.u2, Ator()))

    def testa_sucesso_inserir_filme(self):
        self.assertTrue(self.ud.insert_filme_usuario(self.u1, Filme()))

    def testa_erro_inserir_filme(self):
        self.assertFalse(self.ud.insert_filme_usuario(self.u2, Filme()))

    def testa_sucesso_delecao_filme(self):
        self.assertTrue(self.ud.delete_filme_usuario(self.u1, Filme()))

    def testa_erro_delecao_filme(self):
        self.assertFalse(self.ud.delete_filme_usuario(self.u2, Filme()))


if __name__ == '__main__':
    unittest.main()
