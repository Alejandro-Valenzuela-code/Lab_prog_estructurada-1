MAX = 4

# -------------------------------
# modulo valida
def valida(tablero, candidato, x, y):
    posx = [0, 1, 0, -1]  # derecha, abajo, izquierda, arriba
    posy = [1, 0, -1, 0]
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    if nx < 0 or nx >= MAX: return False
    if ny < 0 or ny >= MAX: return False
    return tablero[nx][ny] == 0  # 0=libre

# -------------------------------
# modulo siguiente_posicion
def siguiente_posicion(tablero, candidato, x, y):
    posx = [0, 1, 0, -1]
    posy = [1, 0, -1, 0]
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    return nx, ny

# -------------------------------
# modulo final
def final(tablero, nx, ny):
    return nx == MAX - 1 and ny == MAX - 1

# -------------------------------
# modulo buscar_xy
def buscar_xy(tablero, contador):
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == contador:
                return i, j
    return None, None

# -------------------------------
# util copiar tablero
def copiar_tablero(tab):
    return [fila[:] for fila in tab]

# -------------------------------
# modulo mostrar_tablero
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(tablero[i][j], end=" ")
        print("")
    print("")

# -------------------------------
# modulo colocar_obstaculo
def colocar_obstaculo(tablero):
    tablero[0][1] = -1
    tablero[0][2] = -1
    tablero[1][1] = -1
    tablero[1][2] = -1

# -------------------------------
# modulo mostrar_solucion_optima
def mostrar_solucion_optima(tab, largo):
    if tab is None:
        print("No hay soluciones.")
        return
    print(f"Solución óptima (longitud = {largo}):")
    for fila in tab:
        print(*fila)
    print("")

# -------------------------------
# modulo solucion 
def solucion(tablero):
    # Estado inicial
    x, y = 0, 0
    contador = 1
    candidato = 1
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]  # último candidato usado por celda

    # Mejor solución
    mejor_tab = None
    mejor_len = None

    # Validaciones de entrada
    if tablero[x][y] != 0 or tablero[MAX - 1][MAX - 1] != 0:
        return mejor_tab, mejor_len

    tablero[x][y] = contador  # inicio

    while True:
        if candidato <= 4:
            if valida(tablero, candidato, x, y):
                nx, ny = siguiente_posicion(tablero, candidato, x, y)
                contador += 1
                tablero[nx][ny] = contador
                tablero_aux[x][y] = candidato

                if final(tablero, nx, ny):
                    # Evaluar óptima (menor cantidad de pasos = menor contador)
                    if mejor_len is None or contador < mejor_len:
                        mejor_len = contador
                        mejor_tab = copiar_tablero(tablero)

                     #deshacer y seguir probando
                    tablero[nx][ny] = 0
                    contador -= 1
                    candidato += 1

                    while candidato == 5 and not (x == 0 and y == 0):
                        tablero[x][y] = 0
                        contador -= 1
                        px, py = buscar_xy(tablero, contador)
                        candidato = tablero_aux[px][py] + 1
                        tablero_aux[px][py] = 0
                        x, y = px, py
                else:
                    # Avanzar
                    x, y = nx, ny
                    candidato = 1
            else:
                candidato += 1
                # Retroceder si agoté candidatos en la celda
                while candidato == 5 and not (x == 0 and y == 0):
                    tablero[x][y] = 0
                    contador -= 1
                    px, py = buscar_xy(tablero, contador)
                    candidato = tablero_aux[px][py] + 1
                    tablero_aux[px][py] = 0
                    x, y = px, py
        else:
            # candidato > 4
            if x == 0 and y == 0:
                break  # agotamos todo desde el origen
            tablero[x][y] = 0
            contador -= 1
            px, py = buscar_xy(tablero, contador)
            candidato = tablero_aux[px][py] + 1
            tablero_aux[px][py] = 0
            x, y = px, py

    return mejor_tab, mejor_len

# -------------------------------
# programa principal
if __name__ == "__main__":
    tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]  # 0=libre; -1=obstáculo
    colocar_obstaculo(tablero)

    print("Tablero inicial:")
    mostrar_tablero(tablero)

    mejor_tab, mejor_len = solucion(tablero)
    mostrar_solucion_optima(mejor_tab, mejor_len)
