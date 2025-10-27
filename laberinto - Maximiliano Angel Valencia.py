import random

MAX = int(input("Ingrese el número de fila y columnas que desea (Será un tablero cuadrado, tendrá la misma cantida de filas y de columnas):  \n> "))
MAX2 = MAX - 1

todas_soluciones = []
soluciones_unicas = set()

def valida(tablero,candidato,x,y):
    posx = [0,1,0,-1]
    posy = [1,0,-1,0]
    nx = x+posx[candidato-1]
    ny = y+posy[candidato-1]
    if (nx < 0 or nx >= MAX):
        return False
    if (ny < 0 or ny >= MAX):
        return False
    if tablero[nx][ny] == 0:
        return True
    return False
    
def siguiente_posicion(candidato, x, y):
    posx = [0,1,0,-1]
    posy = [1,0,-1,0]
    nx = x + posx[candidato-1]
    ny = y + posy[candidato-1]
    return nx,ny

def final(nx, ny):
    return nx == MAX-1 and ny == MAX-1

def buscar_xy(tablero, contador):
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == contador:
                return i,j

def solucion(tablero):
    candidato = 1
    x = 0
    y = 0
    contador = 1
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[x][y] = contador

    while True:
        if candidato <= 4 and valida(tablero, candidato, x, y):
            nx, ny = siguiente_posicion(candidato, x, y)
            tablero[nx][ny] = contador + 1
            if seleccion == "1":
                mostrar_tablero(tablero)
            if final(nx, ny):
                sol_tupla = tuple(tuple(fila) for fila in tablero)
                if sol_tupla not in soluciones_unicas:
                    todas_soluciones.append(([fila[:] for fila in tablero], contador + 1))
                    soluciones_unicas.add(sol_tupla)
                if seleccion == "3":
                    mostrar_tablero(tablero)
                tablero[nx][ny] = 0
                candidato += 1
                continue
            else:
                tablero_aux[x][y] = candidato
                x, y = nx, ny
                contador += 1
                candidato = 1
                continue
        else:
            candidato += 1

        while candidato > 4:
            if x == 0 and y == 0:
                return
            tablero[x][y] = 0
            contador -= 1
            nx, ny = buscar_xy(tablero, contador)
            candidato = tablero_aux[nx][ny] + 1
            tablero_aux[nx][ny] = 0
            x, y = nx, ny
            if seleccion == "1":
                mostrar_tablero(tablero)
            if candidato <= 4:
                break

# Función para mostrar tablero
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            val = str(tablero[i][j])
            print(f"{val:>3}", end=" ")
        print("")
    print("")

def colocar_obstaculo(tablero):
    for _ in range((MAX*MAX)//3):
        rx = random.randint(0, MAX2)
        ry = random.randint(0, MAX2)
        # Evita poner obstáculo en inicio o final
        if (rx, ry) not in [(0, 0), (MAX2, MAX2)]:
            tablero[rx][ry] = "X"

### MAIN ###

tablero = [[0 for _ in range(MAX)] for _ in range(MAX)] # Creación del tablero
colocar_obstaculo(tablero)

while True:
    print("""
|==========Traza del movimiento==========|
    1.- Quiero ver la traza.
    2.- Quiero solo la solución.
    3.- Todas las soluciones
    4.- Mejor solución
    5.- Salir.
|========================================|
""")
    
    print("|==========Tablero generado==========|\n")
    mostrar_tablero(tablero)
    print("|====================================|")

    seleccion = input("Ingrese la opción que desea usar:  \n> ")

    if seleccion == "1":
        if solucion(tablero) is not None:
            print("\nHay al menos 1 solución posible. \n")
            mostrar_tablero(tablero)
        else:
            print("\nNo hay una solución posible. \n")

    elif seleccion == "2":
        if solucion(tablero) is not None:
            print("\nHay al menos 1 solución posible. \n")
            mostrar_tablero(tablero)
        else:
            print("\nNo hay una solución posible. \n")

    elif seleccion == "3":
        solucion(tablero)
        if todas_soluciones:
            with open("Soluciones posibles (Laberinto).txt", "w") as f:
                for i, sol in enumerate(todas_soluciones, 1):
                    f.write(f"Solución N°{i}: \n")
                    for fila in sol[0]:
                        f.write(" ".join(f"{'X' if n=='X' else n:>3}" for n in fila) + "\n")
                    f.write("\n")
            print(f"\nSe encontraron {len(todas_soluciones)} soluciones y se almacenaron en [Soluciones posibles (Laberinto).txt].\n")
        else:
            print("\nNo hay soluciones posibles.\n")

    elif seleccion == "4":
        solucion(tablero)
        if todas_soluciones:
            mejor_tablero, menor_movimientos = min(todas_soluciones, key=lambda s: s[1])
            print(f"\nLa mejor solución tiene {menor_movimientos} movimientos: \n")
            mostrar_tablero(mejor_tablero)
            with open("Mejor solución (Laberinto).txt", "w") as f:
                f.write(f"Mejor solución con {menor_movimientos} movimientos: \n\n")
                for fila in mejor_tablero:
                    f.write(" ".join(f"{'X' if n=='X' else n:>3}" for n in fila) + "\n")
            print(f"\nSe guardó en [Mejor solución (Laberinto).txt].\n")
        else:
            print("\nNo hay soluciones posibles.\n")

    elif seleccion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Error, opción invalida.")
