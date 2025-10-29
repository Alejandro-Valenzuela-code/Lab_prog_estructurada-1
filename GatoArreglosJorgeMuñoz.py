### Gato Arreglos ###
import random

x = " "
tablero = [[x, x, x],
           [x, x, x],
           [x, x, x]]

# escoger ficha jugador
while True:
	fichaj = input("Elige una ficha (O, X): \n>")
	fichaj = fichaj.upper()
	if fichaj == "O" or fichaj == "X":
		break
	else:
		print("\nEntrada inválida.\n\n")

# ficha maquina
if fichaj == "O":
	ficham = "X"
else:
	ficham = "O"


# pregunta al jugador quien parte primero
if input("Quien juega primero? (ingresar algo inválido => empieza la maquina)\n1. Jugador \n2. Maquina\n>") == "1":
    inicio = 0
else:
    inicio = 1


turnos = 9  # turnos maximos
ganador = False  # indica si hay un ganador


def mostrar_tablero():
    print(f"""
  {tablero[0][0]}  |  {tablero[0][1]}  |  {tablero[0][2]}  
-----------------
  {tablero[1][0]}  |  {tablero[1][1]}  |  {tablero[1][2]}  
-----------------
  {tablero[2][0]}  |  {tablero[2][1]}  |  {tablero[2][2]} \n""")

# devuelve las coordenadas de cada casilla
def posiciones():
    return {
        "1": (0,0), "2": (0,1), "3": (0,2),
        "4": (1,0), "5": (1,1), "6": (1,2),
        "7": (2,0), "8": (2,1), "9": (2,2)
    }

# programa principal
while turnos != 0 and ganador == False:

    if inicio == 0:  # turno del jugador
        ocupado = True
        while ocupado == True:
            mostrar_tablero()
            casilla = input("Ingrese la casilla que desea jugar (1 a 9): \n> ")
            pos = posiciones()  # obtiene coordenadas de las casillas

            # si la casilla elegida existe y está vacía, se coloca la ficha
            if casilla in posiciones():
                fila, col = pos[casilla]
                if tablero[fila][col] == x:
                    tablero[fila][col] = fichaj
                    ocupado = False
                else:
                    print("\nCasilla ocupada. Inténtelo de nuevo.\n")
            else:
                print("\nNúmero inválido, Inténtelo de nuevo.\n")

        inicio = 1  # el siguiente turno es de la máquina
        turnos -= 1  # turnos restantes
        print(f"\nQuedan {turnos} turnos restantes.\n")

    else:  # turno de la maquina
        print("Turno de la maquina.\n")
        ocupado = True
        while ocupado == True:
            casilla = str(random.randint(1,9))  # escoge una casilla al azar
            pos = posiciones()
            fila, col = pos[casilla]

            if tablero[fila][col] == x:  # si está libre, coloca la ficha
                tablero[fila][col] = ficham
                ocupado = False

        turnos -= 1
        inicio = 0  # cambia turno al jugador
        print(f"\nQuedan {turnos} turnos restantes.\n")

    # comprueba si hay un ganador
    lineas = [
        [tablero[0][0], tablero[0][1], tablero[0][2]],  # Fila 1
        [tablero[1][0], tablero[1][1], tablero[1][2]],  # Fila 2
        [tablero[2][0], tablero[2][1], tablero[2][2]],  # Fila 3
        [tablero[0][0], tablero[1][0], tablero[2][0]],  # Columna 1
        [tablero[0][1], tablero[1][1], tablero[2][1]],  # Columna 2
        [tablero[0][2], tablero[1][2], tablero[2][2]],  # Columna 3
        [tablero[0][0], tablero[1][1], tablero[2][2]],  # Diagonal \
        [tablero[0][2], tablero[1][1], tablero[2][0]]   # Diagonal /
    ]
    for linea in lineas:
        if linea[0] == linea[1] == linea[2] != x:  # si hay tres fichas iguales
            ganador = 1  # indica que hay un ganador
            mostrar_tablero()  # muestra el tablero final

# muestra el mensaje final (ganó jugador, ganó maquina o empate)
if ganador == True:
    if inicio == 1:
        print("Felicidades. Has ganado! \n")
    else:
        print("Ha ganado la maquina. \n")
else:
    mostrar_tablero()  # muestra el tablero final
    print("La partida ha terminado en empate. \n")