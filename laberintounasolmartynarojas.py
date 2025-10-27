# LABERINTO UNA SOLUCIÓN 

MAX = 4

def valida(tablero, candidato, x, y):  # función para revisar si se puede mover
    mov_x = [1, 0, -1, 0]  # posibles movimientos
    mov_y = [0, 1, 0, -1]

    nx = x + mov_x[candidato - 1]
    ny = y + mov_y[candidato - 1]

    # revisa si el movimiento está dentro del tablero
    if nx < 0 or nx >= MAX or ny < 0 or ny >= MAX:
        return False
    # revisa que no sea una pared y que la casilla esté libre
    if tablero[nx][ny] == 0:
        return True
    else:
        return False

def siguiente_posicion(tablero, candidato, x, y):  # función que devuelve la siguiente posición
    mov_x = [1, 0, -1, 0]
    mov_y = [0, 1, 0, -1]
    nx = x + mov_x[candidato - 1]
    ny = y + mov_y[candidato - 1]
    return nx, ny

def final(tablero, nx, ny):  # función que revisa si se llegó a la meta
    if nx == MAX - 1 and ny == MAX - 1:
        return True
    return False

def buscar_xy(tablero, contador):  # busca la posición actual del jugador en el tablero
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == contador:
                return i, j

def mostrar_tablero(tablero):  # muestra el tablero 
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == -1:
                print("X", end=" ")  # muestra paredes
            else:
                print(tablero[i][j], end=" ")
        print()
    print()

def colocar_obstaculo(tablero):  # función que coloca las paredes (X = -1)
    tablero[0][1] = -1
    tablero[1][3] = -1
    tablero[2][1] = -1
    tablero[3][0] = -1

def solucion(tablero):  # función principal que busca UNA solución
    candidato = 1
    solucion = False
    x = 0
    y = 0
    contador = 1

    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]  # guarda los pasos
    tablero[x][y] = contador

    while candidato <= 4 and not solucion:
        if valida(tablero, candidato, x, y):
            nx, ny = siguiente_posicion(tablero, candidato, x, y)
            tablero[nx][ny] = contador + 1
            mostrar_tablero(tablero)

            if final(tablero, nx, ny):  # si llega a la meta
                solucion = True
            else:
                tablero_aux[x][y] = candidato
                x = nx
                y = ny
                contador += 1
                candidato = 1
        else:
            candidato += 1
            while candidato == 5 and not (x == 0 and y == 0):
                tablero[x][y] = 0
                contador -= 1
                nx, ny = buscar_xy(tablero, contador)
                candidato = tablero_aux[nx][ny] + 1
                tablero_aux[nx][ny] = 0
                x = nx
                y = ny
                mostrar_tablero(tablero)

    return solucion

#SE EJECUTA
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]  # crea el tablero vacío
colocar_obstaculo(tablero)  # pone las paredes
print("LABERINTO")
print("X = PARED")
mostrar_tablero(tablero)

if solucion(tablero):
    print("Solucion encontrada.")
    mostrar_tablero(tablero)
else:
    print("No hay solucion.")
