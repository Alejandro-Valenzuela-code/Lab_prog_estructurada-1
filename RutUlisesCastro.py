Sum = 0
factor = 2
print("INGRESE RUT (sin dígito verificador)")
try:
    rut = int(input())
except ValueError:
    print("Entrada inválida. Debe ingresar solo números.")
    exit()
print(f"el rut leido es {rut}")
Aux = rut
while Aux > 0:
    resto = Aux % 10
    Aux = Aux // 10
    Sum = Sum + (factor * resto)
    factor = factor + 1
    if factor == 8:
        factor = 2
resto_final = Sum % 11
if resto_final == 0:
    print("el digito verificador= 0")
elif resto_final == 1:
    print("el digito verificador es: K")
else:
    dv = 11 - resto_final
    print(f"El digito verificador es {dv}")