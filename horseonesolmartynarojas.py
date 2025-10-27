# CABALLO UNA SOLUCIÓN

MAX = 5  #tablero 5x5

# lista de movimientos en X y Y que puede hacer el caballo
mov_x = [2, 1, -1, -2, -2, -1, 1, 2]  # horizontal
mov_y = [1, 2, 2, 1, -1, -2, -2, -1]  # vertical

def valida(tablero, x, y):  # función que verifica si una posición es válida
    # verifica que x esté entre 0 y MAX-1
    if x < 0 or x >= MAX:
        return False
    # verifica que y esté entre 0 y MAX-1  
    if y < 0 or y >= MAX:
        return False
    # verifica que la casilla esté vacía (-1)
    if tablero[x][y] != -1:
        return False
    return True

def final(tablero):  # función que verifica si el tablero está completo

    for i in range(MAX): #en filas
        
        for j in range(MAX): #en columna
            # si encuentra alguna casilla vacía
            if tablero[i][j] == -1:
                return False  # no está completo
    return True  # está completo

def mostrar_tablero(tablero):  # función que muestra el tablero
    # cada fila
    for fila in tablero:
        #cada numero
        for numero in fila:
            # imprime el número con 2 espacios
            print(f"{numero:2d}", end=" ")
        print()  # salto de línea después de cada fila
    print()  # línea en blanco al final

def solucion(tablero, x, y, paso):  # función principal con backtracking
    # si ya llenamos todo el tablero
    if paso == MAX * MAX:
        return True  # encontramos solución

    # probamos los 8 movimientos posibles del caballo
    for i in range(8):
        # calcula nueva posición en X
        nx = x + mov_x[i]
        # calcula nueva posición en Y  
        ny = y + mov_y[i]
        # si la nueva posición es válida
        if valida(tablero, nx, ny):
            # marcamos esta casilla con el número de paso
            tablero[nx][ny] = paso
            # intentamos continuar desde la nueva posición
            if solucion(tablero, nx, ny, paso + 1):
                return True  # si funciona, retornamos verdadero
            # si no funciona, deshacemos el movimiento
            tablero[nx][ny] = -1
    # si ningún movimiento funciona, retornamos falso        
    return False

def main():  # función principal del programa
    # crea un tablero lleno de -1 (vacío)
    tablero = [[-1 for _ in range(MAX)] for _ in range(MAX)]
    # marca la posición inicial del caballo con 0
    tablero[0][0] = 0

    # intenta encontrar una solución
    if solucion(tablero, 0, 0, 1):
        # si encuentra solución, muestra el mensaje
        print(f"Recorrido del caballo en tablero {MAX}x{MAX}:")
        print()
        # muestra el tablero con la solución
        mostrar_tablero(tablero)
    else:
        # si no encuentra solución, muestra mensaje
        print("No hay solución.")

# ejecuta
main()