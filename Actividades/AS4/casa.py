from cola_dulces import ColaDulces, TrickOrTreater
import cargar_datos as c
import parametros as p
from time import sleep
from random import random, randint, choice


class DCCasa:

    def __init__(self, cola : ColaDulces) -> None:
        self.cola = cola
        self.colones = p.COLONES

    def añadir_protagonista(self, nombre):
        self.cola.tot_llega(nombre)
        self.cola.ultimo.protagonista = True

    def simular_cola(self):     
        atendido = self.cola.atender_tot()
        while not atendido.protagonista:
            print(self.cola)
            posicion_protagonista = self.cola.obtener_posicion_protagonista()
            print(f"La cola ha avanzado un puesto. Tu posición es de {posicion_protagonista}")
            
            sleep(p.TIEMPO_COLA)
            if random() <= p.PROB_COLARSE and self.colones:
                largo = self.cola.obtener_largo()
                pos = randint(0, largo)
                quien = choice(self.colones)
                self.colones.remove(quien)
                self.cola.tot_se_cola(quien, pos)
                print(f"{quien} se logró colar en la posicion {pos} O_o 📹")
            
            sleep(p.TIEMPO_COLA)
            atendido = self.cola.atender_tot()
        print("Has conseguido sacar los mejores dulces!")

        

if __name__ == "__main__":
    cola = ColaDulces()
    personas = c.cargar_personas(p.RUTA_PERSONAS)
    for persona in personas:
        cola.tot_llega(persona)
    casa = DCCasa(cola)

    casa.añadir_protagonista("Juan")


    casa.simular_cola()

