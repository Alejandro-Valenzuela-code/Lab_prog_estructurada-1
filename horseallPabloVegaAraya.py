# horsetallsolpabloVegaAraya.py
# Programa: Recorrido del caballo (todas las soluciones posibles)


N = 5  # Para mostrar todas las soluciones, usamos un tablero 5x5 (más rápido)
soluciones = []

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(f'{x:2}' for x in fila))
    print()

mov_fila = [2, 1, -1, -2, -2, -1, 1, 2]
mov_col = [1, 2, 2, 1, -1, -2, -2, -1]

def es_seguro(x, y, tablero):
    return (x >= 0 and y >= 0 and x < N and y < N and tablero[x][y] == -1)

def recorrer_todas(x, y, paso, tablero):
    if paso == N * N:
        soluciones.append([fila[:] for fila in tablero])
        return

    for i in range(8):
        nuevo_x = x + mov_fila[i]
        nuevo_y = y + mov_col[i]
        if es_seguro(nuevo_x, nuevo_y, tablero):
            tablero[nuevo_x][nuevo_y] = paso
            recorrer_todas(nuevo_x, nuevo_y, paso + 1, tablero)
            tablero[nuevo_x][nuevo_y] = -1  # backtracking

def resolver_todas():
    tablero = [[-1 for _ in range(N)] for _ in range(N)]
    tablero[0][0] = 0
    recorrer_todas(0, 0, 1, tablero)

    print(f"Total de soluciones encontradas: {len(soluciones)}\n")
    for i, sol in enumerate(soluciones[:3]):  # muestra solo las primeras 3
        print(f"Solución #{i+1}:")
        imprimir_tablero(sol)

# Ejecutar programa
resolver_todas()