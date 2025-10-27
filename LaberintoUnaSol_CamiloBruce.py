#modulo valida
def valida(tablero,candidato,x,y):
    posx = [0,1,0,-1]
    posy = [1,0,-1,0]
    nx = x+posx [candidato-1]
    ny = y+posy [candidato-1]
    if (nx < 0 or nx >= n):
        return False
    if (ny < 0 or ny >= n):
        return False
    if (tablero[nx][ny]== 0):
        return True
    else:
        return False
    
#modulo siguiente_posicion 
def siguiente_posicion(tablero,candidato,x,y):
    posx = [0,1,0,-1]
    posy = [1,0,-1,0]
    nx = x+posx [candidato-1]
    ny = y+posy [candidato-1]
    return nx,ny

#modulo final
def final(tablero,nx,ny):
    if (nx == n -1 and ny == n -1):
        return True
    return False
            
#modulo solucion
def solucion(tablero, x, y, contador):
    if final(tablero, x, y):
        return True
    
    for candidato in range(1,5):
        if valida(tablero, candidato, x, y):
            nx, ny = siguiente_posicion(tablero, candidato, x, y)
            tablero[nx][ny]= contador +1

            if solucion(tablero, nx, ny, contador + 1):
                return True
            tablero[nx][ny]=0
    return False

#modulo mostrar tablero
def mostrar_tablero(tablero):
    for i in range(n):
        for j in range(n):
            print(tablero[i][j], end = " ")
        print("")
    print("")

#modulo colocar_obstaculo
def colocar_obstaculo(tablero):
    pass


#programa principal
n=int(input('Ingrese la medida de su tablero (n x n): '))
tablero = [[0 for _ in range(n)] for _ in range(n)]
colocar_obstaculo(tablero)
mostrar_tablero(tablero)
tablero[0][0]=1

if(solucion(tablero, 0, 0, 1)):
    print("Hay solucion")
    mostrar_tablero(tablero)
else:
    print('No hay solucion')