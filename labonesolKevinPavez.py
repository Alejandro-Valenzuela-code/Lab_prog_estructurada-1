MAX = 5

# modulo valido
def valida(tablero, candidato, x, y):
    # direcciones: 1=derecha, 2=abajo, 3=izquierda, 4=arriba
    posx = [0, 1, 0, -1]
    posy = [1, 0, -1, 0]
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    
    # verificar limites del tablero
    if (nx < 0 or nx >= MAX):
        return False
    if (ny < 0 or ny >= MAX):
        return False
    # verificar si la casilla esta libre
    if (tablero[nx][ny] == 0):
        return True
    else:
        return False

# modulo siguiente posicion
def siguiente_posicion(tablero, candidato, x, y):
    posx = [0, 1, 0, -1]
    posy = [1, 0, -1, 0]
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    return nx, ny

# modulo final
def final(tablero, nx, ny):
    if (nx == MAX - 1 and ny == MAX - 1):
        return True
    return False

# modulo buscar xy
def buscar_xy(tablero, contador):
    for i in range(MAX):
        for j in range(MAX):
            if (tablero[i][j] == contador):
                return i, j

# modulo solucion ; encuentra la primera solucion
def solucion(tablero):
    candidato = 1
    solucion = False
    x = 0
    y = 0
    contador = 1
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[x][y] = contador
    
    while (candidato <= 4 and not solucion):
        if (valida(tablero, candidato, x, y)):
            nx, ny = siguiente_posicion(tablero, candidato, x, y)
            tablero[nx][ny] = contador + 1
            
            if (final(tablero, nx, ny)):
                solucion = True
            else:
                tablero_aux[x][y] = candidato
                x = nx
                y = ny
                contador = contador + 1
                candidato = 1
        else:
            candidato = candidato + 1
            # retroceder si no hay mas candidatos
            while (candidato == 5 and not (x == 0 and y == 0)):
                tablero[x][y] = 0
                contador -= 1
                nx, ny = buscar_xy(tablero, contador)
                candidato = tablero_aux[nx][ny] + 1
                tablero_aux[nx][ny] = 0
                x = nx
                y = ny
    
    return solucion

# modulo mostrar tablero
def mostrar_tablero(tablero):
    print("\nTablero:")
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == -1:
                print(" X", end=" ")
            elif tablero[i][j] == 0:
                print(" .", end=" ")
            else:
                print(f"{tablero[i][j]:2}", end=" ")
        print("")
    print("")

# modulo colocar obstaculo
def colocar_obstaculo(tablero):
    # colocar los obstaculos
    tablero[1][1] = -1
    tablero[2][1] = -1
    tablero[3][2] = -1

# programa principal
print("=== LABERINTO PRIMERA SOLUCION ===")
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]
colocar_obstaculo(tablero)
mostrar_tablero(tablero)

if (solucion(tablero) == True):
    print("¡Se encontro una solucion!")
    mostrar_tablero(tablero)
else:
    print('No hay solucion para este laberinto')