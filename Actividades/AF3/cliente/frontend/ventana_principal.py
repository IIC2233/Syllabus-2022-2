"""
Instanciamos la ventana principal de PYQT
"""
import sys
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon, QPixmap
from os.path import join
from utils import data_json
from PyQt5.QtMultimedia import QSound

window_name, base_class = uic.loadUiType(join(*data_json(
    "RUTA_PANTALLA_PRINCIPAL")))


class VentanaPrincipal(window_name, base_class):

    senal_mostrar_ventana_principal = pyqtSignal(str)
    senal_descargar_musica = pyqtSignal(dict)
    senal_actualizar_usuarios = pyqtSignal(list)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.paused = False
        self.ruta = str()
        self.setupUi(self)
        self.musica = None
        self.usuario = ''
        self.init_gui()

    def init_gui(self):
        self.widget = QWidget()
        self.vbox = QVBoxLayout()
        # CONEXIONES
        self.button_play.clicked.connect(self.play_pause)
        self.button_play.setIcon(QIcon(join(*data_json("RUTA_PLAY"))))
        self.musica_buttons = [
            self.musica1, self.musica2, self.musica3, self.musica4]

        self.musica1.clicked.connect(lambda: self.descargar_musica(1))
        self.musica2.clicked.connect(lambda: self.descargar_musica(2))
        self.musica3.clicked.connect(lambda: self.descargar_musica(3))
        self.musica4.clicked.connect(lambda: self.descargar_musica(4))

    def actualizar_usuarios(self, usuarios):
        usuarios = [x for x in usuarios if x != self.usuario]

        # Actualizar items ya existentes
        for i in range(self.vbox.count()):
            item = self.vbox.itemAt(i)
            if i < len(usuarios):
                item.widget().setText(usuarios[i])
            else:
                self.vbox.removeItem(item)

        # Agregar nuevos ítems
        if self.vbox.count() < len(usuarios):
            for i in range(self.vbox.count(), len(usuarios)):
                temp = QLabel(usuarios[i])
                temp.setMinimumHeight(45)
                self.vbox.addWidget(temp)

    def preparar_ventana(self, username, canciones, rutas_caratulas, usuarios):
        # Remplazamos la label con el nombre de usuario
        self.usuario = username
        self.label_usuario.setText(username)
        self.label_state.setText("Sin musica seleccionada")
        self.rutas_caratulas = rutas_caratulas

        for id, button in enumerate(self.musica_buttons):
            # cambiamos el texto de los botones
            button.setText(canciones[id])
            # Agregamos un icon a los botones
            button.setIcon(QIcon(join(*rutas_caratulas[id].split(";"))))

        # Agregamos una label de los usuarios al scrollAreaa
        usuarios = [x for x in usuarios if x != self.usuario]
        for usuario in usuarios:
            temp = QLabel(usuario)
            temp.setMinimumHeight(45)
            self.vbox.addWidget(temp)
        self.widget.setLayout(self.vbox)

        # Scroll Area Properties
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widget)

    def descargar_musica(self, id):
        if self.musica is not None:
            self.musica.stop()
            self.musica = None
            self.button_play.setIcon(QIcon(join(*data_json("RUTA_PLAY"))))

        self.label_state.setText("Descargando música")
        self.senal_descargar_musica.emit(
            {"comando": "descargar_musica", "id": id})

        # Se actualiza la caratula inferior de la cancion
        pixeles_caratula_inferior = QPixmap(
            join(*self.rutas_caratulas[id - 1].split(";"))
        )
        self.label_caratula.setPixmap(pixeles_caratula_inferior)
        self.label_caratula.setScaledContents(True)

    def play_pause(self):
        if self.musica is None:
            # Si todaviá no hay música definida, este botón no hace nada
            return

        if self.paused:
            self.paused = False
            self.button_play.setIcon(QIcon(join(*data_json("RUTA_PAUSE"))))
            self.reanudar_musica()

        else:
            self.paused = True
            self.button_play.setIcon(QIcon(join(*data_json("RUTA_PLAY"))))
            self.detener_musica()

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()

    def salir(self):
        self.close()

    def tocar_musica(self, ruta):
        self.ruta = ruta
        self.label_state.setText("Música descargada")
        self.musica = QSound(ruta)
        self.musica.play()
        self.button_play.setIcon(QIcon(join(*data_json("RUTA_PAUSE"))))

    def detener_musica(self):
        self.musica.stop()

    def reanudar_musica(self):
        self.musica.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.mostrar()
    sys.exit(app.exec_())
