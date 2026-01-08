def sistema_evaluacion():
    # Se utiliza un bucle para validar la cantidad de alumnos
    while True:
        try:
            num_alumnos = int(input("Ingrese el número de alumnos a evaluar: "))
            if num_alumnos <= 0:
                print("El número de alumnos debe ser un entero positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    # Se utiliza un bucle para validar la cantidad de materias
    while True:
        try:
            num_materias = int(input("Ingrese el número de materias por alumno: "))
            if num_materias <= 0:
                print("El número de materias debe ser un entero positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    alumnos = {}

    for i in range(num_alumnos):
        print(f"\n--- Alumno {i+1} ---")
        
        # Validación de campos de alumno
        while True:
            nombre = input("Nombre del alumno: ").strip()
            matricula = input("Matrícula del alumno: ").strip()
            if not nombre or not matricula:
                print("Error: Los campos de nombre y matrícula no pueden estar vacíos.")
            else:
                break
        
        calificaciones = []
        for j in range(num_materias):
            while True:
                try:
                    calif = float(input(f"Calificación de la materia {j+1}: "))
                    calificaciones.append(calif)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número para la calificación.")
        
        promedio = sum(calificaciones) / num_materias
        
        estado = "Aprobado" if promedio > 6 else "Reprobado"
        
        # Se guarda la información en el diccionario
        alumnos[matricula] = {
            "nombre": nombre,
            "calificaciones": calificaciones,
            "promedio": promedio,
            "estado": estado
        }
    
    # Se imprime el reporte de resultados
    print("\n\n--- Reporte de Evaluación ---")
    for matricula, datos in alumnos.items():
        print(f"\nMatrícula: {matricula}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Promedio: {datos['promedio']:.2f}")
        print(f"Estado: {datos['estado']}")

# Se llama a la función para ejecutar el sistema
sistema_evaluacion()
