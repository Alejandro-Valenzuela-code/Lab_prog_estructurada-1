
N = 5  # El tamaño del tablero

# Movimientos posibles del caballo (en coordenadas x e y)

mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
mov_y = [1, 2, 2, 1, -1, -2, -2, -1]

tablero = [[-1 for _ in range(N)] for _ in range(N)] # Se crea un tablero llenos de -1, lo que significa que las casillas aún no han sido visitadas
tablero[0][0] = 0 # El caballo comienza en la esquina superior izquierda del tablero

def es_valido(x, y): # Función para verificar si un movimiento es válido
    return 0 <= x < N and 0 <= y < N and tablero[x][y] == -1 # Devuelve True si: La posición (x, y) está dentro de los límites del tablero y La casilla aún no ha sido visitada (tiene valor -1)

def mover_caballo(x, y, paso): # Función para mover el caballo
    if paso == N * N: # Si el número de paso es igual al total de casillas (N*N), significa que se completó el recorrido
        return True  # Se encontró una solución completa

    for i in range(8): # Se recorre los 8 movimientos posibles del caballo
        
        nx = x + mov_x[i] # Se calcula la nueva posición
        ny = y + mov_y[i]

        
        if es_valido(nx, ny): # Se verifica si el movimiento es válido
            tablero[nx][ny] = paso # Marcamos la casilla con el número del paso actual        
            if mover_caballo(nx, ny, paso + 1): # Llamamos recursivamente a la función para continuar el recorrido desde la nueva posición
                return True  # Si se completa el recorrido, retornamos True
            # Si el movimiento no lleva a una solución, retrocedemos ("backtracking")
            tablero[nx][ny] = -1  # Desmarcamos la casilla (volvemos atrás)
    
    return False # Si ningún movimiento lleva a una solución, devolvemos False

# Iniciamos el recorrido del caballo

if mover_caballo(0, 0, 1):  # Comenzamos desde la casilla (0,0) y el paso 1, Si se encontró una solución, imprimimos el tablero con el orden de los pasos
       for fila in tablero:
        print(fila)   
else:    
    print("No hay solución.") # Si no hay solución posible, se muestra un mensaje


