def calcular_dv(rut):
    suma = 0
    multiplicador = 2

    for d in reversed(str(rut)):
        suma += int(d) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    resto = 11 - (suma % 11)
    if resto == 11:
        return '0'
    if resto == 10:
        return 'K'
    return str(resto)

rut = input("Ingrese rut sin el digito despues del guión: ")

dv = calcular_dv(rut)
print("El dígito verificador es:", dv)