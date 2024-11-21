SPACE = '.'
ROBOT = 'R'
OBSTA = 'X'


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
    with open(f'{nivel}.board', 'r') as f:
        lineas = f.readlines()

        for linea in lines:
            linea = linea[:-1].strip() # quita el ultimo elemento y el espacio
            print(linea)


if __name__ == '__main__':
    leer_tablero('nivel_1')