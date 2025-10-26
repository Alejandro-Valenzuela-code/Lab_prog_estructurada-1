def es_valido(x, y, tablero, n):
    """Verifica si la posición (x, y) está dentro del tablero y no ha sido visitada."""
    return 0 <= x < n and 0 <= y < n and tablero[x][y] == -1


def resolver_caballo(x, y, movi, tablero, mov_x, mov_y, n):
    """Usa backtracking para encontrar una solución al recorrido del caballo."""
    if movi == n * n:
        return True

    for i in range(8):
        sig_x = x + mov_x[i]
        sig_y = y + mov_y[i]
        if es_valido(sig_x, sig_y, tablero, n):
            tablero[sig_x][sig_y] = movi
            if resolver_caballo(sig_x, sig_y, movi + 1, tablero, mov_x, mov_y, n):
                return True
            tablero[sig_x][sig_y] = -1  # retrocede
    return False


def imprimir_tablero(tablero):
    """Imprime el tablero de forma ordenada."""
    for fila in tablero:
        linea = ""
        for celda in fila:
            linea += str(celda).rjust(2) + " "
        print(linea)
    print("")


"""--- Programa principal ---"""

n = int(input("Ingrese el tamaño del tablero (n x n): "))

tablero = [[-1 for _ in range(n)] for _ in range(n)]

mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
mov_y = [1, 2, 2, 1, -1, -2, -2, -1]

tablero[0][0] = 0

if resolver_caballo(0, 0, 1, tablero, mov_x, mov_y, n):
    print("")
    print("Solución encontrada:")
    imprimir_tablero(tablero)
else:
    print("")
    print("No existe solución para este tamaño de tablero.")
