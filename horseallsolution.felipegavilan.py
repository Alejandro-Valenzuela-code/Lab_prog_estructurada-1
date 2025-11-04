# backtracking del caballo de ajedrez


MAX = int(input('Ingrese el tamaño de su tablero: '))  # Esta variable nos modifica el tamaño del tablero 


def valida(tablero, candidato, x, y):
    # Verifica que la posición alcanzada desde x,y con el candidato está dentro del tablero y vacía
    posx = [-2,-1,1,2,2,1,-1,-2] #los movimientos del caballo en x
    posy = [1,2,2,1,-1,-2,-2,-1] #los movimientos del caballo en y
    nx = x + posx[candidato - 1] #nueva posicion del caballo en x
    ny = y + posy[candidato - 1] #nueva posicion del caballo en y
    if nx < 0 or nx >= MAX:
        return False
    if ny < 0 or ny >= MAX:
        return False
    if tablero[nx][ny] != 0:
        return False
    return True


# Se crea la siguiente posición del caballo
def siguiente_posicion(tablero, candidato, x, y):
    # Devuelve la posición nx, ny alcanzada desde x,y con el candidato 
    posx = [-2,-1,1,2,2,1,-1,-2] #los movimientos del caballo en x
    posy = [1,2,2,1,-1,-2,-2,-1] #los movimientos del caballo en y
    nx = x + posx[candidato - 1] #nueva posicion del caballo en x
    ny = y + posy[candidato - 1] #nueva posicion del caballo en y
    return nx, ny


# Verifica si el tablero está completo (todas las casillas visitadas)
def final(tablero):
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == 0:
                return False
    return True


# Módulo que busca las soluciones posibles
def solucion(tablero, x, y, contador, soluciones, ver_proceso=False):
    if final(tablero):
        # se guarda copiando la solucion encontrada
        solucion_encontrada = [fila[:] for fila in tablero]
        soluciones.append(solucion_encontrada) #permite escribirlo como lista
        if ver_proceso:
            print("Solucion encontrada:")
            mostrar_tablero(tablero)
        return


    # Intentar los 8 posibles movimientos del caballo
    for candidato in range(1, 9):
        if valida(tablero, candidato, x, y):
            nx, ny = siguiente_posicion(tablero, candidato, x, y)
            tablero[nx][ny] = contador + 1

            if ver_proceso:
                mostrar_tablero(tablero)

            # Llamada recursiva
            solucion(tablero, nx, ny, contador + 1, soluciones, ver_proceso)

            tablero[nx][ny] = 0


# Esta función muestra el tablero actual
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(f"{tablero[i][j]:2}", end=" ")
        print("")
    print("")

#Panel que interactua con el usuario

ver_proceso = input('¿Quieres ver el proceso? Elija Si = 1 o No = 2: ').strip()
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]
soluciones = []  # Lista que guardará todas las soluciones

# Posición inicial del caballo
x, y = 0, 0
tablero[x][y] = 1

if ver_proceso == '1':
    solucion(tablero, x, y, 1, soluciones, ver_proceso=True)
else:
    solucion(tablero, x, y, 1, soluciones, ver_proceso=False)


# Nos muestra las soluciones finales
if soluciones:
    print(f"\n Se encontraron {len(soluciones)} soluciones en total\n")
    for i, sol in enumerate(soluciones, start=1):#Enumera cada solucion encontrada para poder diferenciarlas
        print(f"Solución {i}")
        mostrar_tablero(sol)
else:
    print("\n No hay soluciones posibles")
