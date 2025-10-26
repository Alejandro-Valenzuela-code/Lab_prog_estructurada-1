
#se define la vartiable del rango que tendra el tablero
MAX = int(input("¿Cuántas casillas tendrá tu tablero? (ej: 4 para 4x4)\n"))

soluciones = []  #se crea una lista para guardar todas las soluciones posibles

#se define el modulo valida que muestra los movimientos que puede hacer el caballo
def valida(tablero, candidato, x, y):
    posx = [-2,-1,1,2,2,1,-1,-2]
    posy = [1,2,2,1,-1,-2,-2,-1]
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    if(nx<0 or nx>=MAX):
        return False
    if(ny<0 or ny>=MAX):
        return False
    if(tablero[nx][ny]!=0):
        return False
    return True

#se define el modulo siguiente posicion que verifica las siguientes posiciones posibles
def siguiente_posicion(tablero, candidato, x, y):
    posx = [-2,-1,1,2,2,1,-1,-2]
    posy = [1,2,2,1,-1,-2,-2,-1]
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    return nx, ny


#se define el modulo final que nos ayuda a saber cuando el tablero esta lleno y asi saber si existe una solucion
def final(tablero):
    for i in range(MAX):
        for j in range(MAX):
            if(tablero[i][j]==0):
                return False
    return True


#se define el modulo buscar
def buscar_xy(tablero, contador):
    for i in range(MAX):
        for j in range(MAX):
            if(tablero[i][j]==contador):
                return i,j


#se define el modulo para mostrar el tablero en la terminal de python
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(tablero[i][j], end = " ")
        print("")
    print("")


def copiar_tablero(tablero):
    return [fila[:] for fila in tablero]


#se define el modulo solucion para encontrar las soluciones posibles en las dimensiones del tablero
def solucion(tablero):
    candidato = 1
    x = 0
    y = 0
    contador = 1
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[x][y] = contador

    while(True):
        if(valida(tablero, candidato, x, y)):
            nx, ny = siguiente_posicion(tablero, candidato, x, y)
            tablero[nx][ny] = contador + 1
            
            if(final(tablero)):
                soluciones.append(copiar_tablero(tablero))# se agrega el tablero a la lista de soluciones creada al principio
                tablero[nx][ny] = 0  # vuelve a la posicion 0 para volver a buscar mas soluciones
            else:
                tablero_aux[x][y] = candidato
                x = nx
                y = ny
                contador += 1
                candidato = 1
                continue  

        candidato += 1
        
        # se define que si se probaron todos los movimientos, vuelve a antes de los movimientos
        while(candidato == 9 and not (x == 0 and y == 0)):
            tablero[x][y] = 0
            contador -= 1
            nx, ny = buscar_xy(tablero, contador)
            candidato = tablero_aux[nx][ny] + 1
            tablero_aux[nx][ny] = 0
            x = nx
            y = ny
        if(x == 0 and y == 0 and candidato == 9):
            break

    return len(soluciones) > 0


#programa principal
print("bienvenido a las soluciones del caballo\n")
input("si quieres ver las soluciones presiona enter...\n")
print("esto puede tardar unos segundos/minutos (dependiendo de que tamaño de tablero elegiste)\n")

tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]
solucion(tablero)

if len(soluciones) == 0:
    print("No hay soluciones para este tablero.")
else:
    print("Soluciones encontradas:\n")
    for numero in soluciones:
        mostrar_tablero(numero)
    print("se encontraron ", len(soluciones),"soluciones")

