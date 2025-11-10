#modulo valida
def valida(tablero,candidato,x,y): # Verifica si un movimiento es válido
    posx = [0,1,0,-1] # Vectores de movimiento en X
    posy = [1,0,-1,0] # Vectores de movimiento en Y
    nx = x+posx [candidato-1] # Calcula nueva pos. de X
    ny = y+posy [candidato-1] # Calcula nueva pos. de Y
    if (nx < 0 or nx >= n): # Si esta fuera de los limites en las coords. X
        return False # Mov. invalido
    if (ny < 0 or ny >= n): # Si esta fuera de los limites en las coords. Y
        return False # Mov. invalido
    if tablero[nx][ny] == -1: # Si la celda es un obstaculo
        return False # Mov. invalido
    if (tablero[nx][ny]== 0): # Verifica si la celda esta vacia
        return True # Mov. valido
    else:
        return False # Mov. invalido, celda ya visitada.
    
#modulo siguiente_posicion 
def siguiente_posicion(candidato,x,y): # Calcula la sig. pos.
    posx = [0,1,0,-1] # Vectores de movimiento en X
    posy = [1,0,-1,0] # Vectores de movimiento en Y
    nx = x+posx [candidato-1] # Calcula nueva pos. de X
    ny = y+posy [candidato-1] # Calcula nueva pos. de Y
    return nx,ny # Devuelve las nuevas posiciones.

#modulo final
def final(nx,ny): # Verifica si llegó al final del laberinto
    if (nx == n -1 and ny == n -1): # Comprueba que este en la esquina inferior derecha.
        return True # Si lo está, entonces devuelve True
    return False # Si no lo está, entonces devuelve False
            
#modulo solucion
def solucion(x, y, contador):
    if final(x, y): # Si se llego al final del lab.
        return True # Se devuelve True, indicando que se halló sol.
    
    for candidato in range(1,5): # Prueba los 4 movimientos posibles
        if valida(tablero, candidato, x, y): # Si el movimiento es válido
            nx, ny = siguiente_posicion(candidato, x, y) # Calcula la nueva pos.
            tablero[nx][ny]= contador +1 # Marca la celda con el número de paso actual + 1

            if solucion(nx, ny, contador + 1):
                return True
            tablero[nx][ny]=0
    return False

#modulo mostrar tablero
def mostrar_tablero(tablero):
    for i in range(n): # Recorre cada fila
        for j in range(n): # Recorre cada columna
            if tablero[i][j] == -1: # Si es obstáculo
                print("X", end=" ") # Marca con X
            elif tablero[i][j] == 0: # Si está vacío
                print(".", end=" ") # Marca con punto
            else: # Si es parte del camino.
                print(tablero[i][j], end=" ") # Muestra el número de paso
        print("")
    print("")

#modulo colocar_obstaculo
def colocar_obstaculo(tablero): # Funcion para poner obstaculos
    obstaculos = [(0,1), (2,1), (0,2)] # Coords. de los obstaculos.
    for fila, columna in obstaculos:
        if fila < n and columna < n: # Verifica que el obstaculo este dentro del tablero
            tablero[fila][columna] = -1 # Si lo está, lo marca como -1


#programa principal
n=int(input('Ingrese la medida de su tablero (n x n): ')) # Pide tamaño del tablero al usuario
tablero = [[0 for _ in range(n)] for _ in range(n)] # Crea tablero nxn lleno de ceros
colocar_obstaculo(tablero) # Coloca los obstaculos
tablero[0][0]=1 # Marca la pos. en la esquina superior izquierda como el inicio del camino

if(solucion(0, 0, 1)): # Busca una solución desde (0,0). Si la encuentra
    print("Hay solucion") # Se notifica que se encontro sol.
    mostrar_tablero(tablero) # Se muestra la solución
else: # Si no se encuentra
    print('No hay solucion') # Se notifica que no hay solucion