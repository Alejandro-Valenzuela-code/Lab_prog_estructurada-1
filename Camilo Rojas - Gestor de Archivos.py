# Camilo Rojas - Gestor de Archivos en Python

import os  # Importa el módulo os para trabajar con archivos del sistema

# Función para crear un archivo nuevo
def crear_archivo(nombre):
    with open(nombre, "w") as f:  # Abre el archivo en modo escritura (crea o sobrescribe)
        print(f"Archivo '{nombre}' creado.")

# Función para sobrescribir el contenido de un archivo
def sobrescribir_archivo(nombre):
    texto = input("Nuevo contenido: ")  # Pide contenido al usuario
    with open(nombre, "w") as f:  # Abre en modo escritura
        f.write(texto + "\n")  # Escribe el contenido con salto de línea
        print(f"Archivo '{nombre}' sobrescrito.")

# Función para agregar texto al final de un archivo existente
def agregar_a_archivo(nombre):
    n = int(input("¿Cuántas líneas deseas agregar?: "))  # Pregunta cuántas líneas agregar
    with open(nombre, "a") as f:  # Abre en modo agregar
        for i in range(n):  # Repite según la cantidad de líneas
            linea = input(f"Línea {i+1}: ")  # Solicita cada línea
            f.write(linea + "\n")  # Agrega la línea al archivo
        print(f"{n} línea(s) agregadas a '{nombre}'.")

# Función para leer y mostrar el contenido de un archivo
def leer_archivo(nombre):
    if os.path.exists(nombre):  # Verifica que el archivo exista
        with open(nombre, "r") as f:  # Abre en modo lectura
            print(f"Contenido de '{nombre}':\n")  # Muestra el nombre
            print(f.read())  # Imprime el contenido completo
    else:
        print("El archivo no existe.")

# Función para eliminar un archivo
def eliminar_archivo(nombre):
    if os.path.exists(nombre):  # Verifica que exista
        os.remove(nombre)  # Elimina el archivo
        print(f"Archivo '{nombre}' eliminado.")
    else:
        print("El archivo no existe.")

# Menú principal del gestor
def menu():
    while True:  # Ciclo que muestra el menú continuamente
        print("\n--- GESTOR DE ARCHIVOS ---")
        print("1. Crear archivo")
        print("2. Sobrescribir archivo")
        print("3. Agregar texto")
        print("4. Leer archivo")
        print("5. Eliminar archivo")
        print("6. Salir")
        
        opcion = input("Selecciona una opción (1-6): ")  # Pide opción al usuario

        if opcion == "1":
            nombre = input("Nombre del archivo: ")
            crear_archivo(nombre)
        elif opcion == "2":
            nombre = input("Nombre del archivo: ")
            sobrescribir_archivo(nombre)
        elif opcion == "3":
            nombre = input("Nombre del archivo: ")
            agregar_a_archivo(nombre)
        elif opcion == "4":
            nombre = input("Nombre del archivo: ")
            leer_archivo(nombre)
        elif opcion == "5":
            nombre = input("Nombre del archivo: ")
            eliminar_archivo(nombre)
        elif opcion == "6":
            print("Saliendo del gestor...")
            break  # Finaliza el programa
        else:
            print("Opción inválida. Intenta nuevamente.")

# Llamada al menú principal
menu()
