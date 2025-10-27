#  LABERINTO - Todas las soluciones posibles

import os

# --- Función mostrar_tablero ---
def mostrar_tablero(tablero):
    for fila in range(MAX):
        for col in range(MAX):
            print(f"{tablero[fila][col]:2}", end=" ")
        print("")
    print("")

# --- Función colocar_obstaculo ---
def colocar_obstaculo(tablero):
    tablero[1][2] = " *"
    tablero[2][1] = " *"
    tablero[3][2] = " *"
# --- Función para verificar si la celda es válida ---
def es_valida(tablero, x, y):
    return 0 <= x < MAX and 0 <= y < MAX and tablero[x][y] == 0

# --- Función para comprobar si llegamos al final ---
def es_final(x, y):
    return x == MAX - 1 and y == MAX - 1

# --- Función para copiar el tablero ---
def copiar_tablero(tablero):
    return [fila[:] for fila in tablero]

# --- Función principal: encontrar TODAS las soluciones ---
def resolver_todas(tablero, x, y, paso, soluciones):
    if es_final(x, y):
        tablero[x][y] = paso
        soluciones.append(copiar_tablero(tablero))
        tablero[x][y] = 0
        return  # no return True, porque queremos seguir buscando más caminos

    # Movimientos posibles: derecha, abajo, izquierda, arriba
    movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    tablero[x][y] = paso

    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        if es_valida(tablero, nx, ny):
            resolver_todas(tablero, nx, ny, paso + 1, soluciones)

    tablero[x][y] = 0  # backtrack (retrocede)

# --- Inicio del programa ---
os.system("cls")
print("----------")
MAX = 4
tab = [[0 for _ in range(MAX)] for _ in range(MAX)]
colocar_obstaculo(tab)

print("Laberinto inicial:")
mostrar_tablero(tab)

soluciones = []
resolver_todas(tab, 0, 0, 1, soluciones)

# Mostrar resultados
if soluciones:
    print(f"Se encontraron {len(soluciones)} soluciones:\n")
    for i, sol in enumerate(soluciones):
        print(f"Solución {i + 1}:")
        mostrar_tablero(sol)
else:
    print("No hay solución.")
