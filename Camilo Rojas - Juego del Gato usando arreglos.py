# Camilo Rojas - Juego del Gato con IA aleatoria usando listas (arreglos)

import random  # Se usa para que la IA elija casillas al azar

# Crea el tablero vacío como lista de listas (3x3)
tablero = [[" " for _ in range(3)] for _ in range(3)]

# Función para mostrar el tablero
def mostrar_tablero():
    print()
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

# Función para verificar si un jugador ganó
def verificar_victoria(jugador):
    # Revisa filas
    for fila in tablero:
        if all(c == jugador for c in fila):
            return True
    # Revisa columnas
    for c in range(3):
        if all(tablero[f][c] == jugador for f in range(3)):
            return True
    # Revisa diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or \
       all(tablero[i][2 - i] == jugador for i in range(3)):
        return True
    return False

# Función para verificar si el tablero está lleno
def tablero_lleno():
    return all(cell != " " for fila in tablero for cell in fila)

# Función para que la IA juegue aleatoriamente en una casilla vacía
def movimiento_ia(ficha_ia):
    vacias = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == " "]
    if vacias:
        i, j = random.choice(vacias)
        tablero[i][j] = ficha_ia
        print(f"La IA juega en fila {i+1}, columna {j+1}")

# ----------------------------
# INICIO DEL JUEGO
# ----------------------------

# El jugador elige su ficha
while True:
    jugador = input("Elige tu ficha (X/O): ").upper()
    if jugador in ["X", "O"]:
        break
    print("Entrada inválida.")

ia = "O" if jugador == "X" else "X"  # La IA toma la otra ficha

# Muestra el tablero inicial
print("\nComienza el juego:")
mostrar_tablero()

turno = "jugador"  # Empieza el jugador

# Bucle principal del juego
while True:
    if turno == "jugador":
        print("\nTu turno:")
        while True:
            try:
                fila = int(input("Fila (1-3): ")) - 1
                col = int(input("Columna (1-3): ")) - 1
                if 0 <= fila <= 2 and 0 <= col <= 2:
                    if tablero[fila][col] == " ":
                        tablero[fila][col] = jugador
                        break
                    else:
                        print("Esa casilla ya está ocupada.")
                else:
                    print("Debes ingresar números del 1 al 3.")
            except ValueError:
                print("Entrada inválida. Usa números del 1 al 3.")
        
        mostrar_tablero()

        if verificar_victoria(jugador):
            print("¡Ganaste!")
            break
        elif tablero_lleno():
            print("¡Empate!")
            break

        turno = "ia"  # Cambia el turno a la IA

    else:
        print("\nTurno de la IA:")
        movimiento_ia(ia)
        mostrar_tablero()

        if verificar_victoria(ia):
            print("¡La IA gana!")
            break
        elif tablero_lleno():
            print("¡Empate!")
            break

        turno = "jugador"  # Vuelve el turno al jugador
