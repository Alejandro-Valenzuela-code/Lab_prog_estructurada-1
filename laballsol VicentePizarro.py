import os, random
MAX = int(input("¿Cuántas casillas tendrá tu tablero? (ej: 4 para 4x4)\n"))

#modulo valida (valida que las posiciones sean factibles para para avanzar)
def valida(tablero, candidato, x, y):
    posx = [0, 1, 0, -1]
    posy = [1, 0, -1, 0]
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    
    if (nx < 0 or nx >= MAX):
        return False
    if (ny < 0 or ny >= MAX):
        return False
    # evita casillas ocupadas o con obstaculo (-1)
    if (tablero[nx][ny] == 0):
        return True
    else:
        return False

#modulo siguiente_posicion (elige la siguiente posicion con los movimientos prederminados)
def siguiente_posicion(tablero, candidato, x, y):
    posx = [0, 1, 0, -1]
    posy = [1, 0, -1, 0]
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    return nx, ny

#modulo final 
def final(tablero, nx, ny):
    if (nx == MAX - 1 and ny == MAX - 1):
        return True
    return False

#modulo buscar_xy
def buscar_xy(tablero, contador):
    for i in range(MAX):
        for j in range(MAX):
            if (tablero[i][j] == contador):
                return i, j

#modulo mostrar tablero
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(tablero[i][j], end=" ")
        print("")
    print("")

#modulo colocar_obstaculo
def colocar_obstaculo(tablero):
    num = random.randint(2, 3)  # se Define aleatoriamente el numero de obstaculos que tendra el tablero
    for _ in range(num):
        i = random.randint(0, MAX - 1)
        j = random.randint(0, MAX - 1)
        if (i, j) != (0, 0) and (i, j) != (MAX - 1, MAX - 1):
            tablero[i][j] = -1

#modulo solucion 
def solucion(tablero): 
    candidato = 1     
    solucion = False
    soluciones = 1
    x = 0
    y = 0
    contador = 1
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[x][y] = contador
    while (candidato <= 4):
        if (valida(tablero, candidato, x, y)):
            nx, ny = siguiente_posicion(tablero, candidato, x, y)
            tablero[nx][ny] = contador + 1
            if (final(tablero, nx, ny)):
                print("\nSolución encontrada:", soluciones)
                soluciones = soluciones + 1
                mostrar_tablero(tablero) 
                tablero[nx][ny] = 0       
                candidato = candidato + 1
                solucion = True
            else:
                tablero_aux[x][y] = candidato
                x = nx
                y = ny
                contador = contador + 1
                candidato = 1
        else:
            candidato = candidato + 1
            while (candidato == 5 and not (x == 0 and y == 0)):
                tablero[x][y] = 0
                contador -= 1
                nx, ny = buscar_xy(tablero, contador)
                candidato = tablero_aux[nx][ny] + 1
                tablero_aux[nx][ny] = 0
                x = nx
                y = ny
    return solucion

#programa principal
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]  # crea tablero
colocar_obstaculo(tablero)
print("\nestos son los obstaculos que hay en el tablero")
mostrar_tablero(tablero)

if (solucion(tablero) == True):
    print("esas son las unicas soluciones posibles con los movimientos establecidos")
else:
    print("No hay solución para este tablero")
