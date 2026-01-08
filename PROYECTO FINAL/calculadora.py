# Módulo Calculadora
# Este archivo define la clase Calculadora, su estructura y sus métodos.

class Calculadora:
    """
    Clase que implementa una calculadora básica con historial de operaciones.
    Ahora soporta múltiples valores en una sola operación.
    """
    
    # El constructor inicializa una lista para los números y el historial.
    def __init__(self):
        self._numeros = []
        self._historial = []

    # Propiedad para un acceso controlado a la lista de números.
    @property
    def numeros(self):
        """Getter que retorna la lista actual de números."""
        return self._numeros

    @numeros.setter
    def numeros(self, nueva_lista):
        # Valida que la entrada sea una lista y que todos sus elementos sean números.
        if isinstance(nueva_lista, list) and all(isinstance(n, (int, float)) for n in nueva_lista):
            self._numeros = nueva_lista
        else:
            raise ValueError("El valor debe ser una lista de números (enteros o flotantes).")

    # Método privado que guarda la operación en el historial.
    def _registrar_operacion(self, operador, resultado):
        """Formatea la operación con múltiples números y la agrega al historial."""
        # Une los números de la lista con el operador para crear un string.
        # Ejemplo: [10, 5, 2] y '+' se convierte en "10 + 5 + 2"
        operacion_str = f" {operador} ".join(map(str, self._numeros))
        
        self._historial.append({
            'operacion': operacion_str,
            'resultado': resultado
        })

    # Métodos para las operaciones matemáticas, ahora adaptados para listas.
    def sumar(self):
        resultado = sum(self._numeros)
        self._registrar_operacion('+', resultado)
        return resultado

    def restar(self):
        # Inicia con el primer número y resta los siguientes.
        resultado = self._numeros[0]
        for num in self._numeros[1:]:
            resultado -= num
        self._registrar_operacion('-', resultado)
        return resultado

    def multiplicar(self):
        # Inicia con el primer número y multiplica por los siguientes.
        resultado = self._numeros[0]
        for num in self._numeros[1:]:
            resultado *= num
        self._registrar_operacion('*', resultado)
        return resultado

    def dividir(self):
        # Inicia con el primer número y divide por los siguientes.
        resultado = self._numeros[0]
        for num in self._numeros[1:]:
            if num == 0:
                return "Error: División por cero no permitida."
            resultado /= num
        self._registrar_operacion('/', resultado)
        return resultado
    
    def potenciar(self):
        # La potencia sigue siendo una operación de dos números por definición.
        if len(self._numeros) != 2:
            return "Error: La potencia solo se puede calcular entre dos números."
        
        resultado = self._numeros[0] ** self._numeros[1]
        self._registrar_operacion('^', resultado)
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