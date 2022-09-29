from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_JUEGO)


class VentanaJuego(window_name, base_class):

    senal_iniciar_juego = pyqtSignal(str)
    senal_tecla = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.labels_bloques = {}
        self.labels_vidas = []
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Ventana de Juego")
        self.asignar_bloques()
        self.labels_vidas = [self.vida_1, self.vida_2, self.vida_3]
        self.boton_salir.clicked.connect(self.close)

    def setear_datos(self, datos: dict):
        self.label_nombre.setText(datos['Usuario'])
        self.label_nombre.repaint()
        self.label_puntos.setText(datos['Puntaje'])
        self.label_puntos.repaint()
        self.label_tiempo.setText(datos['Tiempo'])
        self.label_tiempo.repaint()

    def asignar_bloques(self):
        self.labels_bloques = {
            1: self.bloque_1,
            2: self.bloque_2,
            3: self.bloque_3,
            4: self.bloque_4,
            5: self.bloque_5,
            6: self.bloque_6,
            7: self.bloque_7,
            8: self.bloque_8,
            9: self.bloque_9,
            10: self.bloque_10,
            11: self.bloque_11,
            12: self.bloque_12,
            13: self.bloque_13,
            14: self.bloque_14,
            15: self.bloque_15,
            16: self.bloque_16,
            17: self.bloque_17,
            18: self.bloque_18,
            19: self.bloque_19,
            20: self.bloque_20,
            21: self.bloque_21,
            22: self.bloque_22,
            23: self.bloque_23,
            24: self.bloque_24,
            25: self.bloque_25
        }

    def actualizar_datos(self, datos: dict):
        self.label_puntos.setText(datos['Puntaje'])
        self.label_puntos.repaint()

        self.label_tiempo.setText(datos['Tiempo'])
        self.label_tiempo.repaint()

    def mover_plataforma(self, posicion: tuple):
        self.plataforma.move(posicion[0], posicion[1])

    def mover_pelota(self, posicion: tuple):
        self.pelota.move(posicion[0], posicion[1])

    def eliminar_bloque(self, numero_bloque: int):
        self.labels_bloques[numero_bloque].hide()

    def bajar_vida(self, vidas: int):
        if vidas in range(len(self.labels_vidas)):
            self.labels_vidas[vidas].hide()

    def reset_labels(self):
        for bloque in self.labels_bloques.values():
            bloque.show()
        for vida in self.labels_vidas:
            vida.show()

    def mostrar_ventana(self, usuario):
        # COMPLETAR
        pass

    def keyPressEvent(self, event):
        # COMPLETAR
        pass

