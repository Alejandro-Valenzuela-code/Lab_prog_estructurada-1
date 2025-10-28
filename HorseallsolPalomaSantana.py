tamaño = 5
movimientos = [(2,1),(1,2),(-2,1),(-1,2),
               (-2,-1),(-1,-2),(1,-2),(2,-1)]

soluciones = []

def es_valido(tablero, x,y):
    return 0 <= x < tamaño and 0 <= y < tamaño and tablero[x] [y] == 0

def encontrar_todas_soluciones(tablero, x,y, paso):
    tablero[x] [y] = paso

    if paso == tamaño * tamaño:
        #Guardar una copia de la solucion
        solucion = [fila[:] for fila in tablero]
        soluciones.append(solucion)
        print(f"solución {len(soluciones)} encontrada!")
    else: 
        #Probar todas las soluciones
        for dx, dy in movimientos:
            nuevo_x, nuevo_y = x + dx, y + dy
            if es_valido(tablero, nuevo_x, nuevo_y):
                encontrar_todas_soluciones(tablero, nuevo_x, nuevo_y, paso + 1)

    #Retroceder
    tablero[x] [y] = 0

def mostrar_solucion(solucion, numero):
    print(f"\n--- Solución {numero} ---")
    for fila in solucion:
        for num in fila:
            print(f"{num: 3d}", end = " ")
        print()

#Programa principal
tablero = [ [0 for _ in range(tamaño)] for _ in range(tamaño)]

print("Buscando todas las soluciones...")
encontrar_todas_soluciones(tablero, 0, 0, 1)

print(f"\n Se encontraron {len(soluciones)} soluciones")

#Mostrar algunas soluciones
if soluciones:
    for i in range(min(3, len(soluciones))):
        mostrar_solucion(soluciones[i], i + 1)

        
