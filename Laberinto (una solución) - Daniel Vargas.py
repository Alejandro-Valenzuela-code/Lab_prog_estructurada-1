import random,math

def valida(tablero,candidato,x,y):
    posx = [0,1,0,-1]
    posy = [1,0,-1,0]
    nx = x+posx [candidato-1]
    ny = y+posy [candidato-1]
    #print("\n valores x, y", x,y," nuevo nx, ny",nx,ny)
    #input("Enter para continuar")
    if (nx < 0 or nx >= MAX):
        return False
    if (ny < 0 or ny >= MAX):
        return False
    if (tablero[nx][ny]== 0):
        return True
    else:
        return False
    
def siguiente_posicion(tablero,candidato,x,y):
    posx = [0,1,0,-1]
    posy = [1,0,-1,0]
    nx = x+posx [candidato-1]
    ny = y+posy [candidato-1]
    return nx,ny

def final(tablero,nx,ny):
    if (nx == MAX -1 and ny == MAX -1):
        return True
    return False

def buscar_xy(tablero, contador):
    for i in range(MAX):
        for j in range(MAX):
            if(tablero[i][j]== contador):
                return i,j
            
def solucion(tablero):
    candidato = 1 ; solucion = False ; x = 0; y = 0; contador = 1
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[x][y] = contador
    while(candidato <= 4) and not solucion:
        if(valida(tablero, candidato, x, y)):
            #print("\n entre al valida")
            nx, ny = siguiente_posicion(tablero, candidato, x, y)
            tablero[nx][ny] = contador + 1
            #mostrar_tablero(tablero)
            if(final(tablero,nx,ny)):
                candidato = candidato + 1
                solucion = True
                while(candidato == 5 and not (x==0 and y==0)):
                    tablero[x][y] = 0
                    contador -=1
                    nx, ny = buscar_xy(tablero, contador)
                    candidato = tablero_aux[nx][ny] +1
                    tablero_aux[nx][ny] = 0
                    x =nx; y=ny
                    mostrar_tablero(tablero)
                    solucion = True
            else:
                tablero_aux[x][y] = candidato; x = nx; y = ny; contador = contador + 1
                candidato=1
        else:
            candidato = candidato+1
            while(candidato == 5 and not (x==0 and y==0)):
                tablero[x][y] = 0
                contador -=1
                nx, ny = buscar_xy(tablero, contador)
                candidato = tablero_aux[nx][ny] +1
                tablero_aux[nx][ny] = 0
                x =nx; y=ny
                #mostrar_tablero(tablero)
    return solucion

def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(f'{tablero[i][j]:2}', end = " ")
        print("")
    print("")

# La cantidad de obstáculos depende del tamaño del tablero, basándose en una fórmula. La fórmula consiste en que el 25% de las
# casillas serán obstáculos, replazándose por el emoji de un cuadrado mediano negro (que en el terminal se ve blanco).
def colocar_obstaculos(tablero):
    numero=(MAX**2)*0.25
    cantidad_obstaculos=math.trunc(numero)
    for _ in range(cantidad_obstaculos):
        x=random.randint(0,MAX-1)
        y=random.randint(0,MAX-1)
        while x==y==0 or x==y==MAX-1 or tablero[x][y]!=0:
            x=random.randint(0,MAX-1)
            y=random.randint(0,MAX-1)
        tablero[x][y]=' \u25FC'
        

#================================================ De aquí parte el programa ===================================================

print('\n=================================================================================')
print('\nIngresa la medida del lado del tablero (si la medida es negativa, se tomará como positiva).')
while True:
    try:
        valor_max=abs(int(input('> ')))
        if valor_max!=0 and valor_max!=1:
            MAX=valor_max
            print('\nEl tablero tendrá este aspecto y estos obstáculos aleatorios:\n')
            tablero = [[0 for _ in range(MAX)] for _ in range(MAX)] # Crea el tablero
            colocar_obstaculos(tablero)
            mostrar_tablero(tablero)
            print('\n¿Confirmar acción?\n1 = SÍ\n2 = NO')
            while True:
                validacion1=input('> ')
                if validacion1=='1':
                    print('\n=================================================================================')
                    print('Medidas confirmadas')
                    print('=================================================================================\n')
                    terminar_while1=1
                    break
                else:
                    tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]
                    print('\n=================================================================================')
                    print('Medidas descartadas')
                    print('=================================================================================\n')
                    print('Ingresa nuevamente la medida')
                    terminar_while1=0
                    break
            if terminar_while1==1:
                break
        else:
            print('\nLas medidas no pueden ser 0 ni 1\nIngresa nuevamente la medida')
    except ValueError:
        print('\nIngresa una medida válida.')

if(solucion(tablero) == True):
    print("Esta es una solución:\n")
    mostrar_tablero(tablero)
    print('\n=================================================================================')
    print('PROGRAMA FINALIZADO.')
    print('=================================================================================')
else:
    print('\n=================================================================================')
    print('No hay una solución.')
    print('=================================================================================\n')