SPACE = '🟢'
ROBOT = '👤'
OBSTA = '🥥'
CAJA  = '🟣'

# tablero = (
#     [SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE],
#     [SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE],
#     [SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE],
#     [SPACE, SPACE, SPACE, ROBOT, SPACE, SPACE, SPACE],
#     [SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE],
#     [SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE],
#     [SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE],
#     [SPACE, SPACE, SPACE, SPACE, SPACE, SPACE, SPACE],
# )

def leer_tablero(nivel):

    tablero = []
    seccion = ''
    variables = {}

    with open(f'{nivel}.board', 'r') as f:
        lineas = f.readlines()

        for linea in lineas:
            linea = linea[:-1].strip() # quita el ultimo elemento y el espacio

            if linea in ('', '\n'):
                continue
            if linea in ('# VARIABLES','# TABLERO') :
                seccion = linea
                continue
            if seccion == '# VARIABLES':
                linea = linea.split('=')
                var = linea[0].strip()
                tipo = linea[1].strip()
                if tipo == 'ESPACIO':
                    tipo = SPACE
                elif tipo == 'ROBOT':
                    tipo = ROBOT
                elif tipo == 'MURO':
                    tipo = OBSTA
                elif tipo == 'CAJA':
                    tipo = CAJA


                variables[var] = tipo
            elif seccion == '# TABLERO':

                for var,tipo in variables.items():
                    linea = linea.replace(var, tipo)

            #linea = linea.replace('S', SPACE)        
            #linea = linea.replace('r', ROBOT)
            #linea = linea.replace('o', OBSTA)

                linea = list(linea)
                tablero.append(linea)
    return tablero


if __name__ == '__main__':
    leer_tablero('nivel_1')