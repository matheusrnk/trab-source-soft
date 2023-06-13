from main.models.ator import Ator
from main.models.avaliacao import Avaliacao
from main.models.filme import Filme
from main.models.genero import Genero


class MovieAPI:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def busca_filmes_home(self, busca: str) -> list[Filme]:
        return [Filme()]

    def busca_filmes_id(self, id: str) -> list[Filme]:
        return [Filme()]

    def busca_generos(self) -> list[Genero]:
        return [Genero()]

    def busca_filmes_por_genero(self, genero: Genero) -> list[Filme]:
        return [Filme()]

    def busca_melhores_rankeados(self) -> list[Filme]:
        return [Filme()]

    def __busca_elenco_principal(self, filme: Filme) -> list[Ator]:
        return [Ator()]

    def busca_filme_aleatorio(self) -> Filme:
        return Filme()

    def __busca_generos_filme(self, filme: Filme) -> list[Genero]:
        return [Genero()]

    def __busca_avaliacoes_filme(self, filme: Filme) -> list[Avaliacao]:
        return [Avaliacao()]
