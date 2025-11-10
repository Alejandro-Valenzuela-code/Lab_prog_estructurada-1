MAX = 5

# modulo validar
def valida(tablero, candidato, x, y):
    # direcciones: 1=derecha, 2=abajo, 3=izquierda, 4=arriba
    posx = [0, 1, 0, -1]
    posy = [1, 0, -1, 0]
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    
    # verificar los limites del tablero
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

# modulo todas soluciones - encuentra todas las soluciones
def todas_soluciones(tablero):
    candidato = 1
    x = 0
    y = 0
    contador = 1
    num_soluciones = 0
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[x][y] = contador
    
    while (candidato <= 4):
        if (valida(tablero, candidato, x, y)):
            nx, ny = siguiente_posicion(tablero, candidato, x, y)
            tablero[nx][ny] = contador + 1
            
            if (final(tablero, nx, ny)):
                num_soluciones += 1
                print(f"\n--- Solucion {num_soluciones} ---")
                mostrar_tablero(tablero)
                
                # limpiar y seguir buscando
                tablero[nx][ny] = 0
                candidato = candidato + 1
                
                # retroceder para buscar mas soluciones
                while (candidato == 5 and not (x == 0 and y == 0)):
                    tablero[x][y] = 0
                    contador -= 1
                    nx, ny = buscar_xy(tablero, contador)
                    candidato = tablero_aux[nx][ny] + 1
                    tablero_aux[nx][ny] = 0
                    x = nx
                    y = ny
            else:
                tablero_aux[x][y] = candidato
                x = nx
                y = ny
                contador = contador + 1
                candidato = 1
        else:
            candidato = candidato + 1
            # retroceder si ya no existen mas candidatos
            while (candidato == 5 and not (x == 0 and y == 0)):
                tablero[x][y] = 0
                contador -= 1
                nx, ny = buscar_xy(tablero, contador)
                candidato = tablero_aux[nx][ny] + 1
                tablero_aux[nx][ny] = 0
                x = nx
                y = ny
    
    return num_soluciones

# modulo mostrar tablero
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == -1:
                print(" X", end=" ")
            elif tablero[i][j] == 0:
                print(" .", end=" ")
            else:
                print(f"{tablero[i][j]:2}", end=" ")
        print("")

# modulo colocar obstaculos
def colocar_obstaculo(tablero):
    # colocar los obstaculos
    tablero[1][1] = -1
    tablero[2][1] = -1
    tablero[3][2] = -1

# programa principal
print("=== LABERINTO - TODAS LAS SOLUCIONES ===")
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]
colocar_obstaculo(tablero)
print("\nTablero inicial:")
mostrar_tablero(tablero)

total = todas_soluciones(tablero)

if (total > 0):
    print(f"\nSe encontraron {total} soluciones en total")
else:
    print('\nNo hay soluciones para este laberinto')