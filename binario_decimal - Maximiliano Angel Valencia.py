def binario_decimal(binario): # Se crea la función con el nombre "binario_decimal" y se le asigna el parámetro "binario".
    decimal = 0               # Se inicializa la variable "decimal" en 0. Guardará el número convertido a decimal.
    exponente = 0             # Se inicializa la variable "exponente" en 0. Representa la posición del bit (empezando desde la derecha).

    while binario != 0:       # Se ejecuta mientras el valor de "binario" no sea 0 (mientras queden dígitos por procesar).

        decimal = decimal + (binario % 10) * (2 ** exponente) # Se suma al "decimal" el valor del último dígito multiplicado por 2 elevado al exponente.
        binario = binario // 10                               # Se elimina el último dígito del número binario (se avanza al siguiente).
        exponente = exponente + 1                             # Se incrementa el exponente en 1 para pasar a la siguiente posición.

    return decimal             # Devuelve el valor convertido a decimal.

### main ###
while(True):                   # Inicia un bucle infinito para pedir el número hasta que sea válido.
    try:                       # Intenta ejecutar el bloque de código que podría generar errores.
        binario = int(input("Ingrese un número binario: ")) # Solicita al usuario ingresar un número binario y lo convierte a entero.
        if binario < 0:                            # Comprueba si el número ingresado es negativo.
            print("Número inválido")               # Si es negativo, muestra un mensaje de error.
        print(f"El valor en decimal del número {binario}, es: {binario_decimal(binario)}") # Muestra el número convertido a decimal.
        break                                      # Sale del bucle después de realizar la conversión correctamente.
    except ValueError:                             # Si ocurre un error (por ejemplo, si el usuario ingresa texto).
        print("Error")                             # Muestra un mensaje de error e intenta de nuevo.