import random,math,copy

soluciones=[]
pasos_totales=[]
mejores_soluciones=[]

def valida(tablero,candidato,x,y):
    posx = [0,1,0,-1]
    posy = [1,0,-1,0]
    nx = x+posx [candidato-1]
    ny = y+posy [candidato-1]
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

# Cada vez que se encuentra un solución, se guarda ese tablero un una lista y su contador en otra. Esto se hace para que luego
# ambas listas se mezclen como tuplas y a un tablero le corresponda su cantidad máxima de pasos.
def armando_listas(tablero,contador):
    global soluciones,pasos
    pasos=contador+1
    soluciones.append(copy.deepcopy(tablero))
    pasos_totales.append(copy.deepcopy(pasos))
            
def solucion(tablero):
    global cantidad_soluciones
    candidato = 1 ; solucion = False ; x = 0; y = 0; contador = 1 ; cantidad_soluciones = 0
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[x][y] = contador
    while(candidato <= 4):
        if(valida(tablero, candidato, x, y)):
            nx, ny = siguiente_posicion(tablero, candidato, x, y)
            tablero[nx][ny] = contador + 1
            if(final(tablero,nx,ny)):
                cantidad_soluciones+=1
                armando_listas(tablero,contador)
                tablero[nx][ny] = 0
                candidato = candidato + 1
                while(candidato == 5 and not (x==0 and y==0)):
                    tablero[x][y] = 0
                    contador -=1
                    nx, ny = buscar_xy(tablero, contador)
                    candidato = tablero_aux[nx][ny] +1
                    tablero_aux[nx][ny] = 0
                    x =nx; y=ny
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
    cantidad_obstaculos=math.trunc(numero) # Quita los decimales para que sea un entero
    for _ in range(cantidad_obstaculos):
        x=random.randint(0,MAX-1)
        y=random.randint(0,MAX-1)
        while x==y==0 or x==y==MAX-1 or tablero[x][y]!=0:
            x=random.randint(0,MAX-1)
            y=random.randint(0,MAX-1)
        tablero[x][y]=' X'
        

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
                    print('=================================================================================')
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
        print('Ingresa una medida válida.')

if(solucion(tablero) == True):
    print("Hay solucion")
    mostrar_tablero(tablero)
else:
    print('\n=================================================================================')
    print('No hay más soluciones.\n')

if cantidad_soluciones>0:
    solucion_y_pasos=list(zip(*[soluciones,pasos_totales]))   
    mejores_pasos=min(pasos_totales)
    mejores_soluciones=[(sol, pasos) for sol,pasos in solucion_y_pasos if pasos==mejores_pasos]
    print('¿Deseas guardar las mejores soluciones en un archivo?\n1 = SÍ\n2 = NO')
    while True:
        validacion3=input('> ')
        if validacion3=='1':
            print('¿Cómo quieres que se llame el archivo? (recordar añadir ".txt" al final)')
            nombre_del_archivo=input('> ')
            with open(nombre_del_archivo, "w", encoding="utf-8") as archivo:
                for sol, pasos in mejores_soluciones:
                    archivo.write('\n'.join([' '.join([str(c) for c in fila]) for fila in sol]))
                    archivo.write("\n\n")
            print('\n=================================================================================')
            print('Archivo creado. PROGRAMA FINALIZADO.')
            print('=================================================================================')
            break
        elif validacion3=='2':
            print('\n=================================================================================')
            print('No se ha creado el archivo. PROGRAMA FINALIZADO.')
            print('=================================================================================')
            break
        else:
            print('\nIngresa una opción válida.')
else:
    print('PROGRAMA FINALIZADO.')
    print('=================================================================================')