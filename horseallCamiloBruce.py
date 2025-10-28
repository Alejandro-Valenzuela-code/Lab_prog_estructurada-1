soluciones = [] # Una lista vacia para almacenar las soluciones
def caballo(n): # Funcion principal.
    movimientos = [(2, 1), (2, -1), (-2, 1), (-2, -1),(1, 2), (1, -2), (-1, 2), (-1, -2)] # Movimientos que puede realizar el caballo
    tablero = [[-1] * n for _ in range(n)] # Crea un tablero lleno de -1 para indicar las casillas no visitadas.    
    

    def validar(x, y): # Funcion para validar pos.
        return 0 <= x < n and 0 <= y < n and tablero[x][y] == -1 # Verifica que la posición sea valida y que no haya sido visitada
    
    def resolver(x, y, movimiento, contador): # Funcion para buscar la sol.
        tablero[x][y] = movimiento # Marca la casilla actual con el numero del movimiento
        
        if movimiento == n * n - 1: # Si se llega al ultimo movimiento posible
            solucion_actual = [fila[:] for fila in tablero] # Se crea una copia del tablero actual
            soluciones.append(solucion_actual) # Y se agrega la solución a la lista de soluciones
            contador = contador + 1 # Se suma 1 al contador de soluciones
            tablero[x][y] = -1 # Libera la casilla actual.
            return contador
        
        for dx, dy in movimientos:
            nuevo_x = x + dx # Calcula la nueva coord. X
            nuevo_y = y + dy # Calcula la nueva coord. Y
            if validar(nuevo_x, nuevo_y): # Verifica que sea valida.
                contador = resolver(nuevo_x, nuevo_y, movimiento + 1, contador)
        tablero[x][y] = -1 # Libera la casilla actual
        return contador
    
    print(f"Buscando todas las soluciones para tablero {n}x{n}.")
    contador_fin = resolver(0, 0, 0, 0) # Inicia la busqueda.
    
    if contador_fin > 0: # Si se encontraron soluciones
        print(f'Se encontraron {contador_fin} soluciones y se almacenaron en TotalSoluciones.txt.') # Se notifica al usuario cuantas se encontraron y donde se guardaron
        return True
    else: # Si no se encontraron
        print("No se encontraron soluciones") # Se notifica que no se encontraron soluciones al usuario
        return False

def mostrar_soluciones(soluciones):
    with open('HorseAll.txt', 'w') as f: # Se crea un archivo llamado HorseAll
        for i in range(len(soluciones)): # 
            f.write(f'Solucion {i+1}\n\n') # Escribe el numero de la sol.
            for fila in soluciones[i]: 
                f.write(" ".join(str(num) for num in fila) + "\n") # Muestra la solución
            f.write('='*30+'\n') # Linea para separar soluciones.


n=int(input('¿De cuanto deseas que sea el tablero? (Ingrese un solo numero): '))
caballo(n) # Ejecuta el programa en un tablero de n x n

if soluciones: # Si la lista de soluciones TIENE soluciones
    mostrar_soluciones(soluciones) # Estas se muestran.
else: # Si no tiene
    print('No hay solucion') #Se notifica que no se encontró solucion.