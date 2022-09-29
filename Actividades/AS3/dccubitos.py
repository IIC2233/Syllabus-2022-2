from PyQt5.QtWidgets import QApplication

from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_postjuego import VentanaPostjuego
from backend.logica_inicio import LogicaInicio
from backend.logica_juego import LogicaJuego
from backend.elementos_juego import Pelota, Plataforma


class DCCubitos(QApplication):

    def __init__(self, argv):
        super().__init__(argv)

        # Instanciar Ventanas
        self.ventana_inicio = VentanaInicio()
        self.ventana_juego = VentanaJuego()
        self.ventana_postjuego = VentanaPostjuego()

        # Instanciar Lógicas
        self.plataforma = Plataforma()
        self.pelota = Pelota()
        self.logica_inicio = LogicaInicio()
        self.logica_juego = LogicaJuego(self.plataforma, self.pelota)
        
        # Conectar Señales
        self.conectar_inicio()
        self.conectar_juego()
        self.conectar_postjuego()

    def conectar_inicio(self):
        # COMPLETAR
        pass

    def conectar_juego(self):
        # COMPLETAR


        # Señales ya conectadas: no modificar
        self.logica_juego.senal_cargar_datos_iniciales.connect(
            self.ventana_juego.setear_datos)

        self.logica_juego.senal_mover_pelota.connect(
            self.ventana_juego.mover_pelota)

        self.logica_juego.senal_enviar_datos.connect(
            self.ventana_juego.actualizar_datos)
        
        self.logica_juego.senal_eliminar_bloque.connect(
            self.ventana_juego.eliminar_bloque)

        self.logica_juego.senal_bajar_vida.connect(
            self.ventana_juego.bajar_vida)

        self.logica_juego.senal_cerrar_ventana_juego.connect(
            self.ventana_juego.close)

        self.logica_juego.senal_reset_ventana.connect(
            self.ventana_juego.reset_labels)

        self.logica_juego.senal_terminar_juego.connect(
            self.ventana_postjuego.abrir)
        
    def conectar_postjuego(self):
        self.ventana_postjuego.senal_abrir_inicio.connect(
            self.ventana_inicio.show)

        self.ventana_postjuego.senal_cerrar_juego.connect(self.exit)

    def iniciar(self):
        self.ventana_inicio.show()
