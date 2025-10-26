"""
def solucion(tablero):
    while(hay espacios y no hay ganador):
        mostrar tablero
        pedir jugada al jugador actual
        si(jugada válida):
            marcar jugada
            si(hay ganador):
                mostrar ganador
                solucion = True
            else:
                cambiar turno
        else:
            mostrar "Movimiento inválido"
    si(no hay ganador):
        mostrar "Empate"
"""

# --- VARIABLES ---
tablero = [" " for _ in range(9)] 
jugador_actual = "X"              
ganador = None                    
juego_activo = True                

# --- FUNCIONES ---
def mostrar_tablero():
    print(f"\n {tablero[0]} | {tablero[1]} | {tablero[2]} ")
    print("---+---+---")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
    print("---+---+---")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} \n")

def verificar_ganador():
    # Combinaciones ganadoras (índices del tablero)
    combinaciones = [
        (0,1,2), (3,4,5), (6,7,8), # Filas
        (0,3,6), (1,4,7), (2,5,8), # Columnas
        (0,4,8), (2,4,6)            # Diagonales
    ]
    for a,b,c in combinaciones:
        if tablero[a] == tablero[b] == tablero[c] != " ":
            return tablero[a]
    return None

def hay_espacios():
    return " " in tablero

# --- JUEGO PRINCIPAL ---
while juego_activo:
    mostrar_tablero()
    print(f"Turno del jugador {jugador_actual}")
    posicion = input("Elige una posición (1-9): ")

    if posicion.isdigit():
        posicion = int(posicion) - 1
        if 0 <= posicion < 9 and tablero[posicion] == " ":
            tablero[posicion] = jugador_actual
            ganador = verificar_ganador()
            if ganador:
                mostrar_tablero()
                print(f"¡El jugador {ganador} ha ganado! ")
                juego_activo = False
            elif not hay_espacios():
                mostrar_tablero()
                print("¡Empate!")
                juego_activo = False
            else:
                jugador_actual = "O" if jugador_actual == "X" else "X"
        else:
            print("Movimiento inválido. Intenta nuevamente.")
    else:
        print("Entrada no válida. Usa números del 1 al 9.")
