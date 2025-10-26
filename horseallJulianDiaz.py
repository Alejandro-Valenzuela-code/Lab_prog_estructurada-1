def es_valido(x, y, tablero, n):
    """Verifica si la posición (x, y) está dentro del tablero y no ha sido visitada."""
    return 0 <= x < n and 0 <= y < n and tablero[x][y] == -1


def resolver_todas(x, y, movi, tablero, mov_x, mov_y, n, soluciones):
    """Usa backtracking para encontrar TODAS las soluciones posibles."""
    if movi == n * n:
        copia = []
        for fila in tablero:
            copia.append(fila[:])
        soluciones.append(copia)
        return

    for i in range(8):
        sig_x = x + mov_x[i]
        sig_y = y + mov_y[i]
        if es_valido(sig_x, sig_y, tablero, n):
            tablero[sig_x][sig_y] = movi
            resolver_todas(sig_x, sig_y, movi + 1, tablero, mov_x, mov_y, n, soluciones)
            tablero[sig_x][sig_y] = -1


def imprimir_tablero(tablero):
    """Imprime un tablero de forma ordenada."""
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
soluciones = []

resolver_todas(0, 0, 1, tablero, mov_x, mov_y, n, soluciones)

if len(soluciones) > 0:
    print("")
    print("Se encontraron", len(soluciones), "soluciones.\n")
    contador = 1
    for sol in soluciones:
        print("Solución número", contador, ":")
        imprimir_tablero(sol)
        contador += 1
else:
    print("")
    print("No existen soluciones para este tamaño de tablero.")
