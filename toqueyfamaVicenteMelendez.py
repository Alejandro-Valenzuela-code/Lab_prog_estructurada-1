import random

print('=====Toque o fama=====')
opcion = input('¿Quieres que la maquina elija el numero? (s/n): ')

#genera o ingresa numero secreto
if opcion.lower() in ['s','si']:
    n_secreto = ''.join(random.sample('0123456789', 4))
    print('(La maquina ha creado un número secreto)')
else:
    n_secreto = input('Escribe el numero secreto (son 4 digitos): ')

#numero maximo de intentos
inten_max = 7
intento = 1
acertado = False

while intento <= inten_max and not acertado:
    print(f'\nIntento {intento} de {inten_max}')
    jugador = input('Adivina el número: ')

#comparacion
    for i in range(4):
        if jugador[i] == n_secreto[i]:
            print(jugador[i], 'Es Fama!')
        elif jugador[i] in n_secreto:
            print(jugador[i], 'Es Toque!')
        else:
            print(jugador[i], 'No es Nada...')
            
    #verifica si jugador acertó        
    if jugador == n_secreto:
        print('Correcto!')
        break
    else:
        print('Incorrecto, intenta de nuevo' )
        intento += 1
if not acertado:
    print('\nSe acabaron los intentos. el numero era: ', n_secreto)