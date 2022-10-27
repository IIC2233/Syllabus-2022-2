from cargar_datos import cargar_habitaciones, cargar_conexiones
import parametros as p
from time import sleep


class MansionEmbrujada:
    
    def __init__(self):
        self.nombres = {} # diccionario con los nombres de cada habitacion
        self.vecinos = {} # diccionario con los id de los vecinos de cada habitacion
        self.objetos = {} # diccinoario con los objetos de cada habitacion
        
        
    def explorar(self, id: int):
        '''Devuelve los datos de una habitacion segun su id'''
        nombre = self.nombres[id]
        id_vecinos = self.vecinos[id]
        objetos = self.objetos[id]
        return (nombre, id_vecinos, objetos)

class Habitacion:

    def __init__(self, id: int, nombre: str, id_vecinos: list, objetos: list):
        self.id = id
        self.nombre = nombre
        self.objetos = objetos
        self.id_vecinos = id_vecinos
        self.conexiones = []    # Habitaciones a las que conecta
        self.explorada = False

    def __str__(self):
        return f"{self.nombre}"
    
class Mapa:
    def __init__(self, punto_de_partida: Habitacion):
        self.punto_de_partida = punto_de_partida
        self.habitaciones_creadas = [punto_de_partida]
        
    def crear_habitacion(self, id, nombre, id_vecinos, objetos): # COMPLETAR
        '''Crea una nueva habitacion, si es que no existe, y la retorna'''
        pass



    def registrar_vecino(self, habitacion: Habitacion, vecino: Habitacion): # COMPLETAR
        '''Conecta una habitacion con su vecino'''
        pass



    def descartar_habitacion(self, habitacion: Habitacion): # COMPLETAR
        '''Elimina las conexiones de una habitacion'''
        pass


class Explorador:

    def __init__(self, mansion: MansionEmbrujada, nombre: str, mapa: Mapa):
        self.habitacion_actual = None
        self.mansion = mansion
        self.nombre = nombre
        self.mapa = mapa

        self.objetivo = {"Mascara", "Cuerpo", "Brazos"}
        self.disfraz = set()
        self.habitaciones_creadas = []

    def ingresar_a_habitacion(self, habitacion: Habitacion):
        '''Simula el ingreso a una instancia Habitacion dentro de la mansion'''
        
        print(f"Ingresando a {habitacion}")
        self.habitacion_actual = habitacion

        if not habitacion.explorada:

            habitacion.explorada = True
    
            # Si no hemos explorado la habitacion, registramos a sus vecinos
            for vecino_id in habitacion.id_vecinos:

                nombre, id_vecinos, objetos = self.mansion.explorar(vecino_id)
                nueva_habitacion = self.mapa.crear_habitacion(vecino_id, nombre, id_vecinos, objetos)
                self.mapa.registrar_vecino(self.habitacion_actual, nueva_habitacion)
                
            # Buscamos partes del disfraz en la habitacion
            self.buscar_disfraz(habitacion)
                

        # Si es que la habitacion es un callejón sin salida, la descartamos
        if len(habitacion.conexiones) == 1 and habitacion != self.mapa.punto_de_partida:
            destino = self.habitacion_actual.conexiones[0]
            self.mapa.descartar_habitacion(self.habitacion_actual)
            self.ingresar_a_habitacion(destino)
    
    def explorar(self):
        '''Simula el paso del protagonista por cada habitacion de la mansion'''
        self.ingresar_a_habitacion(self.mapa.punto_de_partida)
        conexiones = self.habitacion_actual.conexiones
        while self.habitacion_actual.conexiones:

            destino = conexiones[0]
            for habitacion in conexiones:
                if destino.explorada and not habitacion.explorada:
                    destino = habitacion
            
            # Si todas los vecinos han sido explorados, descartamos la habitación actual
            # (esto se asegura de romper ciclos de habitaciones exploradas)
            if destino.explorada:
                destino = self.habitacion_actual.conexiones[0]
                self.mapa.descartar_habitacion(self.habitacion_actual)
                self.ingresar_a_habitacion(destino)
                
            else:
                conexiones = destino.conexiones
                self.ingresar_a_habitacion(destino)

            if self.disfraz == self.objetivo:
                print("\nHas encontrado todas las piezas!\nHora de salir de aca.\n")
                return

        # Ya no quedan habitaciones por explorar
        print("No se han encontrado todas las partes del disfraz!")
    
    def buscar_disfraz(self, habitacion: Habitacion):
        '''Busca partes del disfraz dentro de una habitacion'''
        sleep(p.TIEMPO_BUSQUEDA)
        print(f"Buscando el disfraz en {self.habitacion_actual}...")
        sleep(p.TIEMPO_BUSQUEDA)
        for objeto in habitacion.objetos:
            if objeto in self.objetivo:
                print("Has encontrado ", objeto)
                sleep(p.TIEMPO_BUSQUEDA)
                self.disfraz.add(objeto)
                habitacion.objetos.remove(objeto)

