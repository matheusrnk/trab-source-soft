import psycopg2
from main.exceptions.InsertException import InsertException
from main.exceptions.DeleteException import DeleteException
from main.exceptions.UpdateException import UpdateException
from main.exceptions.SelectException import SelectException
from main.persistence.Conexao import Conexao
from main.models.genero import Genero


class GeneroDAO:

    def __init__(self):
        self.__con = Conexao()

    def insert(self, genero: Genero) -> bool:
        try:
            if genero is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise InsertException("GENEROS", "GeneroDAO.insert", genero, erro)
        return False

    def delete(self, genero: Genero) -> bool:
        try:
            if genero is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise DeleteException("GENEROS", "GeneroDAO.delete", genero, erro)
        return False

    def update(self, genero: Genero) -> bool:
        try:
            if genero is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise UpdateException("GENEROS", "GeneroDAO.update", genero, erro)
        return False

    def select(self, id_genero: int) -> Genero | None:
        try:
            if id_genero > 0:
                return Genero()
        except (Exception, psycopg2.DatabaseError) as erro:
            raise SelectException("GENEROS", "GeneroDAO.select", "Genero(id="+str(id_genero)+")", erro)
        return None

    def select_all(self) -> list[Genero]:
        try:
            generos: list[Genero] = [Genero()]
        except (Exception, psycopg2.DatabaseError) as erro:
            raise SelectException("GENEROS", "GeneroDAO.select_all", "Genero(id=Todos)", erro)
        return generos
