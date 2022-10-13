"""
Modulo contiene funciones auxiliares
"""
import json
from os.path import join


def data_json(llave):
    """
    Lee parametros.json y retorna el valor del dato con la key correspondiente
    """
    ruta = join("parametros.json")
    with open(ruta, "r", encoding="UTF-8") as archivo:
        diccionario_data = json.load(archivo)
    valor = diccionario_data[llave]
    return valor


def leer_archivo(ruta):
    """
    Lee y devuelve los bytes del archivo en la ruta
    """
    with open(ruta, "rb") as archivo:
        bytes_ = archivo.read()
    return bytes_
