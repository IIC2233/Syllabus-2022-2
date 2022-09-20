import os
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel,
                             QHBoxLayout, QVBoxLayout, QLineEdit)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap


class VentanaLogin(QWidget):

    #Señales

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):

        #Ventana

        #Imagen
        
        #Usuario

        #Contraseña

        #Boton
        
        #Layouts

        #Conexiones

        pass

    def enviar_login(self):
        #Enviar señal para validar login
        pass

    def recibir_login(self, valido):
        #Abrir ventana principal si es correcto el login
        pass
        
