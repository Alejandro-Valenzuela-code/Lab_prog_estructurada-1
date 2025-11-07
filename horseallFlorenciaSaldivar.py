movimientos = [(-2,1),(-2,-1),(1,2),(-1,2), # movimientos del caballo horizontal y vertical 
               (2,1),(2,-1),(-1,-2),(1,-2)] 
def crear_tablero(n): # crea un tablero n x n inicializado en 0
    return[[0 for _ in range(n)]for _ in range(n)] # devuelve el tablero

def valido(tablero,n,f,c): # verifica si la posicion (f,c) es valida
    return f >=0 and c>=0 and f < n and c < n and tablero[f][c]==0 # la posicion no ha sido visitada

def copiar_tablero(tab): # crea una copia del tablero para guardar la solucion
    copia =[]
    for fila in tab: # copia cada fila del tablero
        nueva=[] # crea una nueva fila
        for valor in fila: # copia cada valor de la fila
            nueva.append(valor)
        copia.append(nueva)
    return copia # devuelve la copia del tablero

def buscar(tablero, n, f, c, paso, soluciones): # busca todas las soluciones del recorrido del caballo
    if paso==n*n: # si se han visitado todas las casillas
        soluciones.append(copiar_tablero(tablero)) # guarda la solucion
        return
    for mov in movimientos: # intenta todos los movimientos del caballo
        nf = f + mov[0]
        nc = c + mov[1]
        if valido(tablero, n, nf, nc): # si el movimiento es valido
            tablero[nf][nc]=paso+1
            buscar(tablero,n, nf,nc, paso +1, soluciones) # llama recursivamente a buscar
            tablero[nf][nc]=0

def todas_las_soluciones(n): # encuentra todas las soluciones del recorrido del caballo en un tablero n x n
    todas=[] # lista para guardar todas las soluciones  
    for i in range(n): # intenta iniciar el recorrido desde cada casilla del tablero
        for j in range(n): # cada columna
            tab= crear_tablero(n) # crea un nuevo tablero
            tab[i][j]=1
            buscar(tab, n, i, j, 1, todas) # busca todas las soluciones desde la posicion (i,j)
    return todas
    
def guardar(soluciones): # guarda las soluciones en un archivo de texto
    archivo=open("soluciones.txt","w")
    numero=1
    for tablero in soluciones: # guarda cada solucion en el archivo
        archivo.write("solucion "+ str(numero)+ "\n") # escribe el numero de la solucion
        for fila in tablero: # escribe cada fila del tablero
            for valor in fila: # escribe cada valor de la fila
                archivo.write(str(valor)+" ") 
            archivo.write("\n") 
        numero= numero+1 # incrementa el numero de la solucion
    archivo.close()
    print("se guardan las soluciones en soluciones.txt")

def main(): # funcion principal del programa
    print("Recorrido del caballo")
    n=int(input("ingrese el tamaño del tablero: "))
    soluciones= todas_las_soluciones(n)
    print("Total de soluciones:", len(soluciones))
    guardar(soluciones)

main()
