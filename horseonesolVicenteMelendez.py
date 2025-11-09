# Movimientos posibles del caballo (en L)
movimientos = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

# Función para verificar si un movimiento es válido
def es_valido(x, y, visitado):
    return 0 <= x < 8 and 0 <= y < 8 and (x, y) not in visitado

# Convierte coordenadas (x, y) a formato tipo "A1", "C3", etc.
def a_casilla(x, y):
    columnas = ['A','B','C','D','E','F','G','H']
    return f"{columnas[y]}{x+1}"

# Función recursiva que intenta recorrer el tablero
def recorrer(x, y, paso, visitado):
    if paso == 64:  # 64 casillas del tablero
        return [a_casilla(x, y)]
    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        if es_valido(nx, ny, visitado):
            resultado = recorrer(nx, ny, paso + 1, visitado + [(nx, ny)])
            if resultado:
                return [a_casilla(x, y)] + resultado
    return None

# Inicia el recorrido desde A1 (esquina inferior izquierda)
camino = recorrer(0, 0, 1, [(0, 0)])

print("Recorrido del caballo (una posible solución):")
if camino:
    print(camino)
else:
    print("No se encontró solución.")