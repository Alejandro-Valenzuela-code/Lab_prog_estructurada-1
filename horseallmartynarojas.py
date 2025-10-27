# CABALLO TODAS LAS SOLUCIONES

MAX = 5  # tablero 5x5

# movimientos que puede hacer el caballo
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

def copiar_tablero(tablero):  # función para copiar el tablero
    return [fila[:] for fila in tablero]

def mostrar_tablero(tablero):  # función que muestra el tablero
    # cada fila
    for fila in tablero:
        # cada numero
        for numero in fila:
            # imprime el número con 2 espacios
            print(f"{numero:2d}", end=" ")
        print()  # salto de línea después de cada fila
    print()  # línea en blanco al final

def solucion_todas(tablero, x, y, paso, todas_soluciones):  # función que busca TODAS las soluciones
    # si ya llenamos todo el tablero
    if paso == MAX * MAX:
        # guardamos esta solución
        todas_soluciones.append(copiar_tablero(tablero))
        return

    # probamos los 8 movimientos posibles del caballo
    for i in range(8):
        # calcula nueva posición en X
        nx = x + mov_x[i]
        # calcula nueva posición en Y  
        ny = y + mov_y[i]
        # si la nueva posición es válida
        if valida(tablero, nx, ny):
            # casilla con el número de paso
            tablero[nx][ny] = paso
            # desde la nueva posición
            solucion_todas(tablero, nx, ny, paso + 1, todas_soluciones)
            # elimina el movimiento
            tablero[nx][ny] = -1

def mostrar_todas_soluciones(soluciones):  # función que muestra todas las soluciones
    if not soluciones:
        print("No hay solución.")
        return
        
    print(f"Hay {len(soluciones)} soluciones:\n")
    for i, sol in enumerate(soluciones, 1):
        print(f" solución {i} ")
        mostrar_tablero(sol)

def main():  #EJECUTA
    # crea un tablero vacío
    tablero = [[-1 for _ in range(MAX)] for _ in range(MAX)]
    # marca la posición inicial del caballo con 0
    tablero[0][0] = 0

    # lista para guardar todas las soluciones
    todas_soluciones = []
    
    # busca las soluciones
    solucion_todas(tablero, 0, 0, 1, todas_soluciones)

    # muestra soluciones
    mostrar_todas_soluciones(todas_soluciones)

# ejecuta
main()