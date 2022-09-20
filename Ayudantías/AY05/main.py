import sys
from PyQt5.QtWidgets import QApplication
from frontend.ventana_login import VentanaLogin
from frontend.ventana_principal import VentanaPrincipal
from backend.logica_login import LogicaLogin

# Función para debuggear
def hook(type, value, traceback):
    print(type)
    print(traceback)
    sys.__excepthook__ = hook

# Se instancia la aplicación
app = QApplication([])

# Se instancian las clases

# Se conectan las señales

# Se muestra la ventana de login

sys.exit(app.exec_())