from main.models.avaliacao import Avaliacao
from main.models.ator import Ator
from main.models.filme import Filme
from main.models.usuario import Usuario
from main.persistence.AvaliacaoDAO import AvaliacaoDAO
from main.persistence.UsuarioDAO import UsuarioDAO


class Sistema:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def cadastrar_usuario(self, usuario: Usuario) -> bool:
        return UsuarioDAO().insert(usuario)

    def salva_filme_usuario(self, usuario: Usuario, filme: Filme) -> bool:
        return UsuarioDAO().insert_filme_usuario(usuario, filme)

    def exclui_filme_usuario(self, usuario: Usuario, filme: Filme) -> bool:
        return UsuarioDAO().delete_filme_usuario(usuario, filme)

    def busca_filmes_salvos_usuario(self, usuario: Usuario) -> list[Filme]:
        return usuario.filmes_salvos

    def salva_ator_usuario(self, usuario: Usuario, ator: Ator) -> bool:
        return UsuarioDAO().insert_ator_usuario(usuario, ator)

    def exclui_ator_usuario(self, usuario: Usuario, ator: Ator) -> bool:
        return UsuarioDAO().delete_ator_usuario(usuario, ator)

    def busca_atores_salvos_usuario(self, usuario: Usuario) -> list[Filme]:
        return usuario.atores_salvos

    def insere_avaliacao_filme(self, usuario: Usuario, aval: Avaliacao) -> bool:
        if usuario is not None:
            return AvaliacaoDAO().insert(aval)
        return False

    def login_usuario(self, nick: str, senha: str) -> bool:
        return UsuarioDAO().login(nick, senha)

    def logout_usuario(self) -> bool:
        return False
