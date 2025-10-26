### Gato con variables ###
print ("Juguemos al gato. \n")  # Muestra un mensaje inicial al jugador

def mostrartablero():  # Se crea la función "mostrartablero" para imprimir el tablero actual
        print(f"""  {a1}  |  {a2}  |  {a3}  
-----------------
  {b1}  |  {b2}  |  {b3}  
-----------------
  {c1}  |  {c2}  |  {c3}  \n""")  

x = " "  # Se asigna un espacio vacío para representar casillas vacías

# Se crean las variables del tablero, todas con valor inicial vacío
a1=x
a2=x
a3=x
b1=x
b2=x
b3=x
c1=x
c2=x
c3=x

# Se pide al jugador elegir su ficha
while True:
    fichaj = input("Elige tu ficha X o O: \n> ")  # Pide al usuario su ficha
    fichaj = fichaj.upper()  # Convierte la ficha elegida a mayúscula
    if fichaj in ("X", "O"):  # Si la ficha es válida (X o O)
        break  # Sale del bucle
    else:   
        print("Elección inválida. \n")  # Mensaje de error si no elige X u O
    
# Se asigna la ficha de la máquina según la elección del jugador
if fichaj == "X":
    ficham = "O"
else:
    ficham = "X"

import random  # Se importa el módulo random para generar números aleatorios

inicio = random.randint(0,1)  # Define aleatoriamente quién comienza (0 jugador, 1 máquina)
turnos = 9  # Hay 9 turnos en total
ocupado = 1  # Controla si la casilla está ocupada
ganador = 0  # Controla si hay un ganador

# Ciclo principal del juego
while turnos != 0 and ganador == 0:
    if inicio == 0:  # Turno del jugador
        ocupado = 1
        while ocupado == 1:
            mostrartablero()  # Muestra el tablero actual
            casilla = input ("Ingrese la casilla (Del 1 al 9) que desea usar: \n> ")  # Pide posición

            # Comprueba qué casilla eligió y si está libre
            if casilla == "1" and a1 == x:
                a1 = fichaj
                ocupado = 0
            elif casilla == "2" and a2 == x:
                a2 = fichaj
                ocupado = 0
            elif casilla == "3" and a3 == x:
                a3 = fichaj
                ocupado = 0
            elif casilla == "4" and b1 == x:
                b1 = fichaj  
                ocupado = 0
            elif casilla == "5" and b2 == x:
                b2 = fichaj
                ocupado = 0
            elif casilla == "6" and b3 == x:
                b3 = fichaj
                ocupado = 0
            elif casilla == "7" and c1 == x:
                c1 = fichaj
                ocupado = 0
            elif casilla == "8" and c2 == x:
                c2 = fichaj
                ocupado = 0
            elif casilla == "9" and c3 == x:
                c3 = fichaj
                ocupado = 0 
            else:
                print ("\nLa casilla seleccionada está ocupada. \n")  # Mensaje si el lugar ya está tomado

        inicio = 1  # Cambia el turno a la máquina
        turnos -= 1  # Resta un turno
        print(f"\nQuedan {turnos} turnos restantes (Fue tu turno). \n")

    else:  # Turno de la computadora
        print("Turno de la computadora. \n")
        ocupado = 1
        while ocupado == 1:
            casilla = str(random.randint(1,9))  # La máquina elige una casilla al azar (1-9)

            # Comprueba si la casilla elegida está libre y la ocupa
            if casilla == "1" and a1 == x:
                a1 = ficham
                ocupado = 0
            elif casilla == "2" and a2 == x:
                a2 = ficham
                ocupado = 0
            elif casilla == "3" and a3 == x:
                a3 = ficham
                ocupado = 0
            elif casilla == "4" and b1 == x:
                b1 = ficham
                ocupado = 0
            elif casilla == "5" and b2 == x:
                b2 = ficham
                ocupado = 0
            elif casilla == "6" and b3 == x:
                b3 = ficham
                ocupado = 0
            elif casilla == "7" and c1 == x:
                c1 = ficham
                ocupado = 0
            elif casilla == "8" and c2 == x:
                c2 = ficham
                ocupado = 0
            elif casilla == "9" and c3 == x:
                c3 = ficham
                ocupado = 0
            else:
                ocupado = 1  # Si está ocupada, vuelve a intentar otra casilla

        turnos -= 1  # Resta un turno
        inicio = 0  # Cambia el turno al jugador
        print(f"\nQuedan {turnos} turnos restantes (Fue turno de la computadora). \n")

    # Comprueba si hay un ganador (horizontal, vertical o diagonal)
    if a1==a2 and a2==a3 and a1!=" " or b1==b2 and b2==b3 and b1!=" " or c1==c2 and c2==c3 and c1!=" " or a1==b1 and b1==c1 and a1!=" " or a2==b2 and b2==c2 and a2!=" " or a3==b3 and b3==c3 and a3!=" " or a1==b2 and b2==c3 and a1!=" " or a3==b2 and b2==c1 and a3!=" ":
        ganador = 1  # Se marca que hay un ganador
        mostrartablero()  # Muestra el tablero final

# Mensaje final según el resultado
if ganador == 1:
    if inicio == 1:
        print("Ganó el jugador. Felicidades. \n")
    else: 
        print("Ganó la maquina. Suerte para la próxima. \n")
else:
    print("Uy, un empate. \n")