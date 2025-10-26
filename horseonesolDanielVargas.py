# Esta función depende de la variable "tablero". La letra "i" y "j" corresponden a las coordenadas de cada posición del tablero.
# Cada vez que genera una posición se pone un espacio vacío a la derecha, con tal de que los números no queden apretados.
# En la primera iteración dará la posición de la primera fila, luego sigue con la segunda, la tercera, y así sucesivamente.
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(f'{tablero[i][j]:2}', end = " ")
        print("")
    print("")

# Se pide las proporciones del tablero. Si la entrada no es un número entero, lanzará un mensaje de error. Luego de verificar la
# entrada, genera el tablero usando dos "for". El primer "for" genera una lista con solo 0, y la longitud de esta depende del
# valor MAX. El segundo "for" se encarga de guardar esa lista en otra lista. La cantidad de listas que se copien depende de MAX.
# Después se muestra el tablero con la función anterior y pregunta si confirmar las medidas. Para esto, se entra a un ciclo
# while. Si es '1' se devuelve el tablero (con sus medidas) y el número MAX, ya que se usan en varias funciones de este programa,
# y al hacer esto, todo el ciclo while termina, finalizando la función. En el caso contrario, rompe el ciclo while de
# confirmación y vuelve al inicio para pedir las medidas del tablero. 
def construccion_del_tablero():
    global MAX
    while True:
        try:
            valor_max=abs(int(input('> ')))
            if valor_max!=0 and valor_max!=1:
                MAX=valor_max
                print('\nEl tablero tendrá este aspecto:\n')
                tablero = [[0 for _ in range(MAX)] for _ in range(MAX)] # Crea el tablero
                mostrar_tablero(tablero)
                print('\n¿Confirmar acción?\n1 = SÍ\n2 = NO')
                while True:
                    validacion1=input('> ')
                    if validacion1=='1':
                        print('\n=================================================================================')
                        print('Medidas confirmadas')
                        print('=================================================================================')
                        return tablero,MAX
                    else:
                        print('\n=================================================================================')
                        print('Medidas descartadas')
                        print('=================================================================================\n')
                        print('Ingresa nuevamente la medida')
                        break
            else:
                print('\nEl tablero no puede medir 0 ni 1. Ingresa una medida válida.')
        except ValueError:
            print('\nIngresa una medida válida.') 

# Se pide las coordenadas en las que partirá el caballo. Los valores deben estar entre 0 y MAX-1, de lo contrario, están fuera
# del tablero. Se pide las coordenadas de partida X y Y, que son guardadas a parte para usarlas más tarde. Para poder usar estas
# coordenadas iniciales, se les asigna esos mismo valores a otras variables, con tal de que sean modificadas durante el proceso y
# se conserve el punto de partida. Luego de esto, se colocará un "1" en el tablero para indicar las coordenadas elegidas. Si
# el usuario confirma o lo descarta, el tablero vuelve a generarse para borrar ese "1" y que todo quede limpio, así se evita que
# al elegir otra posición, aparezcan dos "1" en el tablero. En el caso de la confirmación, se devuelve las coordenadas de partida
# y las coordenadas que van a ser modificadas, que de igual manera tienen los mismos valores que las de partida (solo al inicio).
def punto_de_partida():
    global actual_x,partida_x,actual_y,partida_y,tablero
    while True:
        print(f'\n¿En qué coordenadas quieres empezar?')
        print('*Primero se preguntará por la posición en X y luego en Y.')
        print(f'*La posición en X se lee de arriba hacia abajo (de 0 hasta {MAX-1})')
        print(f'*La posición en Y se lee de izquierda a derecha (de 0 hasta {MAX-1})')
        try:
            partida_x=int(input('Coordenada X > '))
            partida_y=int(input('Coordenada Y > '))
            actual_x=partida_x
            actual_y=partida_y
            if 0<=actual_x<=MAX-1 and 0<=actual_y<=MAX-1:
                tablero[actual_x][actual_y] = 1
                print('\nDonde está "1" partirá el caballo:\n')
                mostrar_tablero(tablero)
                print('\n¿Confirmar punto de partida?\n1 = SÍ\n2 = NO')
                while True:
                    validacion2=input('> ')
                    if validacion2=='1':
                        print('\n=================================================================================')
                        print('Casilla guardada')
                        print('=================================================================================')
                        tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]
                        return actual_x,partida_x,actual_y,partida_y
                    else:
                        print('\n=================================================================================')
                        print('Punto de partida descartado')
                        print('=================================================================================')
                        tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]
                        break
            else:
                print('\n=================================================================================')
                print('La posición no es válida. Ingresa nuevamente.')
                print('=================================================================================')
        except ValueError:
            print('\n=================================================================================')
            print('Entrada inválida. Ingresa nuevamente.')  
            print('=================================================================================')

# Se definen dos listas, todos los movimientos en "x" y en "y". A las coordenadas actuales se le suma el par de movimientos
# (los movimientos se eligen dependiendo del candidato). Verifica que la nueva posición (tomando de referencia la actual) no 
# se salga del tablero y que esté desocupada (con un 0).
def valida(tablero, candidato, actual_x, actual_y):
    movimiento_x = [-2,-1,1,2,2,1,-1,-2]
    movimiento_y = [1,2,2,1,-1,-2,-2,-1]
    nueva_x = actual_x + movimiento_x[candidato-1]
    nueva_y = actual_y + movimiento_y[candidato-1]
    if(nueva_x<0 or nueva_x>=MAX):
        return False
    if(nueva_y<0 or nueva_y>=MAX):
        return False
    if(tablero[nueva_x][nueva_y]!=0):
        return False
    return True

# Hace exactamente lo mismo que la función anterior, solo que ahora ya no se verifica nada (es decir, que ya no devuelve un valor
# booleano), sino que directamente se remplazan las variables "actual_x" y "actual_y" con un número, ya que el proceso de 
# verificación fue hecho con anterioridad.
def siguiente_posicion(tablero, candidato, actual_x,actual_y): 
    movimiento_x = [-2,-1,1,2,2,1,-1,-2]
    movimiento_y = [1,2,2,1,-1,-2,-2,-1]
    nueva_x = actual_x + movimiento_x[candidato - 1]
    nueva_y = actual_y + movimiento_y[candidato - 1]
    return nueva_x,nueva_y

# Verifica que todas la casillas estén ocupadas. Si hubiera una sola casilla con un 0, devolverá False y seguirá encontrando 
# la solución
def final(tablero):
    for i in range(MAX):
        for j in range(MAX):
            if(tablero[i][j]==0):
                return False
    return True

# Esta función se llama cuando no quedan candidatos disponibles. Lo que hace es encontrar las coordenadas del número "contador".
def buscar_coordenadas(tablero, contador):
    for i in range(MAX):
        for j in range(MAX):
            if(tablero[i][j]==contador):
                return i,j
            
# Se definen 5 variables iniciales y un tablero auxiliar. Se parte desde la posición (0,0) y se considera como el primer
# movimiento, que es almacenado en "contador". Mientras hayan candidatos y aún no se encuentre la solución, se intentará realizar
# cada movimiento del caballo. Si el movimiento es válido, las nuevas coordeanadas serán asignadas a la "x" y "y" actual, a esa
# posición se le asigna el segundo movimiento (porque al contador se le suma 1) y el tablero auxiliar guardará el candidato
# anterior (luego el candidato vuelve a ser 1 y el contador inicia como 2). Si no es válido, a "candidato" se le suma 1, y si no 
# hubieran más candidatos disponibles, entra al ciclo "while" para retroceder y buscar otra alternativa. Esto lo hace remplazando
# por un 0 donde estaba el último número, recuperanod las coordenadas del número anterior para ver el número del candidato que se 
# usó (ese candidato debería estar guardado en el tablero auxilar). Si el tablero no tiene solución, entonces nunca devolverá el
# valor True.
def solucion(tablero,mostrar_pasos,actual_x,actual_y,partida_x,partida_y):
    candidato = 1 ; solucion = False ; contador = 1
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[actual_x][actual_y] = contador
    while(candidato <= 8 and not solucion):
        if(valida(tablero, candidato, actual_x, actual_y)):
            nueva_x, nueva_y = siguiente_posicion(tablero, candidato, actual_x, actual_y)
            tablero[nueva_x][nueva_y] = contador + 1
            if mostrar_pasos==1:
             mostrar_tablero(tablero)
            else:
                pass
            if(final(tablero)):
                solucion = True
            else:
                tablero_aux[actual_x][actual_y] = candidato; actual_x = nueva_x; actual_y = nueva_y; contador = contador + 1
                candidato=1
        else:
            candidato = candidato+1 
            while(candidato == 9 and not (actual_x==partida_x and actual_y==partida_y)):
                tablero[actual_x][actual_y] = 0
                contador = contador - 1
                nueva_x, nueva_y = buscar_coordenadas(tablero, contador)
                candidato = tablero_aux[nueva_x][nueva_y] +1
                tablero_aux[nueva_x][nueva_y] = 0
                actual_x =nueva_x; actual_y=nueva_y
                if mostrar_pasos==1:
                    mostrar_tablero(tablero)
                else:
                    pass
    return solucion








#==============================================================================================================================
#================================================ De aquí parte el programa ===================================================
#==============================================================================================================================







print('\n=================================================================================')
print('\nIngresa la medida del lado del tablero (si son negativas, solo se considerará el número)')

tablero,MAX=construccion_del_tablero()

actual_x,partida_x,actual_y,partida_y=punto_de_partida()

# Se pregunta si mostrar cada paso reflejado en el tablero u omitirlos         
print('\n¿Mostrar el paso a paso o la solución directa?\n1 = PASO A PASO\n2 = SOLO SOLUCIÓN ') 
accion=input('> ')
while accion!='1' and accion!='2':
      print('\nIngresa una opción válida.')
      accion=input('> ')      
if accion=='1':
    mostrar_pasos=1
else:
    mostrar_pasos=0   
    
# En el caso de que el tablero sea grande, se muestra un mensaje para indicar que el programa está funcionando de fondo.    
if MAX>=5 and accion=='2':
    print('\nEspere un momento. Se está tratando de encontrar la solución... ')
    print('*En caso de cancelar la búsqueda, presione Ctrl+C')

# El caballo inicia los movimientos
if(solucion(tablero,mostrar_pasos,actual_x,actual_y,partida_x,partida_y) == True):
    print('=================================================================================')
    print("Esta es la solución:\n")
    mostrar_tablero(tablero)
else:
    print('=================================================================================')
    print('No se encontró una solución\n')