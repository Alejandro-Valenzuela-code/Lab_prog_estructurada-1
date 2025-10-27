
MAX = int(input('Ingrese el tamaño del tablero:  '))

#nombre_archivo = f"solucion_tablero_{MAX}.txt"

# Función para mostrar el tablero en consola 
def mostrar_tablero(tablero):
    for i in range(MAX):  
        for j in range(MAX):  
            print(f"{tablero[i][j]:2}", end=" ")  
        print("")
    print("")  

# Función para verificar si una posición es válida
def valida(tablero, x, y):
    
    return 0 <= x < MAX and 0 <= y < MAX and tablero[x][y] == 0

# Función recursiva que implementa el recorrido del caballo (backtracking)
def recorrer(tablero, x, y, contador, soluciones):
    
    if contador == MAX * MAX:
        tablero[x][y] = contador  
        # Guardar una copia del tablero como solución
        solucion_copia = [fila[:] for fila in tablero]
        soluciones.append(solucion_copia)  # Añadir a la lista de soluciones
        tablero[x][y] = 0  # Desmarcar la casilla para backtracking
        return

    # Posibles movimientos del caballo en x e y
    posx = [-2,-1,1,2,2,1,-1,-2]
    posy = [1,2,2,1,-1,-2,-2,-1]

    tablero[x][y] = contador  # Marcar la casilla actual con el número de paso

    # Prueba los 8 posibles movimientos
    for k in range(8):
        nx = x + posx[k]  # Nueva posición en x
        ny = y + posy[k]  # Nueva posición en y
        if valida(tablero, nx, ny):  
            recorrer(tablero, nx, ny, contador+1, soluciones)  # Llamada recursiva

    tablero[x][y] = 0  # Backtracking: desmarcar la casilla antes de volver


'''def guardar_solucion(solucion):                     #Definimos una funcion que almacena una sola solucion del tablero(la primera).
    with open(nombre_archivo, "w") as f:
              
        sol = solucion[0]
        f.write(f"Solucion: \n")
        for fila in sol:
            f.write(" ".join(f"{num:2}" for num in fila) + "\n")
        
    print(f"\nSe guardó la solucion en '{nombre_archivo}'.")'''


# PROGRAMA PRINCIPAL

tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]


solucion = []

# Iniciar recorrido desde la esquina superior izquierda (0,0)
recorrer(tablero, 0, 0, 1, solucion)


if solucion:
    print(f"\nSolución :")
    mostrar_tablero(solucion[0])                                    
else:
    print("No hay soluciones para este tamaño de tablero.")

#guardar_solucion(solucion)  
