import os
# Está expuesto a poner letras y cualquier número, haciendo que falle.
def crear(nombre_del_archivo):
    if os.path.exists(nombre_del_archivo):
        print('\n---------------------------------------------------------------')
        print(f'El archivo "{nombre_del_archivo}.txt" ya existe.')
    else:
        with open(nombre_del_archivo+'.txt','w') as variable_para_que_funcione_el_open:
            print('\n---------------------------------------------------------------')
            print(f'Se ha creado el archivo "{nombre_del_archivo+'.txt'}"')

def buscar(nombre_del_archivo):
    if os.path.exists(nombre_del_archivo):
        print('\n---------------------------------------------------------------')
        print('El archivo SÍ existe.')
    else:
        print('\n---------------------------------------------------------------')
        print('El archivo NO existe.')
        
def leer(nombre_del_archivo):
    if os.path.exists(nombre_del_archivo):
        with open(nombre_del_archivo,'r',encoding='utf-8') as texto:
            lineas=texto.readlines()
            print('\nCONTENIDO:\n---------------------------------------------------------------')
        for i in lineas:
            print(i.replace('\n',''))
    else:
        print('\n---------------------------------------------------------------')
        print('El archivo no existe para su lectura.')
        
def escribir(nombre_del_archivo, contenido):
    if os.path.exists(nombre_del_archivo):
        with open(nombre_del_archivo,'w',encoding='utf-8') as texto:
            texto.write(contenido)
            print('\n---------------------------------------------------------------')
            print('TEXTO GUARDADO CON ÉXITO.')
    else:
        print('\n---------------------------------------------------------------')
        print('El archivo no existe para escribir.')  
    
def agregar(nombre_del_archivo, contenido):
    if os.path.exists(nombre_del_archivo):
        with open(nombre_del_archivo,'a',encoding='utf-8') as texto:
            texto.write(contenido)
            print('\n---------------------------------------------------------------')
            print('TEXTO GUARDADO CON ÉXITO.')
    else:
        print('\n---------------------------------------------------------------')
        print('El archivo no existe para escribir.')  
        
def borrar(nombre_del_archivo):
    if os.path.exists(nombre_del_archivo):
        print('\n---------------------------------------------------------------')
        print(f'¿ESTÁS SEGURO DE ELIMINAR EL ARCHIVO "{nombre_del_archivo}"?')
        print('1 = CANCELAR\n2 = CONTINUAR')
        confirmacion=input('> ')
        if confirmacion!='2':
            print('\n---------------------------------------------------------------')
            print('ACCIÓN CANCELADA.') 
        elif confirmacion=='2':
            print('\n---------------------------------------------------------------')
            print('EL ARCHIVO HA SIDO ELIMINADO.')
            os.remove(nombre_del_archivo)
    else:
        print('\n---------------------------------------------------------------')
        print(f'El archivo "{nombre_del_archivo}" no existe.')    
                   
print('\n---------------------------------------------------------------')
print('GESTOR DE ARCHIVOS')
accion=10

while accion!=7:
    print('---------------------------------------------------------------\n')
    print('¿Qué deseas hacer?')
    print('1 = Crear\n2 = Buscar\n3 = Leer\n4 = Escribir/Reescribir\n5 = Agregar\n6 = Borrar\n7 = Salir')
    accion=input('> ')
    if accion=='1':
        print('\n')
        nombre_del_archivo=input('¿Cómo quieres que se llame el archivo de texto? (".txt" se añade automáticamente): ')
        crear(nombre_del_archivo)
    elif accion=='2':
        print('\n')
        nombre_del_archivo=input('¿Cómo se llama el archivo?, recuerda agregar ".txt" al final: ')
        buscar(nombre_del_archivo)
    elif accion=='3':
        print('\n')
        nombre_del_archivo=input('¿Qué archivo quieres leer?, recuerda agregar ".txt" al final: ')
        leer(nombre_del_archivo)
    elif accion=='4':
        print('\n')
        nombre_del_archivo=input('¿Cuál es el nombre del archivo donde quieres escribir desde cero?, recuerda agregar ".txt" al final: ')
        print('')
        print('ESCRIBE EL TEXTO:')
        contenido=str(input(''))
        escribir(nombre_del_archivo,contenido)
    elif accion=='5':
        print('\n')
        nombre_del_archivo=input('¿Cuál es el nombre del archivo donde quieres agregar texto?, recuerda agregar ".txt" al final: ')
        print('')
        print('ESCRIBE EL TEXTO:')
        contenido=str(input(''))
        agregar(nombre_del_archivo,contenido)
    elif accion=='6':
        print('\n')
        nombre_del_archivo=input('¿Cuál es el nombre del archivo que quieres eliminar?, recuerda agregar ".txt" al final: ')
        borrar(nombre_del_archivo)
    elif accion=='7':
        break
    else: 
        print('\n---------------------------------------------------------------')
        print('OPCIÓN INVÁLIDA. La entrada "'+accion+'" no es una opción.')
print('\n---------------------------------------------------------------')
print('GESTIÓN FINALIZADA')
print('---------------------------------------------------------------\n')