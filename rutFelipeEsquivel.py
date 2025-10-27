sum=0
factor=2
print ("Ingrese su rut")
rut= int (input ())
aux=rut
while aux>0:
#>
    resto= aux%10
    aux= (aux-resto)//10
    sum= sum+factor*resto
    factor= factor+1
    if factor==8:
        factor=2
resto= sum%11
if resto==0:
     print (f"el rut ingresado es {rut},y el dv es {resto}")
else:
     if resto==1:
         print("el dv es = k")
     else:
        print(f"el dv es {11-resto}")
