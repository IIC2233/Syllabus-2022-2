import parametros as p
from cargar_datos import (
    cargar_habitaciones,
    cargar_conexiones,
    cargar_personas,
    cargar_casas,
)
from mansion import MansionEmbrujada, Habitacion, Explorador, Mapa
from protagonista_disfrazado import ProtagonistaDisfrazado
from casa import ColaDulces, DCCasa
from condominio import Condominio


def manejo_inputs(maximo):
    entrada = input("Elija una opcion valida: ")
    if not entrada.isnumeric():
      print("opcion invalida :(")
      return manejo_inputs(maximo)
    if int(entrada) in range(maximo + 1):
        return int(entrada)
    print("opcion invalida :(")
    return manejo_inputs(maximo)


print("ejecutando...\n")


if __name__ == "__main__":

    opcion = 1
    nombre = input("Cual es tu nombre?: ")
    while opcion:
        print("¿Que deseas hacer?")
        print(
            """
      [1] Encontrar SuperTraje (Parte 1)
      [2] Buscar la casa mas Bakana
      [3] Recuperar dulces 

      [0] Salir
      """
        )
        opcion = manejo_inputs(3)
        if opcion == 1:

            ### PARTE 1 ###
            mansion = MansionEmbrujada()
            mansion.nombres, mansion.objetos = cargar_habitaciones(p.RUTA_HABITACIONES)
            mansion.vecinos = cargar_conexiones(p.RUTA_CONEXIONES)
            entrada = Habitacion(0, mansion.nombres[0], mansion.vecinos[0], mansion.objetos[0])
            mapa = Mapa(entrada)

            explorador = Explorador(mansion, nombre, mapa)
            explorador.habitaciones_creadas.append(entrada)
            explorador.explorar()

        ### PARTE 2 ###

        elif opcion == 2:
            condominio = Condominio(cargar_casas(p.RUTA_CASAS))
            condominio.identificar_protagonista()
            condominio.poblar_condominio()
            protagonista_disfrazado = ProtagonistaDisfrazado(nombre)
            print("¿printear arbol?")
            print(' [1] Si')
            print(' [2] No')
            eleccion= manejo_inputs(2)
            if eleccion == 1:
              condominio.mostrar_arbol()
            
            print("Qué metología utilizaras para encontrar la mejor casa?: ")
            print(
                """
          [1] DFS recursivo
          [2] DFS iterativo
          [3] BFS 

          [0] Salir
          """
            )
            metodo = manejo_inputs(3)

            if metodo == 1:
                casas = protagonista_disfrazado.recuperar_casas_DFS_recursivo(
                    condominio.casa_protagonista
                )

            elif metodo == 2:
                casas = protagonista_disfrazado.recuperar_casas_DFS_iterativo(
                    condominio.casa_protagonista
                )

            elif metodo == 3:
                casas = protagonista_disfrazado.recuperar_casas_BFS_iterativo(
                    condominio.casa_protagonista
                )
            else:
                print("volviendo")
                casas = []
            if casas:
              casa_elegida = protagonista_disfrazado.filtrar_casas(casas)
              print(f"{protagonista_disfrazado.nombre} se dirigira a la casa {casa_elegida}")

        ### PARTE 3 ###

        elif opcion == 3:
            cola = ColaDulces()
            personas = cargar_personas(p.RUTA_PERSONAS)
            for persona in personas:
                cola.tot_llega(persona)
            casa = DCCasa(cola)

            casa.añadir_protagonista(nombre)

            casa.simular_cola()
