from collections import defaultdict
from functools import reduce
from random import uniform

import parametros as p
from lista_reproduccion import ListaReproduccion
from parametros import LARGO_LISTA_REPRODUCCION


class Usuario:

    def __init__(self, nombre, preferencias, artista_prohibido):
        self.nombre = nombre
        self.preferencias = preferencias
        self.artista_prohibido = artista_prohibido
        self.listas_reproduccion = {}
        self.afinidades = defaultdict(int)

    @property
    def canciones_favoritas(self):
        return set(self.afinidades)

    def escuchar_canciones(self, nombre_lista):
        # Deben completar
        pass

    def calcular_afinidad(self, cancion):
        afinidad = 0
        for categoria in p.CATEGORIAS:
            afinidad += (
                cancion.rankings[categoria] * self.preferencias[categoria]
            )
        if p.CATEGORIAS:
            afinidad /= len(p.CATEGORIAS)
        else:
            afinidad = 0
        # Guardamos la afinidad para despues!
        self.afinidades[cancion.nombre] = afinidad
        return afinidad

    def calificar_cancion(self, cancion):
        # Una calificacion mayor hará menos probable
        # que le guste el video al usuario
        afinidad = self.afinidades[cancion.nombre]
        calificacion = uniform(0, 5) * uniform(1, 5)
        return calificacion < afinidad

    def crear_lista(self, mapeo_canciones, nombre_lista):
        canciones_favoritas = self.encontrar_canciones_preferidas(mapeo_canciones)
        lista_reproduccion_creada = ListaReproduccion(
            set(canciones_favoritas), self.nombre, nombre_lista,
        )
        self.listas_reproduccion[nombre_lista] = lista_reproduccion_creada

    @staticmethod
    def encontrar_canciones_preferidas(mapeo_canciones):
        canciones_favoritas = set()
        for cancion in mapeo_canciones:
            if len(canciones_favoritas) < LARGO_LISTA_REPRODUCCION:
                canciones_favoritas.add(cancion)
            else:
                cancion_menos_afin = min(
                    canciones_favoritas,
                    key=lambda x: x[1],
                )
                if cancion[1] > cancion_menos_afin[1]:
                    canciones_favoritas.add(cancion)
                    canciones_favoritas.remove(cancion_menos_afin)
        return canciones_favoritas

    def limpiar_listas(self):
        self.listas_reproduccion = {}

    def print_stats(self):
        str_preferencia_categoria = " ".join(
            f"{nombre.upper(): ^15s}" for nombre in self.preferencias
        )
        str_preferencia_valor = " ".join(
            f"{valor: ^15.2f}" for valor in self.preferencias.values()
        )
        print(f"Nombre: {self.nombre}\n"
              f"Artista Prohibido: {self.artista_prohibido}\n"
              f"{str_preferencia_categoria}\n"
              f"{str_preferencia_valor}\n")

    def __add__(self, other):
        union_canciones = self.canciones_favoritas | other.canciones_favoritas
        afinidad_comun = reduce(
            lambda x, y: x + self.afinidades[y] * other.afinidades[y],
            union_canciones,
            0,
        )
        return int(afinidad_comun)

    def __repr__(self):
        return self.nombre
