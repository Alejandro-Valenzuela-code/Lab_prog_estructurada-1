
#se define la vartiable del rango que tendra el tablero
MAX = int(input("cuantas casillas tendra tu tablero ? (ej: 4 (4x4))\n"))

#se define el modulo valida que muestra los movimientos que puede hacer el caballo
def valida(tablero, candidato, x, y):
    #verifica que la posicion alcanzada desde x,y con el candidato está dentro del tablero y vacía
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


def siguiente_posicion(tablero, candidato, x,y):
    #devuelve la posicion nx,ny alcanzada desde x,y con el candidato 
    posx = [-2,-1,1,2,2,1,-1,-2]
    posy = [1,2,2,1,-1,-2,-2,-1]
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    return nx,ny


def final(tablero):
    for i in range(MAX):
        for j in range(MAX):
            if(tablero[i][j]==0):
                return False
    return True


def buscar_xy(tablero, contador):
    for i in range(MAX):
        for j in range(MAX):
            if(tablero[i][j]==contador):
                return i,j

#se define el modulo solucion para encontrar las soluciones posibles en las dimensiones del tablero
def solucion(tablero):
    candidato = 1 ; solucion = False ; x = 0; y = 0; contador = 1
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[x][y] = contador
    while(candidato <= 8 and not solucion):
        if(valida(tablero, candidato, x, y)):
            nx, ny = siguiente_posicion(tablero, candidato, x, y)
            tablero[nx][ny] = contador + 1
            #mostrar_tablero(tablero)
            if(final(tablero)):
                solucion = True
            else:
                tablero_aux[x][y] = candidato; x = nx; y = ny; contador = contador + 1
                candidato=1
        else:
            candidato = candidato+1 
            while(candidato == 9 and not (x==0 and y==0)):
                tablero[x][y] = 0
                contador = contador - 1
                nx, ny = buscar_xy(tablero, contador)
                candidato = tablero_aux[nx][ny] +1
                tablero_aux[nx][ny] = 0
                x =nx; y=ny
                #
                #mostrar_tablero(tablero)
    return solucion


def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(tablero[i][j], end = " ")
        print("")
    print("")


#programa principal

print("bienvenido a las soluciones del caballo\n")

tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]
print("el tablero es de",MAX,"por",MAX,) #crea tablero
mostrar_tablero(tablero)
input("si quieres ver una solucion presiona enter...\n")
if(solucion(tablero) == True):
    print("esta es una solucion\n")
    mostrar_tablero(tablero)
else:
    print('no hay solucion\n')
