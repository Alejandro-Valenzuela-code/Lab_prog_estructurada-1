#                arriba          derecha        abajo           izquierda
movimientos=[(-2,1),(-2,-1), (1,2),(-1,2), (2,1),(2,-1), (-1,-2),(1,-2)]

def mostrarSOL():
        for fila in tabla:
            print(" | ".join(str(l) for l in fila))
        exit()
def juego(posY,posX):
    global espaciosOC,solucion
    for y,x in movimientos:
        
        if comprobacion(posY+y,posX+x): #Si el movimiento es valido se pone en la tabla
            espaciosOC +=1
            tabla[posY+y][posX+x] = espaciosOC 
            if espaciosOC == MAX**2:
                mostrarSOL()
            juego(posY+y,posX+x)#Se accede a la funcion de nuevo desde la posicion nueva
    espaciosOC-=1
    tabla[posY][posX]=0 #No hubo ningun movimiento valido entonces se regresa al movimiento anterior
def comprobacion(y,x):
    if y <0 or x < 0 or y >= MAX or x >= MAX or tabla[y][x] != 0:
        return False
    return True

MAX=int(input("Ingrese el tamaño de la tabla: ")) #tamaño tabla
for yIN in range(MAX):
    for xIN in range(MAX):
        tabla = [[0]*MAX for _ in range(MAX)]
        tabla[yIN][xIN] = 1
        espaciosOC = 1

        juego(yIN,xIN)
print("No tiene soluciones")
