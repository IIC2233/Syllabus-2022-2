import json
import socket
import threading
import random
import sys

class Miner:
    id = 0
    def __init__(self, socket_cliente):
        self.id_minero = Miner.id
        self.socket = socket_cliente
        self.materiales = {
            "Carbon" : 0,
            "Hierro" : 0,
            "Oro" : 0,
            "Diamante" : 0
        }
        Miner.id += 1

class Servidor:

    # Completar
    def __init__(self, host, port):
        pass

    # Completar
    def aceptar_clientes(self):
        pass

    # Completar
    def escuchar_cliente(self, minero):
        pass

    def recibir(self, socket_cliente):
        largo_bytes_mensaje = socket_cliente.recv(4)
        largo_mensaje = int.from_bytes(largo_bytes_mensaje, byteorder='big')
        bytes_mensaje = bytearray()
        while len(bytes_mensaje) < largo_mensaje:
            bytes_mensaje += socket_cliente.recv(60)
        bytes_mensaje_limpios = bytes_mensaje.strip(b'\x00')
        if 5 < len(bytes_mensaje_limpios) < 60:
            mensaje = self.decodificar_mensaje(bytes_mensaje_limpios)
            return mensaje
        else:
            return ""

    def enviar(self, mensaje, socket_cliente):
        bytes_mensaje = self.codificar_mensaje(mensaje)
        while len(bytes_mensaje) % 60 != 0:
            bytes_mensaje += b'\x00'
        largo_bytes_mensaje = len(bytes_mensaje).to_bytes(4, byteorder='big')
        socket_cliente.sendall(largo_bytes_mensaje + bytes_mensaje)

    def enviar_todos(self, mensaje):
        for minero in self.clientes.values():
            bytes_mensaje = self.codificar_mensaje(mensaje)
            while len(bytes_mensaje) % 60 != 0:
                bytes_mensaje += b'\x00'
            largo_bytes_mensaje = len(bytes_mensaje).to_bytes(4, byteorder='big')
            minero.socket.sendall(largo_bytes_mensaje + bytes_mensaje)

    def codificar_mensaje(self, mensaje):
        try:
            mensaje_json = json.dumps(mensaje)
            bytes_mensaje = mensaje_json.encode('utf-8')
            return bytes_mensaje
        except json.JSONDecodeError:
            print('No se pudo codificar el mensaje')
            return b''

    def decodificar_mensaje(self, bytes_mensaje):
        try:
            mensaje = json.loads(bytes_mensaje)
            return mensaje
        except json.JSONDecodeError:
            print('No se pudo decodificar el mensaje')
            return ''

    def manejar_mensaje_recibido(self, mensaje, minero):
        if mensaje == "minar":
            material = random.choice(["Carbon", "Hierro", "Oro", "Diamante"])
            cantidad = random.randint(1, 4)
            minero.materiales[material] += cantidad

            return f"Minero #{minero.id_minero} ha minado {cantidad} de {material}"
        elif mensaje == "stats":
            mensaje_stats = f"Estadisticas del minero #{minero.id_minero}"
            for material in minero.materiales:
                mensaje_stats += f"\n> {material} - {minero.materiales[material]}"
                
            return mensaje_stats
            
        return "Comando no válido"


if __name__ == "__main__":
    host = "localhost"
    port = 5000
    servidor = Servidor(host, port)