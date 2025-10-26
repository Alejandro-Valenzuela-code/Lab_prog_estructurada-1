"""
def solucion(tablero):
    mientras(no hay ganador y hay espacios):
        mostrar tablero
        pedir jugada al jugador actual
        if(jugada válida):
            marcar jugada
            if(hay ganador):
                mostrar ganador
                solucion = True
            else:
                cambiar turno
        elif:
            mostrar "Movimiento inválido"
    if(no hay ganador):
        mostrar "Empate"
"""
# Algoritmo del juego "El Gato" usando arreglos

def crear_tablero():
    # Crea un tablero 3x3 vacío
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    # Muestra el tablero en pantalla
    print("\n")
    for fila in range(3):
        print(" | ".join(tablero[fila]))
        if fila < 2:
            print("--+---+--")
    print("\n")

def hay_ganador(tablero, simbolo):
    # Verifica si el jugador con 'simbolo' ha ganado
    # Filas
    for fila in tablero:
        if fila.count(simbolo) == 3:
            return True
    # Columnas
    for c in range(3):
        if tablero[0][c] == simbolo and tablero[1][c] == simbolo and tablero[2][c] == simbolo:
            return True
    # Diagonales
    if tablero[0][0] == simbolo and tablero[1][1] == simbolo and tablero[2][2] == simbolo:
        return True
    if tablero[0][2] == simbolo and tablero[1][1] == simbolo and tablero[2][0] == simbolo:
        return True
    return False

def tablero_lleno(tablero):
    # Comprueba si ya no hay espacios vacíos
    for fila in tablero:
        if " " in fila:
            return False
    return True

def juego_gato():
    tablero = crear_tablero()
    jugador_actual = "X"
    ganador = False

    while not ganador and not tablero_lleno(tablero):
        mostrar_tablero(tablero)
        print(f"Turno del jugador {jugador_actual}")
        try:
            fila = int(input("Ingrese fila (0-2): "))
            col = int(input("Ingrese columna (0-2): "))
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")
            continue

        # Verificar jugada válida
        if 0 <= fila <= 2 and 0 <= col <= 2 and tablero[fila][col] == " ":
            tablero[fila][col] = jugador_actual

            if hay_ganador(tablero, jugador_actual):
                mostrar_tablero(tablero)
                print(f"¡Jugador {jugador_actual} ha ganado! ")
                ganador = True
            else:
                jugador_actual = "O" if jugador_actual == "X" else "X"
        else:
            print("Movimiento inválido, intente de nuevo.")

    if not ganador:
        mostrar_tablero(tablero)
        print("¡Empate!")

# Ejecutar el juego
juego_gato()
