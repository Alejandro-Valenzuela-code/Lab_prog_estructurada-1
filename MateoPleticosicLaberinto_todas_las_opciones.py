MAX =4

# -------------------------------
# modulo valida
def valida(tablero, candidato, x, y):
    posx = [0, 1, 0, -1]  # derecha, abajo, izquierda, arriba
    posy = [1, 0, -1, 0]
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]

    if nx < 0 or nx >= MAX:
        return False
    if ny < 0 or ny >= MAX:
        return False
    # 0 = libre; -1 = obstáculo; >0 = parte del camino
    return tablero[nx][ny] == 0

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
    # Puedes ajustar obstáculos. Estos dejan 1 solo camino:
    # Camino único: (0,0)->(1,0)->(2,0)->(2,1)->(2,2)
    tablero[0][1] = -1
    tablero[0][2] = -1
    tablero[1][1] = -1
    tablero[1][2] = -1

# -------------------------------
# modulo mostrar_soluciones
def mostrar_soluciones(soluciones):
    if not soluciones:
        print("No hay soluciones.")
        return
    for idx, sol in enumerate(soluciones, 1):
        print(f"Solución #{idx}:")
        for fila in sol:
            print(*fila)
        print("")
    print(f"Total soluciones: {len(soluciones)}")

# -------------------------------
# modulo solucion 
def solucion(tablero):
    soluciones = []

    # Estado inicial
    x, y = 0, 0
    contador = 1
    candidato = 1
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]  # último candidato usado por celda

    # Validaciones de entrada
    if tablero[x][y] != 0 or tablero[MAX - 1][MAX - 1] != 0:
        return soluciones

    tablero[x][y] = contador  # marcamos inicio

    while True:
        if candidato <= 4:
            if valida(tablero, candidato, x, y):
                nx, ny = siguiente_posicion(tablero, candidato, x, y)
                contador += 1
                tablero[nx][ny] = contador
                tablero_aux[x][y] = candidato  # recordamos por dónde salimos desde (x,y)

                if final(tablero, nx, ny):
                    # Guardar copia de la solución encontrada
                    soluciones.append(copiar_tablero(tablero))
                    # Deshacer último paso y probar siguiente candidato desde (x,y)
                    tablero[nx][ny] = 0
                    contador -= 1
                    candidato += 1

                    # Si ya no hay más candidatos desde (x,y), retroceder
                    while candidato == 5 and not (x == 0 and y == 0):
                        tablero[x][y] = 0
                        contador -= 1
                        px, py = buscar_xy(tablero, contador)
                        candidato = tablero_aux[px][py] + 1
                        tablero_aux[px][py] = 0
                        x, y = px, py
                else:
                    # Avanzar a la nueva celda
                    x, y = nx, ny
                    candidato = 1
            else:
                candidato += 1
                # Si ya probamos 4 candidatos, retrocedemos
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
                # agotamos todas las opciones desde el inicio
                break
            # Retroceder una celda
            tablero[x][y] = 0
            contador -= 1
            px, py = buscar_xy(tablero, contador)
            candidato = tablero_aux[px][py] + 1
            tablero_aux[px][py] = 0
            x, y = px, py

    return soluciones

# -------------------------------
# programa principal
if __name__ == "__main__":
    tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]  # 0=libre; -1=obstáculo
    colocar_obstaculo(tablero)

    print("Tablero inicial:")
    mostrar_tablero(tablero)

    sols = solucion(tablero)
    mostrar_soluciones(sols)
