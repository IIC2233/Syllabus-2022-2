from PyQt5.QtCore import QObject, QThread, QTimer
from time import sleep
from random import randint
import parametros as p

class Botella(QThread):

    id = 0

    def __init__(self, x, y, senal_aparecer_agua, senal_desaparecer_agua):
        super().__init__()
        self.id += 1
        Botella.id += 1
        self.x = x
        self.y = y
        self.alto = 80
        self.ancho = 40
        self.senal_aparecer_agua = senal_aparecer_agua
        self.senal_desaparecer_agua = senal_desaparecer_agua

    @property
    def valida(self):
        return self._valida

    @valida.setter
    def valida(self, value):
        self._valida = value
        if not self.valida:
            # Recomendar que investiguen sobre formas de eliminar este elemento en vez de ocultarlo
            self.senal_desaparecer_agua.emit(self.id)
        else:
            self.senal_aparecer_agua.emit(self.id, self.x, self.y,
                                          self.alto, self.ancho)

    def run(self):
        self.valida = True
        sleep(p.TIEMPO_VIDA_BOTELLA) # Sleep necesita el tiempo en segundos
        self.valida = False


class Jugador:

    def __init__(self, nombre, vida, senal_vida):
        self.nombre = nombre
        self._tiempo_vida = vida
        self.tiempo_vida_maximo = vida
        self.senal_vida = senal_vida

    @property
    def tiempo_vida(self):
        return self._tiempo_vida

    @tiempo_vida.setter
    def tiempo_vida(self, value):
        self._tiempo_vida = value
        self.senal_vida.emit(self.tiempo_vida)


class LogInBackend:

    def __init__(self, recibir_login, responder_login):
        self.senal_responder_login = responder_login
        recibir_login.connect(self.login)

    def login(self, nombre):
        # Solo aceptaremos nombres que empiecen con DCC
        self.senal_responder_login.emit(
            {"permiso": nombre.startswith("DCC"), "nombre": nombre}
        )


class Juego(QObject):

    def __init__(self, click_pantalla, actualizar_vida,
                 nombre_jugador, senal_aparecer_agua, senal_desaparecer_agua,
                 confirmar_inicio, senal_iniciar_juego):
        super().__init__()

        # Codigo que le damos
        self.x_max = 800
        self.y_max = 500
        self.senal_iniciar_juego = senal_iniciar_juego
        self.senal_aparecer_agua = senal_aparecer_agua
        self.senal_desaparecer_agua = senal_desaparecer_agua
        self.botellas = []
        confirmar_inicio.connect(self.iniciar_juego)
        
        # Codigo que tienen que hacer 
        self.jugador = Jugador(nombre_jugador, p.VIDA_MAXIMA, actualizar_vida)
        click_pantalla.connect(self.click_pantalla)

        self.timer_calor = QTimer(self)
        self.timer_calor.setInterval(p.TIEMPO_CALOR)
        self.timer_calor.timeout.connect(self.sufrir_calor)
        self.timer_calor.start()

        self.aljibe = QTimer(self)
        self.aljibe.setInterval(p.TIEMPO_REAPARICION_BOTELLA)
        self.aljibe.timeout.connect(self.dar_agua)

    def jugando(self):
        return self.jugador.tiempo_vida >= 0

    def dar_agua(self):
        if self.jugando:
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

    def iniciar_juego(self):
        self.senal_iniciar_juego.emit(self.x_max, self.y_max)
        self.aljibe.start()

    def sufrir_calor(self):
        self.jugador.tiempo_vida -= 1

    def click_pantalla(self, x, y):
        for botella in self.botellas:
            if botella.valida:
                if self.chequear_colision(x, y, botella):
                    self.jugador.tiempo_vida += randint(*p.VIDA_RECUPERA_BOTELLA)
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


    