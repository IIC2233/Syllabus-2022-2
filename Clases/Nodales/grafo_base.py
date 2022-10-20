class Nodo:
    def __init__(self, nombre_ciudad):
        self.nombre_ciudad = nombre_ciudad
        self.vecinos = []

    def agregar_vecino(self, distancia, vecino):
        pass


def ruz_alcanza(inicio, distancia_max):
    # Completar
    pass


def cargar_datos(nombre_archivo):
    dicccionario_nodos = {}
    set_ciudades = set()
    tuplas = []
    with open(nombre_archivo) as f:
        for linea in f:
            ciudad_1, ciudad_2, distancia = linea.strip().split(",")
            set_ciudades.add(ciudad_1)
            set_ciudades.add(ciudad_2)
            tuplas.append((ciudad_1, ciudad_2, int(distancia)))

    for nombre in set_ciudades:
        nodo = Nodo(nombre)
        dicccionario_nodos[nombre] = nodo

    for ciudad_1, ciudad_2, distancia in tuplas:
        ciudad_1_nodo = dicccionario_nodos[ciudad_1]
        ciudad_2_nodo = dicccionario_nodos[ciudad_2]
        ciudad_1_nodo.agregar_vecino(distancia, ciudad_2_nodo)

    return dicccionario_nodos


if __name__ == "__main__":
    dicccionario_nodos = cargar_datos("datos.txt")
    print(dicccionario_nodos)

    ciudad = dicccionario_nodos["Osorno"]
    ruz_alcanza(ciudad, 10)
