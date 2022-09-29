from PyQt5.QtCore import QObject

import parametros as p


class Pelota(QObject):

    def __init__(self):
        super().__init__()
        self._x = p.POS_INICIAL_X_PELOTA
        self._y = p.POS_INICIAL_Y_PELOTA
        self.ancho = p.ANCHO_PELOTA
        self.alto = p.ALTO_PELOTA
        self.velocidad = p.VELOCIDAD_PELOTA

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, valor):
        if valor >= p.LIMITE_DERECHA - self.ancho:
            self._x = p.LIMITE_DERECHA - self.ancho
            self.cambiar_direccion('x')
        elif valor <= p.LIMITE_IZQUIERDA:
            self._x = p.LIMITE_IZQUIERDA
            self.cambiar_direccion('x')
        else:
            self._x = valor

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, valor):
        if valor <= p.LIMITE_ARRIBA:
            self._y = p.LIMITE_ARRIBA
            self.cambiar_direccion('y')
        elif valor >= p.LIMITE_ABAJO:
            self._y = p.LIMITE_ABAJO
            self.resetear_posicion()
        else:
            self._y = valor

    def mover(self):
        self.x += self.velocidad[0]
        self.y += self.velocidad[1]

        return self.x, self.y

    def cambiar_direccion(self, eje):
        if eje == 'x':
            self.velocidad[0] *= -1
        elif eje == 'y':
            self.velocidad[1] *= -1

    def resetear_posicion(self):
        self.x = p.POS_INICIAL_X_PELOTA
        self.y = p.POS_INICIAL_Y_PELOTA
        self.velocidad[1] *= -1


class Plataforma(QObject):

    def __init__(self):
        super().__init__()
        self._x = p.POS_INICIAL_X_PLATAFORMA
        self.y = p.POS_INICIAL_Y_PLATAFORMA
        self.ancho = p.ANCHO_PLATAFORMA
        self.alto = p.ALTO_PLATAFORMA

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, valor):
        if valor >= p.LIMITE_DERECHA - self.ancho:
            self._x = p.LIMITE_DERECHA - self.ancho
        elif valor <= p.LIMITE_IZQUIERDA:
            self._x = p.LIMITE_IZQUIERDA
        else:
            self._x = valor

    def mover(self, tecla: str):
        if tecla == p.TECLA_IZQUIERDA:
            self.x += p.VELOCIDAD_PLATAFORMA
        elif tecla == p.TECLA_DERECHA:
            self.x -= p.VELOCIDAD_PLATAFORMA

        return self.x, self.y

    def revisar_rebote(self, pos: tuple):
        if (p.POS_INICIAL_Y_PLATAFORMA - p.ALTO_PELOTA) <= pos[1]:
            if pos[0] <= (self.x + self.ancho) and \
                    (pos[0] + p.ANCHO_PELOTA) >= self.x:
                return True
        return False

    def resetear_posicion(self):
        self.x = p.POS_INICIAL_X_PLATAFORMA
        self.y = p.POS_INICIAL_Y_PLATAFORMA


class Bloque(QObject):
    num_counter = 1
    x_counter = p.POS_INICIAL_X_BLOQUE
    y_counter = p.POS_INICIAL_Y_BLOQUE

    def __init__(self):
        super().__init__()
        self.ancho = p.ANCHO_BLOQUE
        self.alto = p.ALTO_BLOQUE
        self.numero = Bloque.num_counter
        self.activo = True
        self.x = [Bloque.x_counter, Bloque.x_counter + p.ANCHO_BLOQUE]
        self.y = [Bloque.y_counter, Bloque.y_counter + p.ALTO_BLOQUE]

        Bloque.x_counter += p.ANCHO_BLOQUE
        if Bloque.num_counter % 5 == 0:
            Bloque.x_counter = p.POS_INICIAL_X_BLOQUE
            Bloque.y_counter += p.ALTO_BLOQUE
        Bloque.num_counter += 1

    def revisar_colision(self, posicion: tuple):
        x, y = posicion
        if self.x[0] <= x <= self.x[1] and \
                self.y[0] <= y <= self.y[1]:
            self.activo = False
            return True, self.numero
        return False, None

    def resetear(self):
        self.activo = True
