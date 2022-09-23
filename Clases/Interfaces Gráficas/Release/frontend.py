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

        # Creamos los layouts que usaremos para ajustar los labels
        # en las ventanas y le agregamos los labels correspondientes.
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

    def entrar_juego(self, diccionario):
        # Si el permiso es True, entonces ocultar esta ventana y mostrar una
        # nueva ventana de juego
        pass

    def keyPressEvent(self, event):
        # Detectar cuando se presiona enter (teclas_validas). 
        # En se caso se llama a enviar_login
        teclas_validas = [Qt.Key_Enter, Qt.Key_Return]
        pass

class VentanaJuego(QMainWindow):

    # Definir la señal actualizar_vida, que recibe un int.
    # Definir la señal senal_confirmar_inicio que no recibe nada.
    

    #                            x    y
    click_pantalla = pyqtSignal(int, int)
    #                         (id,   x,   y, alto, ancho)
    aparecer_agua = pyqtSignal(int, int, int, int, int)
    #                             id
    desaparecer_agua = pyqtSignal(int)
    #                               (x_max, y_max)
    senal_iniciar_juego = pyqtSignal(int, int)

    def __init__(self, parent, nombre_jugador):
        super().__init__(parent)
        # Importante! para que el widget esté atento al movimiento del mouse
        self.setMouseTracking(True)

        # Conectar la senal_iniciar_juego con el método para iniciar,
        # instanciar el backend entregándole los parámetros necesarios,
        # conectar las señales de aparecer agua y desaparecer agua.
        # Conectar señales actualizar_vida
        # Setear el atributo background a un QLabel que tenga
        # el pixmap del desierto.

        # Conectar las señales mover_personaje y actualizar_vida
        self.label_vida = QLabel(self)
        self.label_vida.setFont(QFont('Arial', 17))
        self.label_vida.setGeometry(90, 10, 280, 50)
        self.labels_agua = {}  # id: label
        # Importante para que este QLabel sea transparente para los eventos del mouse.
        self.label_vida.setAttribute(Qt.WA_TransparentForMouseEvents)
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

    def iniciar(self, x_max, y_max,):
        # Setear tamaño del juego
        # setear el porte del background para que ande bien
        pass

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
        # Agregar un label para el agua que apareció
        # Recuerda utilizar Qt.WA_TransparentForMouseEvents
        pass
        
        # Código extra para asegurar que el label de disparo
        # Esté siempre encima de todo
        self.label_disparo.raise_()

    def remover_label_agua(self, id):
        # Esconder el label del agua
        pass
