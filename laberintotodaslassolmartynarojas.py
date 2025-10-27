#LABERINTO TODAS LAS SOLUCIONES 

MAX = 4 

def mostrar_laberinto(tablero):  # función para mostrar el laberinto
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == 0:
                print(".", end=" ")  # camino libre
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

def copiar_laberinto(tablero):  # función para copiar el laberinto actual
    return [fila[:] for fila in tablero]

def resolver_todas_soluciones(tablero, x, y, paso, soluciones):  # función que busca todos los caminos posibles
    if x == MAX - 1 and y == MAX - 1:  # si llega a la meta
        tablero[x][y] = paso
        soluciones.append(copiar_laberinto(tablero))  # guarda el camino encontrado
        tablero[x][y] = 0  # limpia para seguir buscando otros
        return

    if valida(tablero, x, y):  # si la posición es válida
        tablero[x][y] = paso  # marca el paso actual

        # prueba moverse en las 4 direcciones posibles
        resolver_todas_soluciones(tablero, x + 1, y, paso + 1, soluciones)  # abajo
        resolver_todas_soluciones(tablero, x, y + 1, paso + 1, soluciones)  # derecha
        resolver_todas_soluciones(tablero, x - 1, y, paso + 1, soluciones)  # arriba
        resolver_todas_soluciones(tablero, x, y - 1, paso + 1, soluciones)  # izquierda

        tablero[x][y] = 0  # limpia la casilla antes de probar otro camino

def crear_laberinto():  # función que crea el laberinto con paredes
    tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[0][1] = -1  # X = PARED
    tablero[1][3] = -1  # X = PARED
    tablero[2][1] = -1  # X = PARED
    return tablero

def mostrar_todas_soluciones(soluciones):  # función que muestra todas las soluciones encontradas
    if not soluciones:
        print("No hay solucion.")
        return

    print(f"Hay {len(soluciones)} soluciones:\n")
    for i, sol in enumerate(soluciones, 1):
        print(f"solución {i}")
        mostrar_laberinto(sol)

#SE EJECUTA
print("LABERINTO")
tablero = crear_laberinto()  # crea el laberinto base

print("X = PARED:")
mostrar_laberinto(tablero)

todas_soluciones = []  # lista donde se guardarán los caminos encontrados

resolver_todas_soluciones(tablero, 0, 0, 1, todas_soluciones)  # busca todos los caminos posibles

mostrar_todas_soluciones(todas_soluciones)  # muestra los resultados