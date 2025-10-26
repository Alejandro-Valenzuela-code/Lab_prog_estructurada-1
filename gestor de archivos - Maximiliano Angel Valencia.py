# Crear
# Escribir
# Leer
# Borrar
# Import os

# Para abrir o crear archivo
# W: Write ; R: Read ; A: Append

import os  # Importa módulo para manejo de archivos y sistema

# Función para crear un archivo nuevo
def crear():
    nombre = input("\nIngrese un nombre para crear un archivo: \n> ")  # Pide nombre
    with open(f"{nombre}.txt", "w") as f:  # Crea/abre archivo en modo escritura
        print(f"\nSe creo un archivo con el nombre {nombre}.\n")  # Mensaje de confirmación

# Función para sobreescribir un archivo existente
def sobreescribir():
    nombre = input("\nIngrese un nombre para el archivo a sobreeescribir: \n> ")  # Pide archivo
    while True:
        print(f"¿Desea sobreescribir el archivo {nombre}.txt y cambiar su contenido?")
        confirmar = input("Ingrese Y si esta deacuerdo o N si desea cancelar la acción: \n> ").upper()  # Confirma
        while True:
            if confirmar == "N":  # Si no, cancela
                break
            if confirmar != "Y" and confirmar != "N":  # Validación
                confirmar = input("Ingrese su respuesta, solo con Y o N: \n> ").upper()
            if confirmar == "Y":
                if os.path.exists(nombre):  # Comprueba que exista
                    try:
                        with open(f"{nombre}.txt", "w") as f:  # Abre en modo escritura
                            escritura = input("Ingrese un texto: ")  # Pide texto
                            f.write(escritura + "\n")  # Escribe en archivo
                        print(f"\nSe sobreescribio el archivo con el nombre {nombre}.\n")
                    except Exception as e:
                        print(f"Error: \n, {e}\n")  # Mensaje de error
                else:
                    print("No se encontro el archivo...")
                    break
        break  # Sale del bucle

# Función para agregar texto a un archivo existente
def agregar():
    nombre = input("\nIngrese un nombre para el archivo a modificar: \n> ")  # Pide archivo
    n = int(input("Cuantos quiere agregar: "))  # Número de textos a agregar
    while n < 0:  # Validación incorrecta (se repetirá hasta n<=0)
        n = int(input("Número ingresado no valido, ingrese otro: "))  # Mensaje error
    while n != 0:
        if os.path.exists(nombre):  # Comprueba existencia
            try:
                with open(f"{nombre}.txt", "a") as f:  # Abre en modo anexar
                    escritura = input("Texto agregar: ")  # Pide texto
                    f.write(" " + escritura)  # Anexa texto
                print(f"\nSe anexó/agregó a un archivo con el nombre {nombre}.\n")
            except Exception as e:
                print(f"Error: \n, {e}\n")
            n -= 1  # Reduce contador
        else:
            print("No se encontro el archivo...")
            break

# Función para leer y mostrar el contenido de un archivo
def lectura():
    nombre = input("\nIngrese el nombre del archivo a leer: \n> ")  # Pide archivo
    try:
        with open(f"{nombre}.txt", "r") as f:  # Abre en modo lectura
            lectura = f.read()  # Lee todo el contenido
            print("\n|==========Contenido del archivo==========|\n")
            print(lectura)  # Muestra contenido
            print("\n|=========================================|\n")
        print(f"Se leyó un archivo con el nombre {nombre}.\n")
    except Exception as e:
        print(f"Error: \n, {e}\n")  # Mensaje de error

# Función para eliminar un archivo existente
def eliminar():
    nombre = input("\nIngrese el nombre del archivo a eliminar: \n> ")  # Pide archivo
    while True:
        print(f"\n¿Desea eliminar el archivo {nombre}.txt para siempre?")
        confirmar = input("\nIngrese Y si esta deacuerdo o N si desea cancelar la acción: \n> ").upper()
        while True:
            if confirmar == "N":  # Cancela
                break
            if confirmar != "Y" and confirmar != "N":  # Validación
                confirmar = input("\nIngrese su respuesta, solo con Y o N: \n> ").upper()
            if confirmar == "Y":
                try:
                    os.remove(f"{nombre}.txt")  # Elimina archivo
                    print(f"\nSe elimino el archivo con el nombre {nombre}.\n")
                except Exception as e:
                    print(f"Error: \n, {e}\n")  # Mensaje de error
                break
        break

# Menú principal de acciones
while True:
    print("""
|==========Acciones de archivo==========|
    1.- Crear
    2.- Sobreescribir
    3.- Anexar/agregar 
    4.- Leer 
    5.- Eliminar
    6.- Ordenar
    7.- Salir 
|=======================================|
 """)
    seleccion = input("Ingrese el número de la acción que desea: \n> ")  # Pide opción

    if seleccion == "1":  # Crear
        crear()
    elif seleccion == "2":  # Sobreescribir
        sobreescribir()
    elif seleccion == "3":  # Agregar
        agregar()
    elif seleccion == "4":  # Leer
        lectura()
    elif seleccion == "5":  # Eliminar
        eliminar()
    elif seleccion == "6": # Ordenar
        print("Sin terminar...")
    elif seleccion == "7":  # Salir
        break
    else:
        print("Error número invalido, ingrese otro: \n> ")  # Mensaje error de opción
