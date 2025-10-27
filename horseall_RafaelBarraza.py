
MAX = int(input('Ingrese el tamaño del tablero:  '))

# Función para mostrar el tablero en consola
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(f"{tablero[i][j]:2}", end=" ")
        print("")
    print("")

'''# Función para convertir un tablero en texto para guardar en archivo
def tablero_a_texto(tablero):
    lineas = []
    for fila in tablero:
        lineas.append(" ".join(f"{num:2}" for num in fila))
    return "\n".join(lineas) + "\n"
                                     '''   

# Función para verificar si una posición es válida
def valida(tablero, x, y):
    return 0 <= x < MAX and 0 <= y < MAX and tablero[x][y] == 0

# Función recursiva que implementa el recorrido del caballo (backtracking)
def recorrer(tablero, x, y, contador, soluciones):
    if contador == MAX * MAX:
        tablero[x][y] = contador
        solucion_copia = [fila[:] for fila in tablero]
        soluciones.append(solucion_copia)
        tablero[x][y] = 0
        return

    posx = [-2,-1,1,2,2,1,-1,-2]
    posy = [1,2,2,1,-1,-2,-2,-1]

    tablero[x][y] = contador

    for k in range(8):
        nx = x + posx[k]
        ny = y + posy[k]
        if valida(tablero, nx, ny):
            recorrer(tablero, nx, ny, contador+1, soluciones)

    tablero[x][y] = 0

# PROGRAMA PRINCIPAL

tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]
soluciones = []

recorrer(tablero, 0, 0, 1, soluciones)

# Guardar soluciones en archivo y mostrar en consola
if soluciones:
    #with open(f"Soluciones_del_tablero{MAX}X{MAX}.txt", "w") as archivo:
    for i, sol in enumerate(soluciones, start=1):
            print(f"Solución {i}:")
            mostrar_tablero(sol)
            
            '''archivo.write(f"Solucion {i}:\n")
            archivo.write(tablero_a_texto(sol))
            archivo.write("\n")'''
    print(f"\nSe encontraron {len(soluciones)} soluciones:\n")
else:
    print("No hay soluciones para este tamaño de tablero.")
