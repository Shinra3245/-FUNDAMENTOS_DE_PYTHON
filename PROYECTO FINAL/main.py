from calculadora import Calculadora

# Esta función ahora "traduce" una expresión con múltiples valores.
def interpretar_expresion(expresion):
    """
    Toma el texto del usuario (ej. "10 + 5 + 3") y lo descompone en
    una lista de números y un operador.
    """
    for operador in ['+', '-', '*', '/', '^']:
        if operador in expresion:
            partes = expresion.split(operador)
            try:
                # Convierte todas las partes de la expresión en números flotantes.
                numeros = [float(p.strip()) for p in partes]
                return numeros, operador
            except ValueError:
                # Si alguna parte no es un número, la expresión no es válida.
                return None, None
    return None, None

# La función main() organiza y ejecuta el flujo principal del programa.
def main():
    """Función principal que ejecuta el programa de la calculadora."""
    calc = Calculadora()
    print("Calculadora Multi-operación. Escribe 'salir' para terminar o 'historial' para ver operaciones.\n")

    while True:
        entrada = input("Ingresa la operación (ejemplo: 5 + 10 + 3): ")

        if entrada.strip().lower() == "salir":
            print("¡Hasta pronto!")
            break

        if entrada.strip().lower() == "historial":
            calc.ver_historial()
            continue

        numeros, operador = interpretar_expresion(entrada)

        if not numeros:
            print("Expresión no válida. Usa el formato: número operador número ... (ej. 5 + 10 + 3)\n")
            continue
        
        # Asigna la lista de números a la instancia de la calculadora.
        calc.numeros = numeros

        if operador == '+':
            print("Resultado:", calc.sumar())
        elif operador == '-':
            print("Resultado:", calc.restar())
        elif operador == '*':
            print("Resultado:", calc.multiplicar())
        elif operador == '/':
            print("Resultado:", calc.dividir())
        elif operador == '^':
            print("Resultado:", calc.potenciar())

if __name__ == "__main__":
    main()