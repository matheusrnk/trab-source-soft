import unittest

from main.models.ator import Ator
from main.models.avaliacao import Avaliacao
from main.models.filme import Filme
from main.models.genero import Genero
from main.models.imagem import Imagem
from main.persistence.FilmeDAO import FilmeDAO


class FilmeDAOTest(unittest.TestCase):
    avals = None
    gens = None
    img = None
    elenco = None
    filme1 = None
    filme2 = None
    genero = None

    def setUp(self) -> None:
        self.fd = FilmeDAO()
        self.avals = [Avaliacao(id=1), Avaliacao(id=2), Avaliacao(id=3)]
        self.gens = [Genero(id=1), Genero(id=2)]
        self.img = Imagem(id=1)
        self.elenco = [Ator(id="nm00000"), Ator(id="nm00001")]
        self.filme1 = Filme(id="tt00000", titulo="Um filme...",
                            classificacao_ind="PG-13", rank=1,
                            sinopse="Uma vez...", ano=2000,
                            avaliacoes=self.avals, generos=self.gens,
                            capa=self.img, elenco_principal=self.elenco)

    def testa_sucesso_insercao(self):
        self.assertTrue(self.fd.insert(self.filme1))

    def testa_erro_insercao(self):
        self.assertFalse(self.fd.insert(self.filme2))

    def testa_sucesso_delecao(self):
        self.assertTrue(self.fd.delete(self.filme1))

    def testa_erro_delecao(self):
        self.assertFalse(self.fd.delete(self.filme2))

    def testa_sucesso_atualizacao(self):
        self.assertTrue(self.fd.update(self.filme1))

    def testa_erro_atualizacao(self):
        self.assertFalse(self.fd.update(self.filme2))

    def testa_sucesso_selecao(self):
        self.assertIsNotNone(self.fd.select(self.filme1.id))

    def testa_erro_selecao(self):
        self.assertIsNone(self.fd.select(id_filme=""))

    def testa_sucesso_selecao_todos(self):
        self.assertIsNotNone(self.fd.select_all())

    def testa_sucesso_busca(self):
        self.assertIsNotNone(self.fd.busca("Algum filme"))

    def testa_erro_busca(self):
        self.assertIsNone(self.fd.busca(""))

    def testa_sucesso_busca_por_genero(self):
        self.assertIsNotNone(self.fd.select_by_genero(Genero()))

    def testa_erro_busca_por_genero(self):
        self.assertIsNone(self.fd.select_by_genero(self.genero))

    def testa_sucesso_busca_por_rank(self):
        self.assertIsNotNone(self.fd.select_by_rank())


if __name__ == '__main__':
    unittest.main()
