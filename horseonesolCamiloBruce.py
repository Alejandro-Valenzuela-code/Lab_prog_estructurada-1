def caballo(n):
    movimientos = [(2, 1), (2, -1), (-2, 1), (-2, -1),(1, 2), (1, -2), (-1, 2), (-1, -2)] # Movimientos posibles
    tablero = [[-1] * n for _ in range(n)] # Se crea un tablero lleno de -1 para mostrar las casillas no visitadas
    
    def validar(x, y): # Funcion para validar pos.
        return 0 <= x < n and 0 <= y < n and tablero[x][y] == -1 # Verifica que la posición sea valida y que no haya sido visitada
    
    def resolver(x, y, movimiento): # Funcion para buscar la sol.
        tablero[x][y] = movimiento # Marca la casilla actual con el numero del movimiento
        if movimiento == n * n - 1: # Si se llego al ultimo movimiento posible
            return True  # Retorna True indicando que se encontro solución
        
        for dx, dy in movimientos:
            nuevo_x = x + dx # Se calcula el nuevo X
            nuevo_y = y + dy # Se calcula el nuevo Y 
            if validar(nuevo_x, nuevo_y):  # Si este nuevo movimiento es valido
                if resolver(nuevo_x, nuevo_y, movimiento + 1): # Llama la función resolver
                    return True # Si encontro sol. se informa retornando True
        tablero[x][y] = -1 # Si no, se libera la casilla
        return False # Y se retorna False
    
    if resolver(0, 0, 0): # Inicia la busqueda 
        mostrar_solucion(tablero) # Si encontro sol. la muestra
        return True
    else: # Si no encontró sol.
        print("No se ha encontrado solución") # Se notifica al usuario que no se encontro sol.
        return False

def mostrar_solucion(tablero): # Funcion para mostrar la solucion encontrada.
    print("Solución encontrada:") # Se notifica al usuario que se encontro Sol.
    for fila in tablero: 
        print(" ".join(str(num)for num in fila)) # Convierte los numeros a strings y los muestra.

n=int(input('¿De cuanto deseas que sea el tablero? (Ingrese un solo numero): '))
caballo(n)