from parametros import RUTA_CANCIONES, RUTA_USUARIOS
from cancion import Cancion
from usuario import Usuario


def cargar_canciones():
    """
    Generador que entrega una secuencia de objetos de la clase Pelicula
    """
    with open(RUTA_CANCIONES, "rt", encoding="utf-8") as archivo:
        archivo.readline()
        for linea in archivo:
            nombre, pop, rap, reggaeton, electronica, kpop, rock, indie, artistas = linea.strip().split(",")
            rankings = {
                "Pop": int(pop),
                "Rap": int(rap),
                "Reggaeton": int(reggaeton),
                "Electronica": int(electronica),
                "Kpop": int(kpop),
                "Rock": int(rock),
                "Indie": int(indie)
            }
            artistas = tuple(artista for artista in artistas.split(";"))
            yield Cancion(nombre, rankings, artistas)


def cargar_usuarios():
    """
    Generador que entrega una secuencia de objetos de la clase Usuario
    """
    with open(RUTA_USUARIOS, "r", encoding="utf-8") as archivo:
        archivo.readline()
        for user in archivo:
            nombre, pop, rap, reggaeton, electronica,   \
                kpop, rock, indie, artista_prohibido = user.strip().split(",")
            preferencias = {
                "Pop": float(pop),
                "Rap": float(rap),
                "Reggaeton": float(reggaeton),
                "Electronica": float(electronica),
                "Kpop": float(kpop),
                "Rock": float(rock),
                "Indie": float(indie)
            }
            yield Usuario(nombre, preferencias, artista_prohibido)
