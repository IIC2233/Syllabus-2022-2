"""
Modulo contiene la clase Logica del servidor
"""

from utils import data_json
from os.path import join


class Logica:
    def __init__(self, parent):
        # Esto permite ejecutar funciones de la clase Servidor
        self.parent = parent

        self.usuarios = {}
        self.contrasena = data_json("PASSWORD")
        self.canciones = data_json("CANCIONES")
        self.rutas_caratulas = [
            ";".join(data_json("CARATULA_1")),
            ";".join(data_json("CARATULA_2")),
            ";".join(data_json("CARATULA_3")),
            ";".join(data_json("CARATULA_4")),
        ]

    def crear_usuarios(self):
        """
        Lee los datos del archivo csv
        y los guarda en estructuras de la clase Usuario
        """
        pass

    def validar_login(self, nombre, contrasena, socket_cliente):
        if self.contrasena == contrasena and \
                nombre not in self.usuarios.values():

            self.usuarios[self.parent.id_cliente - 1] = nombre
            for ruta in self.rutas_caratulas:
                self.parent.enviar_archivo(
                    socket_cliente, join(*ruta.split(";")))
            return {
                "comando": "respuesta_validacion_login",
                "estado": "aceptado",
                "nombre_usuario": nombre,
                "canciones": ",".join(self.canciones),
                "rutas_caratulas": ",".join(self.rutas_caratulas),
                "usuarios": ",".join(self.usuarios.values()),
            }
        return {
            "comando": "respuesta_validacion_login",
            "estado": "rechazado",
            "error": "datos invalidos",
        }

    def procesar_mensaje(self, mensaje, socket_cliente):
        """
        Procesa un mensaje recibido desde el cliente
        """
        try:
            comando = mensaje["comando"]
        except KeyError:
            return {}
        if comando == "validar_login":
            respuesta = self.validar_login(
                mensaje["nombre usuario"], mensaje["contrasena"], socket_cliente
            )
        elif comando == "descargar_musica":
            id = mensaje["id"]
            ruta = ";".join(data_json(f"CANCION_{id}"))
            self.parent.enviar_archivo(socket_cliente, join(*ruta.split(";")))
            respuesta = {
                "comando": "respuesta_descarga_multimedia",
                "ruta": join(*ruta.split(";")),
            }
        return respuesta

    def eliminar_nombre(self, id):
        """
        Elimina el nombre del usuario del diccionario
        """
        self.usuarios.pop(id, None)
