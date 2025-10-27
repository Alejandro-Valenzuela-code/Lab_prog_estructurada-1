# Problema del recorrido del caballo (todas las soluciones)

N = 5  # Tamaño del tablero 

# Movimientos posibles del caballo (8 direcciones)
MOV_X = [2, 1, -1, -2, -2, -1, 1, 2]
MOV_Y = [1, 2, 2, 1, -1, -2, -2, -1]

import os 

def es_valido(tablero, x, y):
    # Verifica si la posición (x, y) está dentro del tablero y libre
    # Y además si no ha sido visitada (valor = -1)
    return 0 <= x < N and 0 <= y < N and tablero[x][y] == -1


def mostrar_tablero(tablero):
    # Muestra el tablero en formato de forma ordenada y legible
    for fila in tablero:
        print(" | ".join(f"{c:2d}" for c in fila))
    print()


def posibles_movimientos(tablero, x, y):
    # Devuelve la lista de movimientos válidos que puede hacer el caballo desde la posición (x, y)
    moves = []
    for i in range(8):
        nx, ny = x + MOV_X[i], y + MOV_Y[i]
        if es_valido(tablero, nx, ny):
            moves.append((nx, ny))
    return moves


def todas_las_soluciones(tablero, x, y, paso, soluciones):
    #Usa backtracking para encontrar todas las formas posibles de recorrer el tablero
    if paso == N * N:
        # Se guarda una copia del tablero actual
        soluciones.append([fila[:] for fila in tablero])
        #mostrar_tablero(tablero)
        return
    # Probar los 8 posibles movimientos
    for i in range(8):
        nx, ny = x + MOV_X[i], y + MOV_Y[i]
        if es_valido(tablero, nx, ny):
            tablero[nx][ny] = paso
            todas_las_soluciones(tablero, nx, ny, paso + 1, soluciones)
            tablero[nx][ny] = -1


# Ejecución del programa
os.system ("cls")
# Se crea el tablero inicial lleno de -1 (casillas sin visitar)
tablero = [[-1 for _ in range(N)] for _ in range(N)]
inicio_x, inicio_y = 0, 0  # Posición inicial del caballo
tablero[inicio_x][inicio_y] = 0
print("=============================================")
print ("RECORRIDO DEL CABALLO, TODAS LAS SOLUCIONES")
print("=============================================")
print(f"Buscando recorrido del caballo en un tablero de {N}x{N}...\n")

soluciones = []
tablero[inicio_x][inicio_y] = 0
todas_las_soluciones(tablero, inicio_x, inicio_y, 1, soluciones)
print(f"Se encontraron {len(soluciones)} soluciones.")
resp= input ("Desea imprimir las soluciones (Si/No)")
if resp.upper()=="SI":

    for i in range(len(soluciones)):
        print ("Tablero "+str(i))
        mostrar_tablero(soluciones[i])
        input ("Presione Enter para continuar")         

