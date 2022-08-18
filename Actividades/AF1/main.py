from cargar import cargar_platos, cargar_ingredientes
from consultas import (
    platos_por_categoria,
    descartar_platos,
    preparar_plato,
    resumen_orden,
)


# NO MODIFICAR
def get_input(op):
    inp = input()
    if inp not in {str(i) for i in range(op + 1)}:
        print(" Debes ingresar una opción válida")
        inp = get_input(op)
    return int(inp)


# NO MODIFICAR
def menu_descartar(descartados, ingredientes):
    def obtener_seleccion(i, ing):
        seleccion = f"[{i}]({'X' if ing in descartados else ' '}) {ing}"
        return seleccion.ljust(25)
    respuesta = ""
    while respuesta != 0:
        print_ing = "\nIngredientes:\n" + "-" * 80 + "\n"
        nombre_ing = list(ingredientes.keys())

        for i in range(0, len(nombre_ing), 3):
            seleccion = obtener_seleccion(i + 1, nombre_ing[i])
            print_ing += seleccion.ljust(25)

            if i + 1 < len(ingredientes):
                seleccion = obtener_seleccion(i + 2, nombre_ing[i + 1])
                print_ing += seleccion.ljust(25)

            if i + 2 < len(ingredientes):
                seleccion = obtener_seleccion(i + 3, nombre_ing[i + 2])
                print_ing += seleccion.ljust(25)

            print_ing += "\n"
        print(print_ing + "\n[0] Continuar Orden\n")

        print("\nSelecciona un ingrediente para descartarlo (X) o incluirlo:")
        respuesta = get_input(len(nombre_ing))
        if respuesta != 0:
            ing = nombre_ing[respuesta - 1]
            if ing in descartados:
                descartados.remove(ing)
                print(f" - {ing} - Se ha vuelto a incluir")
            else:
                descartados.add(ing)
                print(f" - {ing} - Se ha descartado")
    if descartados:
        print("\nSe buscarán platos que no contengan:")
        print("\n".join(f"- {ing}" for ing in descartados))
    input("\nPresione cualquier tecla para continuar")

    return descartados


# NO MODIFICAR
def menu_agregar(platos, ingredientes, platos_ordenados):
    platos_categoria = platos_por_categoria(platos)
    categorias = list(platos_categoria.keys())
    print("\nSelecciona una categoría:")
    print(
        "\n".join(f"[{i + 1}] {categorias[i]}" for i in range(len(categorias)))
        + "\n\n[0] Volver"
    )
    respuesta_2 = get_input(len(categorias))
    if respuesta_2 != 0:
        categoria = categorias[respuesta_2 - 1]
        platos_disponibles = platos_categoria[categoria]

        print(f"\nSelecciona un plato de {categoria}:")
        print(
            "\n".join(
                f"[{i + 1}] {platos_disponibles[i].nombre}"
                for i in range(len(platos_disponibles))
            )
            + "\n\n[0] Volver"
        )
        respuesta_3 = get_input(len(platos_disponibles))

        if respuesta_3 != 0:
            print("\nAgregando plato...\n")
            plato = platos_disponibles[respuesta_3 - 1]
            if preparar_plato(plato, ingredientes):
                platos_ordenados.append(plato)
                print("¡Plato preparado correctamente!")
            else:
                print("No se ha podido preparar este plato :(")
            input("\n* Presione cualquier tecla para continuar *")


# NO MODIFICAR
def main(platos, ingredientes):
    platos_ordenados = []
    ingredientes_descartados = set()
    platos_filtrados = platos

    respuesta = ""
    while respuesta != 0:

        print("\n¡Hola bienvenido a Purble DCCPlace!")
        print("Tu orden actual es:")
        print("\n".join(f"- {plato.nombre}" for plato in platos_ordenados))
        print(
            "\n¿Qué deseas hacer?\n[1] Descartar ingredientes\n"
            "[2] Preparar plato\n[3] Terminar mi orden\n"
            "\n[0] Salir sin preparar un plato"
        )
        respuesta = get_input(3)

        if respuesta == 1:
            ingredientes_descartados = menu_descartar(
                ingredientes_descartados, ingredientes
            )
            if ingredientes_descartados:
                platos_filtrados = descartar_platos(
                    ingredientes_descartados,
                    platos,
                )

        elif respuesta == 2:
            menu_agregar(platos_filtrados, ingredientes, platos_ordenados)

        elif respuesta == 3:
            print("-" * 80)
            resumen = resumen_orden(platos_ordenados)
            print("¡Tu orden se está preparando!")
            print("\n".join(f"- {plato}" for plato in resumen["platos"]))
            print(f"\nTiempo estimado: {resumen['tiempo total']}min")
            print(f"Precio total: ${resumen['precio total']}")
            respuesta = 0
            print("-" * 80)

    print("\nMuchas gracias por preferirnos!")


# NO MODIFICAR
if __name__ == "__main__":
    platos = cargar_platos("platos.csv")
    ingredientes = cargar_ingredientes("ingredientes.csv")

    main(platos, ingredientes)
