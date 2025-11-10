import random,math

# La cantidad de obstáculos depende del tamaño del tablero, basándose en una fórmula. La fórmula consiste en que el 25% de las
# casillas serán obstáculos, replazándose por el emoji de un cuadrado mediano negro (que en el terminal se ve blanco).
def colocar_obstaculos(tablero):
    
    numero=(MAX**2)*0.25
    
    cantidad_obstaculos=math.trunc(numero) # Se quitan los decimales.
    
    for _ in range(cantidad_obstaculos):
        
        # Se genera la posición en X y en Y para determinar la ubicación del obstáculo.
        actual_x=random.randint(0,MAX-1)
        actual_y=random.randint(0,MAX-1)
        
        # Si se quiere poner un obstáculo en el inicio, en el final o donde ya había un obstáculo, entonces se pide reubicarlo
        # hasta encontrar una casilla vacía.
        while actual_x==actual_y==0 or actual_x==actual_y==MAX-1 or tablero[actual_x][actual_y]!=0:
            actual_x=random.randint(0,MAX-1)
            actual_y=random.randint(0,MAX-1)
        
        # Si la ubicación del obstáculo es válida, entonces se colocará un emoji de un cuadrado negro en esa casilla.  
        tablero[actual_x][actual_y]=' \u25FC'

def mostrar_tablero(tablero):
    
    # Primero se arma fila por fila, luego a cada posición de la fila se le da un valor, siendo [0,1,2,3,4,...,MAX-1]. Cada 
    # casilla ocupará dos espacios, y al terminar de generarse, se pone un espacio vacío a su derecha, representado por " ".
    # El print hace que cada fila esté separada por párrafos, de lo contrario todas las filas estarán pegadas en una sola.
    for fila in range(MAX):
        for columna in range(MAX):
            print(f'{tablero[fila][columna]:2}', end=" ")
        print("")

# Regresa True o False
def validar_movimiento(tablero,opcion,actual_x,actual_y):
    
    # Son los movimientos posibles para moverse en el laberinto. Se iran considerando por par, es decir, la opción 1 es [0][1], 
    # luego la opción 2 es [1][0] y así.
    movimiento_x=[0,1,0,-1]
    movimiento_y=[1,0,-1,0]
    
    
    nueva_posicion_x=actual_x+movimiento_x[opcion-1]
    nueva_posicion_y=actual_y+movimiento_y[opcion-1]
    
    # Verifica que tanto en X como en Y no sea una coordenada negativa, mayor que la del tablero o que esté ocupada. Si en la 
    # posición hay un 0, se puede poner el siguiente número en esa casilla.
    if nueva_posicion_x<0 or nueva_posicion_x>=MAX:
        return False
    if nueva_posicion_y<0 or nueva_posicion_y>=MAX:
        return False
    if tablero[nueva_posicion_x][nueva_posicion_y]==0:
        return True
    else:
        return False

# Realiza lo mismo que la función anterior, solo que ahora los valores son asignados y reflejados en el tablero. 
def siguiente_posicion(tablero,opcion,actual_x,actual_y):
    
    movimiento_x=[0,1,0,-1]
    movimiento_y=[1,0,-1,0]
    
    nueva_posicion_x=actual_x+movimiento_x[opcion-1]
    nueva_posicion_y=actual_y+movimiento_y[opcion-1]
    
    return nueva_posicion_x,nueva_posicion_y

# Si la posición final fuese (MAX-1,MAX-1), entonces es el final de tablero, es decir, la esquina inferior derecha. Si no llega
# al final, entonces se seguirá intentando llegar a estas coordenadas.
def final(tablero,nueva_posicion_x,nueva_posicion_y):
    if (nueva_posicion_x==MAX-1 and nueva_posicion_y==MAX-1):
        return True
    return False

# Buscará posición por posición hasta encontrar las coordenadas del contador. De ser así, la función deja de ejecutarse.
def buscar_coordenadas_anteriores(tablero, contador):
    for fila in range(MAX):
        for columna in range(MAX):
            if tablero[fila][columna]==contador:
                return fila,columna
            
def solucion(tablero):
    
    # Se definen las variables iniciales para entrar al ciclo while
    global cantidad_soluciones
    cantidad_soluciones=0
    opcion=1
    actual_x=0 
    actual_y=0
    contador=1
    
    # Se crea otro tablero donde se guardará la opción usada en una determinada posición.
    tablero_de_opciones=[[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[actual_x][actual_y]=contador
    
    while opcion<=4:
        
        if validar_movimiento(tablero,opcion,actual_x,actual_y):
            nueva_posicion_x,nueva_posicion_y=siguiente_posicion(tablero,opcion,actual_x,actual_y)   # La función devuelve los valores de la nueva posición
            tablero[nueva_posicion_x][nueva_posicion_y]=contador+1  # Se coloca en el tablero el siguiente número.
            
            if final(tablero,nueva_posicion_x,nueva_posicion_y):
                cantidad_soluciones=cantidad_soluciones+1
                print('\n=================================================================================')
                print(f'\nSolución {cantidad_soluciones}')
                mostrar_tablero(tablero)
                input("\nPresione Enter para ver la siguiente solución")
                tablero[nueva_posicion_x][nueva_posicion_y]=0 # Borra el último paso de la solución
                opcion=opcion+1 # Toma la opción anterior y del paso anterior. El contador sigue siendo el anterior, no el actual.
                
                while (opcion==5 and not(actual_x==0 and actual_y==0)):
                    tablero[actual_x][actual_y]=0 # Borra la posición y la deja en 0.
                    contador=contador-1 # Regresa un paso atrás
                    nueva_posicion_x,nueva_posicion_y=buscar_coordenadas_anteriores(tablero,contador) # Devuelve las coordenadas del paso anterior.
                    opcion=tablero_de_opciones[nueva_posicion_x][nueva_posicion_y]+1 # Se intenta con la siguiente opción.
                    tablero_de_opciones[nueva_posicion_x][nueva_posicion_y]=0 # La casilla de opciones en esas coordenadas se deja como 0
                    actual_x=nueva_posicion_x 
                    actual_y=nueva_posicion_y
            else:
                # Si aún no hay solución, se coloca en el otro tablero (el que no se ve en el terminal) la posición ocupada en
                # la casilla anterior. Luego de eso, remplaza los valores actuales de X y Y por los nuevos.
                tablero_de_opciones[actual_x][actual_y]=opcion
                actual_x=nueva_posicion_x 
                actual_y=nueva_posicion_y 
                contador=contador+1
                opcion=1
        else:
            # Si la opción actual no es válida, sigue con la siguiente
            opcion=opcion+1
            
            # Si no sirve ninguna de las opciones y no se está en el inicio.
            while opcion==5 and not(actual_x==0 and actual_y==0):
                tablero[actual_x][actual_y]=0 # Se borra la posición actual del tablero
                contador=contador-1 # Se regresa al paso anterior
                nueva_posicion_x, nueva_posicion_y=buscar_coordenadas_anteriores(tablero, contador) # Da las coordeandas del paso anterior
                opcion=tablero_de_opciones[nueva_posicion_x][nueva_posicion_y]+1 # Se le suma 1 a la opción usada en el paso anterior
                
                # La opción en esa casilla se vuelve 0, con tal de que, en caso de tener que retroceder más adelante a este mismo
                # punto, se puedan reelgir las opciones desde 1 a 4 y probar otros caminos. El valor de opción no cambia con esto, sino
                # que mantiene el que obtuvo en la anterior línea de código. 
                tablero_de_opciones[nueva_posicion_x][nueva_posicion_y]=0 
                
                actual_x=nueva_posicion_x 
                actual_y=nueva_posicion_y          

def mostrar_tablero(tablero):
    
    # Primero se arma fila por fila, luego a cada posición de la fila se le da un valor, siendo [0,1,2,3,4,...,MAX-1]. Cada 
    # casilla ocupará dos espacios, y al terminar de generarse, se pone un espacio vacío a su derecha, representado por " ".
    # El print hace que cada fila esté separada por párrafos, de lo contrario todas las filas estarán pegadas en una sola.
    for fila in range(MAX):
        for columna in range(MAX):
            print(f'{tablero[fila][columna]:2}', end=" ")
        print("")
   
        

#================================================ De aquí parte el programa ===================================================

print('\n=================================================================================')
print('\nIngresa la medida del lado del tablero (si la medida es negativa, se tomará como positiva).')

# El ciclo while sirve para preguntar sobre las medidas del tablero.
while True:
    try:
        valor_max=abs(int(input('> ')))
        if valor_max!=0 and valor_max!=1:
            
            MAX=valor_max
            print('\nEl tablero tendrá este aspecto y estos obstáculos aleatorios:\n')
            # El 1er for crea una lista de ceros, y luego esa lista se va a repetir MAX veces. Esto crea el tablero.
            tablero=[[0 for _ in range(MAX)] for _ in range(MAX)] 
            
            colocar_obstaculos(tablero)
            
            mostrar_tablero(tablero)
            
            print('\n¿Confirmar acción?\n1 = SÍ\n2 = NO')
            while True:
                validacion1=input('> ')
                if validacion1=='1':
                    print('\n=================================================================================')
                    print('\nMedidas confirmadas')
                    terminar_while1=1
                    break
                else:
                    # Se limpia el tablero para borrar el 1 y se genera otra vez.
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

solucion(tablero)

print('\n=================================================================================')
print('No hay más soluciones.\n')
print('PROGRAMA FINALIZADO.')
print('=================================================================================')