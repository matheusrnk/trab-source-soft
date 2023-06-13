from main.models.imagem import Imagem
from dataclasses import dataclass, field


@dataclass(order=True)
class Usuario:
    nickname: str = field(default="")
    email: str = field(default="")
    nome: str = field(default="")
    senha: str = field(default="")
    retrato: Imagem = field(default=None, compare=False, repr=False)
    filmes_salvos: list = field(default_factory=list, compare=False, repr=False)  # filmes
    atores_salvos: list = field(default_factory=list, compare=False, repr=False)  # atores
