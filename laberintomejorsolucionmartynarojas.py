# LABERINTO MEJOR SOLUCIÓN

MAX = 4

def mostrar_laberinto(tablero):  # función para mostrar el laberinto
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == 0:
                print("0", end=" ")  # camino libre
            elif tablero[i][j] == -1:
                print("X", end=" ")  # pared
            else:
                print(tablero[i][j], end=" ")  # número del paso
        print()
    print()

def valida(tablero, x, y):  # función que revisa si la posición está libre y dentro del laberinto
    if x < 0 or x >= MAX or y < 0 or y >= MAX:
        return False
    return tablero[x][y] == 0

def copiar_laberinto(tablero):  # función para copiar el laberinto
    return [fila[:] for fila in tablero]

def resolver_todas_soluciones(tablero, x, y, paso, todas_soluciones):  # función que busca TODAS las soluciones
    if x == MAX - 1 and y == MAX - 1:  # si llega a la meta
        tablero[x][y] = paso
        todas_soluciones.append(copiar_laberinto(tablero))  # guarda esta solución
        tablero[x][y] = 0  # limpia para seguir buscando
        return

    if valida(tablero, x, y):  # si la posición es válida
        tablero[x][y] = paso  # marca el paso actual

        # prueba moverse en las 4 direcciones
        resolver_todas_soluciones(tablero, x + 1, y, paso + 1, todas_soluciones)  # abajo
        resolver_todas_soluciones(tablero, x, y + 1, paso + 1, todas_soluciones)  # derecha
        resolver_todas_soluciones(tablero, x - 1, y, paso + 1, todas_soluciones)  # arriba
        resolver_todas_soluciones(tablero, x, y - 1, paso + 1, todas_soluciones)  # izquierda

        tablero[x][y] = 0  # limpia la casilla

def encontrar_mejor_solucion(todas_soluciones):  # función que encuentra la MEJOR solución
    if not todas_soluciones:
        return None, None
    
    mejor_solucion = todas_soluciones[0]
    mejor_longitud = todas_soluciones[0][MAX-1][MAX-1]  # último número del camino
    
    for solucion in todas_soluciones:
        longitud = solucion[MAX-1][MAX-1]  # número en la esquina final
        if longitud < mejor_longitud:
            mejor_longitud = longitud
            mejor_solucion = solucion
    
    return mejor_solucion, mejor_longitud

def crear_laberinto():  # función que crea el laberinto con paredes que SÍ tienen solución
    tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]
    # Obstáculos que permiten varios caminos
    tablero[0][1] = -1  # X = PARED
    tablero[1][1] = -1  # X = PARED  
    tablero[2][3] = -1  # X = PARED
    return tablero

def mostrar_todas_soluciones(soluciones):  # función que muestra TODAS las soluciones
    if not soluciones:
        print("No hay solución.")
        return

    print(f"Hay {len(soluciones)} soluciones:\n")
    for i, sol in enumerate(soluciones, 1):
        print(f"solución {i}")
        mostrar_laberinto(sol)

#SE EJECUTA
print("LABERINTO")
tablero = crear_laberinto()  # crea el laberinto 

print("X = PARED, 0 = camino libre:")
mostrar_laberinto(tablero)

# primero todas las soluciones
todas_soluciones = []
resolver_todas_soluciones(tablero, 0, 0, 1, todas_soluciones)

# Mostrar todas las soluciones encontradas
mostrar_todas_soluciones(todas_soluciones)

#encontrar la mas corta
mejor_solucion, mejor_longitud = encontrar_mejor_solucion(todas_soluciones)

if mejor_solucion:
    print("MEJOR SOLUCIÓN:")
    print(f"solucion de {mejor_longitud} pasos")
    mostrar_laberinto(mejor_solucion)
else:
    print("No hay solución.")