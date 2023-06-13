import psycopg2

from main.exceptions.InsertException import InsertException
from main.exceptions.DeleteException import DeleteException
from main.exceptions.UpdateException import UpdateException
from main.exceptions.SelectException import SelectException
from main.persistence.Conexao import Conexao
from main.models.ator import Ator

# TODO: CRUD e demais funções


class AtorDAO:

    def __init__(self):
        self.__con = Conexao()

    def insert(self, ator: Ator) -> bool:
        try:
            if ator is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise InsertException("ATORES", "AtorDAO.insert", ator, erro)
        return False

    def delete(self, ator: Ator) -> bool:
        try:
            if ator is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise DeleteException("ATORES", "AtorDAO.delete", ator, erro)
        return False

    def update(self, ator: Ator) -> bool:
        try:
            if ator is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise UpdateException("ATORES", "AtorDAO.update", ator, erro)
        return False

    def select(self, id_ator: str) -> Ator | None:
        try:
            if id_ator != "":
                return Ator()
        except (Exception, psycopg2.DatabaseError) or SelectException as erro:
            raise SelectException("ATORES", "AtorDAO.select", "Ator(id="+str(id_ator)+")", erro)
        return None

    def select_all(self) -> list[Ator]:
        try:
            atores: list[Ator] = [Ator()]
        except (Exception, psycopg2.DatabaseError) or SelectException as erro:
            raise SelectException("ATORES", "AtorDAO.select_all", "Ator(id=Todos)", erro)
        return atores
