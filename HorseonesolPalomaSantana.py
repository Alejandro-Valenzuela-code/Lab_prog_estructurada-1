tamaño = 5
movimientos = [(2,1),(1,2),(-1,2),(-2,1),
               (-2,-1),(-1,-2),(2,-1),(1,-2)]

soluciones = []

def es_valido(tablero, x, y):
    """Verificar si la posicion está dentro del tablero y libre"""
    return 0 <= x < tamaño and 0 <= y < tamaño and tablero[x][y] == 0

def resolver_caballo(tablero, x, y, paso):
    tablero [x] [y] = paso
    if paso == tamaño * tamaño:
        return True
    
    #Probar los 8 movimientos posibles
    for dx, dy in movimientos:
        nuevo_x, nuevo_y = x + dx, y + dy 

        if es_valido(tablero, nuevo_x, nuevo_y):
            if resolver_caballo(tablero, nuevo_x, nuevo_y, paso + 1):
                return True
            
    tablero [x] [y] = 0 
    return False

def mostrar_tablero(tablero):
    print(f"\n --- Solucion encontrada: ---")
    for fila in tablero:
        for num in fila: 
            print(f"{num: 3d}", end = " ")
        print()

#programa principal
tablero = [ [ 0 for _ in range(tamaño)] for _ in range(tamaño)]

if resolver_caballo(tablero, 0, 0, 1):
    mostrar_tablero(tablero)
else:
    print("No se encontró solución.")

