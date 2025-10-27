decimal = int(input("\n Ingrese número decimal para transformar: "))

binario = 0
exp = 0

while decimal != 0:
    binario += (decimal % 2) * (10 ** exp)
    decimal //= 2
    exp += 1

print(f"\n Su número decimal en binario es: {binario}")