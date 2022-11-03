"""
En este archivo se encuentran las clases Usuario y Cancion
"""
from random import choice

import parametros as p


class Cancion:

    def __init__(self, nombre, rankings, artistas):
        self.nombre = nombre
        self.rankings = rankings
        self.artistas = artistas

    def reproducir(self):
        """
        Printea arte ASCII o algo así (algo ascii?)
        :return: None
        """
        print(f"Reproduciendo canción {self.nombre}")

        tipo = self.tipo_cancion()
        with open(p.RUTAS_ARTE[tipo], "r", encoding="UTF-8") as archivo:
            print(archivo.read())

    def tipo_cancion(self):
        maxima_afinidad = 0
        tipos_maximos = []
        for tipo in self.rankings.keys():
            if self.rankings[tipo] > maxima_afinidad:
                tipos_maximos = [tipo]
                maxima_afinidad = self.rankings[tipo]
            elif self.rankings[tipo] == maxima_afinidad:
                tipos_maximos.append(tipo)
        return choice(tipos_maximos)

    def __repr__(self):
        return self.nombre
