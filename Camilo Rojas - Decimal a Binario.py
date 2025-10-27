# Camilo Rojas - Decimal a Binario

# Solicita un número decimal
decimal = int(input("Ingresa un número decimal: "))

# Convierte a binario usando bin() y elimina el prefijo '0b'
binario = bin(decimal)[2:]

# Muestra el resultado
print(f"El número binario equivalente es: {binario}")
