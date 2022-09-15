from centro_urbano import CentroUrbano
from time import sleep
from trabajadores import Recolector, Constructor
from parametros import TIEMPO_ATAQUE_BARBAROS, VIDA_PEKKA, \
    RECUPERACION_VIDA_PEKKA
from random import randint


class Pekka:

    def __init__(self) -> None:
        super().__init__()
        self.vida = VIDA_PEKKA

    def recuperar_vida(self) -> None:
        self.vida += RECUPERACION_VIDA_PEKKA
        print(f"El P.E.K.K.A. gananó {RECUPERACION_VIDA_PEKKA} puntos de vida.")
        print(f"El P.E.K.K.A. ahora tiene {self.vida} puntos de vida")


class Simulacion:

    def __init__(self) -> None:
        self.centro_urbano = CentroUrbano()
        self.pekka = Pekka()

    def nuevo_dia(self) -> None:
        # Completar
        pass

    def nueva_noche(self) -> None:
        print("\n¡Ha comenzado la noche!\n")
        print(f"EL PEKKA ATACA EL CENTRO URBANO")
        print(f"El centro urbano tiene {self.centro_urbano.chozas} chozas")
        print(f"Las chozas han generado {self.centro_urbano.barbaros} bárbaros")
        print("¡A atacar al P.E.K.K.A!")

        for barbaro in range(self.centro_urbano.barbaros // 2):
            sleep(TIEMPO_ATAQUE_BARBAROS)
            dano = randint(5, 10)
            print(f"Los bárbaros hacen {dano} puntos de daño al P.E.K.K.A.")
            self.pekka.vida -= dano
            if self.pekka.vida <= 0:
                print("\n¡El P.E.K.K.A. murió! Salvaste el centro urbano :)\n")
                return
            if self.centro_urbano.chozas > 0:
                self.centro_urbano.chozas -= 1
                print(f"El P.E.K.K.A. ha destruido una choza")
                print(f"Quedan {self.centro_urbano.chozas} chozas")
            print(f"El P.E.K.K.A. tiene {self.pekka.vida} puntos de vida")
        print("\n¡Ha terminado la noche!\n")
        print("El P.E.K.K.A. va a dormir y recupera fuerzas")
        self.pekka.recuperar_vida()

    def iniciar(self) -> None:
        while self.pekka.vida > 0:
            self.nuevo_dia()
            self.nueva_noche()
