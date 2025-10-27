import random

print('Juguemos gato')

a1 = a2 = a3 = b1 = b2 = b3 = c1 = c2 = c3 = ' ' #variables de las casillas
posiciones_disponibles = ['a1' , 'a2' , 'a3' , 'b1' , 'b2' , 'b3' , 'c1' , 'c2' , 'c3']

def mostrar_tablero():
    print(f"\n {a1} | {a2} | {a3}") #posiciones de las variables en el tablero
    print(f" {b1} | {b2} | {b3}")
    print(f" {c1} | {c2} | {c3}\n")

def verificar_ganador(ficha):       # verificar si hay ganador
    return (
        (a1 == a2 == a3 == ficha) or
        (b1 == b2 == b3 == ficha) or
        (c1 == c2 == c3 == ficha) or
        (a1 == b1 == c1 == ficha) or
        (a2 == b2 == c2 == ficha) or
        (a3 == b3 == c3 == ficha) or
        (a1 == b2 == c3 == ficha) or
        (a3 == b2 == c1 == ficha))

def poner_ficha():  #hace elergir al jugador una posicion
    while True:
        pos = input('Tu turno: ').lower()
        if pos not in posiciones_disponibles:
            print("Esa posición no existe o ya está ocupada.")
        else:
            return pos #si no pudo elegir esa posicion entonces se devuelve

def elegir_ficha(): #jugador elije si quiere ser X o O
    while True:
        try:
            eleccion = int(input('Elige tu ficha:\n0 = O, 1 = X\nElección: '))
            if eleccion in [0, 1]:
                return eleccion
            else:
                print("INCORRECTO.")
        except ValueError:
            print("INVALIDO.")

# empezar el juego

fichas = ['O', 'X'] #jugador elije X o O
eleccion = elegir_ficha()
ficha_jugador = fichas[eleccion]
ficha_bot = fichas[(eleccion + 1) % 2]

print("\nPosiciones del tablero:") #muestra variables del tablero
print(" a1 | a2 | a3")
print(" b1 | b2 | b3")
print(" c1 | c2 | c3\n")
 
turno = random.randint(0, 1) #turno aleatorio para comenzar
print("COMIENZAS TÚ" if turno == 0 else "JUEGA LA MÁQUINA.")

# Ciclo del juego
while posiciones_disponibles:
    mostrar_tablero()
    if turno == 0:
        # Turno del jugador
        jugada = poner_ficha()
        exec(f"global {jugada}; {jugada} = '{ficha_jugador}'")
        posiciones_disponibles.remove(jugada)
        if verificar_ganador(ficha_jugador):
            mostrar_tablero()
            print("felicidades ¡Ganaste!")
            break
        turno = 1
    else:
        #turno de la maquina
        jugada_bot = random.choice(posiciones_disponibles) 
        exec(f"global {jugada_bot}; {jugada_bot} = '{ficha_bot}'")
        posiciones_disponibles.remove(jugada_bot)
        if verificar_ganador(ficha_bot):
            mostrar_tablero()
            print("Perdiste")
            break
        turno = 0
else:
    mostrar_tablero()
    print("Empate")
