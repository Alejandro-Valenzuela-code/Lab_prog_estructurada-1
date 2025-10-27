# Pseudocódigo.
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
MAX = int(input("Ingrese el número de fila y columnas que desea (Será un tablero cuadrado, tendrá la misma cantida de filas y de columnas):  \n> "))

while True:
    print("""
|===========Traza del caballo===========|
     1.- Quiero ver la traza.
     2.- Quiero solo la solución.
     3.- Salir.
|=======================================|
 """)
    seleccion = int(input("Ingrese la opción que desea usar:  \n> "))
    if seleccion in (1, 2):
        break
    else:
        print("Error, opción invalida.")

# Función validación.
def valida(tablero, candidato, x, y):
    #Verifica si la posición alcanzada desde x, y con el candidato este dentro del tablero y se encuentre vacía.
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

# Función para la siguiente posición
def siguiente_posicion(tablero, candidato, x,y):
    # Devuelve la posicion nx, ny alcanzada desde x, y con el candidato.
    posx = [-2,-1,1,2,2,1,-1,-2]
    posy = [1,2,2,1,-1,-2,-2,-1]
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    return nx, ny

# Función final
def final(tablero):
    for i in range(MAX):
        for j in range(MAX):
            if(tablero[i][j]==0):
                return False
    return True
#Funcion para buscar x, y.
def buscar_xy(tablero, contador):
    for i in range(MAX):
        for j in range(MAX):
            if(tablero[i][j]==contador):
                return i, j
            
# Función para la solución.
def solucion(tablero):
    candidato = 1 ; solucion = False ; x = 0; y = 0; contador = 1
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[x][y] = contador
    while(candidato <= 8 and not solucion):
        if(valida(tablero, candidato, x, y)):
            nx, ny = siguiente_posicion(tablero, candidato, x, y)
            tablero[nx][ny] = contador + 1
            if seleccion == 1:
                mostrar_tablero(tablero)
            if(final(tablero)):
                solucion = True
            else:
                tablero_aux[x][y] = candidato; x = nx; y = ny; contador = contador + 1
                candidato = 1
        else:
            candidato += 1 
            while(candidato == 9 and not (x==0 and y==0)):
                tablero[x][y] = 0
                contador -= 1
                nx, ny = buscar_xy(tablero, contador)
                candidato = tablero_aux[nx][ny] + 1
                tablero_aux[nx][ny] = 0
                x = nx; y = ny
                if seleccion == 1:
                    mostrar_tablero(tablero)
    return solucion

#Función que muestra el tablero
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(tablero[i][j], end = " ")
        print("")
    print("")

### Main ###
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)] # Crea el tablero
if solucion == 1:
    mostrar_tablero(tablero)
if(solucion(tablero) == True):
    print("\nHay al menos 1 solución posible. \n")
    mostrar_tablero(tablero)
else:
    print("\nNo hay una solución posible. \n")