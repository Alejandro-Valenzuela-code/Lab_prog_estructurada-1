Movimientos = [ (2, 1), (1, 2), (-1, 2), (-2, 1),(-2, -1), (-1, -2), (1, -2), (2, -1)] # establece los movimientos en L del caballo

def Es_valido(x, y, visitado): # ayuda a saber si un moviminto es valido
    return 0 <= x < 8 and 0 <= y < 8 and (x, y) not in visitado

def A_casilla(x, y): # hace que las coordenadas sean las casilla del tablero de ajedrez
    columnas = ['A','B','C','D','E','F','G','H']
    return f"{columnas[y]}{x+1}"


def Recorrer(x, y, Paso, visitado): # hace el recorrido del caballo en el tablero hasta completarlo
    if Paso == 64: 
        return [A_casilla(x, y)]
    for dx, dy in Movimientos:
        nx, ny = x + dx, y + dy # representa las distancias entre las casillas del tablero por movimiento
        if Es_valido(nx, ny, visitado):
            resultado = Recorrer(nx, ny, Paso + 1, visitado + [(nx, ny)])
            if resultado:
                return [A_casilla(x, y)] + resultado
    return None

camino = Recorrer(0, 0, 1, [(0, 0)]) # empieza el recorrido desde la casilla A1

print("Recorrido del caballo: ") # muestra el recorrido hecho por el caballo
if camino:
    print(camino)
else:
    print("No se encontró solución.")