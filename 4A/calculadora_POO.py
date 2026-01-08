# La clase Calculadora es el "molde" que define las acciones y datos
# que nuestro objeto calculadora podrá manejar.
class Calculadora:
    """
    Clase que implementa una calculadora básica con historial de operaciones.
    """
    
    # El constructor (__init__) se ejecuta al crear un objeto.
    # Inicializa los atributos que guardarán los números y el historial.
    def __init__(self):
        self._numero1 = 0
        self._numero2 = 0
        self._historial = []

    # Se usan propiedades para un acceso controlado a los atributos.
    @property
    def numero1(self):
        """Getter que retorna el valor actual de _numero1."""
        return self._numero1

    # El "setter" permite validar el dato antes de asignarlo.
    # Esto protege al objeto de recibir valores incorrectos.
    @numero1.setter
    def numero1(self, nuevo_numero1):
        if isinstance(nuevo_numero1, (int, float)):
            self._numero1 = nuevo_numero1
        else:
            raise ValueError("Debe ser un número")

    @property
    def numero2(self):
        """Getter que retorna el valor actual de _numero2."""
        return self._numero2

    @numero2.setter
    def numero2(self, nuevo_numero2):
        if isinstance(nuevo_numero2, (int, float)):
            self._numero2 = nuevo_numero2
        else:
            raise ValueError("Debe ser un número")

    # Método privado que centraliza la lógica para guardar cada operación.
    def _registrar_operacion(self, operador, resultado):
        """Agrega un diccionario a la lista _historial con los detalles de la operación."""
        self._historial.append({
            'operacion': f"{self._numero1} {operador} {self._numero2}",
            'resultado': resultado
        })

    # Métodos para las operaciones matemáticas.
    def sumar(self):
        resultado = self._numero1 + self._numero2
        self._registrar_operacion('+', resultado)
        return resultado

    def restar(self):
        resultado = self._numero1 - self._numero2
        self._registrar_operacion('-', resultado)
        return resultado

    def multiplicar(self):
        resultado = self._numero1 * self._numero2
        self._registrar_operacion('*', resultado)
        return resultado

    def dividir(self):
        # Manejo de un caso especial para evitar un error en el programa.
        if self._numero2 == 0:
            return "Error: División por cero no permitida."
        resultado = self._numero1 / self._numero2
        self._registrar_operacion('/', resultado)
        return resultado

    def ver_historial(self):
        """Muestra el historial de operaciones de forma ordenada."""
        if not self._historial:
            print("No hay operaciones en el historial.")
            return

        print("\n--- Historial de Operaciones ---")
        for i, operacion in enumerate(self._historial, 1):
            print(f"{i}. {operacion['operacion']} = {operacion['resultado']}")
        print("--------------------------------\n")


# Esta función auxiliar "traduce" el texto del usuario a datos que la calculadora puede usar.
def interpretar_expresion(expresion):
    """
    Toma el texto del usuario (ej. "10 + 5") y lo descompone en números y un operador.
    """
    for operador in ['+', '-', '*', '/']:
        if operador in expresion:
            partes = expresion.split(operador)
            if len(partes) == 2:
                try:
                    num1 = float(partes[0].strip())
                    num2 = float(partes[1].strip())
                    return num1, num2, operador
                except ValueError:
                    return None
    return None

# La función main() organiza y ejecuta el flujo principal del programa.
def main():
    """Función principal que ejecuta el programa de la calculadora."""
    calc = Calculadora()
    print("Calculadora Básica. Escribe 'salir' para terminar o 'historial' para ver operaciones.\n")

    # El bucle 'while True' mantiene la aplicación activa, esperando la entrada del usuario.
    while True:
        entrada = input("Ingresa la operación (ejemplo: 5 + 5): ")

        if entrada.strip().lower() == "salir":
            print("¡Hasta pronto!")
            break

        if entrada.strip().lower() == "historial":
            calc.ver_historial()
            continue

        resultado_interpretacion = interpretar_expresion(entrada)

        if not resultado_interpretacion:
            print("Expresión no válida. Usa el formato: número operador número (ej. 5 + 5)\n")
            continue

        num1, num2, operador = resultado_interpretacion
        calc.numero1 = num1
        calc.numero2 = num2

        if operador == '+':
            print("Resultado:", calc.sumar())
        elif operador == '-':
            print("Resultado:", calc.restar())
        elif operador == '*':
            print("Resultado:", calc.multiplicar())
        elif operador == '/':
            print("Resultado:", calc.dividir())

# Esta línea asegura que la función main() se ejecute solo cuando el script se corre directamente.
if __name__ == "__main__":
    main()