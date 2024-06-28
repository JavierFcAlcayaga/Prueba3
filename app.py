from utilidades import agregar_alumno, listar_alumnos, buscar_alumno, promedio, guardar_en_archivo, mostrar_menu


while True:
    opcion = mostrar_menu()

    if opcion == 1:
        agregar_alumno()
    elif opcion == 2:
        listar_alumnos()
    elif opcion == 3:
        buscar_alumno()
    elif opcion == 4:
        promedio()    
    elif opcion == 5:
        guardar_en_archivo()
        break
    else:
        print("Opción no válida. Intente nuevamente.\n")
 














 