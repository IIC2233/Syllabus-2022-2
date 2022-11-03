"""
En este archivo se completan las funciones que son utilizadas para
la creación de la lista de reproducción
"""
from functools import reduce

from usuario import Usuario


def filtrar_prohibidos(iterar_canciones, artista_prohibido):
    """
    Debe filtrar todas canciones que contengan temas prohibidos
    :param artista_prohibido: artista prohibido del usuario
    :param iterar_canciones: iterador sobre lista de canciones
    :return: filter
    """
    # Debes completar esta función


def calcular_afinidades(catalogo_canciones, usuario: Usuario):
    """
    La función debe calcular las afinidades según preferencias del usuario.
    El map retorna tuplas, donde el primer valor es la canción,
    y el segundo valor la afinidad.
    :param usuario: Usuario para quien se crearán las afinidades
    :param catalogo_canciones: zip que retorna canciones
    :return: mapeo que retorna tuplas.
    """
    # Debes completar esta función


def encontrar_canciones_comunes(usuarios_mix_party):
    """
    La función debe encontrar las canciones comunes entre las favoritas
    de cada usuario, y retornar un set que las contenga.
    :param usuarios_mix_party: lista de usuarios que conforman la mix party
    :return: interseccion de las peliculas favoritas de cada usuario
    """
    # Debes completar esta función


def encontrar_usuario_mas_afin(usuario, otros_usuarios):
    """
    Esta función debe encontrar el usuario con mayor compatibilidad.
    Debe primero filtrar usuarios que no tengan el mismo artista_prohibido,
    y luego encontrar aquél con quien tenga mayor compatibilidad
    :param usuario: usuario para quien se encontrará un amigue
    :param otros_usuarios: el resto de los usuarios de DCCanciones
    :return: Usuario más compatible
    """
    # Debes completar esta función
