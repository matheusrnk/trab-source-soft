import psycopg2
from main.exceptions.InsertException import InsertException
from main.exceptions.DeleteException import DeleteException
from main.exceptions.UpdateException import UpdateException
from main.exceptions.SelectException import SelectException
from main.persistence.Conexao import Conexao
from main.models.ator import Ator
from main.models.filme import Filme
from main.models.usuario import Usuario


class UsuarioDAO:

    def __init__(self):
        self.__con = Conexao()

    def insert(self, usuario: Usuario) -> bool:
        try:
            if usuario is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise InsertException("USUARIOS", "UsuarioDAO.insert", usuario, erro)
        return False

    def delete(self, usuario: Usuario) -> bool:
        try:
            if usuario is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise DeleteException("USUARIOS", "UsuarioDAO.delete", usuario, erro)
        return False

    def update(self, usuario: Usuario) -> bool:
        try:
            if usuario is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise UpdateException("USUARIOS", "UsuarioDAO.update", usuario, erro)
        return False

    def select(self, nickname: str) -> Usuario | None:
        try:
            if nickname != "":
                return Usuario()
        except (Exception, psycopg2.DatabaseError) or SelectException as erro:
            raise SelectException("USUARIOS", "UsuarioDAO.select", "Usuario(nick="+str(nickname)+")", erro)
        return None

    def login(self, nickname: str, senha: str) -> bool:
        try:
            if nickname != "" and senha != "":
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise SelectException("USUARIOS", "UsuarioDAO.login", "Usuario(nick="+nickname+")", erro)
        return False

    def insert_ator_usuario(self, usuario: Usuario, ator: Ator) -> bool:
        try:
            if usuario is not None and ator is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise InsertException("AtoresSalvosUsuario", "UsuarioDAO.insert_ator_usuario", (usuario, ator), erro)
        return False

    def delete_ator_usuario(self, usuario: Usuario, ator: Ator) -> bool:
        try:
            if usuario is not None and ator is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise DeleteException("AtoresSalvosUsuario", "UsuarioDAO.delete_ator_usuario", (usuario, ator), erro)
        return False

    def insert_filme_usuario(self, usuario: Usuario, filme: Filme) -> bool:
        try:
            if usuario is not None and filme is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise InsertException("FilmesSalvosUsuario", "UsuarioDAO.insert_filme_usuario", (usuario, filme), erro)
        return False

    def delete_filme_usuario(self, usuario: Usuario, filme: Filme) -> bool:
        try:
            if usuario is not None and filme is not None:
                return True
        except (Exception, psycopg2.DatabaseError) as erro:
            raise DeleteException("FilmesSalvosUsuario", "UsuarioDAO.delete_filme_usuario", (usuario, filme), erro)
        return False
