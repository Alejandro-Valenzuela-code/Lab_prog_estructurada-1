import random

def crear_labe(n, prob_obstaculo=0.25):
    #-----crea un laberinto con obstáculos aleatorios-----
    lab = []
    for i in range(n):
        fila = []
        for j in range(n):
            if random.random() < prob_obstaculo:
                fila.append('|') # muro
            else:
                fila.append('-') # camino libre
        lab.append(fila)
    #----asegurar entrada y salida libres----
    lab[0][0] = 'I'
    lab[n-1][n-1] = 'F'
    return lab

#----imprimir laberinto----
def imp_lab(lab):
    for fila in lab:
        print(''.join(fila))
    print()

#----verifica si la celda(x,y) es válida para moverse----
def es_valido(lab, x, y):
    n = len(lab)
    return 0 <= x < n and 0 <= y < n and lab[x][y] in ('-','F')

#----usa backtracking para encontrar un camino desde I hasta F----
def res_lab(lab, x=0, y=0):
    if lab[x][y] == 'F':
        return True
#marca el camino
    if lab[x][y] == '-':
        lab[x][y] = '*'
    #----derecha, abajo, izquierda, arriba----
    movimientos = [(0,1),(1,0),(0,-1),(-1,0)]
    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        if es_valido(lab, nx, ny) and res_lab(lab, nx, ny):
            return True
    #----retroceder (backtrack)----
    if lab[x][y] not in ('I','F'):
        lab[x][y]= '-'
    return False

#-----Programa principal: mostrar 3 laberintos-----
n = int(input('tamaño del laberinto (ej: 5):'))

for i in range(1, 4):
    print(f'\n--- Laberinto {i} ---\n')
    lab = crear_labe(n)
    imp_lab(lab)
    
    if res_lab(lab):
        print('Se encontró un camino:\n')
    else:
        print('No hay camino posible\n')
    
    imp_lab(lab)