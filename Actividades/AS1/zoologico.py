from random import choice, randint
from atracciones import GranjaHerbivoros, PaseoCarnivoros
from parametros import RANGO_INCUBACION, RECAUDACION_CONSTRUCCION, N_GRANJAS \
                        , N_PASEOS, GAN_CARNIVORO, GAN_HERBIVORO


class DCCentralZoo:

    def __init__(self, semanas_maximas):
        self.semana = 0
        self.semanas_maximas = semanas_maximas
        self.recaudacion_semanal = 0
        self.recaudacion_total = 0
        self.recaudacion_construccion = RECAUDACION_CONSTRUCCION  #! definira si se construyen o no mas atracciones
        self.visitantes_semana = 0
        self.visitantes_totales = 0
        self.atracciones_herbivoros = []
        self.atracciones_carnivoros = []

    def alimentar_animales(self):
        for atraccion in self.atracciones_herbivoros:
            atraccion.alimentar_animales()
        for atraccion in self.atracciones_carnivoros:
            atraccion.alimentar_animales()

    # MODIFICAR
    def calcular_estadisticas(self):
        pass

    def construir_atraccion(self, tipo):
        if tipo == "carnivoros":
            numero = len(self.atracciones_herbivoros)
            atraccion = PaseoCarnivoros(numero)
            self.atracciones_carnivoros.append(atraccion)
            print("Construida nueva atraccion \"Paseo de Carnivoros\"")
        elif tipo == "herbivoros":
            numero = len(self.atracciones_carnivoros)
            atraccion = GranjaHerbivoros(numero)
            self.atracciones_herbivoros.append(atraccion)
            print("Construida nueva atraccion \"Granja de Herbivoros\"")

    def poblar_zoo(self):
        for _ in range(N_PASEOS):
            self.construir_atraccion("carnivoros")
        for _ in range(N_GRANJAS):
            self.construir_atraccion("herbivoros")

    def incubar_animales(self):
        # Itera por cada atraccion y se añaden nuevos animales, imprimira el numero de animales incubados
        animales_nuevos = 0
        for atraccion in self.atracciones_herbivoros:
            cantidad = randint(RANGO_INCUBACION[0], RANGO_INCUBACION[1])
            for _ in range(cantidad):
                atraccion.crear_animales()
                animales_nuevos += 1
        for atraccion in self.atracciones_carnivoros:
            cantidad = randint(RANGO_INCUBACION[0], RANGO_INCUBACION[1])
            for _ in range(cantidad):
                atraccion.crear_animales()
                animales_nuevos += 1
        return animales_nuevos
    
    def reset(self):
        # Al pasar la semana, las estadisticas semanales se deben resetear
        self.recaudacion_total += self.recaudacion_semanal
        self.recaudacion_semanal = 0
        
        self.visitantes_totales += self.visitantes_semana
        self.visitantes_semana = 0

        for atraccion in self.atracciones_herbivoros:
            for animal in atraccion.animales:
                animal.ganancia_actual = GAN_HERBIVORO

        for atraccion in self.atracciones_carnivoros:
            for animal in atraccion.animales:
                animal.ganancia_actual = GAN_CARNIVORO

    def empezar(self):
        print("\n")
        print("*" * 60)
        print("*" * 60)
        print("**** {: ^50s} ****".format("INICIO DE LA SIMULACION"))
        print("*" * 60)
        print("*" * 60 + "\n")
        
        base = "\n------------ {: ^34s} ------------\n"
        print(base.format("POBLANDO EL ZOO"))
        self.poblar_zoo()

        while self.semanas_maximas > self.semana:
            print("\n")
            print("-" * 60)
            print(base.format(f"SEMANA: {self.semana}"))
            print("-" * 60 + "\n")

            #! 1) al comienzo de la semana se incuban animales
            print("Se han incubado: " + str(self.incubar_animales()) + 
            " animales nuevos")

            #! 2) alimentan animales
            print(base.format("ALIMENTANDO ANIMALES"))
            self.alimentar_animales()

            #! 3) ESTADISTICAS
            print("\n")
            print(base.format("SIMULANDO SEMANA"))
            visitantes, recaudacion = self.calcular_estadisticas()
            print(f"Visitantes semana: {visitantes}")
            print(f"recaudacion semanal: {recaudacion}\n")
            self.recaudacion_semanal = recaudacion
            self.visitantes_semana = visitantes

            #! 4) construye nuevas atracciones
            if self.recaudacion_semanal > self.recaudacion_construccion:
                tipo = choice(("carnivoros", "herbivoros"))
                self.construir_atraccion(tipo)
            else:
                print("X No hay dinero suficiente para construir una atraccion\n")
            
            print("Numero de \"Granja de Herbivoros\":" + 
                f"{len(self.atracciones_herbivoros)}")
            print("Numero de \"Paseo de carnivoros\":" +
                f"{len(self.atracciones_carnivoros)}\n")

            #! 5) Resetea Estadisticas
            self.semana += 1
            self.reset()
        
        print("*" * 60)
        print("**** {: ^50s} ****".format("ESTADISTICAS FINALES"))
        print("*" * 60)

        print(f"\nVISITANTES TOTALES: {self.visitantes_totales}")
        print(f"RECAUDACION TOTAL: {self.recaudacion_total}\n")
    




        