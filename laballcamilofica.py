def imprimir_laberinto(lab):
    
    for fila in lab:          # recorre cada fila
        for celda in fila:    # recorre cada elemento dentro de esa fila
            print(celda, end=" ")  
        print()  
    print()
    print()

# Laberinto
laberinto = [
    ['S', 0,    0,    0,    0],
    ["x", 0,   "x",    0,   "x"],
    [0,   0,    0,     0,    0],
    [0,  "x",  "x",   "x",   0],
    [0,   0,    0,   'E',   0]
]

movs = [(-1,0), (1,0), (0,-1), (0,1)]

def buscar_inicio(lab): #con esto encomtramos nuestro inicio por donde partir
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if lab[i][j] == 'S':
                return i, j

# Función para copiar el laberinto 
def copiar_laberinto(lab):
    nuevo = []
    for fila in lab:
        nuevo.append(fila[:])  # [:] hace una copia de la fila
    return nuevo

# Backtracking para encontrar todas las rutas
def encontrar_todos(lab, x, y, paso, soluciones):
    if lab[x][y] == 'E':
        copia = copiar_laberinto(lab)  # hacemos copia 
        soluciones.append(copia)
        return

    if lab[x][y] == 0 or lab[x][y] == 'S':
        pista = lab[x][y]  # guarda lo que había antes (S o 0)
        lab[x][y] = paso  # marca el paso actual

        for dx, dy in movs: #nuevamente vamos probando movimientos
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(lab) and 0 <= ny < len(lab[0]):
                if lab[nx][ny] == 0 or lab[nx][ny] == 'E':
                    encontrar_todos(lab, nx, ny, paso + 1, soluciones)

        lab[x][y] = pista  #con esto volvemos para atras

#  Ejecución 
inicio = buscar_inicio(laberinto)
soluciones = [] #aqui guardaremos las soluciones
encontrar_todos(laberinto, inicio[0], inicio[1], 1, soluciones)

print(f" Total de soluciones encontradas: {len(soluciones)}\n")

for i, sol in enumerate(soluciones, 1): # el enumerate nos permite recibir un valor numerico de posicion apartir del y tambien nos devuelve el valor de esa pocision, en este caso seria la matriz guardada
    print(f"Solución {i}:")
    imprimir_laberinto(sol)