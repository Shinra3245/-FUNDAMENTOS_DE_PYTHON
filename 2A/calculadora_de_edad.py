import datetime

def calcular_edad():
    while True:
        # Se solicita la fecha de nacimiento y se valida que no esté vacía
        fecha_nacimiento_str = input("Ingrese su fecha de nacimiento (DD-MM-AAAA): ")
        if not fecha_nacimiento_str:
            print("Error: La fecha no puede estar vacía.")
            continue

        try:
            # Se analiza la fecha ingresada por el usuario
            dia, mes, anio = map(int, fecha_nacimiento_str.split('-'))
            
            # Validar que el año sea mayor a 1900
            if anio < 1900:
                print("Error: El año de nacimiento debe ser mayor de 1900.")
                continue

            # Validar que la fecha sea válida (maneja días y meses inválidos)
            fecha_nacimiento = datetime.date(anio, mes, dia)
            
            # Se obtiene la fecha actual
            fecha_actual = datetime.date.today()
            
            # Se calcula la edad
            edad = fecha_actual.year - fecha_nacimiento.year
            
            # Se ajusta la edad si el cumpleaños aún no ha pasado este año
            if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
                edad -= 1
            
            print(f"Su edad es: {edad} años.")
            break # El bucle termina si la fecha es válida y la edad se calcula
        
        except ValueError:
            print("Error: Formato de fecha inválido o fecha inexistente. Por favor, use el formato DD-MM-AAAA.")

# Llamar a la función para ejecutar el programa
calcular_edad()