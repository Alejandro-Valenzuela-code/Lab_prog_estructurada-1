
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

def siguiente_posicion(tablero, candidato, actual_x,actual_y):
    #devuelve la posicion nx,ny alcanzada desde x,y con el candidato 
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
def buscar_xy(tablero, contador):
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
# por un 0 donde estaba el último número, recuperando las coordenadas del número anterior para ver el número del candidato que se 
# usó (ese candidato debería estar guardado en el tablero auxilar). Si el tablero no tiene solución, entonces nunca devolverá el
# valor True.
def solucion(tablero,mostrar_pasos):
    candidato = 1 ; solucion = False ; actual_x = 0; actual_y = 0; contador = 1
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
            while(candidato == 9 and not (actual_x==0 and actual_y==0)):
                tablero[actual_x][actual_y] = 0
                contador = contador - 1
                nueva_x, nueva_y = buscar_xy(tablero, contador)
                candidato = tablero_aux[nueva_x][nueva_y] +1
                tablero_aux[nueva_x][nueva_y] = 0
                actual_x =nueva_x; actual_y=nueva_y
                if mostrar_pasos==1:
                    mostrar_tablero(tablero)
                else:
                    pass
    return solucion

# Esta función depende de la variable "tablero". La letra "i" y "j" corresponden a las coordenadas de cada posición del tablero.
# Cada vez que genera una posición se pone un espacio vacío a la derecha, con tal de que los números no queden apretados.
# En la primera iteración dará la posición de la primera fila, luego sigue con la segunda, la tercera, y así sucesivamente.
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(tablero[i][j], end = " ")
        print("")
    print("")

#================================================ De aquí parte el programa ===================================================

print('\nIngresa la medida del lado del tablero')

# Se pregunta por las medidas del tablero
while True:
    try:
        valor_max=abs(int(input('> ')))
        MAX=valor_max
        print('\nEl tablero tendrá este aspecto:\n')
        tablero = [[0 for _ in range(MAX)] for _ in range(MAX)] # Crea el tablero
        mostrar_tablero(tablero)
        print('\n¿Confirmar acción?\n1 = SÍ\n2 = NO')
        while True:
            validacion=input('> ')
            if validacion=='1':
                print('\nMedidas confirmadas')
                print('=================================================================================')
                terminar_while=1
                break
            else:
                print('\nIngresa nuevamente la medida')
                terminar_while=0
                break
        if terminar_while==1:
            break
    except ValueError:
        print('Ingresa una medida válida.')  

# Se pregunta si mostrar cada paso reflejado en el tablero u omitirlos         
print('\n¿Mostrar el paso a paso o la solución directa?\n1 = PASO A PASO\n2 = SOLO SOLUCIÓN ') 
accion=input('> ')
while accion!='1' and accion!='2':
      print('Ingresa una opción válida.')
      accion=input('> ')      
if accion=='1':
    mostrar_pasos=1
else:
    mostrar_pasos=0   
# En el caso de que el tablero sea grande, se muestra un mensaje para indicar que el programa está funcionando de fondo.    
if MAX>=7 and accion=='2':
    print('\nEspere un momento. Se está tratando de encontrar la solución... \n')

#============================================= El caballo inicia los movimientos ==============================================

if(solucion(tablero,mostrar_pasos) == True):
    print('=================================================================================')
    print("Hay solución\n")
    mostrar_tablero(tablero)
else:
    print('=================================================================================')
    print('No se encontró una solución\n')
#falta definir 