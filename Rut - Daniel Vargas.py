print('\n==========================================================================================\n')
print('Ingresa un rut sin dígito verificador.')
while True:
    try:
        rut=abs(int(input('> ')))
        break
    except ValueError:
        print('\nError. Ingrese solo números.')
rut_en_spring=str(rut)

# Aquí es empieza a calcular el dígito verificador del rut.
factor=2
suma=0
while rut>0:
    resto=rut%10
    rut=(rut-resto)/10
    suma=suma+(factor*resto)
    factor=factor+1
    if factor==8:
        factor=2
resto=suma%11
resto=int(resto)
if resto==0:
    resto=resto
      # El dígito verificador es la variable "resto".
elif resto==1:
    resto='K' # el dígito verificador es K".
else:
    resto=11-resto #Aquí es 11-resto, y como ya se le hizo la operación, basta con poner "resto".


print('\nEl dígito del rut ingresado es el siguiente:')
print(f'{rut_en_spring}-{resto}')
print('\n==========================================================================================\n')