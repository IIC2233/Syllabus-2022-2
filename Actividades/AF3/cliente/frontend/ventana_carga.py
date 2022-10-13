"""
Instanciamos la ventana carga de PYQT
"""
import sys
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, QTimer, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QApplication
from os.path import join
from utils import data_json

window_name, base_class = uic.loadUiType(join(*data_json(
    "RUTA_PANTALLA_CARGA")))


class VentanaCarga(window_name, base_class):

    senal_enviar_inicio = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.contador = 0
        self.init_gui()

    def init_gui(self):

        # ELIMINAMOS LA BARRA DE TITULO
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # AGREGAMOS UNA SOMBRA AL REDEDOR DE LA VENTANA CENTRAL
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.centralwidget.setGraphicsEffect(self.shadow)

        self.mostrar()

        # QTIMER ==> START
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(data_json("VELOCIDAD_CARGA"))

        # TEXTO INICIAL
        self.label_descripcion.setText(
            "<strong>BIENVENIDO </strong> al DCChayanne")

        # TEXTO CAMBIANTE
        QTimer.singleShot(
            1500,
            lambda: self.label_descripcion.setText(
                "<strong>CARGANDO</strong> Musica"),
        )
        QTimer.singleShot(
            3000,
            lambda: self.label_descripcion.setText(
                "<strong>CARGANDO</strong> Letras"),
        )

    ########################################################################

    def progress(self):
        # BARRA DE PROGRESO
        self.progressBar.setValue(self.contador)

        # CERRAR VENTANA Y CARGA Y ABRIR PANTALLA INICIO
        if self.contador > 100:
            self.timer.stop()
            self.enviar_inicio()
        self.contador += 1

    def enviar_inicio(self):
        self.senal_enviar_inicio.emit()
        self.close()

    def mostrar(self):
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaCarga()
    sys.exit(app.exec_())
