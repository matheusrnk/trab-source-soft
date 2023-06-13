import unittest

from main.models.ator import Ator
from main.models.avaliacao import Avaliacao
from main.models.filme import Filme
from main.models.usuario import Usuario
from main.views.Sistema import Sistema


class SistemaTest(unittest.TestCase):
    sis = None
    ats = None
    fs = None
    u = None

    def setUp(self) -> None:
        self.sis = Sistema()
        self.ats = [Ator(id="nm00000"), Ator(id="nm00001")]
        self.fs = [Filme(id="tt00000"), Filme(id="tt00001")]
        self.u = Usuario(nickname="nick", email="email@email.com",
                         nome="nome", senha="12345",
                         atores_salvos=self.ats,
                         filmes_salvos=self.fs)

    def testa_unicidade_sistema(self):
        self.assertEqual(self.sis, Sistema())

    def testa_cadastrar_usuario(self):
        self.assertTrue(self.sis.cadastrar_usuario(self.u))

    def testa_login_usuario(self):
        self.assertTrue(self.sis.login_usuario(self.u.nickname, self.u.senha))

    def testa_salvar_filme_usuario(self):
        self.assertTrue(self.sis.salva_filme_usuario(self.u, Filme(id="tt00002")))

    def testa_excluir_filme_usuario(self):
        self.assertTrue(self.sis.exclui_filme_usuario(self.u, Filme(id="tt00002")))

    def testa_buscar_filmes_salvos_usuario(self):
        self.assertIsNotNone(self.sis.busca_filmes_salvos_usuario(self.u))

    def testa_salvar_ator_usuario(self):
        self.assertTrue(self.sis.salva_ator_usuario(self.u, Ator(id="nm00002")))

    def testa_excluir_ator_usuario(self):
        self.assertTrue(self.sis.exclui_ator_usuario(self.u, Ator(id="nm00002")))

    def testa_buscar_atores_salvos_usuario(self):
        self.assertIsNotNone(self.sis.busca_atores_salvos_usuario(self.u))

    def testa_inserir_avaliacao_pelo_usuario(self):
        self.assertTrue(self.sis.insere_avaliacao_filme(self.u, Avaliacao(id=1, data_hora="11/02/2023 12:10",
                                                                          texto="Um filme muito bom...")))

    def testa_logout_usuario(self):
        self.assertFalse(self.sis.logout_usuario())


if __name__ == '__main__':
    unittest.main()
