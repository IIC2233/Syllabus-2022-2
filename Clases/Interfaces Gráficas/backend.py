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
        # Seteo al atributo. Si el nuevo valor es verdadero, emit la señal
        # para que aparezca la botella en el front en caso contrario,
        # emito la señal para que se esconda la botella.
        pass


    def run(self):
        # La botella debe ser válida por p.TIEMPO_VIDA_BOTELLA segundos
        # luego deja de ser valida
        pass
        

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
        # Completar con la señal para actualizar la vida del jugador

class LogInBackend:

    def __init__(self, recibir_login, responder_login):
        self.senal_responder_login = responder_login
        # Conectar la senal para recibir el login desde el front

    def login(self, nombre):
        # Responderle al front, con un diccionario de la forma:
        # {"permiso": bool, "nombre": string}
        # Bonus: Solo aceptaremos nombres que empiecen con DCC :D
        pass


class Juego(QObject):

    def __init__(self, click_pantalla, actualizar_vida,
                 nombre_jugador, senal_aparecer_agua, senal_desaparecer_agua,
                 confirmar_inicio, senal_iniciar_juego):
        # 1. Debemos agregar una instancia de jugador que registrará nuestra vida.
        # 2. Debemos conectar la senal de click_pantalla con el método 
        # encargado chequear_colision
        # 3. Cada p.TIEMPO_CALOR tiempo, se llame al método sufrir_calor para que 
        # el jugador pierda 1 de vida. 
        # 4. Debemos instaciar nuestro camión aljibe para que empieze a distribuir 
        # agua cuando comienze el juego.
        # 5. Para esto. cada p.TIEMPO_REAPARICION_BOTELLA se deberá ejecutar el 
        # método dar_agua cada 5 segundos
        super().__init__()
        self.x_max = 800
        self.y_max = 500
        self.velocidad = 10
        self.senal_iniciar_juego = senal_iniciar_juego
        self.senal_aparecer_agua = senal_aparecer_agua
        self.senal_desaparecer_agua = senal_desaparecer_agua
        self.botellas = []
        confirmar_inicio.connect(self.iniciar_juego)

    @property
    def jugando(self):
        # Vemos si el jugador sigue vivo, y retornamos eso.
        pass

    def dar_agua(self):
        # Si el jugador está vivo, generamos una botella en cualquier lugar
        # aleatorio del mapa, echamos a andar el tiempo de la botella y
        # guardamos la botella junto con las otras botellas
        pass

    def iniciar_juego(self):
        # Avisar al front que comienza el juego, y hacer que el aljibe
        # comienze a repartir agua
        pass

    def sufrir_calor(self):
        self.jugador.tiempo_vida -= 1

    def chequear_colision(self, x, y, botella):
        # Completar con chequear colisión
        pass

    def click_pantalla(self):
        # Chequear si alguna botella que sea válida colisiona con el jugador y
        # se la consigue.
        # Si es así, le aumentamos la vida al jugador en un numero aleatorio
        # según lo que dice p.VIDA_RECUPERA_BOTELLA 
        # y seteamos la botella que se consiguió como no valida.
        pass
