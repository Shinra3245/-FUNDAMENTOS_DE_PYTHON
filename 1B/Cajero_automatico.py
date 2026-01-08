#Ejercicio 1-1B - Cajero automático
# 1. Creación de las variables que representan el inventario por cada denominación de billete.
billetes_1000 = 10
billetes_500 = 10
billetes_200 = 10
billetes_100 = 10
billetes_50 = 10
billetes_20 = 10

# Bucle principal para mantener el programa en ejecución
while True:
    # 3. Mensaje de inicio al sistema y solicitud del monto a retirar del cajero.
    print("\n\n--- Dispensadora de Billetes ---")
    print(f"Inventario disponible: $1000({billetes_1000}), $500({billetes_500}), $200({billetes_200}), $100({billetes_100}), $50({billetes_50}), $20({billetes_20})")

    try:
        entrada = input("\nIngrese el monto a retirar (0 para salir): ")
        monto = int(entrada)
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")
        continue

    # Condición de salida del bucle
    if monto == 0:
        print("\nGracias por utilizar el cajero. ¡Hasta luego!")
        break

    # Validación para montos negativos
    if monto < 0:
        print("Error: No se puede retirar un monto negativo.")
        continue

    # Variable para guardar el monto original y trabajar sobre una copia
    monto_restante = monto

    # 2. Creación de las variables para el número de billetes a entregar por cada denominación.
    entregar_1000 = 0
    entregar_500 = 0
    entregar_200 = 0
    entregar_100 = 0
    entregar_50 = 0
    entregar_20 = 0

    # Lógica para calcular billetes a entregar (de mayor a menor para dar la menor cantidad de billetes)
    
    # Denominación $1000
    if monto_restante >= 1000 and billetes_1000 > 0:
        necesarios = monto_restante // 1000
        # Se entregan los billetes necesarios o los que haya disponibles
        a_entregar = min(necesarios, billetes_1000)
        entregar_1000 = a_entregar
        monto_restante -= a_entregar * 1000

    # Denominación $500
    if monto_restante >= 500 and billetes_500 > 0:
        necesarios = monto_restante // 500
        a_entregar = min(necesarios, billetes_500)
        entregar_500 = a_entregar
        monto_restante -= a_entregar * 500

    # Denominación $200
    if monto_restante >= 200 and billetes_200 > 0:
        necesarios = monto_restante // 200
        a_entregar = min(necesarios, billetes_200)
        entregar_200 = a_entregar
        monto_restante -= a_entregar * 200

    # Denominación $100
    if monto_restante >= 100 and billetes_100 > 0:
        necesarios = monto_restante // 100
        a_entregar = min(necesarios, billetes_100)
        entregar_100 = a_entregar
        monto_restante -= a_entregar * 100

    # Denominación $50
    if monto_restante >= 50 and billetes_50 > 0:
        necesarios = monto_restante // 50
        a_entregar = min(necesarios, billetes_50)
        entregar_50 = a_entregar
        monto_restante -= a_entregar * 50

    # Denominación $20
    if monto_restante >= 20 and billetes_20 > 0:
        necesarios = monto_restante // 20
        a_entregar = min(necesarios, billetes_20)
        entregar_20 = a_entregar
        monto_restante -= a_entregar * 20

    # === VALIDACIÓN Y FINALIZACIÓN DE LA TRANSACCIÓN ===
    
    # Si monto_restante es 0, el retiro es exitoso
    if monto_restante == 0:
        print(f"Retiro exitoso por ${monto}. Se entregan los siguientes billetes:")
        if entregar_1000 > 0:
            print(f"- {entregar_1000} billete(s) de $1000")
        if entregar_500 > 0:
            print(f"- {entregar_500} billete(s) de $500")
        if entregar_200 > 0:
            print(f"- {entregar_200} billete(s) de $200")
        if entregar_100 > 0:
            print(f"- {entregar_100} billete(s) de $100")
        if entregar_50 > 0:
            print(f"- {entregar_50} billete(s) de $50")
        if entregar_20 > 0:
            print(f"- {entregar_20} billete(s) de $20")
            
        # Actualizar el inventario del cajero
        billetes_1000 -= entregar_1000
        billetes_500 -= entregar_500
        billetes_200 -= entregar_200
        billetes_100 -= entregar_100
        billetes_50 -= entregar_50
        billetes_20 -= entregar_20
    else:
        # Si sobró dinero, es que no se pudo completar el monto con los billetes disponibles
        print("Lo sentimos, el cajero no cuenta con la combinación de billetes")
        print("suficiente para satisfacer el importe solicitado. No se dispensará ningún billete.")
        
        
        
        
