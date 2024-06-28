import random 
import math
diccionario = {}
notas = [1,2,3,4,5]

def agregar_alumno():
    print()
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    edad = int(input("Ingrese la edad del alumno: "))
    nivel = input("Ingrese el curso del alumno(Ej: 1ro, 2do, 3ro, etc.): ")
    notas = random.randrange(1,10)

    diccionario[nivel] = {
        "nombre":nombre, 
        "apellido":apellido,
        "edad":edad,
        "nivel":nivel
    }
    print()
    print("Alumno agregado correctamente.\n")

def listar_alumnos():
    if diccionario:
        print()
        print("Listado de alumnos")
        for nivel, i in diccionario.items():
            print()
            print(f"Nombre: {i["nombre"]}")
            print(f"Apellido: {i["apellido"]}")
            print(f"Edad: {i["edad"]}")
            print(f"Nivel: {nivel}")
            print(f"Notas: {notas}")
            print()
    else:
        print("No hay alumnos registrados.\n")        

def buscar_alumno():

    print()
    nivel_buscar = input("Ingresa el nivel del alumno(Ej: 1ro, 2do, 3ro, etc.): ")
    encontrar = False
    for nivel, i in diccionario.items():
        if nivel == nivel_buscar:
            encontrar = True 
            print()
            print("Alumno encontrado:")
            print()
            print(f"Nombre: {i["nombre"]}")
            print(f"Apellido: {i["apellido"]}")
            print(f"Edad: {i["edad"]}")
            print(f"Nivel: {nivel}")
            print(f"Notas: {notas}")
            print()
            break 
    if encontrar:
        return
    print(f"No se encontró ninguna película con el código '{nivel_buscar}'.\n")

def promedio():
    notas

def guardar_en_archivo():
    print()
    with open("Archivo_alumnos.txt",'w') as archivo:
        for nivel, i in diccionario.items():
            archivo.write(f"Nombre: {i["nombre"]}\n")
            archivo.write(f"Apellido: {i["apellido"]}\n")
            archivo.write(f"Edad: {i["edad"]}\n")
            archivo.write(f"Nivel: {nivel}\n")
            archivo.write(f"Notas: {notas}\n")
            archivo.write("\n")
    print(f"Películas guardadas correctamente en Archivo_alumnos.txt\n")

def mostrar_menu():
    print("---- MENÚ ----")
    print("1. Agregar alumno")
    print("2. Listar todos los alumnos")
    print("3. Buscar alumnos por nivel")
    print("4. Calcular la nota promedio de los alumnos")
    print("5. Salir del programa y guardar")
    print()
    
    while True:
            try:
                opcion = int(input("Seleccione una opción: "))
                if opcion>=1 and opcion<=5:
                    return opcion
                else:
                    print("Opción inválida. Intente nuevamente.")
            except ValueError:
                print("Error: Ingrese un número válido para la opción.")   