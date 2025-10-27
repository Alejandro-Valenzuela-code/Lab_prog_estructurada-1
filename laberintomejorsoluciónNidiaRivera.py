#  LABERINTO - Mejor solución (camino más corto)

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

# --- Función principal: encontrar el camino más corto ---
def mejor_camino(tablero, x, y, paso, mejor_sol):
    if es_final(x, y):
        tablero[x][y] = paso
        # Guardar solución si es la primera o si es más corta
        if mejor_sol["tablero"] is None or paso < mejor_sol["pasos"]:
            mejor_sol["tablero"] = copiar_tablero(tablero)
            mejor_sol["pasos"] = paso
        tablero[x][y] = 0
        return

    # Movimientos posibles: derecha, abajo, izquierda, arriba
    movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    tablero[x][y] = paso

    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        if es_valida(tablero, nx, ny):
            mejor_camino(tablero, nx, ny, paso + 1, mejor_sol)

    tablero[x][y] = 0  # backtrack

# --- Inicio del programa ---
os.system("cls")
print("----------")
MAX = 4
tab = [[0 for _ in range(MAX)] for _ in range(MAX)]
colocar_obstaculo(tab)

print("Laberinto inicial:")
mostrar_tablero(tab)

mejor_sol = {"tablero": None, "pasos": float("inf")}

mejor_camino(tab, 0, 0, 1, mejor_sol)

# Mostrar el resultado
if mejor_sol["tablero"]:
    print(f"Camino más corto encontrado ({mejor_sol['pasos']} pasos):\n")
    mostrar_tablero(mejor_sol["tablero"])
else:
    print("No hay solución posible.")
