# Camilo Rojas - Dígito Verificador de RUT

# Solicita el número base del RUT sin el dígito verificador
rut = input("Ingresa el RUT sin dígito verificador: ")

# Reversamos el RUT para aplicar correctamente los factores
reverso = rut[::-1]

# Lista de factores cíclicos [2, 3, 4, 5, 6, 7]
factores = [2, 3, 4, 5, 6, 7]

# Suma acumulada para aplicar el algoritmo de módulo 11
suma = 0

# Recorremos los dígitos del RUT y multiplicamos por los factores cíclicos
for i in range(len(reverso)):
    suma += int(reverso[i]) * factores[i % len(factores)]

# Calculamos el dígito verificador usando módulo 11
resto = 11 - (suma % 11)

# Convertimos el resultado a dígito verificador según reglas del RUT chileno
if resto == 11:
    digito = "0"
elif resto == 10:
    digito = "K"
else:
    digito = str(resto)

# Mostramos el RUT completo con guion y dígito verificador
print(f"El RUT completo es: {rut}-{digito}")
