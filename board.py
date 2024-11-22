SPACE = '🟢'
ROBOT = '🔴'
OBSTA = '⚫'


tablero = (
    [SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE],
    [SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE],
    [SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE],
    [SPACE, SPACE, SPACE, ROBOT, SPACE, SPACE, SPACE],
    [SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE],
    [SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE],
    [SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE],
    [SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE],
)

def leer_tablero(nivel):

    tablero = []
    

    with open(f'{nivel}.board', 'r') as f:
        lineas = f.readlines()

        for linea in lineas:
            linea = linea[:-1].strip() # quita el ultimo elemento y el espacio
            linea = linea.replace('s', SPACE)
            linea = linea.replace('r', ROBOT)
            linea = linea.replace('o', OBSTA)

            linea = list(linea)
            tablero.append(linea)
    return tablero


if __name__ == '__main__':
    leer_tablero('nivel_1')