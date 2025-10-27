print("ingrese su numero binario")
try:
    binario = int(input())
except ValueError:
    print("Entrada inválida.")
    exit()
aux = binario
sum = 0
exponente = 0
while aux > 0:
    resto = aux % 10
    aux = aux // 10
    sum = sum + (resto * (2 ** exponente))
    exponente = exponente + 1
print(f"tu numero entero: {sum}")