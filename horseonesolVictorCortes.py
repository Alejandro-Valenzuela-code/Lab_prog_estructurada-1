"""
def solucion(tablero):
    while(hay candidatos y no solucion):
        ordenar candidatos por menor grado (heurística de Warnsdorff)
        if(candidato válido):
            avanza (marcar paso k y mover (x,y))
            if(final: k == N*N):
                solucion = True
            else:
                dejo pistas (continuar desde nueva celda)
        else:
            siguiente candidato
        while(no hay candidatos y not inicio):
            retroceder (desmarcar paso k-1 y probar otro)
"""

from typing import List, Tuple, Optional

# Movimientos posibles del caballo
movidas = [
    (-2, +1), (-1, +2), (+1, +2), (+2, +1),
    (+2, -1), (+1, -2), (-1, -2), (-2, -1),
]

def dentro(n: int, x: int, y: int) -> bool:
    return 0 <= x < n and 0 <= y < n

def imprimir_tablero(tablero: List[List[int]]):
    n = len(tablero)
    ancho = len(str(n*n))
    for fila in tablero:
        print(" ".join(f"{c:>{ancho}}" for c in fila))
    print()

def vecinos_no_visitados(n, x, y, visitado):
    vecinos = []
    for dx, dy in movidas:
        nx, ny = x + dx, y + dy
        if dentro(n, nx, ny) and not visitado[nx][ny]:
            vecinos.append((nx, ny))
    return vecinos

def warnsdorff_orden(n, x, y, visitado):
    vecinos = vecinos_no_visitados(n, x, y, visitado)
    def grado(celda):
        cx, cy = celda
        return len(vecinos_no_visitados(n, cx, cy, visitado))
    vecinos.sort(key=grado)
    return vecinos

def una_solucion_knight_tour(n: int, inicio: Tuple[int, int]=(0, 0)) -> Optional[List[List[int]]]:
    x0, y0 = inicio
    tablero = [[0]*n for _ in range(n)]
    visitado = [[False]*n for _ in range(n)]

    def bt(k, x, y):
        tablero[x][y] = k
        visitado[x][y] = True
        if k == n*n:
            return True
        for nx, ny in warnsdorff_orden(n, x, y, visitado):
            if bt(k+1, nx, ny):
                return True
        tablero[x][y] = 0
        visitado[x][y] = False
        return False

    if bt(1, x0, y0):
        return tablero
    else:
        return None

# Ejemplo
if __name__ == "__main__":
    N = 12
    inicio = (0, 0)
    sol = una_solucion_knight_tour(N, inicio)
    if sol:
        print(f"=== Una solución del recorrido del caballo en un tablero {N}x{N} ===")
        imprimir_tablero(sol)
    else:
        print("No se encontró solución.")
