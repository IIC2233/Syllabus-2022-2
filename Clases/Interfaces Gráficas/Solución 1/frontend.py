from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import (
    QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
)
from PyQt5.QtGui import QFont, QPixmap
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QMainWindow)
from backend import Juego, LogInBackend


class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(str)
    senal_recibir_login = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 150)
        self.setWindowTitle("Log In")

        # Creamos los labels que vamos a necesitar en nuestra ventana de LogIn
        username_label = QLabel('Ingrese su nombre:', self)
        self.input_usuario = QLineEdit('', self)
        self.boton_ingresar = QPushButton("Ingresar", self)

        # Creamos los layouts que usaremos para ajustar los labels en
        # las ventanas y le agregamos los labels correspondientes.
        layout_principal = QVBoxLayout()
        layout_formulario = QHBoxLayout()
        layout_boton = QHBoxLayout()
        layout_formulario.addWidget(username_label)

        layout_boton.addWidget(self.boton_ingresar)

        layout_formulario.addWidget(self.input_usuario)
        layout_principal.addLayout(layout_formulario)
        layout_principal.addLayout(layout_boton)
        self.setLayout(layout_principal)

        # Finalmente, dejamos las señales conectadas para que todo ande bien,
        # y le asignamos un backend a la ventana
        self.boton_ingresar.clicked.connect(self.enviar_login)
        self.senal_recibir_login.connect(self.entrar_juego)
        self.backend = LogInBackend(self.senal_enviar_login,
                                    self.senal_recibir_login)
        self.show()


    def enviar_login(self):
        # Le avisamos al backend que nos estamos conectando mediante la señal.
        self.senal_enviar_login.emit(self.input_usuario.text())

    # BONUS: detectar cuando se presiona enter. En se caso se llama a enviar_login
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.enviar_login()

    def entrar_juego(self, diccionario):
        if diccionario["permiso"]:
            VentanaJuego(self, diccionario["nombre"])
            self.hide()
        else:
            #TODO para la casa: notificar en la interfaz que no tiene permiso para no 
            #usar prints.
            print("No tienes permiso")


class VentanaJuego(QMainWindow):

    click_pantalla = pyqtSignal(int, int)
    actualizar_vida = pyqtSignal(int)
    #                         (id,   x,   y, alto, ancho)
    aparecer_agua = pyqtSignal(int, int, int, int, int)
    #                             id
    desaparecer_agua = pyqtSignal(int)
    #                               (x_max, y_max)
    senal_iniciar_juego = pyqtSignal(int, int)
    senal_confirmar_inicio = pyqtSignal()

    def __init__(self, parent, nombre_jugador):
        super().__init__(parent)
        self.senal_iniciar_juego.connect(self.iniciar)
        # Importante! para que el widget esté atento al movimiento del mouse
        self.setMouseTracking(True)

        # QLabel para el Background
        self.background = QLabel(self)
        background = QPixmap('./sprites/desierto.jpg')
        self.background.setPixmap(background)
        # Importante para que este QLabel sea transparente para los eventos del mouse.
        self.background.setAttribute(Qt.WA_TransparentForMouseEvents)

        # QLabel para la Vida
        self.label_vida = QLabel(self)
        self.label_vida.setFont(QFont('Arial', 17))
        self.label_vida.setGeometry(90, 10, 280, 50)
        # Importante para que este QLabel sea transparente para los eventos del mouse.
        self.label_vida.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.labels_agua = {}  # id: label
        self.aparecer_agua.connect(self.agregar_label_agua)
        self.desaparecer_agua.connect(self.remover_label_agua)
        self.pixmap_agua = QPixmap('./sprites/water.png')

        # QLabel para la mira del disparo
        self.label_disparo = QLabel(self)
        pixmap = QPixmap('./sprites/shooting-target.png')
        self.label_disparo.setPixmap(pixmap)
        self.label_disparo.setScaledContents(True)
        self.label_disparo.setGeometry(-100, -100, 100, 100)
        
        # Importante para que este QLabel sea transparente para los eventos del mouse.
        self.label_disparo.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.show()
  
        self.actualizar_vida.connect(self.actualizar_label_vida)
        self.backend = Juego(
            self.click_pantalla,
            self.actualizar_vida,
            nombre_jugador,
            self.aparecer_agua,
            self.desaparecer_agua,
            self.senal_confirmar_inicio,
            self.senal_iniciar_juego
        )
        self.backend.iniciar_juego()
        

    def iniciar(self, x_max, y_max):
        self.setGeometry(100, 100, x_max, y_max)
        self.background.setGeometry(0, 0, x_max, y_max)  
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x = event.pos().x()
            y = event.pos().y()
            self.click_pantalla.emit(x, y)
    
    def mouseMoveEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        # Hacemos -50 para asegurar que esté en el centro.
        self.label_disparo.move(x - 50, y - 50)

    def actualizar_label_vida(self, vida):
        self.label_vida.setText(f'Tienes {vida} de vida')

    def agregar_label_agua(self, id, x, y, alto, ancho):
        label = QLabel(self)
        label.setPixmap(self.pixmap_agua)
        label.setScaledContents(True)
        label.setGeometry(x, y, ancho, alto)
        # Importante para que este QLabel sea transparente para los eventos del mouse.
        label.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.labels_agua[id] = label
        label.show()
        self.label_disparo.raise_()

    def remover_label_agua(self, id):
        # Recomendar que investiguen sobre formas de eliminar este elemento en vez de ocultarlo
        self.labels_agua[id].hide()
