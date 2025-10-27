"""
'''def todas_las_soluciones(tablero):
    while(hay candidatos y no final):
        if(candidato válido):
            avanza (marcar paso)
            if(final: k == N*N):
                guardar solución
            else:
                dejo pistas (seguir explorando)
        else:
            siguiente candidato
        while(no hay candidatos y not inicio):
            retroceder
"""

from typing import List, Tuple, Callable, Optional

movidas = [
    (-2, +1), (-1, +2), (+1, +2), (+2, +1),
    (+2, -1), (+1, -2), (-1, -2), (-2, -1),
]

def dentro(n, x, y):
    return 0 <= x < n and 0 <= y < n

def imprimir_tablero(tablero):
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

def todas_las_soluciones_knight_tour(
    n: int,
    inicio: Tuple[int, int]=(0, 0),
    on_solution: Optional[Callable[[List[List[int]]], None]] = None
) -> int:
    x0, y0 = inicio
    tablero = [[0]*n for _ in range(n)]
    visitado = [[False]*n for _ in range(n)]
    total = 0

    def bt(k, x, y):
        nonlocal total
        tablero[x][y] = k
        visitado[x][y] = True
        if k == n*n:
            total += 1
            if on_solution:
                copia = [fila[:] for fila in tablero]
                on_solution(copia)
        else:
            for nx, ny in vecinos_no_visitados(n, x, y, visitado):
                bt(k+1, nx, ny)
        tablero[x][y] = 0
        visitado[x][y] = False

    bt(1, x0, y0)
    return total

if __name__ == "__main__":
    N = 5
    inicio = (0, 0)
    print(f"=== Buscando todas las soluciones en un tablero {N}x{N} ===")
    total = todas_las_soluciones_knight_tour(N, inicio, on_solution=imprimir_tablero)
    print(f"Total de soluciones completas encontradas: {total}")
