import psycopg2

from main.exceptions.InsertException import InsertException
from main.exceptions.DeleteException import DeleteException
from main.exceptions.UpdateException import UpdateException
from main.exceptions.SelectException import SelectException
from main.persistence.Conexao import Conexao
from main.models.avaliacao import Avaliacao


class AvaliacaoDAO:

    def __init__(self):
        self.__con = Conexao()

    def insert(self, avaliacao: Avaliacao) -> bool:
        try:
            if avaliacao is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise InsertException("AVALIACOES", "AvaliacaoDAO.insert", avaliacao, erro)
        return False

    def delete(self, avaliacao: Avaliacao) -> bool:
        try:
            if avaliacao is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise DeleteException("AVALIACOES", "AvaliacaoDAO.delete", avaliacao, erro)
        return False

    def update(self, avaliacao: Avaliacao) -> bool:
        try:
            if avaliacao is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise UpdateException("AVALIACOES", "AvaliacaoDAO.update", avaliacao, erro)
        return False

    def select(self, id_aval: int) -> Avaliacao | None:
        try:
            if id_aval > 0:
                return Avaliacao()
        except (Exception, psycopg2.DatabaseError) or SelectException as erro:
            raise SelectException("AVALIACOES", "AvaliacaoDAO.select", "Filme(id=" + str(id_aval) + ")", erro)
        return None
