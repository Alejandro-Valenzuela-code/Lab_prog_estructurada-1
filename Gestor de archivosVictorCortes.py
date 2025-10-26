"""
def solucion(gestor):
    mientras(el usuario no elija salir):
        mostrar menú de opciones
        pedir opción al usuario
        si(opción válida):
            ejecutar acción correspondiente
            si(crear archivo):
                solicitar nombre y contenido
                guardar archivo
            si(ver archivos):
                mostrar lista de archivos
            si(leer archivo):
                pedir nombre y mostrar contenido
            si(eliminar archivo):
                pedir nombre y borrar
        sino:
            mostrar "Opción inválida"
    mostrar "Programa finalizado"
"""
import os

#Funciones

def crear_archivo(nombre):
    """Crear un archivo vacio"""
    with open(nombre, "w") as f:
        pass
    print(f" Archivo '{nombre}' creado correctamente.")


def eliminar_archivo(nombre):
    """Elimina un archivo existente."""
    if os.path.exists(nombre):
        os.remove(nombre)
        print(f" Archivo '{nombre}' eliminado correctamente.")
    else:
        print(" El archivo no existe.")


def escribir_archivo(nombre):
    """Escribe (sobrescribe) contenido en el archivo (modo w)."""
    texto = input("Ingrese el texto que desea escribir: ")
    with open(nombre, "w") as f:
        f.write(texto)
    print(" Texto escrito correctamente.(modo write)")


def leer_archivo(nombre):
    """Lee y muestra el contenido del archivo (modo r)."""
    if os.path.exists(nombre):
        with open(nombre, "r") as f:
            contenido = f.read()
            print("\n Contenido del archivo:")
            print(contenido)
    else:
        print(" El archivo no existe.")


def agregar_archivo(nombre):
    """Agrega texto al final del archivo (modo a)."""
    texto = input("Ingrese el texto que desea agregar: ")
    with open(nombre, "a") as f:
        f.write("\n" + texto)
    print(" Texto agregado correctamente (modo a).")

    #menu principal

def menu():
    while True:
        print("\n--- MENÚ DE ARCHIVOS ---")
        print("1. Crear archivo")
        print("2. Eliminar archivo")
        print("3. Escribir archivo")
        print("4. Leer archivo ")
        print("5. Agregar archivo")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingresa el nombre del archivo (ej. test.txt): ")
            crear_archivo(nombre)

        elif opcion == "2":
            nombre = input("Ingresa el nombre del archivo a eliminar: ")
            eliminar_archivo(nombre)

        elif opcion == "3":
            nombre = input("Ingresa el nombre del archivo: ")
            escribir_archivo(nombre)

        elif opcion == "4":
            nombre = input("Ingresa el nombre del archivo: ")
            leer_archivo(nombre)

        elif opcion == "5":
            nombre = input("Ingresa el nombre del archivo: ")
            agregar_archivo(nombre)

        elif opcion == "6":
            print(" Saliendo del programa")
            break

        else:
            print(" Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
