### Gato Variables ###
import random

def mostrar_tablero():
    print(f"""
  {a1}  |  {a2}  |  {a3}  
-----------------
  {b1}  |  {b2}  |  {b3}  
-----------------
  {c1}  |  {c2}  |  {c3}  \n""")  

x = " "  # Se asigna un espacio vacío para representar casillas vacías

# asignar espacios vacios a cada casilla
a1 = a2 = a3 = b1 = b2 = b3 = c1 = c2 = c3 = x

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

# programa principal
while turnos != 0 and ganador == False:
    if inicio == 0:  # turno del jugador
        ocupado = True
        while ocupado == True:
            mostrar_tablero()
            casilla = input ("Ingrese la casilla que desea jugar (1 a 9): \n> ")

            # comprueba si la casilla seleccionada está libre
            if casilla == "1" and a1 == x:
                a1 = fichaj
                ocupado = False
            elif casilla == "2" and a2 == x:
                a2 = fichaj
                ocupado = False
            elif casilla == "3" and a3 == x:
                a3 = fichaj
                ocupado = False
            elif casilla == "4" and b1 == x:
                b1 = fichaj  
                ocupado = False
            elif casilla == "5" and b2 == x:
                b2 = fichaj
                ocupado = False
            elif casilla == "6" and b3 == x:
                b3 = fichaj
                ocupado = False
            elif casilla == "7" and c1 == x:
                c1 = fichaj
                ocupado = False
            elif casilla == "8" and c2 == x:
                c2 = fichaj
                ocupado = False
            elif casilla == "9" and c3 == x:
                c3 = fichaj
                ocupado = False 
            else:
                print("\nSelección inválida, intentelo de nuevo.\n")

        inicio = 1  # turno de la máquina
        turnos -= 1  # turnos restantes
        print(f"\nQuedan {turnos} turnos restantes. \n")

    else:  # turno de la computadora
        print("Turno de la computadora. \n")
        ocupado = True
        while ocupado == True:
            casilla = str(random.randint(1,9))  # la máquina escoge una casilla al azar entre el 1 y el 9

            # comprueba si la casilla elegida está libre y la ocupa
            if casilla == "1" and a1 == x:
                a1 = ficham
                ocupado = False
            elif casilla == "2" and a2 == x:
                a2 = ficham
                ocupado = False
            elif casilla == "3" and a3 == x:
                a3 = ficham
                ocupado = False
            elif casilla == "4" and b1 == x:
                b1 = ficham
                ocupado = False
            elif casilla == "5" and b2 == x:
                b2 = ficham
                ocupado = False
            elif casilla == "6" and b3 == x:
                b3 = ficham
                ocupado = False
            elif casilla == "7" and c1 == x:
                c1 = ficham
                ocupado = False
            elif casilla == "8" and c2 == x:
                c2 = ficham
                ocupado = False
            elif casilla == "9" and c3 == x:
                c3 = ficham
                ocupado = False
            else:
                ocupado = True  # si la casilla está ocupada, vuelve a intentarlo

        turnos -= 1
        inicio = 0  # el siguiente turno es del jugador
        print(f"\nQuedan {turnos} turnos restantes. \n")

    # verifica si hay un ganador
    if (a1==a2 and a2==a3 and a1!=x) or (b1==b2 and b2==b3 and b1!=x) or (c1==c2 and c2==c3 and c1!=x) or (a1==b1 and b1==c1 and a1!=x) or (a2==b2 and b2==c2 and a2!=x) or (a3==b3 and b3==c3 and a3!=x) or (a1==b2 and b2==c3 and a1!=x) or (a3==b2 and b2==c1 and a3!=x):
        ganador = True  # indica si hay un ganador
        mostrar_tablero()  # muestra el tablero final

#  muestra el mensaje final (ganó jugador, ganó maquina o empate)
if ganador == True:
    if inicio == 1:
        print("Felicidades. Has ganado! \n")
    else: 
        print("Ha ganado la maquina. \n")
else:
    mostrar_tablero()  # muestra el tablero final
    print("La partida ha terminado en empate. \n")