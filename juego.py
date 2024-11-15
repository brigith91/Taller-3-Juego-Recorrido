import board
import movimiento_juego_recorrido as mv
import os


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def imprimir_tablero(tablero):
    """
    Funcion para imprimir el tablero

    Parametros
    ----------
        tablero: list[list[str]]
            Corresponde al tablero de juego

    Retorno
    -------
        None
    """

    limpiar_pantalla()

    print('    ', end='')
    for i in range(len(tablero[0])):
        print(f'{i + 1} ', end='')
    print()

    for i, fila in enumerate(tablero):

        print(f'{i + 1} | ', end='')

        for columna in fila:
            print(columna, end=' ')

        print(f'| {i + 1}')

    print('    ', end='')
    for i in range(len(tablero[0])):
        print(f'{i + 1} ', end='')
    print()


def buscar_robot(tablero):
    for i, fila in enumerate(tablero):
        for j, columna in enumerate(fila):
            if columna == board.ROBOT:
                return i, j
    return -1, -1


def mover_robot(tablero, direccion):
    fila, columna = buscar_robot(tablero)
    fila_obj, columna_obj = fila, columna

    if direccion == mv.ARRIBA:
        fila_obj -= 1 # fila = fila - 1
    elif direccion == mv.ABAJO:
        fila_obj += 1
    elif direccion == mv.IZQUIERDA:
        columna_obj -= 1
    elif direccion == mv.DERECHA:
        columna_obj += 1
    else:
        print('No se reconoce la direccion')

    if fila_obj < 0 or columna_obj < 0 or \
        fila_obj >= len(tablero) or columna_obj >= len(tablero[0]):
        print('Movimiento no valido')
        return

    if tablero[fila_obj][columna_obj] == board.SPACE:
        tablero[fila][columna] = board.OBSTA
        tablero[fila_obj][columna_obj] = board.ROBOT
    else:
        print('Movimiento no valido')


def win(tablero):
    victoria = True

    for fila in tablero:
        for columna in fila:
            if columna == board.SPACE:
                victoria = False

    return victoria

def leer_direccion():
    """
    Lee la dirección del usuario Numpy

    Retorno
    -------
        str: dirección en la que va a mover el robot
    """
    direccion = input('Ingrese el movimiento (W/A/S/D) o X para salir: ')
    direccion = direccion.upper()

    if direccion == 'W':
        return mv.ARRIBA
    elif direccion == 'A':
        return mv.IZQUIERDA
    elif direccion == 'S':
        return mv.ABAJO
    elif direccion == 'D':
        return mv.DERECHA
    elif direccion == 'X':
        return mv.EXIT
    else:
        return leer_direccion()


def juego():
    tab = board.tablero
    imprimir_tablero(tab)
    direccion = leer_direccion()

    while direccion != mv.EXIT and not win(tab):
        mover_robot(tab, direccion)
        imprimir_tablero(tab)
        direccion = leer_direccion()

    print('Chao')

def menu():
    print('--------------------------------')
    print( '1. Iniciar juego nuevo')
    print( '2. salir')
    print('--------------------------------')
    opt = input('ingrese la operacion de preferancia: ')

    if opt == '1':
        juego()
    elif opt == '2':
        print('nos vemmops la proxima: ')
    else:
        print('opcion no valida')
        menu()

menu()

