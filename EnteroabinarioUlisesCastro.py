print("ingrese su numero entero")
try:
    N_entero = int(input())
except ValueError:
    print("Entrada inválida.")
    exit()
aux = N_entero
sum = 0
posicion = 1
while aux >= 2:
    resto = aux % 2
    aux = aux // 2
    sum = sum + (resto * posicion)
    posicion = posicion * 10
resultado_binario = sum + (aux * posicion)
print(f"tu numero binario es: {resultado_binario}")