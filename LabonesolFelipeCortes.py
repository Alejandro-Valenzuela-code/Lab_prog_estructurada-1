laberinto = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', 'E', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', ' ', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', 'S', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]

def imprimir_laberinto(lab):
    for fila in lab:
        print(' '.join(fila))  #Une todos los caracteres de la fila en un solo string
    print() #Añade una línea en blanco para separar

def resolver(lab, y, x):
   
    if lab[y][x] == 'S':  #Detecta si se llego a la Salida 'S'
        return True

    if y < 0 or y >= len(lab) or x < 0 or x >= len(lab[0]): #Detecta si se está fuera de los límites del laberinto
        return False

    if lab[y][x] == '#' or lab[y][x] == '.': #Detecta si se ha chocado con una Pared '#' o un camino ya visitado '.'
        return False

    caracter_original = lab[y][x] #Se guarda el carácter original (puede ser 'E' o ' ')
    lab[y][x] = '.' #Se marca la casilla como "visitada"

    #Intenta moverse en las 4 direcciones (Abajo, Arriba, Derecha, Izquierda)
    if resolver(lab, y + 1, x): #Abajo
        return True
    if resolver(lab, y - 1, x): #Arriba
        return True
    if resolver(lab, y, x + 1): #Derecha
        return True
    if resolver(lab, y, x - 1): #Izquierda
        return True

    #Si ninguna direccion sirve se deshace el movimiento y devolvemos False.
    lab[y][x] = caracter_original #Restaura ' ' o 'E'
    return False

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
    print("---Buscando solución---")
    if resolver(laberinto, inicio_y, inicio_x):
        print("\n--- ¡Solución Encontrada! ---")
        laberinto[inicio_y][inicio_x] = 'E' #Se pone la 'E' de vuelta solo para comprension visual
        imprimir_laberinto(laberinto)
    else:
        print("\n--- No se encontró solución ---")
        imprimir_laberinto(laberinto)
else:
    print("Error: No se encontró la 'E' (Entrada) en el laberinto.")