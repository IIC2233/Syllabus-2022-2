from PyQt5.QtCore import QObject, pyqtSignal

class LogicaLogin(QObject):

    #Señales

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, usuario, contrasena):
        #Validar si el usuario y la contraseña es correcta y enviar señal
        pass