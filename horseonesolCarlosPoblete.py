tamaño_tablero = 5  


def valida(tablero, candidato, x, y):
    
    mov_x = [-2, -1, 1, 2, 2, 1, -1, -2]
    mov_y = [1, 2, 2, 1, -1, -2, -2, -1]

    nx = x + mov_x[candidato - 1]
    ny = y + mov_y[candidato - 1]

    if nx < 0 or nx >= tamaño_tablero or ny < 0 or ny >= tamaño_tablero:
        return False

    if tablero[nx][ny] != 0:
        return False

    return True


def siguiente_posicion(candidato, x, y):
    mov_x = [-2, -1, 1, 2, 2, 1, -1, -2]
    mov_y = [1, 2, 2, 1, -1, -2, -2, -1]
    return x + mov_x[candidato - 1], y + mov_y[candidato - 1]


def final(tablero):
    for fila in tablero:
        if 0 in fila:
            return False
    return True


# -----------------------------------------------------------
# Busca la posición del número "contador" en el tablero
# (sirve para retroceder en el backtracking)
# -----------------------------------------------------------
def buscar_xy(tablero, contador):
    for i in range(tamaño_tablero):
        for j in range(tamaño_tablero):
            if tablero[i][j] == contador:
                return i, j


# -----------------------------------------------------------
# Imprime el tablero
# -----------------------------------------------------------
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(str(c).rjust(2) for c in fila))
    print("")


# -----------------------------------------------------------
# Encuentra la primera solución del recorrido del caballo
# -----------------------------------------------------------
def solucion(tablero):
    candidato = 1
    solucion_encontrada = False
    x, y, contador = 0, 0, 1
    tablero_aux = [[0 for _ in range(tamaño_tablero)] for _ in range(tamaño_tablero)]

    tablero[x][y] = contador  # posición inicial

    while candidato <= 8 and not solucion_encontrada:
        if valida(tablero, candidato, x, y):
            nx, ny = siguiente_posicion(candidato, x, y)
            tablero[nx][ny] = contador + 1
            mostrar_tablero(tablero)  # muestra progreso

            if final(tablero):
                solucion_encontrada = True
            else:
                tablero_aux[x][y] = candidato
                x, y, contador = nx, ny, contador + 1
                candidato = 1
        else:
            candidato += 1
            # retroceso si no hay movimientos válidos
            while candidato == 9 and not (x == 0 and y == 0):
                tablero[x][y] = 0
                contador -= 1
                nx, ny = buscar_xy(tablero, contador)
                candidato = tablero_aux[nx][ny] + 1
                tablero_aux[nx][ny] = 0
                x, y = nx, ny
                mostrar_tablero(tablero)

    return solucion_encontrada


# -----------------------------------------------------------
# Programa principal
# -----------------------------------------------------------
tablero = [[0 for _ in range(tamaño_tablero)] for _ in range(tamaño_tablero)]

print("Tablero inicial:")
mostrar_tablero(tablero)

if solucion(tablero):
    print("Solución:")
    mostrar_tablero(tablero)
else:
    print("No hay solución.")

