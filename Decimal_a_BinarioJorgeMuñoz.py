### Algoritmo numero decimal a binario ###

# Ingresar un numero natural
negativo = False
while True:
    try:
        ndecimal = int(input("Ingrese un numero entero en formato decimal (ej: 6): "))
        break
    except ValueError:
            print("Error, numero invalido.")


# Asignar variables
negativo = ndecimal < 0  # detectar si es negativo
nd = abs(ndecimal)  # toma el valor absoluto del numero ingresado
posicion = 1
suma = 0

# Algoritmo decimal a binario
while nd != 0:
    suma += (nd % 2) * posicion  # el mod 2 se multiplica por la posicion de derecha a izquierda
    nd //= 2  # el numero original se divide en 2 sin resto
    posicion *= 10  # la posicion avanza un digito a la izquierda

nbinario = suma


if negativo and ndecimal != 0:
    print(f"el numero ingresado es {ndecimal}\nel numero binario es: -{nbinario}")
else:
    print(f"el numero ingresado es {ndecimal}\nel numero binario es: {nbinario}")