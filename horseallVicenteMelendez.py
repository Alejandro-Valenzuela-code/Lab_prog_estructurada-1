movimientos = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def es_valido(x, y, visitado):
    return 0 <= x < 5 and 0 <= y < 5 and (x, y) not in visitado

def a_casilla(x, y):
    columnas = ['A','B','C','D','E']
    return f"{columnas[y]}{x+1}"

# Guarda las soluciones encontradas
soluciones = []

def recorrer(x, y, paso, visitado):
    if len(soluciones) >= 3:  # Detener después de 3 soluciones
        return
    if paso == 25:
        camino = [a_casilla(px, py) for px, py in visitado + [(x, y)]]
        soluciones.append(camino)
        return
    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        if es_valido(nx, ny, visitado):
            recorrer(nx, ny, paso + 1, visitado + [(nx, ny)])

# Empieza desde A1
recorrer(0, 0, 1, [(0, 0)])

print(f"Se encontraron {len(soluciones)} soluciones.\n")
for i, s in enumerate(soluciones, start=1):
    print(f"Solución {i}:")
    print(s)
    print()