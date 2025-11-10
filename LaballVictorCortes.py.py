'''
def solucion(laberinto):
    while(hay caminos disponibles):
        if(celda válida y no visitada):
            avanzar (marcar paso)
            if(final: llegó a la meta):
                guardar solucion actual
            else:
                seguir explorando desde nueva posición
        else:
            siguiente dirección
        while(no hay caminos y no inicio):
            retroceder (desmarcar paso anterior y continuar)
'''

import random

def generar_laberinto_con_ruta(n):
    lab = [[1 for _ in range(n)] for _ in range(n)]
    x, y = 0, 0
    lab[x][y] = 0
    while (x, y) != (n-1, n-1):
        mov = random.choice([(1,0), (0,1)])  # genera camino válido
        nx, ny = x + mov[0], y + mov[1]
        if 0 <= nx < n and 0 <= ny < n:
            lab[nx][ny] = 0
            x, y = nx, ny
    for i in range(n):
        for j in range(n):
            if lab[i][j] != 0:
                lab[i][j] = random.choice([0,1])
    return lab

def mostrar(lab, sol=None):
    for i in range(len(lab)):
        for j in range(len(lab)):
            if sol and sol[i][j] == 1:
                print("*", end=" ")
            elif lab[i][j] == 1:
                print("█", end=" ")
            else:
                print("·", end=" ")
        print()
    print()

def buscar_todas(lab, x, y, sol, todas):
    n = len(lab)
    if x == n - 1 and y == n - 1:
        sol[x][y] = 1
        todas.append([fila[:] for fila in sol])
        sol[x][y] = 0
        return
    if 0 <= x < n and 0 <= y < n and lab[x][y] == 0 and sol[x][y] == 0:
        sol[x][y] = 1
        buscar_todas(lab, x + 1, y, sol, todas)
        buscar_todas(lab, x - 1, y, sol, todas)
        buscar_todas(lab, x, y + 1, sol, todas)
        buscar_todas(lab, x, y - 1, sol, todas)
        sol[x][y] = 0

n = 6
lab = generar_laberinto_con_ruta(n)
print(" Laberinto generado (con al menos una ruta):")
mostrar(lab)
todas = []
buscar_todas(lab, 0, 0, [[0]*n for _ in range(n)], todas)

print(f" Se encontraron {len(todas)} soluciones:")
mostrar(lab, todas[0])  # muestra la primera
