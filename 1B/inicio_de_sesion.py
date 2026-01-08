#Ejercicio 2-1B - Inicio de sesión 
# 1. Variables que almacenan al usuario y contraseña a las que se les dará el acceso.
usuario_correcto = "admin"
clave_correcta = "1234"

# Variables para el control de intentos
intentos = 3
login_exitoso = False

# === INICIO DE LA LÓGICA DEL PROGRAMA ===

# El bucle se ejecutará mientras queden intentos disponibles
while intentos > 0:
    # 2. Mensaje de inicio al sistema, intentos que tienes, solicitud de usuario y contraseña.
    print("\n\n--- Sistema de Inicio de Sesión ---")
    print(f"Intentos restantes: {intentos}")

    # Solicitar credenciales
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")

    # Se verifica si alguno de los campos está vacío
    if usuario == "" or clave == "":
        print("Error de autentificación: Usuario y contraseña no pueden estar vacíos.")
    
    # Si no están vacíos, se verifica si las credenciales son correctas
    elif usuario == usuario_correcto and clave == clave_correcta:
        print("¡Inicio de sesión exitoso! Bienvenido.")
        login_exitoso = True
        break  # Rompe el bucle porque el inicio de sesión fue correcto
        
    # Si ninguna de las condiciones anteriores se cumple, los datos son incorrectos
    else:
        print("Error: Usuario o contraseña incorrectos.")

    # Se resta un intento en cada ciclo fallido
    intentos -= 1

# === VALIDACIÓN FINAL ===

# Si el bucle terminó y el login no fue exitoso, es porque se agotaron los intentos
if not login_exitoso:
    print("Has agotado tus 3 intentos. Acceso bloqueado.")
    
    
    