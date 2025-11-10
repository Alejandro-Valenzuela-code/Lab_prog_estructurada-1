import random  # Importa el módulo random para generar valores aleatorios

# ------------------- utilidades -------------------

x = random.randint(5, 15)  # Genera un número aleatorio entre 5 y 15 para definir el tamaño del tablero
tablero = [[0 for _ in range(x)] for _ in range(x)]  # Crea una matriz (lista de listas) de tamaño x por x llena de ceros
movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Define los movimientos posibles: derecha, abajo, izquierda y arriba
max_tablero = len(tablero)  # Guarda el tamaño del tablero (cantidad de filas)
inicio = (0, 0)  # Define la posición inicial (esquina superior izquierda)
final = (max_tablero - 1, max_tablero - 1)  # Define la posición final (esquina inferior derecha)


def imprimir_tablero(tablero):
    for fila in tablero:  # Recorre cada fila del tablero
        print(" ".join(str(c) for c in fila))  # Imprime los valores de la fila separados por espacios


def obstaculos(tablero):
    objetivo = max_tablero + max_tablero // 2 + 1  # Calcula cuántos obstáculos (piedras) se van a colocar
    colocadas = 0  # Contador de obstáculos colocados
    while colocadas < objetivo:  # Mientras falten obstáculos por colocar
        i = random.randint(0, max_tablero - 1)  # Genera una coordenada aleatoria en filas
        j = random.randint(0, max_tablero - 1)  # Genera una coordenada aleatoria en columnas

        if (i, j) == (0, 0) or (i, j) == (max_tablero - 1, max_tablero - 1):  # Evita poner obstáculos en inicio o final
            continue  # Salta a la siguiente iteración
        if tablero[i][j] == "X":  # Si ya hay un obstáculo en esa posición
            continue  # No hace nada y vuelve al inicio del bucle

        tablero[i][j] = "X"  # Coloca un obstáculo (una "X") en esa posición
        colocadas += 1  # Aumenta el contador de obstáculos
    return tablero  # Devuelve el tablero con los obstáculos colocados


def validacion(tablero, x, y):
    if not (0 <= x < max_tablero and 0 <= y < max_tablero):  # Verifica que las coordenadas estén dentro del tablero
        return False  # Si no lo están, devuelve False
    if tablero[x][y] == "X":  # Si la posición es un obstáculo
        return False  # No se puede pasar por ahí
    if tablero[x][y] == ".":  # Si la posición ya fue visitada
        return False  # No se puede volver a pasar
    return True  # Si ninguna condición anterior se cumple, es válida


def backtracking(tablero):
    camino = []  # Lista donde se guardará el camino recorrido

    if not validacion(tablero, *inicio) or not validacion(tablero, *final):  # Verifica que inicio y fin no estén bloqueados
        return []  # Si alguno está bloqueado, devuelve una lista vacía

    def dfs(i, j):  # Función interna que realiza la búsqueda recursiva
        if not validacion(tablero, i, j):  # Si la posición actual no es válida
            return False  # No se puede continuar

        anterior = tablero[i][j]  # Guarda el valor original de la celda (por si hay que restaurarlo)
        tablero[i][j] = "."  # Marca la celda como visitada con un punto
        camino.append((i, j))  # Agrega la posición actual al camino

        if (i, j) == final:  # Si se llegó a la posición final
            return True  # Indica que se encontró una solución

        for di, dj in movimientos:  # Recorre cada posible dirección de movimiento
            ni, nj = i + di, j + dj  # Calcula la nueva posición (vecino)
            if dfs(ni, nj):  # Llama recursivamente al DFS para explorar el siguiente paso
                return True  # Si se encontró un camino, retorna True

        camino.pop()  # Si no se encontró camino desde aquí, elimina la última posición (retrocede)
        tablero[i][j] = anterior  # Restaura el valor original de la celda
        return False  # Indica que desde esta celda no hay solución

    return camino if dfs(*inicio) else []  # Devuelve el camino si se encontró, o lista vacía si no


def marcar_camino(tablero, camino):
    for r in range(max_tablero):  # Recorre todas las filas
        for c in range(max_tablero):  # Recorre todas las columnas
            if tablero[r][c] == ".":  # Si hay una marca de visita
                tablero[r][c] = 0  # La limpia y la vuelve a 0

    if not camino:  # Si no hay camino encontrado
        return tablero  # Devuelve el tablero sin modificar

    sx, sy = camino[0]  # Obtiene las coordenadas de inicio
    gx, gy = camino[-1]  # Obtiene las coordenadas de fin
    tablero[sx][sy] = "I"  # Marca el punto inicial con "I"
    if len(camino) > 2:  # Si el camino tiene más de dos posiciones
        for (i, j) in camino[1:-1]:  # Recorre las posiciones intermedias
            tablero[i][j] = "*"  # Las marca con asteriscos para mostrar el camino
    tablero[gx][gy] = "F"  # Marca el punto final con "F"
    return tablero  # Devuelve el tablero con el camino marcado


# ------------------- ejecución -------------------

print(f"Tablero de tamaño {x}x{x}:")  # Muestra el tamaño del tablero generado
obstaculos(tablero)  # Coloca los obstáculos en el tablero
imprimir_tablero(tablero)  # Imprime el tablero con los obstáculos

ruta = backtracking(tablero)  # Ejecuta el algoritmo de backtracking para encontrar un camino
if ruta:  # Si encontró un camino
    print("\nCamino encontrado:")  # Muestra mensaje
    imprimir_tablero(marcar_camino(tablero, ruta))  # Imprime el tablero con el camino marcado
else:  # Si no encontró camino
    print("\nNo se encontró un camino.")  # Muestra mensaje indicando que no hay solución
