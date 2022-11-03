"""
En este archivo se encuentra la clase central de DCCanciones.
Esta instancia las clases y desarrolla el flujo principal
de la actividad.
"""
import time
from cargar_archivos import cargar_canciones, cargar_usuarios
from funciones import (
    calcular_afinidades, filtrar_prohibidos,
    encontrar_canciones_comunes, encontrar_usuario_mas_afin,
)
from parametros import TIEMPO_REPRODUCCION


class DCCanciones:

    def __init__(self):
        print("Iniciando DCCanciones...")
        self.usuarios = {
            usuario.nombre: usuario
            for usuario in cargar_usuarios()
        }
        # Creamos y limpiamos las listas de todos los usuarios.
        # Esto ayuda pues queda guardada la afinidad de sus canciones favoritas
        for usuario in self.usuarios.values():
            self.crear_lista_principal(usuario)
            usuario.limpiar_listas()

    @property
    def canciones(self):
        for cancion in cargar_canciones():
            yield cancion

    def crear_lista_principal(self, usuario):
        print(f"Creando lista de reproducción para {usuario.nombre}")
        canciones_permitidas = filtrar_prohibidos(
            self.canciones, usuario.artista_prohibido,
        )
        mapeo_afinidades = calcular_afinidades(canciones_permitidas, usuario)
        usuario.crear_lista(mapeo_afinidades, "Principal")

    def crear_mix_party(self, usuario):
        mix_party_completa = False
        mix_party = [usuario]
        prompt_str = "¿A quién quieres agregar a tu Mix Party?"
        finalizar_str = "Finalizar Mix Party"
        while not mix_party_completa:
            amigues = filter(
                lambda x: self.usuarios[x] not in mix_party,
                self.usuarios.keys(),
            )
            nombre = self.recibir_input(amigues, prompt_str, finalizar_str)
            if nombre == finalizar_str:
                mix_party_completa = True
            else:
                nuevo_miembro = self.usuarios[nombre]
                mix_party.append(nuevo_miembro)
                print(f"Agregando a {nombre} a la Mix Party...")
                print(f"Compatibilidad: {usuario + nuevo_miembro}")

        if len(mix_party) < 2:
            print("Necesitas al menos dos personas para una Watch Party!")
            return

        canciones_comunes = encontrar_canciones_comunes(mix_party)
        if canciones_comunes:
            nombre_lista = input("Introduce un nombre para la lista: ")
            filtro_nombre = filter(
                lambda x: str(x) in canciones_comunes,
                usuario.listas_reproduccion["Principal"],
            )
            for amigue in mix_party:
                mapeo_afinidad = map(
                    lambda x: (x, amigue.afinidades[str(x)]),
                    filtro_nombre,
                )
                amigue.crear_lista(set(mapeo_afinidad), nombre_lista[:10])
            print(f"Mix Party {nombre_lista} creada exitosamente!")
        else:
            print("No tienes canciones comunes con estos usuarios u.u")

    def recomendar_amigue(self, usuario):
        filtro_amigues = filter(lambda x: x != usuario, self.usuarios.values())
        usuario_mas_afin = encontrar_usuario_mas_afin(usuario, filtro_amigues)
        print(f"DCCanciones recomienda a {usuario_mas_afin}!")
        print(f"Tienen una compatibilidad de {usuario + usuario_mas_afin}!")

    def iniciar_reproduccion(self, usuario):
        prompt_str = "¿Cuál Lista de Reproducción deseas reproducir?"
        nombre = self.recibir_input(
            usuario.listas_reproduccion.keys(), prompt_str,
        )
        if nombre == "Volver":
            return
        self.reproducir_lista(usuario, nombre)


    def reproducir_lista(self, usuario, nombre_lista):
        feedback_canciones = usuario.escuchar_canciones(nombre_lista)
        for like, rankings_cancion in feedback_canciones:
            time.sleep(TIEMPO_REPRODUCCION)
            for ranking, valor in usuario.preferencias.items():
                diferencia = rankings_cancion[ranking] - valor
                if like:
                    # Sólo las preferencias cuyo valor
                    # es menor al ranking de la cancion suben
                    usuario.preferencias[ranking] += max(
                        min(diferencia / 10, 1.), 0.,
                    )
                else:
                    # Sólo las preferencias cuyo valor
                    # es mayor al ranking de la cancion bajan
                    usuario.preferencias[ranking] -= max(
                        min(-diferencia / 10, 1.), 0.,
                    )
        # Volvemos a crear la lista con la nueva información
        print(
            "Input recibido. Se procederá a modificar la lista "
            "Principal del usuario"
        )
        self.crear_lista_principal(usuario)

    def run(self):
        running = True
        usuario = None
        while running:
            nombre = self.recibir_input(
                self.usuarios.keys(),
                "¿A cuál usuario deseas acceder?",
                "Salir",
            )
            if nombre == "Salir":
                running = False
            else:
                usuario = self.usuarios[nombre]
                print(f"Cargando lista de reproducción para {usuario.nombre}")
                self.crear_lista_principal(usuario)
            while usuario is not None:
                usuario.print_stats()
                self.__imprimir_acciones()
                accion = input("Ingresa el número de la acción "
                               "correspondiente: ")
                if accion == "0":
                    # Liberamos algo de espacio en la memoria
                    usuario.limpiar_listas()
                    usuario = None
                elif accion == "1":
                    self.iniciar_reproduccion(usuario)
                elif accion == "2":
                    self.crear_mix_party(usuario)
                elif accion == "3":
                    self.recomendar_amigue(usuario)
                else:
                    print("Opción inválida")
        print("Hasta Luego! Gracias por preferirnos :)")

    def recibir_input(self, opciones, prompt, accion_volver="Volver"):
        opciones_numeradas = tuple(enumerate(opciones, 1))
        dict_opciones = {
            str(numero): opcion
            for numero, opcion in opciones_numeradas
        }
        dict_opciones["0"] = accion_volver
        self.__imprimir_opciones_en_filas(opciones_numeradas, accion_volver)
        respuesta = None
        while respuesta is None:
            respuesta = input(prompt + "\nIngresa el número correspondiente: ")
            if respuesta not in dict_opciones:
                print("Opción inválida")
                respuesta = None

        return dict_opciones[respuesta]

    @staticmethod
    def __imprimir_acciones():
        print("0.- Cerrar sesión\n"
              "1.- Reproducir Lista\n"
              "2.- Crear Mix Party!\n"
              "3.- Recomendar Amigue")

    @staticmethod
    def __imprimir_opciones_en_filas(opciones_numeradas,
                                     accion_volver="Volver"):
        columnas = 0
        for numero, opcion in opciones_numeradas:
            end = "\n" if columnas == 3 else "  "
            print(f"{numero: >3d}.-  {opcion: <30.30s}", end=end)
            columnas += 1
            if columnas > 3:
                columnas = 0
        print(f"\n  0.-  {accion_volver}")
