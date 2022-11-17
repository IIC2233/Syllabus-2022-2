from typing import NamedTuple, List
import re

from parametros import REGEX_FILTRO


# Otra forma de definir named tuples
# https://docs.python.org/3/library/typing.html#typing.NamedTuple

class Anime(NamedTuple):
    nombre: str
    ano: str
    etiquetas: List[str]

    def __repr__(self) -> str:
        return f'({self.ano}) {self.nombre} -- Tags: {len(self.etiquetas)}'


def filtro_animes(animes: List[Anime]) -> List[Anime]:
    patron = re.compile(REGEX_FILTRO)
    return [x for x in animes if patron.match(x.nombre.lower())]


if __name__ == "__main__":
    un_anime = Anime("Spy x Family", "2021", ["Family Life", "Spy"])
