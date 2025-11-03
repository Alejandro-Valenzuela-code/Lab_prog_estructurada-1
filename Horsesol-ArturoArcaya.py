MAX = 8

movimientos = [(2, 1), (1, 2), (-1, 2), (-2, 1),(-2, -1), (-1, -2), (1, -2), (2, -1)]
#movimiento del caballo

def validacion(x,y, tablero):
    return 0 <= x < MAX and 0 <= y < MAX and tablero[x][y] == -1
#comprueba que el movimiento no salga del casillero

def solucion(x,y,tablero,movimiento):
    if movimiento == MAX*MAX: #comprueba si el tablero esta lleno
        return True
    for ax, ay in movimientos: #utiliza los movimientos del caballo
        sx , sy = x+ax , y+ay #mueve al caballo
        if validacion(sx,sy, tablero): 
            tablero[sx][sy] = movimiento #si la validacion es correcta le otorga el numero de movimiento a la casilla
            if solucion(sx,sy, tablero, movimiento + 1): #comprueba las demas casillas desde una nueva posicion
                return True
            tablero[sx][sy] = -1 #regresa si no encontro solucion
    return False


#-inicio-
tablero= [[-1 for _ in range(MAX)]for _ in range(MAX)] #genera tablero
tablero[0][0] = 0 #posiciona al caballo en 0,0
if solucion(0, 0, tablero, 1): #empieza el juego
    for i in tablero: #inicia si hay solucion
        print(' '.join(f'{aux:2}' for aux in i)) #imprime el tablero solucionado con una separacion, en esta caso de 2
else:
    print('No hay solucion')