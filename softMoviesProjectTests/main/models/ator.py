from main.models.imagem import Imagem
from dataclasses import dataclass, field


@dataclass(order=True, repr=True)
class Ator:
    id: str = field(default="")
    nome: str = field(default="")
    bio: str = field(default="")
    data_nasc: str = field(default="")
    local_nasc: str = field(default="")
    sexo: str = field(default="")
    altura: float = field(default=0)
    foto: Imagem = field(default=None, compare=False, repr=False)
    participacoes: list = field(default_factory=list, compare=False, repr=False)  # filmes
