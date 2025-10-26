# horseonesolpabloVegaAraya.py
# Programa: Recorrido del caballo en un tablero de ajedrez (una solución)
# Autor: Pablo Vega Araya
# Fecha: 20/10/25

N = 8  # tamaño del tablero 8x8

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(f'{x:2}' for x in fila))
    print()

# Movimientos posibles del caballo
mov_fila = [2, 1, -1, -2, -2, -1, 1, 2]
mov_col = [1, 2, 2, 1, -1, -2, -2, -1]

def es_seguro(x, y, tablero):
    """Verifica si la casilla (x, y) es válida y aún no visitada."""
    return (x >= 0 and y >= 0 and x < N and y < N and tablero[x][y] == -1)

def resolver_caballo():
    tablero = [[-1 for _ in range(N)] for _ in range(N)]
    tablero[0][0] = 0  # posición inicial del caballo

    if not recorrer(0, 0, 1, tablero):
        print("No existe solución.")
    else:
        imprimir_tablero(tablero)

def recorrer(x, y, paso, tablero):
    """Intenta encontrar una ruta completa para el caballo."""
    if paso == N * N:
        return True

    for i in range(8):
        nuevo_x = x + mov_fila[i]
        nuevo_y = y + mov_col[i]
        if es_seguro(nuevo_x, nuevo_y, tablero):
            tablero[nuevo_x][nuevo_y] = paso
            if recorrer(nuevo_x, nuevo_y, paso + 1, tablero):
                return True
            tablero[nuevo_x][nuevo_y] = -1  # backtracking

    return False

# Ejecutar programa
resolver_caballo()