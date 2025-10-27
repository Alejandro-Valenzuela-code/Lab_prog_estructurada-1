import random

print('Jueguemos gato')

fichas_colocadas = [' ' for _ in range(9)] # crea lista vacia de 9 espacios vacios El tablero se presenta vacio

combinaciones_ganadoras = [       # estas son las posiciones posibles que hacen ganar (3 en línea). (filas, columnas,diagonales)
    [0, 1, 2], [3, 4, 5], [6, 7, 8], 
    [0, 3, 6], [1, 4, 7], [2, 5, 8], 
    [0, 4, 8], [2, 4, 6]             
    ]

def mostrar_tablero(tablero): # funcion para mostrar cómo va el tablero
    print(f"\n {tablero[0]} | {tablero[1]} | {tablero[2]}")  
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]}")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]}\n")

def verificar_ganador(tablero, ficha): #funcion que revisa si alguien ha ganado
    for combo in combinaciones_ganadoras:
        if all(tablero[i] == ficha for i in combo): #si hay las mismas fichas estan en una combinacion ganadora
            return True
    return False 

def poner_ficha(tablero): #funcion jugador elige posicion
    while True:
        try:
            pos = int(input('Tu turno:')) - 1 #el jugador elije una posicion y a ese numero que pone se resta 1 (numeros 0 al 8)
            if pos not in range(9): #si no esta en el rango
                print("Número fuera del tablero.") #notifica
            elif tablero[pos] != ' ': #verifica espacio vacio
                print("Espacio ocupado.") #notifica
            else:
                return pos
        except ValueError: #si no es un numero
            print("INVALIDO.")

def elegir_ficha(): #jugador elige X o O
    while True:
        try:
            eleccion = int(input('Elige tu ficha:\n0 = O, 1 = X\nElección: ')) #pide al jugador elegir
            if eleccion in [0, 1]: #si es 0 o x
                return eleccion
            else:
                print("INCORRECTO.") #si no, notifica
        except ValueError:
            print("INVALIDO.") #si no puso numero

# empezar el juego

fichas = ['O', 'X']
eleccion = elegir_ficha() 
ficha_jugador = fichas[eleccion] 
ficha_bot = fichas[(eleccion + 1) % 2] 

print("\nPosiciones del tablero:")   #va a mostrar como son las posiciones del tablero
for i in range(3):
    print(f" {i*3+1} | {i*3+2} | {i*3+3}")
print()

turno = random.randint(0, 1) #1 o 0 al azar
print("COMIENZA" if turno == 0 else "JUEGA CONTRINCANTE.") #si es 0, juegas, si no, juega bot

while ' ' in fichas_colocadas: #bucle mientras hayan espacios vacios
    mostrar_tablero(fichas_colocadas) #muestra trablero despues de cada turno
    if turno == 0:
        # Turno del jugador
        pos = poner_ficha(fichas_colocadas)
        fichas_colocadas[pos] = ficha_jugador #verifica si gana
        if verificar_ganador(fichas_colocadas, ficha_jugador):
            mostrar_tablero(fichas_colocadas)
            print("felicidades ¡Ganaste!")
            break
        turno = 1
    else:
        # Turno de la maquina
        pos_bot = random.choice([i for i, x in enumerate(fichas_colocadas) if x == ' '])
        fichas_colocadas[pos_bot] = ficha_bot
        if verificar_ganador(fichas_colocadas, ficha_bot):
            mostrar_tablero(fichas_colocadas)
            print("Perdiste")
            break
        turno = 0
else:
    mostrar_tablero(fichas_colocadas) #si termina el bucle sin ganador
    print("Empate")
