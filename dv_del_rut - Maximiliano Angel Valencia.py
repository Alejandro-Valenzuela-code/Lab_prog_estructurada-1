def calcular_dv(rut): # Se crea la función con el nombre "calcular_dv" y se le asigna el parametro "rut".
    multiplicador = 2 # A la variable "multiplicador" se le asigna el valor 2.
    suma = 0 # A la variable "suma" se le asigna el valor 0.

    while rut != 0: # Ciclo "while" que se ejecutará mientras "rut" sea distinto de 0.
        digito = rut % 10 # A la variable "digito" se le asigna "rut" mod 10, que dará 0 o 1 dependiendo si es o no una division justa.
        suma += digito * multiplicador # La variable "suma" será la suma de (suma(digito x multiplicador)).
        rut = rut // 10 # A "rut" se le asigna (rut // 10) que es dividir "rut" en 10, pero que solo de enteros (Elimina los decimales).
        multiplicador += 1 # A la variable "multiplicador" se le suma 1 cada vez que se repite y se le vuelve asignar "multiplicador". Ej: 1ro será = 1, después = 2 y asi sucesivamente.
        if multiplicador > 7: # Si "multiplicador" es mayor que 7. 
            multiplicador = 2 # Al "multiplicador" se le asigna 2.

    resto = suma % 11 # A la variable "resto" se le asigna (suma % 11) que es "suma" mod 11.
    dv = 11 - resto # A "dv" se le asigna (11 - resto).

    if dv == 11: # Si "dv" es igual a 11 retorna "0".
        return "0"
    elif dv == 10: # Si no se cumple lo anterior y si se cumple que "dv" sea igual a 10 retorna "K".
        return "K"
    else: # Si no se cumple nada de lo anterior, se retorna "dv" como cadena de texto.
        return str(dv)

### Main ###
while True: # Ciclo "while" que se repetirá sin parar hasta que se haga "break".
    try: # Se intenta hacer lo que esta en su interior.
        rut = int(input("Ingrese el RUT (sin dígito verificador): ")) # A la variable "rut" se le asigna un "int(input(...))" ya que pide ingresar el RUT y este será un entero.
        if rut < 0: # Si "rut" es menor a 0, dirá que el RUT es inválido. 
            print("RUT inválido")
        else: # Si no se cumple lo anterior.
            print(f"El dígito verificador del RUT {rut} es: {calcular_dv(rut)}") # Dirá el RUT y su digito verificador.
            break # Rompe el ciclo "while".
    except ValueError: # Si no se logro hacer se ejecuta lo siguiente.
        print("Error")
