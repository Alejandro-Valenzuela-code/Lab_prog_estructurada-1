MAX = 4

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
    # Obstáculos para que haya un único camino:
    # Camino único: (0,0)->(1,0)->(2,0)->(2,1)->(2,2)
    tablero[0][1] = -1
    tablero[0][2] = -1
    tablero[1][1] = -1
    tablero[1][2] = -1

# -------------------------------
# modulo solucion 
def solucion(tablero):
    # Posicion de inicio
    x, y = 0, 0
    contador = 1
    candidato = 1
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]  # guarda último candidato usado por celda

    # Validaciones de entrada
    if tablero[x][y] != 0 or tablero[MAX - 1][MAX - 1] != 0:
        return False

    tablero[x][y] = contador  # marcamos inicio

    while True:
        if candidato <= 4:
            if valida(tablero, candidato, x, y):
                nx, ny = siguiente_posicion(tablero, candidato, x, y)
                contador += 1
                tablero[nx][ny] = contador
                tablero_aux[x][y] = candidato  # recordamos por dónde salimos desde (x,y)

                if final(tablero, nx, ny):
                    # Primera solución encontrada: detenerse y devolver True
                    mostrar_tablero(tablero)
                    return True

                # Avanzar
                x, y = nx, ny
                candidato = 1  # al entrar a una nueva celda, probamos candidatos desde 1
            else:
                candidato += 1
        else:
            # No quedan candidatos desde (x,y) -> retroceder
            if x == 0 and y == 0:
                # Volvimos al inicio sin más candidatos: no hay solución
                return False

            # Borrar paso actual y volver una celda
            tablero[x][y] = 0
            contador -= 1
            px, py = buscar_xy(tablero, contador)  # celda anterior en el camino
            # Siguiente candidato a probar desde la celda anterior
            siguiente = tablero_aux[px][py] + 1
            tablero_aux[px][py] = 0  # limpiamos memoria (opcional)
            x, y = px, py
            candidato = siguiente

# -------------------------------
# programa principal
if __name__ == "__main__":
    tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]  # 0=libre; -1=obstáculo
    colocar_obstaculo(tablero)

    print("Tablero inicial:")
    mostrar_tablero(tablero)

    if solucion(tablero):
        print("Hay solucion")
    else:
        print("No hay solucion.")
