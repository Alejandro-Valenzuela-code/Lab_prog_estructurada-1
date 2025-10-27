binario = input("Ingresa un número binario: ")

decimal = 0 
potencia = 0  

for digito in reversed(binario):
    if digito == '1':       
        decimal += 2 ** potencia
    potencia += 1             

print("El número decimal es:", decimal)