from PyQt5.QtCore import QObject, QThread, QTimer, pyqtSignal
from time import sleep
from random import randint
import parametros as p


class Botella(QThread):
    id = 0

    def __init__(self, x, y, senal_aparecer, senal_desaparecer):
        super().__init__()
        self.x = x
        self.y = y
        self.senal_aparecer = senal_aparecer
        self.senal_desaparecer = senal_desaparecer
        self.alto = 80
        self.ancho = 40
        self._valida = None
        self.id += 1
        Botella.id += 1

    @property
    def valida(self):
        return self._valida

    @valida.setter
    def valida(self, value):
        if self._valida != value:
            self._valida = value
            if not self.valida:
                self.senal_desaparecer.emit(self.id)
            else:
                self.senal_aparecer.emit(self.id,
                                         self.x,
                                         self.y,
                                         self.alto,
                                         self.ancho)

    def run(self):
        self.valida = True
        sleep(p.TIEMPO_VIDA_BOTELLA)  # Sleep necesita el tiempo en segundos
        self.valida = False


class Jugador:
    def __init__(self, nombre, vida, senal_vida):
        self.nombre = nombre
        self._vida = vida
        self._vida_maxima = vida
        self.senal_vida = senal_vida

    @property
    def tiempo_vida(self):
        return self._vida

    @tiempo_vida.setter
    def tiempo_vida(self, value):
        self._vida = value
        if self.tiempo_vida == 0:
            self.senal_vida.emit(f'{self.nombre} ha muerto de sed')
        else:
            self.senal_vida.emit(
                f'{self.nombre} tiene {self.tiempo_vida} de vida')


class Juego(QObject):
    senal_enviar_validacion = pyqtSignal(dict)
    senal_configurar_juego = pyqtSignal(int, int)
    senal_aparecer_agua = pyqtSignal(int, int, int, int, int)
    senal_desaparecer_agua = pyqtSignal(int)
    senal_cambio_vida = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.jugador = None
        self.x_max = 800
        self.y_max = 500
        self.botellas = []

        self.timer_calor = QTimer(self)
        self.timer_calor.setInterval(p.TIEMPO_CALOR)
        self.timer_calor.timeout.connect(self.sufrir_calor)

        self.timer_aljibe = QTimer(self)
        self.timer_aljibe.setInterval(p.TIEMPO_BOTELLA)
        self.timer_aljibe.timeout.connect(self.dar_agua)

    def login(self, nombre):
        # Solo aceptaremos nombres que empiecen con DCC
        self.senal_enviar_validacion.emit(
            {
                "permiso": nombre.lower().startswith("dcc"),
                "nombre": nombre
            }
        )

    def dar_agua(self):
        x = randint(0, self.x_max)
        y = randint(0, self.y_max)
        botella = Botella(
            x,
            y,
            self.senal_aparecer_agua,
            self.senal_desaparecer_agua
        )
        self.botellas.append(botella)
        botella.start()

    def iniciar_juego(self, nombre):
        self.jugador = Jugador(nombre, p.VIDA_MAXIMA, self.senal_cambio_vida)
        self.senal_configurar_juego.emit(self.x_max, self.y_max)
        self.timer_calor.start()
        self.timer_aljibe.start()

    def sufrir_calor(self):
        self.jugador.tiempo_vida -= 1
        if self.jugador.tiempo_vida == 0:
            self.timer_aljibe.stop()
            self.timer_calor.stop()

    def click_pantalla(self, x, y):
        for botella in self.botellas:
            if botella.valida:
                if self.chequear_colision(x, y, botella):
                    self.jugador.tiempo_vida += randint(*p.VIDA_BOTELLA)
                    botella.valida = False

    def chequear_colision(self, x, y, botella):
        if x >= botella.x + botella.ancho:
            return False
        if x <= botella.x:
            return False
        if y >= botella.y + botella.alto:
            return False
        if y <= botella.y:
            return False
        return True
