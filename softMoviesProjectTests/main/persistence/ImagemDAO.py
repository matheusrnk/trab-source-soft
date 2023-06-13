import psycopg2
from main.exceptions.InsertException import InsertException
from main.exceptions.DeleteException import DeleteException
from main.exceptions.UpdateException import UpdateException
from main.exceptions.SelectException import SelectException
from main.persistence.Conexao import Conexao
from main.models.imagem import Imagem


class ImagemDAO:

    def __init__(self):
        self.__con = Conexao()

    def insert(self, imagem: Imagem) -> bool:
        try:
            if imagem is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise InsertException("IMAGENS", "ImagemDAO.insert", imagem, erro)
        return False

    def delete(self, imagem: Imagem) -> bool:
        try:
            if imagem is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise DeleteException("IMAGENS", "ImagemDAO.delete", imagem, erro)
        return False

    def update(self, imagem: Imagem) -> bool:
        try:
            if imagem is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise UpdateException("IMAGENS", "ImagemDAO.update", imagem, erro)
        return False

    def select(self, id_imagem: int) -> Imagem | None:
        try:
            if id_imagem > 0:
                return Imagem()
        except (Exception, psycopg2.DatabaseError) as erro:
            raise SelectException("IMAGENS", "ImagemDAO.select_imagem", "Imagem(id="+str(id_imagem)+")", erro)
        return None
