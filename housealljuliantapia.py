import time

# Numero de filas y columnas del tablero.
rango_tablero = 5 

# Función que crea el tablero se movera el caballo.
def tablero():
    tablero = [[0 for i in range (rango_tablero)] for j in range(rango_tablero)]
    return(tablero)

# Función que muestra el tablero en pantalla
def mostrar_tablero(tablero):
    print()
    for linea in tablero:
        print(linea)
    print()

# Función que guarda en una lista el conjunto de movimientos que puede efectuar el caballo en una coordenada especifica.
def conjunto_movimientos(tablero,coordenadas):
    x = coordenadas[0]
    y = coordenadas[1]
    mov_x = [-2,-1,1,2,2,1,-1,-2]
    mov_y = [1,2,2,1,-1,-2,-2,-1]
    movimientos_posibles = []
    for i in range(8):
        nueva_x = x+mov_x[i]
        nueva_y = y+mov_y[i]
        if (0<= nueva_x<rango_tablero and 0<=nueva_y<rango_tablero):
            if tablero[nueva_x][nueva_y] == 0:
                movimientos_posibles.append([nueva_x,nueva_y])
    return(movimientos_posibles)

# Función que retorna la coordenada/posición de una marca que se le indique.
def buscar_coordenada(tablero, marca):
    for fila in tablero:
        if marca in fila:
            return [tablero.index(fila),fila.index(marca)]

# Función para definir el punto de inicio del recorrido del caballo
def definir_comienzo():
    x = y = -1
    while not (0<= x <rango_tablero and 0<= y <rango_tablero):
        try:
            x = int(input(f'Componente x del inicio (de 0 a {rango_tablero-1}): '))
            y = int(input(f'Componente y del inicio (de 0 a {rango_tablero-1}): '))
            if not (0<= x <rango_tablero and 0<= y <rango_tablero):
                print('Datos fuera de intervalo')
        except ValueError:
            print('Dato no valido.')
    return [x,y]

# Función principal que determina si hay solución o no para el inicio ingresado.
def solucion(tablero,inicio):
    x,y = inicio ; marca = 1; solucion = False
    tablero[x][y] = 1
    coordenadas = inicio
    # El tablero auxiliar guarda el indice del siguiento movimiento en la lista de movimientos posibles en una posición determinada.
    tablero_aux = [[-1 for i in range(rango_tablero)] for j in range(rango_tablero)]
    
    # El ciclo continua mientras no haya solución o se borre la marca del inicio.
    while (not solucion and marca != 0):
        movimiento = conjunto_movimientos(tablero,coordenadas)
        c_x, c_y = coordenadas
        
        # Si no hay movimientos para la (c_x,c_y) o ya se probaron todos sus movimientos, retrocede.
        if movimiento == [] or tablero_aux[c_x][c_y] == len(movimiento)-1:
            tablero_aux[c_x][c_y] = -1
            tablero[c_x][c_y] = 0
            marca += -1
            print('retroceso')
            coordenadas = buscar_coordenada(tablero,marca)
            mostrar_tablero(tablero)
        else: # Siguiente posición.
            tablero_aux[c_x][c_y] += 1
            indice = tablero_aux[c_x][c_y]
            coordenadas = movimiento[indice]
            c_x,c_y = coordenadas
            marca += 1
            tablero[c_x][c_y] = marca
            mostrar_tablero(tablero)
            if marca == 25: # Si se llego a la ultima marca posible, hay solución.
                solucion = True

    return solucion

# Programa principal

tablero_real = tablero()
comienzo = definir_comienzo()

contador_inicio = time.perf_counter()

if solucion(tablero_real,comienzo):
    print('Tiene solución \n')
else:
    print(f'No hay solución para el inicio {tuple(comienzo)}. \n')

contador_fin = time.perf_counter()

print(f'Tiempo de ejecución: {contador_fin-contador_inicio}[s]')

# PD: No hay filtros para los caminos que toma el caballo, por lo que en algunas 
# posiciones puede tardar varios minutos en determinar la solución.