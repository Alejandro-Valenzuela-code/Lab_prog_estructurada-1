soluciones_encontradas = [] #Lista que guarda todas las soluciones encontradas

laberinto = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', 'E', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', '#', '#', ' ', ' ', 'S', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]

def imprimir_laberinto(lab):
    for fila in lab:
        print(' '.join(fila)) #Une todos los caracteres de la fila en un solo string
    print() #Añade una línea en blanco para separar

def encontrar_todas_soluciones(lab, y, x):

    if y < 0 or y >= len(lab) or x < 0 or x >= len(lab[0]):  #Detecta si se está fuera de los límites
        return

    if lab[y][x] == '#' or lab[y][x] == '.': #Detecta si se ha chocado con una Pared '#' o un camino ya visitado '.'
        return

    if lab[y][x] == 'S': #Detecta si se llego a la Salida 'S'
        copia_solucion = [fila[:] for fila in lab] #Se guarda la solución
        soluciones_encontradas.append(copia_solucion)
        return

    caracter_original = lab[y][x] #Se guarda el carácter original (puede ser 'E' o ' ')
    lab[y][x] = '.' #Se marca la casilla como "visitada"

    #Intenta moverse en las 4 direcciones (Abajo, Arriba, Derecha, Izquierda)
    encontrar_todas_soluciones(lab, y + 1, x) #Abajo
    encontrar_todas_soluciones(lab, y - 1, x) #Arriba
    encontrar_todas_soluciones(lab, y, x + 1) #Derecha
    encontrar_todas_soluciones(lab, y, x - 1) #Izquierda

    lab[y][x] = caracter_original #Se deshace el movimiento para que se pueda usar la casilla de nuevo


print("--- Laberinto Inicial ---")
imprimir_laberinto(laberinto)

inicio_y, inicio_x = None, None #Encontrar las coordenadas de la 'E' (Entrada)
for y, fila in enumerate(laberinto):
    for x, celda in enumerate(fila):
        if celda == 'E':
            inicio_y, inicio_x = y, x
            break
    if inicio_y is not None:
        break

if inicio_y is not None:
    print("---Buscando las soluciones---")
    
    encontrar_todas_soluciones(laberinto, inicio_y, inicio_x) #Inicia la búsqueda

    if soluciones_encontradas: #Imprimir los resultados
        print(f"\n--- ¡Se encontraron {len(soluciones_encontradas)} soluciones! ---")
        
        for i, solucion in enumerate(soluciones_encontradas):
            print(f"--- Solución #{i + 1} ---")
            solucion[inicio_y][inicio_x] = 'E' #Se pone la 'E' de vuelta solo para comprension visual
            imprimir_laberinto(solucion)
            
    else:
        print("\n--- No se encontró ninguna solución ---")
else:
    print("Error: No se encontró la 'E' (Entrada) en el laberinto.")