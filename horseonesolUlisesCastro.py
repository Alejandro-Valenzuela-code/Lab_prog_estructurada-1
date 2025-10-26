#tamaño del tablero
N = 5
MOVIMIENTOS = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]
def es_seguro(tablero, x, y):
#Verifica si la casilla (x, y) está dentro del tablero y no ha sido visitada.
    return (x >= 0 and x < N and
            y >= 0 and y < N and
            tablero[x][y] == 0)

def imprimir_solucion(tablero):
    #Imprime el tablero con el orden de visita.
    print(f"¡Solución encontrada para un tablero {N}x{N}!")
    for fila in tablero:
        print(' '.join(f'{celda:2d}' for celda in fila))
    print("-" * (N * 3))
def resolver_recorrido_caballo_util(tablero, x, y, contador_pasos):
    # 1. Caso base de éxito: Se visitaron todas las casillas (N*N)
    if contador_pasos == N * N + 1:
        return True
    #Explorar los 8 movimientos posibles
    for i in range(8):
        siguiente_x = x + MOVIMIENTOS[i][0]
        siguiente_y = y + MOVIMIENTOS[i][1]
        #Verificar si el movimiento es seguro/válido
        if es_seguro(tablero, siguiente_x, siguiente_y):
            tablero[siguiente_x][siguiente_y] = contador_pasos
            #Llamada recursiva: Intentar resolver desde la nueva posición
            if resolver_recorrido_caballo_util(tablero, siguiente_x, siguiente_y, contador_pasos + 1):
                return True
            tablero[siguiente_x][siguiente_y] = 0
    return False

def resolver_recorrido_caballo():
    #Inicializa el tablero y comienza el proceso de búsqueda.
    tablero = [[0 for _ in range(N)] for _ in range(N)]
    pos_inicial_x, pos_inicial_y = 0, 0
    tablero[pos_inicial_x][pos_inicial_y] = 1
    print(f"Iniciando la búsqueda del recorrido del caballo en {N}x{N}...")
    print(f"Posición inicial: ({pos_inicial_x}, {pos_inicial_y})\n")
    if not resolver_recorrido_caballo_util(tablero, pos_inicial_x, pos_inicial_y, 2):
        print(f"No se encontró ninguna solución comenzando en ({pos_inicial_x}, {pos_inicial_y}).")
    else:
        imprimir_solucion(tablero)
# Ejecutar el programa
if __name__ == "__main__":
    resolver_recorrido_caballo()