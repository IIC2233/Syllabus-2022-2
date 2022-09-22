from PyQt5.QtWidgets import QApplication
from frontend import VentanaInicio
import sys

if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    login = VentanaInicio()
    sys.exit(app.exec())
