#Backtracking del caballo ajedrez

MAX =int(input('Ingrese el tamaño de su tablero :'))#Esta variable nos modifica el tamaño del tablreo 

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

#Se crea la siguinete posision del caballo
def siguiente_posicion(tablero, candidato, x,y):

    #devuelve la posicion nx,ny alcanzada desde x,y con el candidato 
    posx = [-2,-1,1,2,2,1,-1,-2]
    posy = [1,2,2,1,-1,-2,-2,-1]
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    return nx,ny
#Tablero final
def final(tablero):
    for i in range(MAX):
        for j in range(MAX):
            if(tablero[i][j]==0):
                return False
    return True

def solucion(tablero, x, y,contador, ver_proceso=False):
   if final(tablero):
       return True
   for candidato in range (1,9):
       if valida(tablero, candidato, x, y):
           nx,ny = siguiente_posicion(tablero, candidato, x,y)
           tablero[nx][ny] =contador + 1
           if ver_proceso:
               mostrar_tablero(tablero)
           if solucion(tablero, nx,ny,contador +1, ver_proceso):
               return True
           tablero[nx][ny] = 0
   return False
#Esta funcion nos muestra el tablero
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(tablero[i][j], end = " ")
        print("")
    print("")

#Nos dice si tiene o no tiene solucion
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)] 
x, y =0,0
tablero[x][y] = 1
tiene_solucion = solucion(tablero, x, y, 1)

#Nos consulta si queremos ver el proceso 
ver_proceso = input('¿Quieres ver el proceso? Elija Si = 1 o No = 2: ').strip()

if ver_proceso == '1':
    tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[x][y] = 1
    tiene_solucion= solucion(tablero, x, y ,1, ver_proceso=True)

    if tiene_solucion:
        print('Hay solucion:')
        mostrar_tablero(tablero)
    else:
        print('No tiene solucion')
else:
    print('Gracias')