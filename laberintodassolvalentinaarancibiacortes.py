MAX = 4

# ---- Movimientos posibles (derecha, abajo, izquierda, arriba) ----
mov_x = [0, 1, 0, -1]
mov_y = [1, 0, -1, 0]

# ---- Verifica si una posición es válida ----
def es_valida(tablero, x, y, visitado):
    return (0 <= x < MAX) and (0 <= y < MAX) and tablero[x][y] != -1 and not visitado[x][y]

# ---- Backtracking para encontrar todos los caminos ----
def encontrar_caminos(tablero, x, y, camino, visitado, soluciones):
    # Si llegamos al final, guardamos el camino
    if x == MAX - 1 and y == MAX - 1:
        soluciones.append(camino.copy())
        return

    # Marcamos la posición como visitada
    visitado[x][y] = True

    # Probamos las 4 direcciones
    for i in range(4):
        nx = x + mov_x[i]
        ny = y + mov_y[i]

        if es_valida(tablero, nx, ny, visitado):
            camino.append((nx, ny))
            encontrar_caminos(tablero, nx, ny, camino, visitado, soluciones)
            camino.pop()  # retroceder (backtrack)

    # Desmarcamos al volver
    visitado[x][y] = False

# ---- Coloca obstáculos ----
def colocar_obstaculos(tablero):
    tablero[0][3] = -1
    tablero[1][1] = -1
    tablero[2][1] = -1
    tablero[2][2] = -1
    tablero[2][3] = -1

# ---- Guarda los caminos en un archivo txt ----
def guardar_en_txt(soluciones):
    with open("soluciones.txt", "w", encoding="utf-8") as f:
        if not soluciones:
            f.write("No hay caminos válidos.\n")
            return
        for i, camino in enumerate(soluciones, 1):
            f.write(f"Camino {i}: " + " → ".join(str(p) for p in camino) + "\n")
        f.write(f"\nTotal de caminos encontrados: {len(soluciones)}\n")

# ---- Programa principal ----
def main():
    tablero = [[0]*MAX for _ in range(MAX)]
    colocar_obstaculos(tablero)

    visitado = [[False]*MAX for _ in range(MAX)]
    soluciones = []

    # Comienza desde (0,0)
    if tablero[0][0] == -1 or tablero[MAX-1][MAX-1] == -1:
        print("Inicio o fin bloqueado. No hay solución.")
        return

    encontrar_caminos(tablero, 0, 0, [(0,0)], visitado, soluciones)

    if soluciones:
        print(f"Se encontraron {len(soluciones)} caminos válidos.")
    else:
        print("No se encontró ningún camino.")

    guardar_en_txt(soluciones)
    print("Soluciones guardadas en 'soluciones.txt'.")

# ---- Ejecutar ----
if __name__ == "__main__":
    main()