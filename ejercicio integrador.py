nombres = []
notas = []

while True:
    print("\n===== SISTEMA DE GESTIÓN ACADÉMICA =====")
    print("1. Registrar estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Estadísticas generales")
    print("4. Buscar estudiante por nombre")
    print("5. Mostrar aprobados y reprobados")
    print("6. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        nombre = input("Nombre del estudiante: ")

        while True:
            nota = float(input("Nota (0-100): "))
            if 0 <= nota <= 100:
                break
            print("La nota debe estar entre 0 y 100.")

        nombres.append(nombre)
        notas.append(nota)
        print("Estudiante registrado correctamente.")

    elif opcion == 2:
        if len(nombres) == 0:
            print("No hay estudiantes registrados.")
        else:
            print("\nLista de estudiantes:")
            for i in range(len(nombres)):
                print(nombres[i], "-", notas[i])


    elif opcion == 3:
        if len(nombres) == 0:
            print("No hay datos para calcular estadísticas.")
        else:
            suma = 0
            mayor = notas[0]
            menor = notas[0]
            nombre_mayor = nombres[0]
            nombre_menor = nombres[0]
            aprobados = 0
            reprobados = 0

            for i in range(len(notas)):
                suma = suma + notas[i]

                if notas[i] > mayor:
                    mayor = notas[i]
                    nombre_mayor = nombres[i]

                if notas[i] < menor:
                    menor = notas[i]
                    nombre_menor = nombres[i]

                if notas[i] >= 60:
                    aprobados += 1
                else:
                    reprobados += 1

            promedio = suma / len(notas)

            print("Promedio general:", promedio)
            print("Nota más alta:", nombre_mayor, mayor)
            print("Nota más baja:", nombre_menor, menor)
            print("Aprobados:", aprobados)
            print("Reprobados:", reprobados)

    elif opcion == 4:
        buscar = input("Ingrese el nombre del estudiante a buscar: ")

        encontrado = False

        for i in range(len(nombres)):
            if nombres[i].lower() == buscar.lower():
                print("Estudiante encontrado:")
                print("Nombre:", nombres[i])
                print("Nota:", notas[i])
                encontrado = True

        if encontrado == False:
            print("Estudiante no encontrado.")


    elif opcion == 5:
        if len(nombres) == 0:
            print("No hay estudiantes registrados.")
        else:
            print("\nAprobados:")
            for i in range(len(nombres)):
                if notas[i] >= 60:
                    print(nombres[i], "-", notas[i])

                    print("\nReprobados:")
            for i in range(len(nombres)):
                if notas[i] < 60:
                    print(nombres[i], "-", notas[i])

    elif opcion == 6:
        print("Programa finalizado.")
        break
    else:
            print("Opción inválida.")