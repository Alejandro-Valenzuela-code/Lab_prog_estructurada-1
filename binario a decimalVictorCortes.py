"""def solucion(binario):
    while(hay dígitos en binario):
        tomar dígito
        multiplicar por 2^posición
        acumular resultado
    mostrar número decimal
"""

def binario_a_decimal(binario):
    # Verifica que la entrada sea solo de 0 y 1
    for digito in binario:
        if digito not in ('0', '1'):
            print("Entrada inválida: solo se permiten 0 y 1.")
            return

    decimal = 0
    potencia = len(binario) - 1

    # Recorre cada dígito binario
    for digito in binario:
        decimal += int(digito) * (2 ** potencia)
        potencia -= 1

    print(f"El número binario {binario} equivale a {decimal} en decimal.")
    return decimal

# Ejemplo de uso
binario = input("Ingrese un número binario: ")
binario_a_decimal(binario)
