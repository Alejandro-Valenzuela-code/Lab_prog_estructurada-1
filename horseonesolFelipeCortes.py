N = 5 #Se define el tamaño del tablero (N x N)

def validar_casilla(x, y, tablero):
    return (0 <= x < N and
            0 <= y < N and
            tablero[x][y] == -1)

def imprimir_solucion(tablero):
    print(f"Solución encontrada para el tablero {N}x{N}:")
    for i in range(N):
        for j in range(N):
            print(f"{tablero[i][j]:>2}", end=" ") #Se usa :>2 para alinear los números
        print()

def resolver_backtracking(x, y, mov_actual, tablero, mov_x, mov_y):
    if mov_actual == N * N: #Revisa si hemos visitado todas las casillas (N*N movimientos)
        return True

    for k in range(8): #Hacer los 8 movimientos posibles del caballo
        siguiente_x = x + mov_x[k]
        siguiente_y = y + mov_y[k]

        if validar_casilla(siguiente_x, siguiente_y, tablero):
            tablero[siguiente_x][siguiente_y] = mov_actual #Marcar la casilla como visitada

            if resolver_backtracking(siguiente_x, siguiente_y, mov_actual + 1, tablero, mov_x, mov_y): #Si devuelve true, encontro una solución
                return True 
            else:
                tablero[siguiente_x][siguiente_y] = -1 #Si no encontro la solución, se desmarca la casilla

    return False  #Si ningún movimiento funcionó desde esta casilla

def movimiento_caballo():
    tablero = [[-1 for _ in range(N)] for _ in range(N)] #Inicia el tablero con -1 (no visitado)

    #Movimientos del caballo (relativos a 'X, Y')
    mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
    mov_y = [1, 2, 2, 1, -1, -2, -2, -1]

    tablero[0][0] = 0

    if not resolver_backtracking(0, 0, 1, tablero, mov_x, mov_y):
        print(f"No existe solución para el tablero {N}x{N} empezando en (0,0)")
    else:
        imprimir_solucion(tablero)

movimiento_caballo()