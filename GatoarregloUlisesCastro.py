import random
def dibujar_tablero(tablero):
    """Dibuja el tablero de Gato."""
    print(f"""
          {tablero[0]} | {tablero[1]} | {tablero[2]}
         ---+---+---
          {tablero[3]} | {tablero[4]} | {tablero[5]}
         ---+---+---
          {tablero[6]} | {tablero[7]} | {tablero[8]}
    """)
def verificar_ganador(tablero, jugador):
    """Verifica si el jugador actual ha ganado."""
    combinaciones_ganadoras = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
        (0, 4, 8), (2, 4, 6)             # Diagonales
    ]
    for a, b, c in combinaciones_ganadoras:
        if tablero[a] == tablero[b] == tablero[c] == jugador:
            return True
    return False
def jugar_gato():
    tablero = [' ' for _ in range(9)]
    jugador_actual = 'X'
    turnos = 0
    print("¡Bienvenido al Gato (Tic-Tac-Toe)!")
    print("Usa los números del 1 al 9 para seleccionar una casilla:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    while turnos < 9:
        dibujar_tablero(tablero)
        while True:
            try:
                movimiento = int(input(f"Turno de {jugador_actual}. Ingresa una casilla (1-9): "))
                indice = movimiento - 1
                if 0 <= indice <= 8 and tablero[indice] == ' ':
                    tablero[indice] = jugador_actual
                    break
                else:
                    print("Movimiento inválido. Elige un número entre 1 y 9 que esté vacío.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")
        turnos += 1
        if verificar_ganador(tablero, jugador_actual):
            dibujar_tablero(tablero)
            print(f"¡El jugador {jugador_actual} ha ganado! 🎉")
            return
        jugador_actual = 'O' if jugador_actual == 'X' else 'X'
    dibujar_tablero(tablero)
    print("¡Es un empate!")
if __name__ == "__main__":
    jugar_gato()