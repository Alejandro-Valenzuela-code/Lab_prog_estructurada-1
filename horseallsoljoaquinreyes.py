def crear_tablero(tamaño):
    return [[0 for _ in range(tamaño)] for _ in range(tamaño)]

def mostrar_tablero(tablero):
    for i in range(tamaño):
        for j in range(tamaño):
            print(tablero[i][j], end = " ") 
        print(" ")
    print(" ")

def final(tablero, tamaño):
    for i in range(tamaño):
        for j in range(tamaño):
            if tablero[i][j] == 0:
                return False
    return True

def mover_caballo_todas(tablero, x, y, tamaño):
    global soluciones
    
    if final(tablero, tamaño):
       soluciones+=1
       print(soluciones)
       return False

    movimientos_x = [2, 1, -1, -2, -2, -1, 1, 2]
    movimientos_y = [1, 2, 2, 1, -1, -2, -2, -1]

    for i in range(8):
        nx = x + movimientos_x[i]
        ny = y + movimientos_y[i]
        if 0 <= nx < tamaño and 0 <= ny < tamaño and tablero[nx][ny] == 0:
            tablero[nx][ny] = tablero[x][y] + 1

            if mover_caballo_todas(tablero, nx, ny, tamaño):
                return True
            tablero[nx][ny] = 0  # Retroceso
    return False

def recorrido_caballo(tamaño, x_inicial, y_inicial):
    tablero = crear_tablero(tamaño)
    tablero[x_inicial][y_inicial] = 1  # Comienza en 1
    mover_caballo_todas(tablero, x_inicial, y_inicial, tamaño)

# Ejecución principa
soluciones=0
tamaño = int(input("Ingrese el tamaño del tablero: "))
for y in range(tamaño):
    for x in range(tamaño):
        recorrido_caballo(tamaño,x,y)
