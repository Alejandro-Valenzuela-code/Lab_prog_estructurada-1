
#este permite retener todas las soluciones y luego mostralo en la lista

N = 5 #tamño del tablero

#estos de aqui representan las formas posibles que se puede mover el caballo que en total son 8 formas en total
mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
mov_y = [1, 2, 2, 1, -1, -2, -2, -1]
#aqui voy a guardar todas las soluciones
soluciones = []

#aqui verifica si es que el movimiento es posible
def es_valido(x, y, tablero):
    return 0 <= x < N and 0 <= y < N and tablero[x][y] == -1

#este permite hacer una copia independiente del tablero para poder guardarlo a la lista de soluciones
def copiar_tablero(tablero):
    return [fila[:] for fila in tablero]

#este es la funcion principal
def resolver(tablero, x, y, paso):
    if paso == N * N: #si la cantiadad de pasos equila al numero de casillas del tablero se dice que se encontro una solucion
        soluciones.append(copiar_tablero(tablero))
        return

    for i in range(8): #la i adquiere y recorre los 8 movimientos posbles echos por el caballo
        nuevo_x = x + mov_x[i]
        nuevo_y = y + mov_y[i]
        if es_valido(nuevo_x, nuevo_y, tablero): 
            tablero[nuevo_x][nuevo_y] = paso #se marca la casilla
            resolver(tablero, nuevo_x, nuevo_y, paso + 1)
            tablero[nuevo_x][nuevo_y] = -1

tablero = [[-1 for _ in range(N)] for _ in range(N)] #se creea el tablero
tablero[0][0] = 0 #el valor del tablero esta repleto de -1, exepto la primera casilla con valor 0

resolver(tablero, 0, 0, 1)

print(f"Se encontraron {len(soluciones)} soluciones.")
contador = 1
for sol in soluciones:
    print(f"\nSolución {contador}:")
    for fila in sol:
        print(fila)
    contador += 1