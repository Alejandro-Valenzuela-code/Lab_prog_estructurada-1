tablero = [' '] * 9
jugador = 'X'

def mostrar_tablero():
    print(f"\n{tablero[6]} | {tablero[7]} | {tablero[8]}")
    print('---------')
    print(f"{tablero[3]} | {tablero[4]} | {tablero[5]}")
    print('---------')
    print(f"{tablero[0]} | {tablero[1]} | {tablero[2]}\n")

def hay_ganador():
    combinaciones = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for c in combinaciones:
        if tablero[c[0]] == tablero[c[1]] == tablero[c[2]] != ' ':
            return True
    return False

for turno in range(9):
    mostrar_tablero()
    print(f"Turno de {jugador}")
    pos = int(input("Elige una posición (0-8): "))

    if tablero[pos] == ' ':
        tablero[pos] = jugador
    else:
        print("Esa posición ya está ocupada.")
        continue

    if hay_ganador():
        mostrar_tablero()
        print(f"¡Gana {jugador}!")
        break

    jugador = 'O' if jugador == 'X' else 'X'
else:
    mostrar_tablero()
    print("¡Empate!")
