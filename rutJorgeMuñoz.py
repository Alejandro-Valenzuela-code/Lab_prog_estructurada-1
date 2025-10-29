### Algoritmo RUT ###

# Solicitar un RUT hasta que sea válido
while True:
    rut = input("Ingrese su RUT sin el dígito verificador: ")
    if rut.isdigit():
        break
    print("Error: El RUT debe contener solo números enteros. Intente nuevamente.\n")


# Variables
factor = 2
suma = 0
rut_num = int(rut)

# Algoritmo (suma ponderada con factores de 2 a 7)
while rut_num > 0:
    resto = rut_num % 10
    rut_num //= 10
    suma += factor * resto
    factor += 1
    if factor == 8:
        factor = 2  # Reiniciar factor a 2 después de 7


# Calcular digito verificador
resto = suma % 11

if resto == 0:
    dv = 0
elif resto == 1:
    dv = "k"
else:
    dv = 11 - resto
dv = str(dv)

print(f"El RUT leído es: {rut} y el dígito verificador es: {dv}")
print(f"El RUT completo es: {rut}-{dv}")