import unittest

from main.models.genero import Genero
from main.views.MovieAPI import MovieAPI


class MovieAPITest(unittest.TestCase):

    ma = None

    def setUp(self) -> None:
        self.ma = MovieAPI()

    def testa_unicidade_movie_api(self):
        self.assertEqual(self.ma, MovieAPI())

    def testa_busca_filmes_home(self):
        self.assertIsNotNone(self.ma.busca_filmes_home("algum filme"))

    def testa_busca_filme_id(self):
        self.assertIsNotNone(self.ma.busca_filmes_id(id="tt00001"))

    def testa_busca_generos(self):
        self.assertIsNotNone(self.ma.busca_generos())

    def testa_busca_filmes_por_genero(self):
        self.assertIsNotNone(self.ma.busca_filmes_por_genero(Genero(id=1, nome="Aventura")))

    def testa_busca_melhores_rankeados(self):
        self.assertIsNotNone(self.ma.busca_melhores_rankeados())

    def testa_busca_filme_aleatorio(self):
        self.assertIsNotNone(self.ma.busca_filme_aleatorio())


if __name__ == '__main__':
    unittest.main()
