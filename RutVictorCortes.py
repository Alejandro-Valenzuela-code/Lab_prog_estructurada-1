"""
def solucion(rut):
    mientras(haya rut ingresado):
        limpiar entrada eliminando puntos y guiones
        separar parte numérica
        calcular dígito verificador con módulo 11
        mostrar solo el dígito final (DV)
"""

def limpiar_rut(rut: str) -> str:
    """Quita puntos, guiones y espacios y pasa a minúsculas."""
    return "".join(ch for ch in rut if ch.isalnum()).lower()

def calcular_dv(rut_sin_dv: str) -> str:
    """Calcula solo el dígito verificador (DV) del RUT."""
    suma = 0
    factor = 2
    for d in reversed(rut_sin_dv):
        suma += int(d) * factor
        factor += 1
        if factor > 7:
            factor = 2
    resto = suma % 11
    resultado = 11 - resto
    if resultado == 11:
        return "0"
    if resultado == 10:
        return "k"
    return str(resultado)

# Programa principal
rut = input("Ingrese el número del RUT (sin dígito verificador): ")
dv = calcular_dv(limpiar_rut(rut))
print("El dígito verificador es:", dv)
