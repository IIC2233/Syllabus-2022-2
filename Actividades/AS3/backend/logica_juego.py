from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QEventLoop

from backend.elementos_juego import Bloque
import parametros as p


class LogicaJuego(QObject):

    senal_cargar_datos_iniciales = pyqtSignal(dict)
    senal_enviar_datos = pyqtSignal(dict)
    senal_mover_plataforma = pyqtSignal(tuple)
    senal_mover_pelota = pyqtSignal(tuple)
    senal_eliminar_bloque = pyqtSignal(int)
    senal_bajar_vida = pyqtSignal(int)
    senal_terminar_juego = pyqtSignal(dict)
    senal_cerrar_ventana_juego = pyqtSignal()
    senal_reset_ventana = pyqtSignal()

    def __init__(self, plataforma, pelota):
        super().__init__()
        self.plataforma = plataforma
        self.pelota = pelota
        self._vidas = p.VIDAS
        self._puntaje = p.PUNTAJE_INICIAL
        self.timer_juego = QTimer()
        self.timer_actualizar_juego = QTimer()
        self.timer_pelota = QTimer()
        self.bloques = []
        self.crear_bloques()
        self.configurar_timers()

    @property
    def vidas(self):
        return self._vidas

    @vidas.setter
    def vidas(self, valor):
        if valor == 0:
            self.terminar_juego()
        else:
            self._vidas = valor

    @property
    def puntaje(self):
        return self._puntaje

    @puntaje.setter
    def puntaje(self, valor):
        if valor <= 0:
            self._puntaje = 0
        else:
            self._puntaje = valor

    def crear_bloques(self):
        self.bloques.clear()
        for _ in range(p.NUM_BLOQUES):
            self.bloques.append(
                Bloque()
            )

    def configurar_timers(self):
        # COMPLETAR
        pass

    def iniciar(self, usuario):
        self.timer_juego.start()
        self.timer_actualizar_juego.start()
        self.timer_pelota.start()

        self.senal_cargar_datos_iniciales.emit({
            'Usuario': usuario,
            'Puntaje': str(self.puntaje),
            'Tiempo': str(p.TIEMPO_JUEGO)
        })

    def mover_plataforma(self, tecla: str):
        # COMPLETAR
        pass

    def mover_pelota(self):
        nueva_pos = self.pelota.mover()
        self.senal_mover_pelota.emit(nueva_pos)
        rebote_plataforma = self.plataforma.revisar_rebote(nueva_pos)
        rebote_bloque = self.eliminar_bloque(nueva_pos)
        if rebote_plataforma or rebote_bloque:
            self.pelota.cambiar_direccion('y')
        if nueva_pos[1] >= p.LIMITE_VIDA:
            self.bajar_vida()
        if rebote_bloque:
            self.puntaje += p.PUNTAJE_BLOQUE
            if self.revisar_ganador():
                self.terminar_juego()

    def revisar_ganador(self):
        for bloque in self.bloques:
            if bloque.activo:
                return False
        return True

    def bajar_vida(self):
        self.vidas -= 1
        self.puntaje -= p.PUNTAJE_VIDA
        self.senal_bajar_vida.emit(self.vidas)

    def eliminar_bloque(self, posicion: tuple):
        for bloque in self.bloques:
            if bloque.activo:
                datos = bloque.revisar_colision(posicion)
                if datos[0]:
                    self.senal_eliminar_bloque.emit(datos[1])
                    return True
        return False

    def actualizar_juego(self):
        tiempo_juego = self.timer_juego.remainingTime() // 1000
        self.senal_enviar_datos.emit({
            'Puntaje': str(self.puntaje),
            'Tiempo': str(tiempo_juego)
        })

    def terminar_juego(self):
        self.timer_juego.stop()
        self.timer_actualizar_juego.stop()
        self.timer_pelota.stop()
        if self.vidas > 0:
            resultado = True
        else:
            resultado = False
        self.senal_terminar_juego.emit({
            'Puntaje': str(self.puntaje),
            'Resultado': resultado})
        self.senal_cerrar_ventana_juego.emit()
        self.reset_datos()

    def reset_datos(self):
        self.puntaje = p.PUNTAJE_INICIAL
        self.vidas = p.VIDAS
        for bloque in self.bloques:
            bloque.resetear()
        self.pelota.resetear_posicion()
        self.plataforma.resetear_posicion()

        self.senal_reset_ventana.emit()
        self.senal_cargar_datos_iniciales.emit({
            'Usuario': '',
            'Puntaje': str(self.puntaje),
            'Tiempo': str(p.TIEMPO_JUEGO)
        })

    def cheatcode(self):
        for bloque in self.bloques:
            if bloque.activo:
                bloque.activo = False
                self.senal_eliminar_bloque.emit(bloque.numero)
                loop = QEventLoop()
                QTimer.singleShot(p.TIEMPO_RETRASO, loop.quit)
                loop.exec()
        self.terminar_juego()
