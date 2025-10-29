### Caballo 1 solucion ###

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


# ---------------- FUNCIONES SOLUCION ---------------- #
# buscar la primera solucion
def solucion_unica(candidato, tablero, contador, x, y, MAX):
    if final(tablero, MAX):
        return True
    
    while candidato <= 8:
        if valida(tablero, candidato, x, y, MAX):
            xsiguiente, ysiguiente = siguiente_posicion(candidato, x, y)
            contador += 1
            tablero[xsiguiente][ysiguiente] = contador
            if solucion_unica(1, tablero, contador, xsiguiente, ysiguiente, MAX):  # va a proseguir con la siguiente posición hasta llegar al final
                return True  # si encuentra el final, devuelve True
            
            # si no encuentra el final, se devuelve
            tablero[xsiguiente][ysiguiente] = 0  # borra el ultimo movimiento
            contador -= 1
        candidato += 1  # prueba el siguiente candidato

    return False


# verifica si debe buscar una solucion o todas las soluciones
def encontrar_solucion(tablero, contador, candidato, MAX, x, y, xsiguiente, ysiguiente, soluciones, camino):
    if solucion_unica(candidato, tablero, contador, x, y, MAX):
        print("Solución encontrada:\n")
        mostrar_tablero(tablero, MAX)
    else:
        print("No hay solución.")


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