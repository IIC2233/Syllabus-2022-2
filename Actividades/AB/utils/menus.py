from typing import List
import re

from utils.data import Tokens, Issues
from utils.anime import filtro_animes
from apis import get_animes, post_issue, put_lock_issue, delete_lock_issue


def menu_opciones(titulo: str, opciones: List[str],
                  descripcion: str = '', cancelar: str = 'Cancelar'):

    print(f'\n\n\n  {titulo}:\n')
    if descripcion != '':
        print(f'{descripcion}\n')

    digits = len(str(len(opciones)))
    plantilla = '\t[{:' + str(digits) + '}] {}'
    for i, o in enumerate(opciones):
        print(plantilla.format(i + 1, o))
    print(plantilla.format(0, cancelar))

    pregunta = f'\n  Ingresa un número entre 0 y {len(opciones)}: '
    while not (opcion := input(pregunta).strip()).isdigit() \
            or (opcion := int(opcion)) > len(opciones):
        input(f'  La opción [{opcion}] no es válida.'
              f' Presione Enter para continuar.')
        return -1
    return opcion


def pedir_texto(titulo: str, patron_regex: str) -> str:

    patron = re.compile(patron_regex)

    while not patron.match(texto := input(f'  Ingresa {titulo}: ')):
        print(f' "{texto}" no es válido, intenta de nuevo.')
    return texto


def menu_inicial(tokens: Tokens, issues: Issues) -> bool:
    if tokens:
        opciones = ['Borrar Github Token', 'Probar APIs']
    else:
        opciones = ['Ingresar Github Token']

    opcion = -1
    while opcion != 0:

        if opcion == 1:
            if tokens:
                tokens.clear()
            else:
                tokens.append(pedir_texto('Token', r'^[A-Za-z0-9_]{40}$'))
            tokens.guardar()
            return True

        if opcion == 2:
            menu_partes(tokens, issues)

        datos_menu = {
            'titulo': 'Menú inicial',
            'opciones': opciones,
            'cancelar': 'Salir'
        }
        opcion = menu_opciones(**datos_menu)
    return False


def menu_partes(tokens: Tokens, issues: Issues) -> bool:
    opciones_base = ['Get Animes', 'Post Issue']
    opciones_issue = ['Put Lock Issue', 'Delete Lock Issue']

    animes = []
    status = None

    opcion = -1
    while opcion != 0:

        if opcion == 1:
            status, animes_crudos = get_animes()
            animes = filtro_animes(animes_crudos)

        elif opcion == 2:
            status, numero_issue = post_issue(tokens[-1], animes)
            if numero_issue > 0:
                issues.append(numero_issue)
                issues.guardar()

        elif opcion == 3:
            status = put_lock_issue(tokens[-1], issues[-1])

        elif opcion == 4:
            status = delete_lock_issue(tokens[-1], issues[-1])

        opciones = opciones_base.copy()
        if issues:
            opciones.extend(opciones_issue)

        descripcion = f'\tAnimes:\n'
        for anime in animes:
            descripcion += f'\t  {anime}\n'
        descripcion += f'\tCantidad Animes: {len(animes)}\n'
        descripcion += f'\tIssue: {str(issues[-1] if issues else None)}\n'
        if opcion != -1:
            descripcion += f'\tResult: {opciones[opcion - 1]} -> {str(status)}'
        datos_menu = {
            'titulo': 'Probar APIs',
            'descripcion': descripcion,
            'opciones': opciones,
            'cancelar': 'Regresar'
        }
        opcion = menu_opciones(**datos_menu)
    return False
