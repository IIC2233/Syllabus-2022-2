from PyQt5.QtWidgets import QApplication
from frontend import VentanaInicio, VentanaJuego
import sys
from backend import Juego


class ShootApplication:
    def __init__(self):
        self.frontend_login = VentanaInicio()
        self.frontend_juego = VentanaJuego()
        self.backend = Juego()

    def conectar(self):
        # Frontend avisa al backend que se intentó hacer login
        self.frontend_login.senal_enviar_login.connect(
            self.backend.login)

        # Backend avisa al frontend resultado del login
        self.backend.senal_enviar_validacion.connect(
            self.frontend_login.entrar_juego)

        # Frontend avisa al backend que debe empezar el juego
        self.frontend_login.senal_empezar_juego.connect(
            self.backend.iniciar_juego)

        # Frontend notifica al backend cuando se hace click en pantalla
        self.frontend_juego.senal_click_pantalla.connect(
            self.backend.click_pantalla)

        # Backend le avisa al frontend el tamaño de ventana y que se muestre
        self.backend.senal_configurar_juego.connect(
            self.frontend_juego.configurar_juego)

        # Backend notifica al frontend la aparición y esconder agua
        self.backend.senal_aparecer_agua.connect(
            self.frontend_juego.agregar_label_agua)
        self.backend.senal_desaparecer_agua.connect(
            self.frontend_juego.remover_label_agua)

        # Backend notifica cuando se cambia la vida
        self.backend.senal_cambio_vida.connect(
            self.frontend_juego.actualizar_label_vida)

    def iniciar(self):
        self.frontend_login.show()


if __name__ == '__main__':
    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    game = ShootApplication()
    game.conectar()
    game.iniciar()

    sys.exit(app.exec())
