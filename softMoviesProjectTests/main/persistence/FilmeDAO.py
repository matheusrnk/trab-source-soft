import psycopg2
from main.exceptions.InsertException import InsertException
from main.exceptions.DeleteException import DeleteException
from main.exceptions.UpdateException import UpdateException
from main.exceptions.SelectException import SelectException
from main.persistence.Conexao import Conexao
from main.models.genero import Genero
from main.models.filme import Filme


class FilmeDAO:

    def __init__(self):
        self.__con = Conexao()

    def insert(self, filme: Filme) -> bool:
        try:
            if filme is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise InsertException("FILMES", "FilmeDAO.insert", filme, erro)
        return False

    def delete(self, filme: Filme) -> bool:
        try:
            if filme is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise DeleteException("FILMES", "FilmeDAO.delete", filme, erro)
        return False

    def update(self, filme: Filme) -> bool:
        try:
            if filme is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise UpdateException("FILMES", "FilmeDAO.update", filme, erro)
        return False

    def select(self, id_filme: str) -> Filme | None:
        try:
            if id_filme != "":
                return Filme()
        except (Exception, psycopg2.DatabaseError) or SelectException as erro:
            raise SelectException("FILMES", "FilmeDAO.select", "Filme(id=" + str(id_filme) + ")", erro)
        return None

    def busca(self, busca: str) -> list[Filme] | None:
        try:
            if busca != "":
                filmes: list[Filme] = [Filme()]
                return filmes
        except (Exception, psycopg2.DatabaseError) or SelectException as erro:
            raise SelectException("FILMES", "FilmeDAO.search", "BUSCA(" + busca + ")", erro)
        return None

    def select_by_genero(self, genero: Genero) -> list[Filme] | None:
        try:
            if genero is not None:
                filmes: list[Filme] = [Filme()]
                return filmes
        except (Exception, psycopg2.DatabaseError) or SelectException as erro:
            raise SelectException("especificaGenerosFilme", "FilmeDAO.select_by_genero", genero, erro)
        return None

    def select_by_rank(self) -> list[Filme]:
        try:
            filmes: list[Filme] = [Filme()]
        except (Exception, psycopg2.DatabaseError) or SelectException as erro:
            raise SelectException("FILMES", "FilmeDAO.select_by_rank", "Filme(id=Todos)", erro)
        return filmes

    def select_all(self) -> list[Filme]:
        try:
            filmes: list[Filme] = [Filme()]
        except (Exception, psycopg2.DatabaseError) or SelectException as erro:
            raise SelectException("FILMES", "FilmeDAO.select_all", "Filme(id=Todos)", erro)
        return filmes
