"""
def solucion(numero):
    mientras(numero > 0):
        obtener residuo de dividir por 2
        agregar residuo al resultado
        dividir número por 2
    invertir resultado
    mostrar número binario
"""

def decimal_a_binario(numero):
    # Verificamos que el número sea válido
    if numero == 0:
        return "0"

    binario = ""  # Cadena vacía para construir el número binario
    while numero > 0:
        residuo = numero % 2  # Obtenemos el residuo (0 o 1)
        binario = str(residuo) + binario  # Lo agregamos al inicio del resultado
        numero = numero // 2  # Dividimos el número entre 2 (división entera)

    return binario


# Ejemplo de uso:
numero = int(input("Ingrese un número decimal: "))
print("El número en binario es:", decimal_a_binario(numero))
