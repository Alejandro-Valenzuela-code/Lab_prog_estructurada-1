#           arriba - derecha - abajo - izquierda
movimientos=[(-1,0) , (0,1) , (1,0) , (0,-1)]
def escribirSOL():
    with open("soluciones.txt","a") as f:
        for num,tabla in enumerate(soluciones):
            f.write(f"solucion {num+1} \n")
            for fila in tabla:
                f.write(" | ".join(str(l) for l in fila)+"\n")
            f.write("------------------------------\n")

def juego(posY,posX):
    global espaciosOC,solucion
    for y,x in movimientos:
        if comprobacion(posY+y,posX+x): #Si el movimiento es valido se pone en la tabla
            espaciosOC+=1
            tabla[posY+y][posX+x] = espaciosOC
            if (posY+y,posX+x) == (MAX-1,MAX-1):#Se comprueba si llegaron a la ultima casilla del laberinto
                solucion +=1
                soluciones.append([fila[:] for fila in tabla])
                print(f"hay {solucion} soluciones",end="\r")
                tabla[MAX-1][MAX-1] = 0
                espaciosOC -=1
                continue # para reiniciar el bucle y que se elija otro movimiento
            juego(posY+y,posX+x)#Se accede a la funcion de nuevo desde la posicion nueva
    espaciosOC-=1
    tabla[posY][posX]=0 #No hubo ningun movimiento valido entonces se regresa al movimiento anterior

def comprobacion(y,x):
    if y <0 or x < 0 or y >= MAX or x >= MAX or tabla[y][x] != 0:
        return False
    return True

def ponerObstaculos(obs):
    for o in obs:
        y,x = o.split(",")
        tabla[int(y[1])][int(x[0])] = -1

MAX=int(input("Ingrese el tamaño de la tabla: ")) #tamaño tabla
tabla = [[0]*MAX for _ in range(MAX)]

obstaculos=input(f"Ingrese las coordenadas (x,y) donde desea poner los obstaculos ej:(0,2) (1,1) (3,2)\nLas coordenadas solo deben ser numeros entre 0-{MAX-1} y no se pueden poner en (0,0) n en ({MAX-1},{MAX-1})\n: ")
ponerObstaculos(obstaculos.split(" "))

solucion=0
soluciones=[] #se guardan las tablas con las soluciones

#Inicio del laberinto
tabla[0][0] = 1

espaciosOC = 1

juego(0,0)

if soluciones:
    escribirSOL()
    print(f"hay {solucion} soluciones y se guardaron en el archivo 'soluciones.txt'")
else: 
    print("No tiene soluciones")
