from main.models.imagem import Imagem
from main.models.genero import Genero
from dataclasses import dataclass, field


@dataclass(order=True, repr=True)
class Filme:
    id: str = field(default="")
    titulo: str = field(default="")
    ano: int = field(default=0)
    rank: int = field(default=0)
    sinopse: str = field(default="")
    classificacao_ind: str = field(default="")
    capa: Imagem = field(default=None, compare=False, repr=False)
    generos: list[Genero] = field(default_factory=list, compare=False, repr=False)
    elenco_principal: list = field(default_factory=list, compare=False, repr=False)  # atores
    avaliacoes: list = field(default_factory=list, compare=False, repr=False)
