MAX = 5# Tamaño del tablero

# módulo valida
def valida(tablero, candidato, x, y): # verifica si el movimiento es válido
    posx = [-2, -1, 1, 2, 2, 1, -1, -2]
    posy = [1, 2, 2, 1, -1, -2, -2, -1]
    nx = x + posx[candidato - 1] 
    ny = y + posy[candidato - 1]
    if nx < 0 or nx >= MAX:  #que no se salga del tablero
        return False  
    if ny < 0 or ny >= MAX: 
        return False
    if tablero[nx][ny] != 0: # que no haya sido visitado
        return False 
    return True 

def copiar_tablero(tab):
    return [fila[:] for fila in tab]

# módulo siguiente_posicion
def siguiente_posicion(tablero, candidato, x, y): # calcula la siguiente posición del caballo
    posx = [-2, -1, 1, 2, 2, 1, -1, -2] 
    posy = [1, 2, 2, 1, -1, -2, -2, -1]
    nx = x + posx[candidato - 1] 
    ny = y + posy[candidato - 1]
    return nx, ny

# módulo final
def final(tablero): # verifica si el tablero está completo
    for i in range(MAX): # fila
        for j in range(MAX): # columna
            if tablero[i][j] == 0: # si hay alguna celda vacía
                return False 
    return True 

# módulo buscar_xy
def buscar_xy(tablero, contador): # busca la posición (x,y) del contador en el tablero
    for i in range(MAX): # fila
        for j in range(MAX): # columna
            if tablero[i][j] == contador: 
                return i, j
    return None, None

# módulo mostrar_tablero
def mostrar_tablero(tablero): 
    for i in range(MAX):
        for j in range(MAX):
            print(f"{tablero[i][j]:2}", end=" ") 
        print("")
    print("")

# módulo solucion (principal)
def solucion(tablero):  
    candidato = 1
    soluciones = []
    x, y, contador = 0, 0, 1
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[x][y] = contador  # marca la primera posición
    while True:
        if 1 <= candidato <= 8:
            # Probar el candidato actual
            if valida(tablero, candidato, x, y):
                nx, ny = siguiente_posicion(tablero, candidato, x, y)
                tablero[nx][ny] = contador + 1
                
                if final(tablero):
                    # Guardar solución y seguir probando desde (x,y)
                    soluciones.append(copiar_tablero(tablero))
                    tablero[nx][ny] = 0     
                    candidato += 1         
                else:
                    tablero_aux[x][y] = candidato
                    x, y = nx, ny
                    contador += 1
                    candidato = 1
            else:
                candidato += 1
        else:
            if x == 0 and y == 0:
                break

            tablero[x][y] = 0
            contador -= 1
            nx, ny = buscar_xy(tablero, contador)  # volver a la casilla anterior
            candidato = tablero_aux[nx][ny] + 1  # retomar desde el siguiente candidato
            tablero_aux[nx][ny] = 0
            x, y = nx, ny
            # mostrar_tablero(tablero)  # opcional
    return soluciones

# programa principal
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)] # inicializa el tablero

soluciones = solucion(tablero)
print(f"Total de soluciones: {len(soluciones)}")

