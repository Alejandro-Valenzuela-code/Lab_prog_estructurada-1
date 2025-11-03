Movimientos = [(2, 1), (1, 2), (-1, 2), (-2, 1),(-2, -1), (-1, -2), (1, -2), (2, -1)] # establece los movimientos en L del caballo

def Es_valido(x, y, visitado): # ayuda a saber si un movimiento es valido o no
    return 0 <= x < 8 and 0 <= y < 8 and (x, y) not in visitado

def A_casilla(x, y): # hace que las coordenadas sean las casillas del tablero de ajedrez
    columnas = ['A','B','C','D','E','F','G','H']
    return f"{columnas[y]}{x+1}"

soluciones = [] # Muestra las posibles soluciones

def recorrer(x, y, paso, visitado): # Hace el recorrido del caballo hasta terminar el tablero
    if len(soluciones) >= 3:  
        return
    if paso == 64:
        camino = [A_casilla(px, py) for px, py in visitado + [(x, y)]]
        soluciones.append(camino)
        return
    for dx, dy in Movimientos:
        nx, ny = x + dx, y + dy # representa la distancia entre las casillas del tablero por movimientos
        if Es_valido(nx, ny, visitado):
            recorrer(nx, ny, paso + 1, visitado + [(nx, ny)])

recorrer(0, 0, 1, [(0, 0)]) # muestra el inicio del caballo en la Casilla A1

print(f"Se encontraron {len(soluciones)} soluciones.\n") #Muestra 3 de las posibles soluciones
for i, s in enumerate(soluciones, start=1):
    print(f"Solución {i}:")
    print(s)
    print()