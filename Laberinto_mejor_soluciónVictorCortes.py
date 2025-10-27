'''
def solucion(laberinto):
    inicializar cola con (posición inicial, camino)
    while(cola no vacía y no solucion):
        tomar primer elemento (posición actual y ruta)
        if(llegó a la meta):
            guardar ruta como mejor solucion
        else:
            explorar vecinos válidos
            añadirlos a la cola con la nueva ruta
    al final, devolver el camino más corto
'''

import random
from collections import deque

def generar_laberinto_con_ruta(n):
    lab = [[1 for _ in range(n)] for _ in range(n)]
    x, y = 0, 0
    lab[x][y] = 0
    while (x, y) != (n-1, n-1):
        mov = random.choice([(1,0), (0,1)])
        nx, ny = x + mov[0], y + mov[1]
        if 0 <= nx < n and 0 <= ny < n:
            lab[nx][ny] = 0
            x, y = nx, ny
    for i in range(n):
        for j in range(n):
            if lab[i][j] != 0:
                lab[i][j] = random.choice([0,1])
    return lab

def mostrar(lab, camino=None):
    n = len(lab)
    for i in range(n):
        for j in range(n):
            if camino and (i, j) in camino:
                print("*", end=" ")
            elif lab[i][j] == 1:
                print("█", end=" ")
            else:
                print("·", end=" ")
        print()
    print()

def mejor_solucion(lab):
    n = len(lab)
    movs = [(1,0),(-1,0),(0,1),(0,-1)]
    cola = deque([((0,0), [(0,0)])])
    visitado = set()

    while cola:
        (x, y), camino = cola.popleft()
        if (x, y) == (n-1, n-1):
            return camino
        for dx, dy in movs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and lab[nx][ny] == 0 and (nx,ny) not in visitado:
                visitado.add((nx,ny))
                cola.append(((nx,ny), camino + [(nx,ny)]))
    return None

n = 6
lab = generar_laberinto_con_ruta(n)
print(" Laberinto generado (siempre con solución):")
mostrar(lab)
camino = mejor_solucion(lab)
print(" Mejor solución (más corta):")
mostrar(lab, camino)
