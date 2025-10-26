import copy

# Definición del tamaño del tablero
N = 5
MOVIMIENTOS = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

# Almacena todas las soluciones encontradas
SOLUCIONES_ENCONTRADAS = [] 

def es_seguro(tablero, x, y):
    return (x >= 0 and x < N and
            y >= 0 and y < N and
            tablero[x][y] == 0)

def resolver_recorrido_todas_util(tablero, x, y, contador_pasos):
    global SOLUCIONES_ENCONTRADAS
    if contador_pasos == N * N + 1:
        SOLUCIONES_ENCONTRADAS.append(copy.deepcopy(tablero))
        #Continuamos buscando otras rutas.
        return 
    #Explorar los 8 movimientos posibles
    for i in range(8):
        siguiente_x = x + MOVIMIENTOS[i][0]
        siguiente_y = y + MOVIMIENTOS[i][1]

        if es_seguro(tablero, siguiente_x, siguiente_y):
            tablero[siguiente_x][siguiente_y] = contador_pasos
            resolver_recorrido_todas_util(tablero, siguiente_x, siguiente_y, contador_pasos + 1)
            tablero[siguiente_x][siguiente_y] = 0
def imprimir_soluciones():
    global SOLUCIONES_ENCONTRADAS
    total = len(SOLUCIONES_ENCONTRADAS)
    print(f"\n--- Resumen de Búsqueda ({N}x{N}) ---")
    print(f"Se encontraron un total de {total} soluciones.")
    # Solo imprimir las primeras N soluciones para no saturar si hay muchas
    max_imprimir = min(total, 1) #cambiar el num para buscar las soluciones que necesite ver
    if max_imprimir > 0:
        print(f"Mostrando las primeras {max_imprimir} soluciones:")
        print("=" * 40)
        for i in range(max_imprimir):
            print(f"\nSolución #{i + 1}:")
            for fila in SOLUCIONES_ENCONTRADAS[i]:
                print(' '.join(f'{celda:2d}' for celda in fila))
            print("-" * (N * 3))
    elif total == 0:
        print("No se encontró ninguna solución para la posición inicial dada.")
def resolver_todas_las_soluciones():
    #Inicializa el tablero y comienza el proceso de búsqueda total.
    tablero = [[0 for _ in range(N)] for _ in range(N)]
    # Posición inicial del caballo.
    pos_inicial_x, pos_inicial_y = 0, 0
    tablero[pos_inicial_x][pos_inicial_y] = 1
    print(f"Iniciando la búsqueda de TODAS las soluciones posibles en {N}x{N}...")
    print(f"Posición inicial: ({pos_inicial_x}, {pos_inicial_y})")
    resolver_recorrido_todas_util(tablero, pos_inicial_x, pos_inicial_y, 2)
    # Imprimir los resultados
    imprimir_soluciones()
if __name__ == "__main__":
    resolver_todas_las_soluciones()