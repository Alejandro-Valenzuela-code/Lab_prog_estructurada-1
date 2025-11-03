


N = 5  # tamaño del tablero 

#estos de aqui representan las formas posibles que se puede mover el caballo que en total son 8 formas en total
mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
mov_y = [1, 2, 2, 1, -1, -2, -2, -1]

def mostrar_tablero(tablero):
    for fila in tablero:
        print(fila)
    print()

#aqui verifica si es que el movimiento es posible
def es_valido(x, y, tablero):
    return 0 <= x < N and 0 <= y < N and tablero[x][y] == -1

#este es la funcion principal
def resolver(tablero, x, y, paso):
    if paso == N * N: #si la cantiadad de pasos equila al numero de casillas del tablero se dice que se encontro una solucion
        return True

    for i in range(8): #la i adquiere y recorre los 8 movimientos posbles echos por el caballo
        nuevo_x = x + mov_x[i]
        nuevo_y = y + mov_y[i]
        if es_valido(nuevo_x, nuevo_y, tablero):
            tablero[nuevo_x][nuevo_y] = paso #se marca la casilla
            if resolver(tablero, nuevo_x, nuevo_y, paso + 1):
                return True
            tablero[nuevo_x][nuevo_y] = -1  # retrocede
    return False

# Programa principal
tablero = [[-1 for _ in range(N)] for _ in range(N)] #se creea el tablero
print(tablero)
print(mostrar_tablero(tablero))
print(type(tablero))
tablero[0][0] = 0  # el valor es cambiado a 0 en el principio de la tabla

if resolver(tablero, 0, 0, 1):
    print("Una solución encontrada:")
    mostrar_tablero(tablero)
else:
    print("No se encontró solución.")