from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont, QPixmap


class VentanaInicio(QWidget):
    senal_enviar_login = pyqtSignal(str)
    senal_empezar_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 150)
        self.setWindowTitle("Log In")

        # Creamos los labels que vamos a necesitar en nuestra ventana de LogIn
        username_label = QLabel('Ingrese su nombre:', self)
        self.input_usuario = QLineEdit('', self)
        self.boton_ingresar = QPushButton("Ingresar", self)

        # Creamos el layout de nuestra venana y agregamos los elementos
        layout_formulario = QHBoxLayout()
        layout_formulario.addWidget(username_label)
        layout_formulario.addWidget(self.input_usuario)

        layout_boton = QHBoxLayout()
        layout_boton.addWidget(self.boton_ingresar)

        layout_principal = QVBoxLayout()
        layout_principal.addLayout(layout_formulario)
        layout_principal.addLayout(layout_boton)

        self.setLayout(layout_principal)

        # Conectamos las señales de los elementos
        self.boton_ingresar.clicked.connect(self.enviar_login)

        self.show()

    def enviar_login(self):
        # Le avisamos al backend que nos estamos conectando mediante la señal.
        self.senal_enviar_login.emit(self.input_usuario.text())

    # BONUS: detectar cuando se presiona enter para también enviar_login
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.enviar_login()

    def entrar_juego(self, diccionario):
        if diccionario["permiso"]:
            self.senal_empezar_juego.emit(diccionario["nombre"])
            self.hide()
        else:
            # TODO: notificar en la GUI para no usar prints.
            print("No tienes permiso")


class VentanaJuego(QMainWindow):
    senal_click_pantalla = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()
        # Importante el QLabel sea transparente a los eventos del mouse.
        self.setMouseTracking(True)

        # QLabel para el Background
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap('./sprites/desierto.jpg'))
        # Importante el QLabel sea transparente a los eventos del mouse.
        self.background.setAttribute(Qt.WA_TransparentForMouseEvents)

        # QLabel para la Vida
        self.label_vida = QLabel(self)
        self.label_vida.setFont(QFont('Arial', 17))
        self.label_vida.setGeometry(90, 10, 280, 50)
        # Importante el QLabel sea transparente a los eventos del mouse.
        self.label_vida.setAttribute(Qt.WA_TransparentForMouseEvents)

        self.labels_agua = {}  # id: label
        self.pixmap_agua = QPixmap('./sprites/water.png')

        # QLabel para la mira del disparo
        self.label_disparo = QLabel(self)
        self.label_disparo.setPixmap(QPixmap('./sprites/shooting-target.png'))
        self.label_disparo.setScaledContents(True)
        self.label_disparo.setGeometry(-100, -100, 100, 100)
        # Importante el QLabel sea transparente a los eventos del mouse.
        self.label_disparo.setAttribute(Qt.WA_TransparentForMouseEvents)

    def configurar_juego(self, x_max, y_max):
        self.setGeometry(100, 100, x_max, y_max)
        self.background.setGeometry(0, 0, x_max, y_max)
        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x = event.pos().x()
            y = event.pos().y()
            self.senal_click_pantalla.emit(x, y)

    def mouseMoveEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        # Hacemos -50 para que esté en el centro.
        self.label_disparo.move(x - 50, y - 50)

    def actualizar_label_vida(self, texto):
        self.label_vida.setText(texto)
        self.label_vida.resize(self.label_vida.sizeHint())

    def agregar_label_agua(self, id_agua, x, y, alto, ancho):
        label = QLabel(self)
        label.setPixmap(self.pixmap_agua)
        label.setScaledContents(True)
        label.setGeometry(x, y, ancho, alto)
        # Importante el QLabel sea transparente a los eventos del mouse.
        label.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.labels_agua[id_agua] = label
        self.label_disparo.raise_()
        label.show()

    def remover_label_agua(self, id_agua):
        # Recomendamos investigar como eliminar elementos y no solo ocultarlos
        self.labels_agua[id_agua].hide()
