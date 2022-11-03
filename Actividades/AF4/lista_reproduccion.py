"""
En este archivo se encuentra la clase ListaReproduccion, la Iterable que
contiene los videos ordenados
"""


class ListaReproduccion:

    def __init__(self, lista_canciones, usuario, nombre):
        self.lista_canciones = lista_canciones
        self.usuario = usuario
        self.nombre = nombre

    def __iter__(self):
        # Debes completar este método
        pass

    def __str__(self):
        return f"Lista de Reproducción de {self.usuario}: {self.nombre}"


class IterarLista:

    def __init__(self, lista_canciones):
        self.lista_canciones = lista_canciones

    def __iter__(self):
        # Debes completar este método
        pass

    def __next__(self):
        # Debes completar este método
        pass
