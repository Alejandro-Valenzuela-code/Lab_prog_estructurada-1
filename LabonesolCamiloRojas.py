# Encuentra UNA solución de un laberinto usando backtracking (puede no tener solución)

import random  # Importa random para tamaño aleatorio y obstáculos

def generar_tablero(MAX):  # Define función para crear matriz de MAX x MAX
    return [[0 for _ in range(MAX)] for _ in range(MAX)]  # Retorna matriz de ceros (celdas libres)

def mostrar_tablero(tablero):  # Convierte el tablero a texto legible
    return "\n".join(" ".join(f"{c:2}" for c in fila) for fila in tablero)  # Une filas y columnas formateadas

def colocar_obstaculos(tablero, porcentaje=0.15):  # Coloca obstáculos aleatorios
    total = len(tablero) * len(tablero)  # Total de celdas
    cantidad = int(total * porcentaje)  # Número de obstáculos a poner
    colocados = 0  # Contador de puestos
    while colocados < cantidad:  # Bucle hasta completar cantidad
        i = random.randint(0, len(tablero) - 1)  # Fila aleatoria válida
        j = random.randint(0, len(tablero) - 1)  # Columna aleatoria válida
        if (i, j) not in [(0, 0), (len(tablero) - 1, len(tablero) - 1)] and tablero[i][j] == 0:  # Evita inicio/fin y dupes
            tablero[i][j] = -1  # Marca obstáculo
            colocados += 1  # Aumenta contador

def valida(tablero, candidato, x, y):  # Verifica si el movimiento candidato desde (x,y) es válido
    posx = [0, 1, 0, -1]  # Desplazamientos en x: derecha, abajo, izquierda, arriba
    posy = [1, 0, -1, 0]  # Desplazamientos en y: derecha, abajo, izquierda, arriba
    nx = x + posx[candidato - 1]  # Nueva x según candidato (1..4)
    ny = y + posy[candidato - 1]  # Nueva y según candidato (1..4)
    if nx < 0 or nx >= len(tablero) or ny < 0 or ny >= len(tablero):  # Fuera de rango -> inválido
        return False  # Retorna inválido
    if tablero[nx][ny] == 0:  # Celda libre (0) -> válido
        return True  # Retorna válido
    return False  # Si hay -1 (muro) o >0 (visitada), inválido

def siguiente_posicion(candidato, x, y):  # Calcula siguiente (nx,ny) a partir del candidato
    posx = [0, 1, 0, -1]  # Desplazamientos en x
    posy = [1, 0, -1, 0]  # Desplazamientos en y
    return x + posx[candidato - 1], y + posy[candidato - 1]  # Retorna nueva coordenada

def final(tablero, x, y):  # ¿Está en la meta?
    return x == len(tablero) - 1 and y == len(tablero) - 1  # True si esquina inferior derecha

def backtracking(tablero):  # Busca UNA solución con backtracking iterativo estilo clase
    MAX = len(tablero)  # Tamaño del tablero
    x = y = 0  # Posición inicial
    contador = 1  # Marca de visita (orden de paso)
    tablero[x][y] = contador  # Marca inicio como paso 1
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]  # Guarda último candidato usado en cada celda
    candidato = 1  # Comienza probando candidato 1 (derecha)

    while candidato <= 4:  # Mientras haya candidatos por intentar
        if valida(tablero, candidato, x, y):  # Si el movimiento es válido
            nx, ny = siguiente_posicion(candidato, x, y)  # Calcula nueva posición
            tablero[nx][ny] = contador + 1  # Marca la nueva celda con el siguiente paso
            if final(tablero, nx, ny):  # Si llegamos a la meta
                return tablero  # Devuelve el tablero con el camino marcado
            else:  # Si no es meta, avanzar “en profundidad”
                tablero_aux[x][y] = candidato  # Recuerda el candidato usado en (x,y)
                x, y = nx, ny  # Mover a la nueva celda
                contador += 1  # Aumenta paso
                candidato = 1  # Reinicia candidatos en la nueva celda
        else:  # Movimiento inválido
            candidato += 1  # Prueba siguiente candidato
            while candidato == 5 and not (x == 0 and y == 0):  # Si agotó 1..4, toca retroceder (si no estamos en inicio)
                tablero[x][y] = 0  # Desmarca la celda (backtracking)
                contador -= 1  # Retrocede contador de pasos
                for i in range(MAX):  # Busca anterior celda por su número
                    for j in range(MAX):  # Recorre columna
                        if tablero[i][j] == contador:  # Si coincide el número de paso
                            x, y = i, j  # Actualiza posición al paso anterior
                candidato = tablero_aux[x][y] + 1  # Retoma desde el siguiente candidato en esa celda
                tablero_aux[x][y] = 0  # Limpia rastro del candidato en esa celda
    return None  # Si sale del bucle, no hay solución

def main():  # Punto de entrada
    solucion = None  # Aún no hay solución
    intentos = 0  # Contará intentos de generar laberinto

    while solucion is None:  # Repetir hasta lograr un laberinto resoluble
        MAX = random.randint(4, 8)  # Tamaño aleatorio entre 4 y 8
        tablero = generar_tablero(MAX)  # Crea tablero vacío
        colocar_obstaculos(tablero)  # Agrega obstáculos aleatorios
        intentos += 1  # Incrementa intentos
        print(f"Intento {intentos}: Laberinto {MAX}x{MAX}\n")  # Muestra intento y tamaño
        print(mostrar_tablero(tablero))  # Imprime el laberinto generado
        print("\nBuscando UNA solución...\n")  # Mensaje de búsqueda
        solucion = backtracking(tablero)  # Intenta resolver; retorna tablero o None

    print("¡Se encontró una solución!\n")  # Mensaje de éxito
    print(mostrar_tablero(solucion))  # Imprime el tablero con el camino

if __name__ == "__main__":  # Ejecuta main
    main()  # Llama a main
