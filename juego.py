import board
import movimiento as mv
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
        print(f'{i + 1} ', end=' ')
    print()

    for i, fila in enumerate(tablero):

        print(f'{i + 1} | ', end='')

        for columna in fila:
            print(columna, end=' ')

        print(f'| {i + 1}')

    print('    ', end='')
    for i in range(len(tablero[0])):
        print(f'{i + 1} ', end=' ')
    print()


def buscar_robot(tablero):
    for i, fila in enumerate(tablero):
        for j, columna in enumerate(fila):
            if columna == board.ROBOT:
                return i, j
    return -1, -1

def movimiento_en_limites(fila, columna, len_filas, len_columnas):
    if fila < 0 or columna < 0 or fila >= len_filas or columna >= len_columnas:
        return False
    return True
def mover_objeto(tablero, fila, columna, fila_obj, columna_obj, obj):
    tablero[fila_obj][columna_obj] = tablero[fila][columna]
    tablero[fila][columna] = obj

def get_coordenada_direccion(fila, columna, direccion):
    fila_obj, columna_obj = fila, columna

    if direccion == mv.ARRIBA:
        fila_obj -= 1  # fila = fila - 1
    elif direccion == mv.ABAJO:
        fila_obj += 1
    elif direccion == mv.IZQUIERDA:
        columna_obj -= 1
    elif direccion == mv.DERECHA:
        columna_obj += 1
    else:
        return (-1, -1)

    return(fila_obj, columna_obj)


def empujar_caja(fila, columna, direccion, tablero):
    
    fila_obj, columna_obj = get_coordenada_direccion(fila, columna, direccion)
    if fila_obj == -1 or columna_obj == -1:
        return False

    if not movimiento_en_limites(fila_obj, columna_obj, len(tablero), len(tablero[0])):
        print('Movimiento no valido')
        return False

    if tablero[fila_obj][columna_obj] == board.SPACE:
        tablero[fila][columna]=board.SPACE
        tablero[fila_obj][columna_obj]=board.CAJA
        mover_objeto(tablero, fila, columna, fila_obj, columna_obj, board.SPACE)
        return True

    else:
        return False

def mover_robot(tablero, direccion):
    fila, columna = buscar_robot(tablero)
    fila_obj, columna_obj = fila, columna

    fila_obj, columna_obj = get_coordenada_direccion(fila, columna, direccion)
    if fila_obj == -1 or columna_obj == -1:
        return False

    if not movimiento_en_limites(fila_obj, columna_obj, len(tablero), len(tablero[0])):
        print('Movimiento no valido')
        return False

    if tablero[fila_obj][columna_obj] == board.SPACE:
        mover_objeto(tablero, fila, columna, fila_obj, columna_obj, board.OBSTA)
        return True

    elif tablero[fila_obj][columna_obj] == board.CAJA:
        pudo_mover = empujar_caja(fila_obj, columna_obj, direccion, tablero)
        if pudo_mover:
            mover_objeto(tablero, fila, columna, fila_obj, columna_obj, board.OBSTA)

        return pudo_mover

    else:
        return False


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
    tab = board.leer_tablero('nivel_1')
    imprimir_tablero(tab)
    direccion = leer_direccion()

    while direccion != mv.EXIT and not win(tab):
        mover_robot(tab, direccion)
        imprimir_tablero(tab)
        direccion = leer_direccion()

    print('Chao')

def manual(idioma):
    menu_manual = {
        'es' : {
            'desc': 'El juego consiste en recorrer todo el tablero ',
            board.ROBOT : 'Es el robot',
            board.OBSTA : 'Es el obstaculo',
        },

        'en' : {
            'desc':' You have to move around the full board',
            board.ROBOT : 'This is a pretty robot',
            board.OBSTA : 'This is a awful robot',
        },

    }

    for k in menu_manual[idioma]:
        if k != 'desc':
            print(f'\t{k} - {menu_manual[idioma][k]}')
        else:
            print(menu_manual[idioma])
    
    input()


def menu():

    mi_menu = {
        'es' : {
        '1' : 'Iniciar juego nuevo',
        '2' : 'Ver manual de juego',
        '3' : 'Salida'
        },
        'en' : {
        '1' : 'Start new game',
        '2' : 'Show manual',
        '3' : 'Exit'
        },
    }
    print('--------------------------------')
    lang = input('Indique el idioma (en/es): ')

    for k in mi_menu[lang]:
        print(f'{k}, {mi_menu[lang][k]} ')

    print('--------------------------------')
    opt = input('ingrese la operacion de preferancia: ')

    if opt == '1':
        juego()
    if opt == '2':
        manual(lang)
    elif opt == '3':
        print('nos vemos la proxima: ')
    else:
        print('opcion no valida')
        menu()

menu()

#def menu():
#    print('--------------------------------')
#   print( '1. Iniciar juego nuevo')
#  print( '2. salir')
#   print('--------------------------------')
#   opt = input('ingrese la operacion de preferancia: ')
#
#   if opt == '1':
#       juego()
#   elif opt == '2':
#       print('nos vemmops la proxima: ')
#   else:
#       print('opcion no valida')
#       menu()

#menu()

