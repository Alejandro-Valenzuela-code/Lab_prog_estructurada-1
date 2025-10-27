import random  # Importa el módulo para generar números aleatorios

# Función que genera un tablero vacío de tamaño MAX x MAX
def generar_tablero(MAX):
    return [[0 for _ in range(MAX)] for _ in range(MAX)]

# Función que convierte el tablero en un string para mostrarlo bonito :)
def mostrar_tablero(tablero):
    return "\n".join(" ".join(f"{c:2}" for c in fila) for fila in tablero)

# Función que coloca obstáculos aleatorios en el tablero
def colocar_obstaculos(tablero, porcentaje=0.15):
    total = len(tablero) * len(tablero)  # Cantidad total de casillas
    cantidad = int(total * porcentaje)   # Cantidad de obstáculos a poner
    colocados = 0
    while colocados < cantidad:
        i = random.randint(0, len(tablero)-1)
        j = random.randint(0, len(tablero)-1)
        # Verifica que no sea la casilla de inicio o fin
        if (i, j) not in [(0, 0), (len(tablero)-1, len(tablero)-1)] and tablero[i][j] == 0:
            tablero[i][j] = -1  # Coloca obstáculo
            colocados += 1

# Función que evalúa si un movimiento es válido
def valida(tablero, candidato, x, y):
    # Direcciones posibles: derecha, abajo, izquierda, arriba
    posx = [0, 1, 0, -1]
    posy = [1, 0, -1, 0]
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    # Verifica si está dentro del tablero y si no hay obstáculo
    if nx < 0 or nx >= len(tablero) or ny < 0 or ny >= len(tablero):
        return False
    if tablero[nx][ny] == 0:
        return True
    return False

# Función que calcula la nueva posición según dirección candidata
def siguiente_posicion(candidato, x, y):
    posx = [0, 1, 0, -1]
    posy = [1, 0, -1, 0]
    return x + posx[candidato - 1], y + posy[candidato - 1]

# Busca las coordenadas donde está un número específico en el tablero
def buscar_xy(tablero, valor):
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] == valor:
                return i, j

# Verifica si estamos en la casilla final (esquina inferior derecha)
def final(tablero, x, y):
    return x == len(tablero) - 1 and y == len(tablero) - 1

# Función principal de backtracking que busca caminos válidos
def backtracking(tablero, max_solutions=1):
    MAX = len(tablero)
    soluciones = []  # Lista para guardar soluciones encontradas
    contador = 1  # Número que representa el orden del recorrido
    candidato = 1  # Dirección a intentar (1=derecha, 2=abajo, etc)
    x = y = 0  # Posición inicial
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]  # Historial de candidatos usados
    tablero[x][y] = contador  # Marca la posición inicial

    while candidato <= 4:  # Hay 4 direcciones posibles
        if valida(tablero, candidato, x, y):
            nx, ny = siguiente_posicion(candidato, x, y)
            tablero[nx][ny] = contador + 1  # Avanza y marca siguiente número

            if final(tablero, nx, ny):
                soluciones.append([fila[:] for fila in tablero])  # Guarda la solución
                if len(soluciones) >= max_solutions:
                    break  # Si ya se alcanzó el máximo, termina
                tablero[nx][ny] = 0  # Desmarca para seguir probando caminos
                candidato += 1
                # Retrocede en caso necesario
                while candidato == 5 and not (x == 0 and y == 0):
                    tablero[x][y] = 0
                    contador -= 1
                    nx, ny = buscar_xy(tablero, contador)
                    candidato = tablero_aux[nx][ny] + 1
                    tablero_aux[nx][ny] = 0
                    x, y = nx, ny
            else:
                tablero_aux[x][y] = candidato  # Guarda el candidato usado
                x, y = nx, ny
                contador += 1
                candidato = 1  # Reinicia candidatos
        else:
            candidato += 1
            # Retrocede si no hay más candidatos
            while candidato == 5 and not (x == 0 and y == 0):
                tablero[x][y] = 0
                contador -= 1
                nx, ny = buscar_xy(tablero, contador)
                candidato = tablero_aux[nx][ny] + 1
                tablero_aux[nx][ny] = 0
                x, y = nx, ny
    return soluciones  # Devuelve la lista de soluciones encontradas

# ---------------------
# PROGRAMA CON MENÚ
# ---------------------

print("MENÚ DE OPCIONES:")  # Muestra el menú en pantalla
print("1. Forzar un tablero con una única solución")
print("2. Forzar un tablero con múltiples soluciones")
print("3. Forzar un tablero sin solución")
opcion = input("Selecciona una opción (1/2/3): ")  # Input del usuario

MAX = random.randint(3, 10)  # Tamaño aleatorio del tablero entre 3x3 y 10x10
tablero = generar_tablero(MAX)  # Crea el tablero vacío

# Opción 1: busca una sola solución
if opcion == "1":
    colocar_obstaculos(tablero)
    soluciones = backtracking(tablero, max_solutions=1)
    resultado = "TIENE UNA SOLUCIÓN" if soluciones else "NO TIENE SOLUCIÓN"

# Opción 2: busca muchas soluciones (hasta 1000)
elif opcion == "2":
    colocar_obstaculos(tablero)
    soluciones = backtracking(tablero, max_solutions=1000)
    resultado = f"TIENE {len(soluciones)} SOLUCIONES" if soluciones else "NO TIENE SOLUCIÓN"

# Opción 3: construye un tablero sin salida
elif opcion == "3":
    for i in range(MAX):
        for j in range(MAX):
            tablero[i][j] = 0
    tablero[MAX-1][MAX-2] = -1  # Obstáculo antes de la meta
    tablero[MAX-2][MAX-1] = -1  # Otro obstáculo
    soluciones = backtracking(tablero, max_solutions=1)
    resultado = "NO TIENE SOLUCIÓN"

else:
    print("Opción no válida.")  # Si elige otra opción, termina
    exit()

# Muestra resultados por pantalla
print(f"\nTamaño del tablero: {MAX}x{MAX}")
print(mostrar_tablero(tablero))
print("\nRESULTADO:", resultado)

# Guarda resultados en archivo de texto
with open("resultado_menu.txt", "w") as f:
    f.write(f"Tamaño del tablero: {MAX}x{MAX}\n\n")
    f.write(mostrar_tablero(tablero) + "\n\n")
    f.write("RESULTADO: " + resultado + "\n")
# Fin del programa
