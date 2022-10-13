"""
Módulo principal del cliente.
"""
import sys
from os.path import join
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from backend.cliente import Cliente
from backend.interfaz import Interfaz
from utils import data_json

if __name__ == "__main__":
    HOST = data_json("HOST")
    PORT = data_json("PORT")
    RUTA_ICONO = join(*data_json("RUTA_ICONO"))
    try:
        # =========> Instanciamos la APP <==========
        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon(RUTA_ICONO))

        # =========> Iniciamos el cliente <==========
        cliente = Cliente(HOST, PORT)
        interfaz = Interfaz()

        # =========> Conectamos señales <==========
        # Cliente
        cliente.senal_mostrar_ventana_carga.connect(
            interfaz.mostrar_ventana_carga
            )
        cliente.senal_manejar_mensaje.connect(
            interfaz.manejar_mensaje
            )

        # Señales ventana de carga
        interfaz.ventana_carga.senal_enviar_inicio.connect(
            interfaz.ventana_login.mostrar
            )

        # Señales ventana de login
        interfaz.ventana_login.senal_enviar_login.connect(
            cliente.enviar
            )

        # Señales ventana principal
        interfaz.ventana_principal.senal_descargar_musica.connect(
            cliente.enviar
            )

        # Señales interfaz
        interfaz.senal_preparar_ventana_principal.connect(
            interfaz.ventana_principal.preparar_ventana
            )

        interfaz.senal_actualizar_usuarios.connect(
            interfaz.ventana_principal.actualizar_usuarios
            )
        interfaz.senal_abrir_ventana_principal.connect(
            interfaz.abrir_ventana_principal
            )
        interfaz.senal_login_rechazado.connect(
            interfaz.ventana_login.mostrar_error
            )
        interfaz.senal_tocar_musica.connect(
            interfaz.ventana_principal.tocar_musica
            )

        sys.exit(app.exec_())

    except ConnectionError as e:
        print("Ocurrió un error.", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente...")
        cliente.salir()
        sys.exit()
