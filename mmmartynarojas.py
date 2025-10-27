def mm(A, B):                       #Define función "mm" que multiplica dos matrices A y B
    BT = list(zip(*B))  #Transpone matriz B, convierte filas en columnas y viceversa

    C = []  #Matriz (vacia) resultante asignada como 'C'
    for fila in A: #Toma cada fila de la matriz A
        nueva_fila = []  #Fila resultante nueva
        for col in BT:  #Toma cada columna de B transpuesta

            valor = sum(x * y for x, y in zip(fila, col)) #calcula producto punto de fila de A * columna de B
            nueva_fila.append(valor)  #agrega resultados en la fila
        C.append(nueva_fila) #agregar fila a matriz resultante
    return C #retorna matriz resultante 

#Ejemplo
A = [[1, 2, 3],  #matriz A (2x3)
     [4, 5, 6]] 

B = [[7, 8],    
     [9, 10],   #matriz B (3x2)
     [11, 12]]  
#MATRIZ RESULTANTE SERA DE 2X2

for fila in mm(A, B):  #En cada fila aplicar la funcion definida, aplicar A * B
    print(fila)  #Imprimir fila resultante
    