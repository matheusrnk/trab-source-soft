from dataclasses import dataclass, field


@dataclass(order=True)
class Genero:
    id: int = field(default=0)
    nome: str = field(default="")
