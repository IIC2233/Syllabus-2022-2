class NodoArbolGenealogico:
    def __init__(self, nombre, padre=None):
        self.padre = padre
        self.nombre = nombre
        self.hijos = []

    def obtener_persona(self, nombre_persona):
        return None

    def agregar_descendencia(self, nombre_padre, nombre_hijo):
        return False


if __name__ == "__main__":
    descendencia = [
        ["Yor", ["Nico", "Dani"]],
        ["Fran", ["Sakura"]],
        ["Nico", ["Anya", "Felipe"]],
        ["Anya", ["Hernán", "Bon"]],
        ["Felipe", ["Bojji", "Fran"]],
        ["Fran", ["Lukas"]],
    ]
    raiz = NodoArbolGenealogico("Yor")

    for padre, hijos in descendencia:
        for hijo in hijos:
            resultado = raiz.agregar_descendencia(padre, hijo)
            print(f"Agregando {padre} a {hijo} --> Resultado: {resultado} ")
