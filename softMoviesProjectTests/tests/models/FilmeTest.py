import unittest

from main.models.ator import Ator
from main.models.avaliacao import Avaliacao
from main.models.filme import Filme
from main.models.genero import Genero
from main.models.imagem import Imagem


class FilmeTest(unittest.TestCase):

    avals = None
    gens = None
    img = None
    elenco = None
    filme = None

    def setUp(self) -> None:
        self.avals = [Avaliacao(id=1), Avaliacao(id=2), Avaliacao(id=3)]
        self.gens = [Genero(id=1), Genero(id=2)]
        self.img = Imagem(id=1)
        self.elenco = [Ator(id="nm00000"), Ator(id="nm00001")]
        self.filme = Filme(id="tt00000", titulo="Um filme...",
                           classificacao_ind="PG-13", rank=1,
                           sinopse="Uma vez...", ano=2000,
                           avaliacoes=self.avals, generos=self.gens,
                           capa=self.img, elenco_principal=self.elenco)

    def testa_busca_id(self):
        self.assertEqual("tt00000", self.filme.id)

    def testa_busca_titulo(self):
        self.assertEqual("Um filme...", self.filme.titulo)

    def testa_busca_classificacao_ind(self):
        self.assertEqual("PG-13", self.filme.classificacao_ind)

    def testa_busca_rank(self):
        self.assertEqual(1, self.filme.rank)

    def testa_busca_sinopse(self):
        self.assertEqual("Uma vez...", self.filme.sinopse)

    def testa_busca_ano(self):
        self.assertEqual(2000, self.filme.ano)

    def testa_busca_avaliacoes(self):
        self.assertEqual(self.avals, self.filme.avaliacoes)

    def testa_busca_generos(self):
        self.assertEqual(self.gens, self.filme.generos)

    def testa_busca_capa(self):
        self.assertEqual(self.img, self.filme.capa)

    def testa_busca_elenco_principal(self):
        self.assertEqual(self.elenco, self.filme.elenco_principal)


if __name__ == '__main__':
    unittest.main()
