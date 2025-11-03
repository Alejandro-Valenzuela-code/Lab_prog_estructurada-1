def crear_tablero(n):
    # crea un tablero de n x n
    tablero = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(0)
        tablero.append(fila)
    return tablero

def imprimir_tablero(tablero):
    # imprime el tablero
    n = len(tablero)
    for i in range(n):
        for j in range(n):
            print(tablero[i][j], end="  ")
        print()
    print()

def es_valido(tablero, x, y):
    # revisa si la posicion x,y es valida
    n = len(tablero)
    # primero ver si esta dentro del tablero
    if x < 0 or x >= n:
        return False
    if y < 0 or y >= n:
        return False
    # verificar que la casilla este vacia
    if tablero[x][y] != 0:
        return False
    return True

def resolver(tablero, x, y, movimiento):
    # esta funcion resuelve el problema
    n = len(tablero)
    
    # poner el numero del movimiento actual
    tablero[x][y] = movimiento
    
    # si ya completamos el tablero retornamos true
    if movimiento == n * n:
        return True
    
    # estos son los movimientos del caballo
    # el caballo se mueve en L
    mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
    mov_y = [1, 2, 2, 1, -1, -2, -2, -1]
    
    # probar cada uno de los 8 movimientos
    for i in range(8):
        nuevo_x = x + mov_x[i]
        nuevo_y = y + mov_y[i]
        
        # si el movimiento es valido intentamos desde ahi
        if es_valido(tablero, nuevo_x, nuevo_y):
            if resolver(tablero, nuevo_x, nuevo_y, movimiento + 1):
                return True
            else:
                # si no funciono limpiamos esa casilla
                tablero[nuevo_x][nuevo_y] = 0
    
    # si probamos todos y no funciono retornamos falso
    return False


# ==== PROGRAMA ====

print("RECORRIDO DEL CABALLO")
print("El caballo debe recorrer todo el tablero sin repetir casillas")
print()

# pedir el tamano
tamano = int(input("Ingrese el tamano del tablero: "))

print()
print(f"Tablero de {tamano} x {tamano}")
print()

# crear el tablero
tablero = crear_tablero(tamano)

print("Tablero vacio:")
imprimir_tablero(tablero)

# preguntar desde donde comenzar la posicion
print("Posicion inicial del caballo:")
x_inicial = int(input("  Fila: "))
y_inicial = int(input("  Columna: "))

print()
print("Buscando solucion...")
print()

# intento para resolver y encontrar soluciones
if resolver(tablero, x_inicial, y_inicial, 1):
    print("SOLUCION ENCONTRADA!")
    print()
    imprimir_tablero(tablero)
else:
    print("No se encontro solucion")