from typing import List, TypeVar, Generic
import os
from abc import ABC, abstractmethod
from collections import deque

from parametros import TOKENS_FILE_PATH, ISSUES_FILE_PATH

# Una forma de definir tipos genéricos
# https://docs.python.org/3/library/typing.html#typing.Generic

T = TypeVar('T')


class DequeCSV(ABC, deque, Generic[T]):
    def __init__(self, archivo: str, cabeceras: list) -> None:
        super().__init__()
        self.archivo: str = archivo
        self.cabeceras: list = cabeceras
        self.ancho: int = len(self.cabeceras)
        self.cargado: bool = False

    @abstractmethod
    def campos_a_objeto(self, campos: List[str]) -> T:
        pass

    @abstractmethod
    def objeto_a_campos(self, objeto: T) -> List[str]:
        pass

    def cargar(self):
        self.clear()
        if not self.cargado and not os.path.isfile(self.archivo):
            self.cargado = True
            self.guardar()
        try:
            with open(self.archivo, 'r+', encoding='utf-8') as f:
                if f.readline().replace('\n', '') == ','.join(self.cabeceras):
                    while linea := f.readline():
                        campos = linea.replace('\n', '').split(',', self.ancho)
                        self.append(self.campos_a_objeto(campos))
                    self.cargado = True
                else:
                    raise Exception(0, 'Format Error')
        except Exception as e:
            print(f'Error Grave: {self.archivo} - {e.args[1]}')
            exit(1)

    def guardar(self):
        if not self.cargado:
            return False
        try:
            with open(self.archivo, 'w+', encoding='utf-8') as f:
                f.write(','.join(self.cabeceras) + '\n')
                for e in self:
                    f.write(','.join(self.objeto_a_campos(e)) + '\n')
                return True
        except Exception as e:
            print(f'Error Grave: {self.archivo} - {e.args[1]}')
            exit(1)


class Tokens(DequeCSV[str]):
    def __init__(self):
        kwargs = {'archivo': TOKENS_FILE_PATH, 'cabeceras': ['token']}
        super().__init__(**kwargs)
        self.cargar()

    def campos_a_objeto(self, campos: List[str]) -> str:
        return campos[0]

    def objeto_a_campos(self, objeto: str) -> List[str]:
        return [objeto]


class Issues(DequeCSV[int]):
    def __init__(self):
        kwargs = {'archivo': ISSUES_FILE_PATH, 'cabeceras': ['numero']}
        super().__init__(**kwargs)
        self.cargar()

    def campos_a_objeto(self, campos: List[str]) -> int:
        return int(campos[0])

    def objeto_a_campos(self, objeto: int) -> List[str]:
        return [str(objeto)]
