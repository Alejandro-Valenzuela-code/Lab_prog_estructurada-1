# Camilo Rojas - Juego Toque y Fama

import random  # Importa el módulo random para generar números aleatorios

# Función que genera un número secreto de 4 dígitos únicos
def generar_numero_secreto():
    digitos = list(range(10))     # Crea una lista de los dígitos del 0 al 9
    random.shuffle(digitos)       # Mezcla los dígitos aleatoriamente
    return digitos[:4]            # Retorna los primeros 4 dígitos (sin repetir)

# Función que compara el número secreto con el intento del jugador
def comparar_numeros(secreto, intento):
    fama = 0   # Contador de dígitos en la posición correcta
    toque = 0  # Contador de dígitos correctos en posición incorrecta

    for i in range(4):  # Recorre cada una de las 4 posiciones
        if intento[i] == secreto[i]:     # Coincide número y posición
            fama += 1
        elif intento[i] in secreto:      # El número existe pero en otra posición
            toque += 1

    return toque, fama  # Devuelve los totales de toques y famas

# Inicio del juego
secreto = generar_numero_secreto()  # Genera el número secreto
intentos = 0  # Inicializa contador de intentos

print("Bienvenido a TOQUE Y FAMA")
print("Adivina el número secreto de 4 cifras (sin repetir dígitos)")

# Bucle principal del juego
while True:
    entrada = input("Ingresa tu número: ")  # Pide número al jugador

    # Verifica que la entrada sea válida (4 dígitos únicos)
    if len(entrada) != 4 or not entrada.isdigit() or len(set(entrada)) != 4:
        print("Entrada inválida. Deben ser 4 dígitos distintos.")
        continue  # Pide nuevamente

    intento = [int(c) for c in entrada]  # Convierte entrada en lista de enteros
    intentos += 1  # Suma un intento

    toque, fama = comparar_numeros(secreto, intento)  # Compara con el número secreto

    print(f"Toques: {toque}, Famas: {fama}")  # Muestra resultado del intento

    if fama == 4:  # Si todos los dígitos están bien posicionados
        print(f"¡Felicidades! Descubriste el número en {intentos} intentos.")
        break  # Fin del juego
