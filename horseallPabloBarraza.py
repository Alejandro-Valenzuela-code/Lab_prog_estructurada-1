
N = 5  # El tamaño del tablero

# Movimientos posibles del caballo (en coordenadas x e y)

mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
mov_y = [1, 2, 2, 1, -1, -2, -2, -1]

def es_valido(x, y, tablero): # Función para verificar si un movimiento es válido
    # Retorna True si la posición (x, y): Está dentro del tablero (no se sale de los límites) y la casilla aún no ha sido visitada (es -1)
    return 0 <= x < N and 0 <= y < N and tablero[x][y] == -1

def imprimir_tablero(tablero): # Función para imprimir el tablero de forma ordenada
    for fila in tablero: # Recorre cada fila del tablero y muestra los números alineados
        print(" ".join(f"{c:2}" for c in fila))  # ":2" reserva 2 espacios para alinear
    print()  # Línea en blanco entre tableros

def resolver_todas(): # Función principal: resuelve y muestra todas las soluciones posibles    
    tablero = [[-1 for _ in range(N)] for _ in range(N)] # Creamos un tablero lleno de -1 (sin visitar)    
    tablero[0][0] = 0 # Colocamos el caballo en la posición inicial (0,0)
    soluciones = [] # Lista donde se almacenarán todas las soluciones encontradas
    backtrack_todas(0, 0, 1, tablero, soluciones) # Llamamos a la función recursiva que buscará todas las rutas posibles

    print(f"Se encontraron {len(soluciones)} soluciones.") # Mostramos cuántas soluciones se encontraron

    for i, sol in enumerate(soluciones, 1): # Imprimimos cada solución encontrada con su número correspondiente
        print(f"Solución {i}:")
        imprimir_tablero(sol)

def backtrack_todas(x, y, paso, tablero, soluciones): # Función recursiva que genera todas las soluciones (backtracking)    
    if paso == N * N: # Si se alcanzó el total de casillas (N*N), se encontró una solución completa
        # Se guarda una copia del tablero actual (para no perderla al seguir probando movimientos)
        soluciones.append([fila[:] for fila in tablero])
        return  # No se sigue más por este camino
    
    for i in range(8): # Recorremos los 8 posibles movimientos del caballo
        nx = x + mov_x[i]  # Nueva posición en x
        ny = y + mov_y[i]  # Nueva posición en y
        
        if es_valido(nx, ny, tablero): # Verificamos si el movimiento es válido            
            tablero[nx][ny] = paso # Marcamos la casilla con el número del paso actual           
            backtrack_todas(nx, ny, paso + 1, tablero, soluciones)  # Llamamos recursivamente a la función para continuar desde la nueva posición            
            tablero[nx][ny] = -1 # Retrocedemos (backtracking): desmarcamos la casilla

resolver_todas()  # Ejecutamos la función principal

