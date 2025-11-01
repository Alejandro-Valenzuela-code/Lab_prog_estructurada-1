numero = int(input("ingrese un numero: "))
residuo = 0
numbin = ""

while numero != 0:
    residuo = numero % 2
    numero = numero // 2
    numbin += str(residuo)

print(f"El numero en binario es: {numbin[::-1]}")
