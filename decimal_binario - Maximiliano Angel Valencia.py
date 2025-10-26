def decimal_binario(decimal):  # Se define la función "decimal_binario" con el parámetro "decimal".
    binario = 0                # Se inicializa la variable "binario" en 0. Guardará el número convertido a binario.
    exponente = 0              # Se inicializa la variable "exponente" en 0. Representa la posición del dígito en base 10.

    while decimal != 0:        # Se ejecuta mientras "decimal" no sea 0 (mientras queden divisiones por hacer).

        binario = binario + ((decimal % 2) * (10 ** exponente)) # Se calcula el residuo de dividir entre 2 (bit menos significativo)
                                                                # y se multiplica por 10^exponente para colocarlo en su posición correcta.
        decimal = decimal // 2  # Se divide "decimal" entre 2 (división entera), para obtener el siguiente bit.
        exponente = exponente + 1  # Se incrementa el exponente en 1 (para avanzar una posición a la izquierda en el binario).

    return binario              # Devuelve el número binario calculado.

### main ###
while(True):                    # Inicia un bucle infinito para solicitar datos hasta obtener una entrada válida.
    try:                        # Intenta ejecutar el bloque de código que puede generar errores.
        decimal = int(input("Ingrese un número decimal: ")) # Pide al usuario ingresar un número y lo convierte a entero.
        if decimal < 0:                             # Comprueba si el número es negativo.
            print("Número inválido")                # Si lo es, muestra un mensaje de error.
        print(f"El valor en binario del número {decimal}, es: {decimal_binario(decimal)}") # Muestra el resultado de la conversión.
        break                                       # Termina el bucle después de realizar la conversión correctamente.
    except ValueError:                              # Si ocurre un error (por ejemplo, si se ingresa texto no numérico).
        print("Error")                              # Muestra un mensaje de error y vuelve a pedir un número.
