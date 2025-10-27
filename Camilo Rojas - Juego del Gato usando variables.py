# Camilo Rojas - Juego del Gato usando variables individuales

# Se inicializan las casillas como espacios vacíos
a1 = a2 = a3 = ' '
b1 = b2 = b3 = ' '
c1 = c2 = c3 = ' '

# El jugador "X" comienza el juego
jugador = "X"

# Función para mostrar el estado actual del tablero
def mostrar_tablero():
    print(f" {a1} | {a2} | {a3} ")
    print("---+---+---")
    print(f" {b1} | {b2} | {b3} ")
    print("---+---+---")
    print(f" {c1} | {c2} | {c3} ")
    print()

# Función para verificar si hay una jugada ganadora
def verificar_victoria(j):
    return (
        # Revisa filas
        (a1 == a2 == a3 == j) or
        (b1 == b2 == b3 == j) or
        (c1 == c2 == c3 == j) or
        # Revisa columnas
        (a1 == b1 == c1 == j) or
        (a2 == b2 == c2 == j) or
        (a3 == b3 == c3 == j) or
        # Revisa diagonales
        (a1 == b2 == c3 == j) or
        (a3 == b2 == c1 == j)
    )

# Contador de turnos para detectar empate
turnos = 0

# Bucle principal del juego
while True:
    mostrar_tablero()  # Muestra el tablero

    print(f"Turno del jugador {jugador}")

    # Pide fila y columna al usuario (1 a 3)
    fila = int(input("Fila (1-3): "))
    col = int(input("Columna (1-3): "))

    # Determina la variable correspondiente según fila y columna
    if fila == 1 and col == 1 and a1 == ' ':
        a1 = jugador
    elif fila == 1 and col == 2 and a2 == ' ':
        a2 = jugador
    elif fila == 1 and col == 3 and a3 == ' ':
        a3 = jugador
    elif fila == 2 and col == 1 and b1 == ' ':
        b1 = jugador
    elif fila == 2 and col == 2 and b2 == ' ':
        b2 = jugador
    elif fila == 2 and col == 3 and b3 == ' ':
        b3 = jugador
    elif fila == 3 and col == 1 and c1 == ' ':
        c1 = jugador
    elif fila == 3 and col == 2 and c2 == ' ':
        c2 = jugador
    elif fila == 3 and col == 3 and c3 == ' ':
        c3 = jugador
    else:
        print("Casilla ocupada o inválida. Intenta de nuevo.")
        continue  # Salta el cambio de jugador

    turnos += 1  # Se suma un turno

    # Verifica si el jugador actual ha ganado
    if verificar_victoria(jugador):
        mostrar_tablero()
        print(f"¡Jugador {jugador} gana!")
        break

    # Verifica si hay empate
    if turnos == 9:
        mostrar_tablero()
        print("¡Empate!")
        break

    # Cambia de jugador
    jugador = "O" if jugador == "X" else "X"
