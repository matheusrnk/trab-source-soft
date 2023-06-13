import unittest

from flask import render_template

from main.models.usuario import Usuario
from main.views.App import home
from main.views.MovieAPI import MovieAPI
from main.views import forms


class AppTest(unittest.TestCase):

    def setUp(self) -> None:
        self.formulario_busca = forms.FormularioBusca()

    def testa_home(self):
        gs = MovieAPI().busca_generos()
        self.assertEqual(home(), render_template("home.html", form=self.formulario_busca, generos_buscados=gs,
                                                 usuario_logado=Usuario()))

    def testa_cadastro(self):
        pass

    def testa_login(self):
        pass

    def testa_filme(self):
        pass

    def testa_ator(self):
        pass

    def testa_usuario(self):
        pass

    def testa_lista_filmes(self):
        pass

    def testa_melhores_filmes(self):
        pass

    def testa_filmes_por_genero(self):
        pass

    def testa_salva_filme_usuario(self):
        pass

    def testa_exclui_filme_usuario(self):
        pass

    def testa_salva_filme_ator(self):
        pass

    def testa_exclui_filme_ator(self):
        pass

    def testa_logout(self):
        pass
