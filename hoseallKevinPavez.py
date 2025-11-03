# contador de cuantas soluciones encontramos
cantidad_soluciones = 0

def crear_tablero(n):
    # funcion para crear el tablero
    tablero = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(0)
        tablero.append(fila)
    return tablero

def imprimir_tablero(tablero):
    # muestra el tablero
    n = len(tablero)
    for i in range(n):
        for j in range(n):
            if tablero[i][j] < 10:
                print(tablero[i][j], end="  ")
            else:
                print(tablero[i][j], end=" ")
        print()
    print()

def copiar_tablero(tablero):
    # crea una copia del tablero
    n = len(tablero)
    nuevo = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(tablero[i][j])
        nuevo.append(fila)
    return nuevo

def es_valido(tablero, x, y):
    # verifica si x,y es una posicion valida
    n = len(tablero)
    if x >= 0 and x < n and y >= 0 and y < n:
        if tablero[x][y] == 0:
            return True
    return False

def buscar_todas(tablero, x, y, mov, lista_soluciones):
    # busca todas las soluciones posibles
    global cantidad_soluciones
    
    n = len(tablero)
    tablero[x][y] = mov
    
    # si completamos el tablero guardamos la solucion
    if mov == n * n:
        cantidad_soluciones = cantidad_soluciones + 1
        print(f"Solucion {cantidad_soluciones} encontrada!")
        
        # guardar copia del tablero
        copia = copiar_tablero(tablero)
        lista_soluciones.append(copia)
        
        # limpia para luego seguir buscando
        tablero[x][y] = 0
        return
    
    # movimientos del caballo
    mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
    mov_y = [1, 2, 2, 1, -1, -2, -2, -1]
    
    # probar todos los movimientos
    for i in range(8):
        nx = x + mov_x[i]
        ny = y + mov_y[i]
        
        if es_valido(tablero, nx, ny):
            buscar_todas(tablero, nx, ny, mov + 1, lista_soluciones)
    
    # limpiar esta casilla
    tablero[x][y] = 0


# ==== PROGRAMA MAIN ====

print("TODAS LAS SOLUCIONES DEL RECORRIDO DEL CABALLO")
print()

# pedir datos
tamano = int(input("Tamano del tablero: "))

print()

# crear tablero
tablero = crear_tablero(tamano)

# posicion inicial
print("Posicion inicial:")
x = int(input("  Fila: "))
y = int(input("  Columna: "))

# lista para guardar soluciones
soluciones = []

print()
print("Buscando todas las soluciones...")
print()

# buscar
buscar_todas(tablero, x, y, 1, soluciones)

# mostrar resultados
print()
print("=" * 40)
print(f"TOTAL: {cantidad_soluciones} soluciones encontradas")
print()

if cantidad_soluciones > 0:
    for i in range(len(soluciones)):
        print(f"Solucion {i+1}:")
        imprimir_tablero(soluciones[i])
else:
    print("No hay soluciones para esa configuracion")