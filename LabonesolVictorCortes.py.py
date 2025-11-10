"""
def solucion(laberinto):
    while(hay caminos posibles y no solucion):
        elegir dirección (derecha, abajo, izquierda, arriba)
        if(celda válida y libre):
            avanzar (marcar paso como parte del camino)
            if(llegó a la meta):
                solucion = True
            else:
                seguir buscando desde nueva posición
        else:
            probar otra dirección
        while(no hay más caminos y no inicio):
            retroceder (desmarcar paso anterior y buscar otra ruta)
"""

import random

def generar_laberinto_con_ruta(n):
    lab = [[1 for _ in range(n)] for _ in range(n)]
    x, y = 0, 0
    lab[x][y] = 0
    while (x, y) != (n-1, n-1):
        mov = random.choice([(1,0), (0,1)])  # solo abajo o derecha
        nx, ny = x + mov[0], y + mov[1]
        if 0 <= nx < n and 0 <= ny < n:
            lab[nx][ny] = 0
            x, y = nx, ny
    # llenar el resto al azar sin bloquear la ruta
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

def resolver_una_solucion(lab, x, y, sol):
    n = len(lab)
    if x == n - 1 and y == n - 1:
        sol[x][y] = 1
        return True
    if 0 <= x < n and 0 <= y < n and lab[x][y] == 0:
        sol[x][y] = 1
        lab[x][y] = 2
        if resolver_una_solucion(lab, x + 1, y, sol): return True
        if resolver_una_solucion(lab, x, y + 1, sol): return True
        if resolver_una_solucion(lab, x - 1, y, sol): return True
        if resolver_una_solucion(lab, x, y - 1, sol): return True
        sol[x][y] = 0
    return False

n = 6
lab = generar_laberinto_con_ruta(n)
print(" Laberinto generado (siempre con solución):")
mostrar(lab)
sol = [[0]*n for _ in range(n)]
resolver_una_solucion(lab, 0, 0, sol)
print(" Solución encontrada:")
mostrar(lab, sol)
