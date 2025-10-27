import random

print("Juguemos toque y fama")

# Se guarda el número secreto con 4 dígitos diferentes
numero_secreto = []

for i in range(4):  #mientras el numero sea de 4 digitos
    while True: 
        if i == 0:
            digito = random.randint(1, 9)  # el primer número no puede ser 0
        else:
            digito = random.randint(0, 9) #numero aleatorio entre 0 y 9
        if str(digito) not in numero_secreto: #convierte el numero a texto, y verifica si esta repetido
            numero_secreto.append(str(digito)) #agrega al numero secreto
            break

# Pide un número válido al jugador
def pedir_numero(): #pide numero
    while True:
        try:
            num = input("Escribe un número de 4 cifras (sin repetir): ")
            if len(num) != 4 or not num.isdigit(): #si no es de cuatro digitos
                print("Debe tener 4 números.") #notifica
            elif len(set(num)) != 4: #si los numeros son iguales
                print("No repitas números.") #notifica
            else:
                return num 
        except ValueError:    #si no es numnero
            print("Dato no válido.") #notifica

# Empieza el juego
intentos = 7
famas = 0

print("\nAdivina el número secreto.")
print("Tienes 7 intentos.\n")

while intentos > 0 and famas != 4: #mientras queden intentos y los digitos sean 4 
    famas = 0 #se reinician en cada intento
    toques = 0
    print(f"Intentos restantes: {intentos}")
    numero = pedir_numero()    #mientras no este terminado, seguira pidiendo numero

    # Revisa cada dígito
    for i in range(4):
        if numero[i] == numero_secreto[i]: 
            famas += 1  #si digito coincide se agrega fama
        elif numero[i] in numero_secreto:
            toques += 1 #si digito en lugar equivocado se agrega toque

    print(f"Toques: {toques}  |  Famas: {famas}\n") #muestra toques y famas del intento
    intentos -= 1 #resta un intento

# Resultado final
if famas == 4: # si se consiguen 4 famas
    print("¡CORRECTO! Haz adivinado")
else: #si no, pierdes
    print("Te quedaste sin intentos.")
    print("El número era:", ''.join(numero_secreto))