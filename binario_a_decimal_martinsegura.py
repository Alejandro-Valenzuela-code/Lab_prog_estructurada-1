binum = input("INgrese el numero en binario: ")[::-1]
decnum = 0
for i in range(len(binum)):
    decnum += int(binum[i])* 2**i
print(f"El numero en decimal es: {decnum}")
