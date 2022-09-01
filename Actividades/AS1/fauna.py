from random import randint
from parametros import INCREMENTO_FEROCIDAD, MAX_EX_CARNIVORO, MAX_EX_HERVIBORO, \
                        MIN_EX_CARNIVORO, MIN_EX_HERVIBORO, INCREMENTO_ADORABILIDAD, \
                        GAN_CARNIVORO, GAN_HERBIVORO



# MODIFICAR
class Animal:

    # MODIFICAR
    def __init__(self, especie):
        pass

    # MODIFICAR
    def alimentarse(self):
        pass

    # MODIFICAR
    def exhibicion(self):
        pass

    def __str__(self):
        return f"Animal de especie {self.especie}"


# MODIFICAR
class Carnivoro:

    # MODIFICAR
    def __init__(self, ferocidad, **kwargs):
        pass

    # MODIFICAR
    def alimentarse(self):
        super().alimentarse()

    # MODIFICAR
    def exhibicion(self):
        super().exhibicion()


# MODIFICAR
class Herbivoro:

    # MODIFICAR
    def __init__(self, adorabilidad, **kwargs):
        pass

    # MODIFICAR
    def alimentarse(self):
        super().alimentarse()

    # MODIFICAR
    def exhibicion(self):
        super().exhibicion()


# MODIFICAR
class Omnivoro:

    # MODIFICAR
    def __init__(self, **kwargs):
        pass

    # MODIFICAR
    def alimentarse(self):
        pass

    # MODIFICAR
    def exhibicion(self):
        pass

