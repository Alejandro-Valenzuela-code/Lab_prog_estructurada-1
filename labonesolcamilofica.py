def imprimir_laberinto(lab):
    
    for fila in lab:          # recorre cada fila
        for celda in fila:    # recorre cada elemento dentro de esa fila
            print(celda, end=" ")  
        print()  


# Laberinto base   las x significa que esta bloqueado el camino
laberinto = [
    ['S', 0,   "x",    0,    0],
    ["x", 0,   "x",    0,   "x"],
    [0,   0,    0,     0,    0],
    [0,  "x",  "x",   "x",   0],
    [0,   0,   "x",   'E',   0]
]

movs = [(-1,0), (1,0), (0,-1), (0,1)] #movimientos disponibles para moverse

def buscar_inicio(lab): #esto permite buscar el inicio del laberinto
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if lab[i][j] == 'S':
                return i, j

def encontrar_uno(lab, x, y, paso): # este te dice si estas en la casilla de la salida
    if lab[x][y] == 'E':
        return True

    # Marca el paso si es libre o inicio
    if lab[x][y] == 0 or lab[x][y] == 'S':
        lab[x][y] = paso

        for dx, dy in movs: #vamos probando todos los movimientos posibles
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(lab) and 0 <= ny < len(lab[0]):
                if lab[nx][ny] == 0 or lab[nx][ny] == 'E':
                    if encontrar_uno(lab, nx, ny, paso + 1):
                        return True

        # Backtracking
        if lab[x][y] != 'S':
            lab[x][y] = 0

    return False

# Ejecución 
inicio = buscar_inicio(laberinto)
if encontrar_uno(laberinto, inicio[0], inicio[1], 1):
    print("Camino encontrado:")
else:
    print("No hay camino.")
imprimir_laberinto(laberinto)