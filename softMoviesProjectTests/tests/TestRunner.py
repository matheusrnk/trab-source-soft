import unittest

from tests.models.AtorTest import AtorTest
from tests.models.AvaliacaoTest import AvaliacaoTest
from tests.models.FilmeTest import FilmeTest
from tests.models.GeneroTest import GeneroTest
from tests.models.ImagemTest import ImagemTest
from tests.models.UsuarioTest import UsuarioTest
from tests.persistence.AtorDAOTest import AtorDAOTest
from tests.persistence.AvaliacaoDAOTest import AvaliacaoDAOTest
from tests.persistence.ConexaoTest import ConexaoTest
from tests.persistence.FilmeDAOTest import FilmeDAOTest
from tests.persistence.GeneroDAOTest import GeneroDAOTest
from tests.persistence.ImagemDAOTest import ImagemDAOTest
from tests.persistence.UsuarioDAOTest import UsuarioDAOTest
from tests.views.SistemaTest import SistemaTest
from tests.views.MovieAPITest import MovieAPITest

test_loader = unittest.TestLoader()

testes = [AtorTest, AvaliacaoTest, FilmeTest,
          GeneroTest, ImagemTest, UsuarioTest,
          AtorDAOTest, AvaliacaoDAOTest, ConexaoTest,
          FilmeDAOTest, GeneroDAOTest, ImagemDAOTest,
          UsuarioDAOTest, SistemaTest, MovieAPITest]

for t in testes:
    test_suite = test_loader.loadTestsFromTestCase(t)
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)
