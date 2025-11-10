soluciones=[] # Lista para almacenar todas las soluciones encontradas

def valida(tablero,candidato,x,y): # Función que verifica si un movimiento es válido
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
    nx = x+posx [candidato-1]  # Calcula nueva pos. de X
    ny = y+posy [candidato-1] # Calcula nueva pos. de Y
    return nx,ny # Devuelve las nuevas posiciones.

#modulo final
def final(nx,ny): # Verifica si llegó al final del laberinto
    if (nx == n -1 and ny == n -1): # Comprueba que este en la esquina inferior derecha.
        return True # Si lo está, entonces devuelve True
    return False # Si no lo está, entonces devuelve False
            
#modulo solucion
def solucion(tablero, x, y, contador):
    if final(x, y): # Si se llego al final del lab.
        sol_actual = [fila[:] for fila in tablero] # Se crea una copia de la solucion actual
        soluciones.append(sol_actual) # Guarda la solucion actual.
        return False # Continua buscando soluciones 
    
    for candidato in range(1,5): # Prueba los 4 movimientos posibles (1-4)
        if valida(tablero, candidato, x, y): # Si el movimiento es valido 
            nx, ny = siguiente_posicion(candidato, x, y) # Calcula la sig. pos.
            tablero[nx][ny]= contador +1 # Marca la celda con el número de paso
            solucion(tablero, nx, ny, contador + 1) # Llama recursivamente
            tablero[nx][ny]=0 # Backtracking: desmarca la celda
    return False 

#modulo mostrar tablero
def mostrar_tablero(tablero): # Convierte el tablero a string legible
    resultado='' 
    for i in range(n): # Recorre cada fila
        for j in range(n): # Recorre cada columna
            if tablero[i][j] == -1: # Si es obstáculo
                resultado += "X " # Marca con X
            elif tablero[i][j] == 0: # Si está vacío
                resultado += ". " # Marca con punto
            else: # Si es parte del camino.
                resultado += str(tablero[i][j]) + " " # Muestra el número de paso
        resultado += "\n"
    resultado += "\n"
    return resultado # Retorna el string completo

#modulo colocar_obstaculo
def colocar_obstaculo(tablero): # Funcion para poner obstaculos
    obstaculos = [(0,1), (2,1), (0,2)] # Coords. de los obstaculos.
    for fila, columna in obstaculos: 
        if fila < n and columna < n: # Verifica que el obstaculo este dentro del tablero
            tablero[fila][columna] = -1 # Si lo está, lo marca como -1

def mostrar_soluciones(soluciones): # Muestra y guarda las soluciones encontradas
    print(f'Se encontraron {len(soluciones)} soluciones y se almacenaron en TotalSoluciones.txt.') # Se notifica la cantidad de sol. encontradas y donde se guardaron
    with open('TotalSoluciones.txt', 'w') as f: # Abre archivo para escribir
        for i in range(len(soluciones)): # Recorre cada solución
            f.write(f'Solucion {i+1}\n\n')
            f.write(mostrar_tablero(soluciones[i]))
            f.write('='*30+'\n')

#programa principal
n=int(input('Ingrese la medida de su tablero (n x n): ')) # Pide tamaño del tablero al usuario
tablero = [[0 for _ in range(n)] for _ in range(n)] # Crea tablero nxn lleno de ceros
tablero[0][0]=1 # Marca la pos. en la esquina superior izquierda como el inicio del camino
colocar_obstaculo(tablero) # Coloca los obstaculos
solucion(tablero, 0, 0, 1) # Inicia la busqueda de soluciones desde (0,0)

if soluciones: # Si se encontraron soluciones
    mostrar_soluciones(soluciones) # Se muestran y se guardan
else: # Si no se encontraron
    print('No hay solucion') # Entonces se notifica que no hay solucion.