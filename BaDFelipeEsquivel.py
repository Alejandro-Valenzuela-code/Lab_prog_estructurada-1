
Numero = int(input("Ingrese el número binario: "))

print(f"El número binario leído es {Numero}")

Suma = 0
Potencia = 0
Auxiliar = Numero

while Auxiliar >= 10:
    Digito = Auxiliar % 10
    Suma += Digito * (2 ** Potencia)
    Potencia += 1
    Auxiliar = (Auxiliar - Digito) // 10

Suma += Auxiliar * (2 ** Potencia)

print(f"El número binario es {Numero} y el decimal es: {Suma}")