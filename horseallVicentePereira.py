MAX = 5
#modulo solucion
'''def solucion(tablero):
    while(hay candidtos y no solucion):
        if(valida):
            avanza
            if(final):
                solucion = True
            else:
                dejo pistas
        else:
            siguiente candidato
            while(no hay candidatos y not inicio):
                retroceder
'''
#modulo valida
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
#modulo siguiente_posicion
def siguiente_posicion(tablero, candidato, x,y):
    #devuelve la posicion nx,ny alcanzada desde x,y con el candidato 
    posx = [-2,-1,1,2,2,1,-1,-2]
    posy = [1,2,2,1,-1,-2,-2,-1]
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    return nx,ny
#modulo final
def final(tablero):
    for i in range(MAX):
        for j in range(MAX):
            if(tablero[i][j]==0):
                return False
    return True
#modulo buscar xy
def buscar_xy(tablero, contador):
    for i in range(MAX):
        for j in range(MAX):
            if(tablero[i][j]==contador):
                return i,j
#modulo solucion
def soluciones_todas(tablero):
    candidato = 1
    x = 0; y = 0; contador = 1
    
    # soluciones encontradas
    contador_soluciones = 0 
    
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[x][y] = contador
    
    # el bucle se detiene cuando retrocede hasta el inicio y el candidato es 9
    while(candidato <= 8):
        
        if(valida(tablero, candidato, x, y)):
            # avanza
            nx, ny = siguiente_posicion(tablero, candidato, x, y)
            tablero[nx][ny] = contador + 1
            
            if(final(tablero)):
                contador_soluciones = contador_soluciones + 1
                print("solucion numero " + str(contador_soluciones))
                mostrar_tablero(tablero)
                
                #se furza el retroceso
                tablero[nx][ny] = 0
                #que pruebe el siguente candidato
                candidato = candidato + 1
            
            else:
                # avance normal
                tablero_aux[x][y] = candidato; x = nx; y = ny; contador = contador + 1
                candidato=1
        else:
            # camino bloqueado 
            candidato = candidato + 1 
            
            # bucle de retroceso
            while(candidato == 9 and not (x==0 and y==0)):
                tablero[x][y] = 0
                contador = contador - 1
                nx, ny = buscar_xy(tablero, contador)
                candidato = tablero_aux[nx][ny] + 1
                tablero_aux[nx][ny] = 0
                x =nx; y=ny
                
    return contador_soluciones
#cada vez que encuentre solucion, mostrara el tablero y en donde hay solucion.

#modulo mostrar tablero
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(tablero[i][j], end = " ")
        print("")
    print("") 
#programa principal
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)] #crea tablero
if(soluciones_todas(tablero) == True):
    print("hay solucion")
else:
    print('no hay solucion')