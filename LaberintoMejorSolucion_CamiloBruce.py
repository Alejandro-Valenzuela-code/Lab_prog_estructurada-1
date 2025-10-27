
mejor_sol=None
mejor_cont= 0
#modulo valida
def valida(tablero,candidato,x,y):
    posx = [0,1,0,-1]
    posy = [1,0,-1,0]
    nx = x+posx [candidato-1]
    ny = y+posy [candidato-1]
    if (nx < 0 or nx >= n):
        return False
    if (ny < 0 or ny >= n):
        return False
    if (tablero[nx][ny]== 0):
        return True
    else:
        return False
    
#modulo siguiente_posicion 
def siguiente_posicion(tablero,candidato,x,y):
    posx = [0,1,0,-1]
    posy = [1,0,-1,0]
    nx = x+posx [candidato-1]
    ny = y+posy [candidato-1]
    return nx,ny

#modulo final
def final(tablero,nx,ny):
    if (nx == n -1 and ny == n -1):
        return True
    return False
            
#modulo solucion
def solucion(tablero, x, y, contador):
    global mejor_sol, mejor_cont

    if final(tablero, x, y):
        if mejor_cont == 0 or contador < mejor_cont:
            mejor_cont = contador
            mejor_sol = [fila[:] for fila in tablero]
        return False
    
    for candidato in range(1,5):
        if valida(tablero, candidato, x, y):
            nx, ny = siguiente_posicion(tablero, candidato, x, y)
            tablero[nx][ny]= contador +1

            solucion(tablero, nx, ny, contador + 1)
            tablero[nx][ny]=0
    return False

#modulo mostrar tablero
def mostrar_tablero(tablero):
    for i in range(n):
        for j in range(n):
            print(tablero[i][j], end = " ")
        print("")
    print("")

#modulo colocar_obstaculo
def colocar_obstaculo(tablero):
    pass

def guardar_sol(tablero):
    with open('MejorSolucion.txt', 'w') as f:
        f.write('Mejor solucion encontrada:\n')
        f.write(f"Longitud del camino: {mejor_cont} pasos\n\n")
        for i in range(n):
            for j in range(n):
                f.write(f"{tablero[i][j]:2d} ")
            f.write("\n")

#programa principal
n=int(input('Ingrese la medida de su tablero (n x n): '))
tablero = [[0 for _ in range(n)] for _ in range(n)]
colocar_obstaculo(tablero)
tablero[0][0]=1

solucion(tablero, 0, 0, 1)

if mejor_cont!=0:
    print("Se encontró la mejor solución y se guardó en MejorSolucion.txt")
    guardar_sol(mejor_sol)
else:
    print('No hay solucion')