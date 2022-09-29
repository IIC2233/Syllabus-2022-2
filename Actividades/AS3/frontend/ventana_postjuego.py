from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_POSTJUEGO)


class VentanaPostjuego(window_name, base_class):

    senal_abrir_inicio = pyqtSignal()
    senal_cerrar_juego = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.puntaje = 0
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Ventana PostJuego")
        self.boton_salir.clicked.connect(self.salir)
        self.boton_volver.clicked.connect(self.volver_inicio)

        logo_gameover = QPixmap(p.RUTA_GAMEOVER)
        self.logo_game_over.setPixmap(logo_gameover)
        self.logo_game_over.setScaledContents(True)

    def volver_inicio(self):
        self.senal_abrir_inicio.emit()
        self.hide()

    def abrir(self, datos: dict):
        self.show()
        self.puntaje = datos['Puntaje']
        self.label_puntaje.setText(datos['Puntaje'])
        self.label_puntaje.repaint()

    def salir(self):
        self.hide()
        self.senal_cerrar_juego.emit()
