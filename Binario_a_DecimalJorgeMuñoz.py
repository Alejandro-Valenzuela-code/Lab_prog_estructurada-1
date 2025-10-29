### Algoritmo numero binario a decimal ###

while True:
    nbinario = input("Ingrese un numero binario (ej. 101)\n>")
    
    # convierte de binario a decimal
    try:
        decimal = int(nbinario, 2)
        break
    except ValueError:
        print("Error. El numero solo debe tener 1 o 0.")


print(f"El número binario {nbinario} equivale a {decimal} en decimal.")