# Encuentra TODAS las soluciones de un laberinto con backtracking y luego muestra la mejor (más corta)

import random  # Usado para tamaño y obstáculos aleatorios

def generar_tablero(MAX):  # Crea matriz de MAX x MAX
    return [[0 for _ in range(MAX)] for _ in range(MAX)]  # Retorna ceros (libre)

def mostrar_tablero(tablero):  # Representa el tablero como texto
    return "\n".join(" ".join(f"{c:2}" for c in fila) for fila in tablero)  # Une filas formateadas

def colocar_obstaculos(tablero, porcentaje=0.15):  # Coloca obstáculos 
    total = len(tablero) * len(tablero)  # Total de celdas
    cantidad = int(total * porcentaje)  # Obstáculos a colocar
    colocados = 0  # Contador
    while colocados < cantidad:  # Repite hasta llegar a la cantidad
        i = random.randint(0, len(tablero) - 1)  # Fila aleatoria
        j = random.randint(0, len(tablero) - 1)  # Columna aleatoria
        if (i, j) not in [(0, 0), (len(tablero) - 1, len(tablero) - 1)] and tablero[i][j] == 0:  # Evita inicio/fin
            tablero[i][j] = -1  # Marca obstáculo
            colocados += 1  # Incrementa contador

def valida(tablero, x, y):  # ¿(x,y) es celda transitable?
    return 0 <= x < len(tablero) and 0 <= y < len(tablero) and tablero[x][y] == 0  # Dentro y libre

def backtracking_todas(tablero, x, y, camino, soluciones):  # Busca y guarda todas las rutas
    if x == len(tablero) - 1 and y == len(tablero) - 1:  # Caso base: llegó a la meta
        soluciones.append(camino[:])  # Guarda copia del camino actual
        return  # Retorna para seguir buscando más

    tablero[x][y] = 1  # Marca visitado con 1 (temporal)
    direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Movimientos: derecha, abajo, izquierda, arriba

    for dx, dy in direcciones:  # Itera sobre las 4 direcciones
        nx, ny = x + dx, y + dy  # Calcula nueva coordenada
        if valida(tablero, nx, ny):  # Si la celda nueva es válida
            camino.append((nx, ny))  # Agrega al camino
            backtracking_todas(tablero, nx, ny, camino, soluciones)  # Recurre
            camino.pop()  # Quita la última celda (backtracking)

    tablero[x][y] = 0  # Desmarca visitado para otras rutas

def imprimir_mejor_solucion(tablero, camino):  # Nueva función para mostrar la mejor solución en el tablero
    copia = [fila[:] for fila in tablero]  # Crea una copia del laberinto original
    paso = 1  # Contador de pasos
    for (x, y) in camino:  # Recorre el camino
        copia[x][y] = paso  # Marca el paso del recorrido
        paso += 1
    print("\nLaberinto con la mejor solución marcada:\n")  # Título visual
    print(mostrar_tablero(copia))  # Muestra el laberinto con la solución

def main():  # Punto de entrada
    MAX = random.randint(4, 8)  # Tamaño aleatorio entre 4 y 8
    tablero = generar_tablero(MAX)  # Crea tablero vacío
    colocar_obstaculos(tablero)  # Coloca obstáculos aleatorios

    print(f"Laberinto generado de tamaño {MAX}x{MAX}:\n")  # Encabezado
    print(mostrar_tablero(tablero))  # Muestra el laberinto
    print("\nBuscando TODAS las soluciones...\n")  # Mensaje

    soluciones = []  # Lista de todos los caminos solución
    backtracking_todas(tablero, 0, 0, [(0, 0)], soluciones)  # Busca rutas desde (0,0)

    if soluciones:  # Si hay al menos una ruta
        print(f"Total de soluciones encontradas: {len(soluciones)}\n")  # Cantidad

        soluciones.sort(key=len)  # Ordena por longitud ascendente
        mejor = soluciones[0]  # La primera es la más corta

        print("MEJOR SOLUCIÓN (más corta):")  # Título
        print(f"Longitud del camino: {len(mejor)} pasos")  # Muestra número de pasos
        imprimir_mejor_solucion(tablero, mejor)  # Imprime el tablero con el camino marcado

    else:  # Si no hubo rutas
        print("No se encontró ninguna solución.")  # Mensaje de no solución

if __name__ == "__main__":  # Ejecutar
    main()  # Llama a main

