### Caballo ###

# ---------------- PREPARAR TABLERO ---------------- #
def crear_tablero(MAX):
    return [[0 for _ in range(MAX)] for _ in range(MAX)]


def mostrar_tablero(tablero, MAX):
    for i in range(MAX):
        for j in range(MAX):
            print(f"{tablero[i][j]:3}", end = " ")
        print("")
    print("")


# ---------------- ELEGIR PARÁMETROS ---------------- #
def elegir_dimensiones():
    while True:
        try:
            MAX = int(input("Introduzca la dimension para la matriz cuadrada (mayor que 2):\n>"))
        except ValueError:
            print("Error. Introduzca un número entero mayor que 2\n")
            continue
        if MAX <= 2:
            print("Error. Introduzca un número entero mayor que 2\n")
        else:
            return MAX


# ---------------- FUNCIONES POSICION ---------------- #
def valida(tablero, candidato, x, y, MAX):
    xdireccion = [1, 2, 2, 1, -1, -2, -2, -1]
    ydireccion = [2, 1, -1, -2, -2, -1, 1, 2]
    xsiguiente = x + xdireccion[candidato - 1]
    ysiguiente = y + ydireccion[candidato - 1]
    if xsiguiente < 0 or xsiguiente >= MAX:
        return False
    if ysiguiente < 0 or ysiguiente >= MAX:
        return False
    if tablero[xsiguiente][ysiguiente] == 0:
        return True
    else:
        return False


def siguiente_posicion(candidato, x, y):
    xdireccion = [1, 2, 2, 1, -1, -2, -2, -1]
    ydireccion = [2, 1, -1, -2, -2, -1, 1, 2]
    xsiguiente = x + xdireccion[candidato - 1]
    ysiguiente = y + ydireccion[candidato - 1]
    return xsiguiente, ysiguiente


def final(tablero, MAX):
    for i in range(MAX):
        for j in range(MAX):
            if(tablero[i][j] == 0):
                return False
    return True


def buscar_xy(tablero, contador, MAX):
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == contador:
                return i, j


# ---------------- FUNCIONES SOLUCION ---------------- #
# buscar todas las soluciones
def solucion_todas(candidato, tablero, contador, x, y, xsiguiente, ysiguiente, MAX, soluciones, camino):
    if final(tablero, MAX):
        soluciones.append(camino.copy())
        return
    
    while candidato <= 8:
        if valida(tablero, candidato, x, y, MAX):
            xsiguiente, ysiguiente = siguiente_posicion(candidato, x, y)
            contador += 1
            tablero[xsiguiente][ysiguiente] = contador
            camino.append((xsiguiente, ysiguiente))

            solucion_todas(1, tablero, contador, xsiguiente, ysiguiente, 0, 0, MAX, soluciones, camino)

            # retroceder
            camino.pop()
            tablero[xsiguiente][ysiguiente] = 0
            contador -= 1
        
        candidato += 1


# verifica si debe buscar una solucion o todas las soluciones
def encontrar_solucion(tablero, contador, candidato, MAX, x, y, xsiguiente, ysiguiente, soluciones, camino):
    solucion_todas(candidato, tablero, contador, x, y, xsiguiente, ysiguiente, MAX, soluciones, camino)
    if soluciones:
        print(f"Se han encontrado {len(soluciones)} soluciones:")
        for i, sol in enumerate(soluciones, 1):
            print(f"\nsolucion {i}:")
            mostrar_soluciones_tablero(tablero, sol, MAX)
    else:
        print("No hay solución.")


# mostrar las soluciones como matrices
def mostrar_soluciones_tablero(tablero_original, camino, MAX):
    # crea una copia del tablero original
    tablero_aux = [fila.copy() for fila in tablero_original]

    for casilla, (x, y) in enumerate(camino, start=1):
        tablero_aux[x][y] = casilla

    mostrar_tablero(tablero_aux, MAX)


# ---------------- PROGRAMA PRINCIPAL ---------------- #
def main():
    soluciones = []
    candidato = 1
    contador = 1
    x = y = xsiguiente = ysiguiente = 0
    MAX = elegir_dimensiones()
    tablero = crear_tablero(MAX)
    mostrar_tablero(tablero, MAX)
    tablero[x][y] = 1
    encontrar_solucion(tablero, contador, candidato, MAX, x, y, xsiguiente, ysiguiente, soluciones, [(0, 0)])

main()