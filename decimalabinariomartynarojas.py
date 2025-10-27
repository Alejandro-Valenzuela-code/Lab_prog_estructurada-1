# 3. Decimal a binario

n = int(input("Ingresa un número decimal: "))
binario = ""

if n == 0:
    binario = "0"
else:
    while n > 0:
        binario = str(n % 2) + binario
        n //= 2

print("En binario es:", binario)