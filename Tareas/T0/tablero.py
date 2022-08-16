def print_tablero_con_utf8(tablero):
    n = len(tablero)
    m = len(tablero[0])

    tablero = [['■' if x == ' ' else x for x in y] for y in tablero]
    tablero = [[str(x) if isinstance(x, int) else x for x in y] for y in tablero]

    columnas = ' ' * 5
    for indice in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:m]:
        columnas += f' {indice}'

    print(columnas)
    print(' ' * 4 + '┌' + '─' * (2 * m + 1) + '┐')

    for indice in range(n):
        fila = ''
        if indice < 10:
            fila += f'  {indice} │'
        else:
            fila += f' {indice} │'

        fila += ' ' + ' '.join(tablero[indice]) + ' │'
        print(fila)

    print(' ' * 4 + '└' + '─' * (2 * m + 1) + '┘')


def print_tablero_sin_utf8(tablero):
    n = len(tablero)
    m = len(tablero[0])

    tablero = [['_' if x == ' ' else x for x in y] for y in tablero]
    tablero = [[str(x) if isinstance(x, int) else x for x in y] for y in tablero]

    columnas = ' ' * 4
    for indice in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:m]:
        columnas += f' {indice}'

    print(columnas)
    print()

    for indice in range(n):
        fila = ''
        if indice < 10:
            fila += f'  {indice} '
        else:
            fila += f' {indice} '

        fila += ' ' + ' '.join(tablero[indice])
        print(fila)


def print_tablero(tablero, utf8=True):
    if utf8:
        print_tablero_con_utf8(tablero)
    else:
        print_tablero_sin_utf8(tablero)
