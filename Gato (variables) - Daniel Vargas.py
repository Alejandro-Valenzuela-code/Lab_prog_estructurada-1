# No limita letras ni números de todo tipo cuando pida ingresar datos.
import random
C1=' '
C2=' '
C3=' '
C4=' '
C5=' '
C6=' '
C7=' '
C8=' '
C9=' '
partida=0  
ganador=False

print('\n--------------------------------------------------------------------------------')
print('JUEGO DEL GATO')
print('--------------------------------------------------------------------------------')
print('Así es cómo se verá el tablero durante la partida:\n')
print(f'| {C1} | {C2} | {C3} |')
print(f'| {C4} | {C5} | {C6} |')
print(f'| {C7} | {C8} | {C9} |')
print('\n--------------------------------------------------------------------------------')
print('Elige tu ficha:\n1 = X\n2 = O')
ficha_jugador=int(input('> '))
if ficha_jugador==1:
        print('\n--------------------------------------------------------------------------------')
        print('Tu ficha será X')
        print('La máquina será O')
        print('--------------------------------------------------------------------------------\n')
elif ficha_jugador==2:
        print('\n--------------------------------------------------------------------------------')
        print('Tu ficha será O')
        print('La máquina será X')
        print('--------------------------------------------------------------------------------\n')
print('¿Quién parte?:\n1 = TÚ\n2 = MÁQUINA')
turno=int(input('> '))
if turno==1:
    print('\n--------------------------------------------------------------------------------') 
    print('Empiezas TÚ')
    print('--------------------------------------------------------------------------------\n')
elif turno==2:
    print('\n--------------------------------------------------------------------------------')
    print('Empieza la MÁQUINA')
    print('--------------------------------------------------------------------------------\n')
if turno==1:
    print(f'| {C1} | {C2} | {C3} |')
    print(f'| {C4} | {C5} | {C6} |')
    print(f'| {C7} | {C8} | {C9} |')
while partida<9 and ganador!=True:
    if turno==1:
        if ficha_jugador==1:
            print('\nElige la casilla (del 1 al 9):')
            posicion=int(input('> '))
            if posicion==1:
                if C1==' ':
                    C1='X'
                    turno=turno+1
                    partida=partida+1
                else:
                    print('\n--------------------------------------------------------------------------------')
                    print('Casilla ocupada.')
                    print('--------------------------------------------------------------------------------\n')
            elif posicion==2:
                if C2==' ':
                    C2='X'
                    turno=turno+1
                    partida=partida+1
                else:
                    print('\n--------------------------------------------------------------------------------')
                    print('Casilla ocupada.')
                    print('--------------------------------------------------------------------------------\n')
            elif posicion==3:
                if C3==' ':
                    C3='X'
                    turno=turno+1
                    partida=partida+1
                else:
                    print('\n--------------------------------------------------------------------------------')
                    print('Casilla ocupada.')
                    print('--------------------------------------------------------------------------------\n')
            elif posicion==4:
                if C4==' ':
                    C4='X'
                    turno=turno+1
                    partida=partida+1
                else:
                    print('\n--------------------------------------------------------------------------------')
                    print('Casilla ocupada.')
                    print('--------------------------------------------------------------------------------\n')
            elif posicion==5:
                if C5==' ':
                    C5='X'
                    turno=turno+1
                    partida=partida+1
                else:
                    print('\n--------------------------------------------------------------------------------')
                    print('Casilla ocupada.')
                    print('--------------------------------------------------------------------------------\n')
            elif posicion==6:
                if C6==' ':
                    C6='X'
                    turno=turno+1
                    partida=partida+1
                else:
                    print('\n--------------------------------------------------------------------------------')
                    print('Casilla ocupada.')
                    print('--------------------------------------------------------------------------------\n')
            elif posicion==7:
                if C7==' ':
                    C7='X'
                    turno=turno+1
                    partida=partida+1
                else:
                    print('\n--------------------------------------------------------------------------------')
                    print('Casilla ocupada.')
                    print('--------------------------------------------------------------------------------\n')
            elif posicion==8:
                if C8==' ':
                    C8='X'
                    turno=turno+1
                    partida=partida+1
                else:
                    print('\n--------------------------------------------------------------------------------')
                    print('Casilla ocupada.')
                    print('--------------------------------------------------------------------------------\n')
            elif posicion==9:
                if C9==' ':
                    C9='X'
                    turno=turno+1
                    partida=partida+1
                else:
                    print('\n--------------------------------------------------------------------------------')
                    print('Casilla ocupada.')
                    print('--------------------------------------------------------------------------------\n')
            else:
                print('\n--------------------------------------------------------------------------------')
                print('NÚMERO INVÁLIDO.')
                print('--------------------------------------------------------------------------------\n')
            if ((C1==C2==C3!=' ') or (C4==C5==C6!=' ') or (C7==C8==C9!=' ') or (C1==C5==C9!=' ') or (C7==C5==C3!=' ') or (C1==C4==C7!=' ') or (C2==C5==C8!=' ') or (C3==C6==C9!=' ')):
                ganador=True
            else:
                ganador=False
        elif ficha_jugador==2:
            print('\nElige la casilla (del 1 al 9):')
            posicion=int(input('> '))
            if posicion==1:
                if C1==' ':
                    C1='O'
                    turno=turno+1
                    partida=partida+1
                else:
                    print('\n--------------------------------------------------------------------------------')
                    print('Casilla ocupada.')
                    print('--------------------------------------------------------------------------------\n')
            elif posicion==2:
                if C2==' ':
                    C2='O'
                    turno=turno+1
                    partida=partida+1
                else:
                    print('\n--------------------------------------------------------------------------------')
                    print('Casilla ocupada.')
                    print('--------------------------------------------------------------------------------\n')
            elif posicion==3:
                if C3==' ':
                    C3='O'
                    turno=turno+1
                    partida=partida+1
                else:
                    print('\n--------------------------------------------------------------------------------')
                    print('Casilla ocupada.')
                    print('--------------------------------------------------------------------------------\n')
            elif posicion==4:
                if C4==' ':
                    C4='O'
                    turno=turno+1
                    partida=partida+1
                else:
                    print('\n--------------------------------------------------------------------------------')
                    print('Casilla ocupada.')
                    print('--------------------------------------------------------------------------------\n')
            elif posicion==5:
                if C5==' ':
                    C5='O'
                    turno=turno+1
                    partida=partida+1
                else:
                    print('\n--------------------------------------------------------------------------------')
                    print('Casilla ocupada.')
                    print('--------------------------------------------------------------------------------\n')
            elif posicion==6:
                if C6==' ':
                    C6='O'
                    turno=turno+1
                    partida=partida+1
                else:
                    print('\n--------------------------------------------------------------------------------')
                    print('Casilla ocupada.')
                    print('--------------------------------------------------------------------------------\n')
            elif posicion==7:
                if C7==' ':
                    C7='O'
                    turno=turno+1
                    partida=partida+1
                else:
                    print('\n--------------------------------------------------------------------------------')
                    print('Casilla ocupada.')
                    print('--------------------------------------------------------------------------------\n')
            elif posicion==8:
                if C8==' ':
                    C8='O'
                    turno=turno+1
                    partida=partida+1
                else:
                    print('\n--------------------------------------------------------------------------------')
                    print('Casilla ocupada.')
                    print('--------------------------------------------------------------------------------\n')
            elif posicion==9:
                if C9==' ':
                    C9='O'
                    turno=turno+1
                    partida=partida+1
                else:
                    print('\n--------------------------------------------------------------------------------')
                    print('Casilla ocupada.')
                    print('--------------------------------------------------------------------------------\n')
            else:
                print('\n--------------------------------------------------------------------------------')
                print('NÚMERO INVÁLIDO.')
                print('--------------------------------------------------------------------------------\n')    
            if ((C1==C2==C3!=' ') or (C4==C5==C6!=' ') or (C7==C8==C9!=' ') or (C1==C5==C9!=' ') or (C7==C5==C3!=' ') or (C1==C4==C7!=' ') or (C2==C5==C8!=' ') or (C3==C6==C9!=' ')):
                ganador=True
            else:
                ganador=False           
    elif turno==2:
        if ficha_jugador==1:
            posicion=random.randrange(9)
            posicion=posicion+1
            if posicion==1:
                if C1==' ':
                    C1='O'
                    turno=turno-1
                    partida=partida+1
                    print(f'| {C1} | {C2} | {C3} |')
                    print(f'| {C4} | {C5} | {C6} |')
                    print(f'| {C7} | {C8} | {C9} |')
            elif posicion==2:
                if C2==' ':
                    C2='O'
                    turno=turno-1
                    partida=partida+1
                    print(f'| {C1} | {C2} | {C3} |')
                    print(f'| {C4} | {C5} | {C6} |')
                    print(f'| {C7} | {C8} | {C9} |')
            elif posicion==3:
                if C3==' ':
                    C3='O'
                    turno=turno-1
                    partida=partida+1
                    print(f'| {C1} | {C2} | {C3} |')
                    print(f'| {C4} | {C5} | {C6} |')
                    print(f'| {C7} | {C8} | {C9} |')
            elif posicion==4:
                if C4==' ':
                    C4='O'
                    turno=turno-1
                    partida=partida+1
                    print(f'| {C1} | {C2} | {C3} |')
                    print(f'| {C4} | {C5} | {C6} |')
                    print(f'| {C7} | {C8} | {C9} |')
            elif posicion==5:
                if C5==' ':
                    C5='O'
                    turno=turno-1
                    partida=partida+1
                    print(f'| {C1} | {C2} | {C3} |')
                    print(f'| {C4} | {C5} | {C6} |')
                    print(f'| {C7} | {C8} | {C9} |')
            elif posicion==6:
                if C6==' ':
                    C6='O'
                    turno=turno-1
                    partida=partida+1
                    print(f'| {C1} | {C2} | {C3} |')
                    print(f'| {C4} | {C5} | {C6} |')
                    print(f'| {C7} | {C8} | {C9} |')
            elif posicion==7:
                if C7==' ':
                    C7='O'
                    turno=turno-1
                    partida=partida+1
                    print(f'| {C1} | {C2} | {C3} |')
                    print(f'| {C4} | {C5} | {C6} |')
                    print(f'| {C7} | {C8} | {C9} |')
            elif posicion==8:
                if C8==' ':
                    C8='O'
                    turno=turno-1
                    partida=partida+1
                    print(f'| {C1} | {C2} | {C3} |')
                    print(f'| {C4} | {C5} | {C6} |')
                    print(f'| {C7} | {C8} | {C9} |')
            elif posicion==9:
                if C9==' ':
                    C9='O'
                    turno=turno-1
                    partida=partida+1
                    print(f'| {C1} | {C2} | {C3} |')
                    print(f'| {C4} | {C5} | {C6} |')
                    print(f'| {C7} | {C8} | {C9} |')
            else:
                pass
            if ((C1==C2==C3!=' ') or (C4==C5==C6!=' ') or (C7==C8==C9!=' ') or (C1==C5==C9!=' ') or (C7==C5==C3!=' ') or (C1==C4==C7!=' ') or (C2==C5==C8!=' ') or (C3==C6==C9!=' ')):
                ganador=True
            else:
                ganador=False            
        elif ficha_jugador==2: 
            posicion=random.randrange(9)
            posicion=posicion+1
            if posicion==1:
                if C1==' ':
                    C1='X'
                    turno=turno-1
                    partida=partida+1
                    print(f'| {C1} | {C2} | {C3} |')
                    print(f'| {C4} | {C5} | {C6} |')
                    print(f'| {C7} | {C8} | {C9} |')
            elif posicion==2:
                if C2==' ':
                    C2='X'
                    turno=turno-1
                    partida=partida+1
                    print(f'| {C1} | {C2} | {C3} |')
                    print(f'| {C4} | {C5} | {C6} |')
                    print(f'| {C7} | {C8} | {C9} |')
            elif posicion==3:
                if C3==' ':
                    C3='X'
                    turno=turno-1
                    partida=partida+1
                    print(f'| {C1} | {C2} | {C3} |')
                    print(f'| {C4} | {C5} | {C6} |')
                    print(f'| {C7} | {C8} | {C9} |')
            elif posicion==4:
                if C4==' ':
                    C4='X'
                    turno=turno-1
                    partida=partida+1
                    print(f'| {C1} | {C2} | {C3} |')
                    print(f'| {C4} | {C5} | {C6} |')
                    print(f'| {C7} | {C8} | {C9} |')
            elif posicion==5:
                if C5==' ':
                    C5='X'
                    turno=turno-1
                    partida=partida+1
                    print(f'| {C1} | {C2} | {C3} |')
                    print(f'| {C4} | {C5} | {C6} |')
                    print(f'| {C7} | {C8} | {C9} |')
            elif posicion==6:
                if C6==' ':
                    C6='X'
                    turno=turno-1
                    partida=partida+1
                    print(f'| {C1} | {C2} | {C3} |')
                    print(f'| {C4} | {C5} | {C6} |')
                    print(f'| {C7} | {C8} | {C9} |')
            elif posicion==7:
                if C7==' ':
                    C7='X'
                    turno=turno-1
                    partida=partida+1
                    print(f'| {C1} | {C2} | {C3} |')
                    print(f'| {C4} | {C5} | {C6} |')
                    print(f'| {C7} | {C8} | {C9} |')
            elif posicion==8:
                if C8==' ':
                    C8='X'
                    turno=turno-1
                    partida=partida+1
                    print(f'| {C1} | {C2} | {C3} |')
                    print(f'| {C4} | {C5} | {C6} |')
                    print(f'| {C7} | {C8} | {C9} |')
            elif posicion==9:
                if C9==' ':
                    C9='X'
                    turno=turno-1
                    partida=partida+1
                    print(f'| {C1} | {C2} | {C3} |')
                    print(f'| {C4} | {C5} | {C6} |')
                    print(f'| {C7} | {C8} | {C9} |')
            else:
                pass
            if ((C1==C2==C3!=' ') or (C4==C5==C6!=' ') or (C7==C8==C9!=' ') or (C1==C5==C9!=' ') or (C7==C5==C3!=' ') or (C1==C4==C7!=' ') or (C2==C5==C8!=' ') or (C3==C6==C9!=' ')):
                ganador=True
            else:
                ganador=False 
if partida==9 and ganador==True:
    if turno==2:
        print('\n--------------------------------------------------------------------------------')
        print('GANASTE')
        print('--------------------------------------------------------------------------------\n')
    else:
        print('\n--------------------------------------------------------------------------------')
        print('GANÓ LA MÁQUINA')
        print('--------------------------------------------------------------------------------\n')
elif partida<9 and ganador==True:
     if turno==2:
        print('\n--------------------------------------------------------------------------------')
        print('GANANSTE')
        print('--------------------------------------------------------------------------------\n')
     else:
        print('\n--------------------------------------------------------------------------------')
        print('GANÓ LA MÁQUINA')
        print('--------------------------------------------------------------------------------\n')
elif partida==9 and ganador==False:
    print('\n--------------------------------------------------------------------------------')
    print('EMPATE')
    print('--------------------------------------------------------------------------------\n')           