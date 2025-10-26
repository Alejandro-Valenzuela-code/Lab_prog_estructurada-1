print('------------------------------------------------------------------------')
print('Ingrese un número entero común y corriente para convertirlo a binario.')
numero_decimal=int(input('>'))
numero_binario=bin(numero_decimal)[2:]
print('El número',numero_decimal,'en binario es',numero_binario)
print('------------------------------------------------------------------------')