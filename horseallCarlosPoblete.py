tamaño_tablero = 5  

mov_x = [-2, -1, 1, 2, 2, 1, -1, -2]
mov_y = [1, 2, 2, 1, -1, -2, -2, -1]

def es_valida(x, y, tablero):
    return 0 <= x < tamaño_tablero and 0 <= y < tamaño_tablero and tablero[x][y] == 0

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(str(c).rjust(2) for c in fila))
    print("")


def resolver(tablero, x, y, paso, soluciones):
    tablero[x][y] = paso

    # Si se llena el tablero se guarda una solucion
    if paso == tamaño_tablero * tamaño_tablero:
        print(f"✅ Solución #{len(soluciones) + 1}:")
        mostrar_tablero(tablero)
        soluciones.append([fila[:] for fila in tablero])
        tablero[x][y] = 0
        return

    for i in range(8):
        nx, ny = x + mov_x[i], y + mov_y[i]
        if es_valida(nx, ny, tablero):
            resolver(tablero, nx, ny, paso + 1, soluciones)

    tablero[x][y] = 0  

# Programa principal

tablero = [[0 for _ in range(tamaño_tablero)] for _ in range(tamaño_tablero)]
soluciones = []

resolver(tablero, 0, 0, 1, soluciones)

print(f"Total de soluciones encontradas: {len(soluciones)}")
