# ----------------------------------------------
#    Recorrido del caballo (Backtracking) (TODAS LAS SOLUCIONES)
# ----------------------------------------------

# Solicita al usuario el tamaño del tablero (ejemplo: 5x5)
MAX = int(input("ingrese la dimensión del tablero (ejemplo: 5): "))
# NOTA: Para MAX = 4 no hay soluciones. Prueba con MAX = 5 para ver resultados.

# ---------------------------------------------------------------
''' Función: mostrar_tablero '''
# Muestra el estado actual del tablero en consola
# ---------------------------------------------------------------
def mostrar_tablero(tablero):
    print("\n" + "-" * (MAX * 4 + 1))
    for fila in tablero:
        for celda in fila:
            print(f"| {celda:2}", end=" ")
        print("|")
        print("-" * (MAX * 4 + 1))
    print("")

# ---------------------------------------------------------------
''' Función: valida '''
# Verifica si el caballo puede moverse a una nueva posición
# sin salirse del tablero ni caer en una celda ocupada
# ---------------------------------------------------------------
def valida(tablero, candidato, x, y):
    # Movimientos posibles del caballo (8 saltos diferentes)
    posx = [-2,-1,1,2,2,1,-1,-2]
    posy = [1,2,2,1,-1,-2,-2,-1]
    
    # Calcula nueva posición según el movimiento candidato
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    
    # Verifica que esté dentro del tablero
    if nx < 0 or nx >= MAX or ny < 0 or ny >= MAX:
        return False
    # Verifica que no haya sido visitada antes
    if tablero[nx][ny] != 0:
        return False
    return True

# ---------------------------------------------------------------
''' Función: siguiente_posicion '''
# Devuelve las coordenadas del siguiente movimiento posible
# ---------------------------------------------------------------
def siguiente_posicion(tablero, candidato, x, y):
    posx = [-2,-1,1,2,2,1,-1,-2]
    posy = [1,2,2,1,-1,-2,-2,-1]
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    return nx, ny

# ---------------------------------------------------------------
''' Función: final '''
# Determina si el tablero está completamente recorrido
# (todas las casillas ocupadas)
# ---------------------------------------------------------------
def final(tablero):
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == 0:
                return False
    return True

# ---------------------------------------------------------------
''' Función: buscar_xy '''
# Busca la posición (x, y) de un número específico en el tablero
# ---------------------------------------------------------------
def buscar_xy(tablero, contador):
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == contador:
                return i, j

# ---------------------------------------------------------------
''' Función: escribir_soluciones '''
# Guarda todas las soluciones encontradas en un archivo de texto
# ---------------------------------------------------------------
def escribir_soluciones(soluciones, archivo_salida):
    try:
        with open(archivo_salida, 'w') as f:
            if not soluciones:
                f.write("No se encontraron soluciones.\n")
                return

            f.write(f"Se encontraron {len(soluciones)} soluciones.\n")
            
            for i, tablero in enumerate(soluciones):
                f.write(f"\n--- Solución {i + 1} ---\n")
                f.write("-" * (MAX * 4 + 1) + "\n")
                for fila in tablero:
                    for celda in fila:
                        f.write(f"| {celda:2} ")
                    f.write("|\n")
                    f.write("-" * (MAX * 4 + 1) + "\n")
        print(f"Todas las soluciones han sido guardadas en '{archivo_salida}'.")
    except IOError as e:
        print(f"Error al escribir en el archivo: {e}")

# ---------------------------------------------------------------
''' Función principal: solucion '''
# Implementa el algoritmo de backtracking para hallar
# TODAS las posibles rutas del caballo
# ---------------------------------------------------------------
def solucion(tablero):
    candidato = 1                 # Movimiento actual del caballo (1 a 8 posibles)
    soluciones_encontradas = []   # Lista donde se guardarán las soluciones
    x, y = 0, 0                   # Comienza en la esquina superior izquierda (0,0)
    contador = 1                  # Marca la cantidad de casillas ocupadas
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]  # Almacena los movimientos probados
    tablero[x][y] = contador      # Marca la primera posición del caballo

    # ------------------------------
    # Bucle principal del backtracking
    # ------------------------------
    while True: 
        # Si el movimiento actual es válido
        if valida(tablero, candidato, x, y):
            # Mueve el caballo a la siguiente posición válida
            nx, ny = siguiente_posicion(tablero, candidato, x, y)
            tablero[nx][ny] = contador + 1
            tablero_aux[x][y] = candidato  # Guarda el movimiento usado
            x, y = nx, ny
            contador += 1
            candidato = 1  # Reinicia candidatos para el nuevo paso
            
            # Si todas las casillas fueron ocupadas → se encontró una solución
            if final(tablero):
                print(f"✅ ¡Solución {len(soluciones_encontradas) + 1} encontrada!")
                soluciones_encontradas.append([fila[:] for fila in tablero])  # Guarda una copia del tablero
                mostrar_tablero(tablero)  # Muestra la solución en pantalla
                
        else:
            # Prueba el siguiente movimiento posible
            candidato += 1
            
            # Si ya probó los 8 movimientos y no hay solución → retrocede (backtrack)
            while candidato == 9 and not (x == 0 and y == 0):
                tablero[x][y] = 0            # Desmarca la posición actual
                contador -= 1
                nx, ny = buscar_xy(tablero, contador)  # Vuelve al paso anterior
                candidato = tablero_aux[nx][ny] + 1    # Retoma desde el siguiente candidato
                tablero_aux[nx][ny] = 0
                x, y = nx, ny 

        # Condición de salida del bucle principal:
        # cuando vuelve al punto de inicio sin más movimientos posibles
        if x == 0 and y == 0 and candidato == 9:
            break

    return soluciones_encontradas

# ---------------------------------------------------------------
''' Programa principal '''
# ---------------------------------------------------------------

# Crea el tablero inicial lleno de ceros
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]

print("Tablero inicial:")
mostrar_tablero(tablero)
print(f"Buscando TODAS las soluciones para un tablero {MAX}x{MAX}...")

# Ejecuta el algoritmo principal
lista_de_soluciones = solucion(tablero)
archivo_salida = "soluciones_caballo.txt"

# Si se encontraron soluciones, se muestran y guardan
if lista_de_soluciones:
    print(f"\n🎉 ¡Búsqueda completada! Se encontraron {len(lista_de_soluciones)} soluciones en total.")
    print("Mostrando la primera solución encontrada:")
    mostrar_tablero(lista_de_soluciones[0])
    escribir_soluciones(lista_de_soluciones, archivo_salida)
else:
    # Si no hay soluciones, se informa y se crea un archivo indicando el resultado
    print("❌ No se encontró ninguna solución.")
    escribir_soluciones([], archivo_salida)