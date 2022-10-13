import json
import socket
import threading


class Cliente:

    # Completar
    def __init__(self, host, port):
        pass

    # Completar
    def recibir_input(self):
        pass

    # Completar
    def escuchar_servidor(self):
        pass

    def recibir(self):
        largo_bytes_mensaje = self.socket_cliente.recv(4)
        largo_mensaje = int.from_bytes(largo_bytes_mensaje, byteorder='big')
        bytes_mensaje = bytearray()
        while len(bytes_mensaje) < largo_mensaje:
            bytes_mensaje += self.socket_cliente.recv(60)
        bytes_mensaje_limpios = bytes_mensaje.strip(b'\x00')
        mensaje = self.decodificar_mensaje(bytes_mensaje_limpios)
        return mensaje

    def enviar(self, mensaje):
        bytes_mensaje = self.codificar_mensaje(mensaje)
        while len(bytes_mensaje) % 60 != 0:
            bytes_mensaje += b'\x00'
        largo_bytes_mensaje = len(bytes_mensaje).to_bytes(4, byteorder='big')
        self.socket_cliente.sendall(largo_bytes_mensaje + bytes_mensaje)

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

    def manejar_mensaje_recibido(self, mensaje):
        # Aquí va la lógica de recibir el mensaje
        pass


if __name__ == "__main__":
    host = "localhost"
    port = 5000
    cliente = Cliente(host, port)