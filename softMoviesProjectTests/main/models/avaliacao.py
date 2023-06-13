from main.models.usuario import Usuario
from main.models.filme import Filme
from dataclasses import dataclass, field


@dataclass(order=True)
class Avaliacao:
    id: int = field(default=0)
    upvotes: int = field(default=0)
    downvotes: int = field(default=0)
    data_hora: str = field(default="")
    classificacao: bool = field(default=False)
    texto: str = field(default="")
    filme: Filme = field(default=None, compare=False, repr=False)
    usuario: Usuario = field(default=None, compare=False, repr=False)
