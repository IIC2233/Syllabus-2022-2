import parametros as p
def cargar_habitaciones(ruta_archivo: str) -> dict:

    with open(ruta_archivo, "r", encoding="utf-8") as habitaciones:
        
        nombres = {}
        objetos = {}
        for habitacion in habitaciones:
            habitacion = habitacion.strip()
            id, nombre, contenido = habitacion.split(";") 
            id = int(id)
            nombres[id] = nombre
            objetos[id] = contenido.strip().split(",")

    return nombres, objetos

def cargar_conexiones(ruta_archivo)-> dict:

    with open(ruta_archivo, "r", encoding="utf-8") as conexiones:

        dict_conexiones = {}

        for conexion in conexiones:

            conexion = conexion.strip()
            id, lista = conexion.split(";")
            id = int(id)
            lista = lista.split(",")
            lista = [int(i) for i in lista]
            dict_conexiones[id] = lista
            

    return dict_conexiones 


def cargar_casas(ruta_archivo) -> dict:

    with open(ruta_archivo, "r", encoding="utf-8") as casas:

        dict_casas = {}

        for casa in casas:
            if len(casa)!=0:
                casa = casa.strip().split(";")
                id_, id_padre, distancia, nivel_decoracion, posicion = casa
                id_ = int(id_)
                id_padre = int(id_padre)
                distancia = int(distancia)
                nivel_decoracion = int(nivel_decoracion)
                posicion = int(posicion)
                dict_casas[id_] = [id_padre, distancia, nivel_decoracion, posicion]
            
    return dict_casas

def cargar_personas(ruta_archivo) -> dict:
    with open(ruta_archivo, "r", encoding="utf-8") as personas:
        lista = []
        for persona in personas:
            persona = persona.strip()
            lista.append(persona)
    return lista
