"""Modulo provee matemáticas """

import math
import logging
import sys

# Configuración del logging para escribir tanto en archivo como en consola
# Crear un formateador que usaremos para ambos handlers


formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Configurar el logger
logger = logging.getLogger('CalculadoraCientifica')
logger.setLevel(logging.INFO)

# Handler para archivo
file_handler = logging.FileHandler('calculadora.log')
file_handler.setFormatter(formatter)

# Handler para consola
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# Añadir ambos handlers al logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


class CalculadoraCientifica:
    """Class representando a CalculadoraCientifica """

    def __init__(self):
        logger.info("Iniciando calculadora científica")

    def validar_numeros(self, *args):
        """Valida que los argumentos sean números"""
        for num in args:
            if not isinstance(num, (int, float)):
                raise TypeError(
                    f"Se esperaba un número, se recibió {type(num)}")

    # Operaciones básicas
    def sumar(self,
              a,
              b):
        """Suma dos números"""
        self.validar_numeros(a, b)
        logger.info("Sumando %d + %d", a, b)
        return a + b

    def restar(self,
               a,
               b):
        """Resta dos números"""
        self.validar_numeros(a, b)
        logger.info("Restando %d - %d", a, b)
        return a - b

    def multiplicar(self, a, b):
        """Multiplica dos números"""
        self.validar_numeros(a, b)
        logger.info("Multiplicando %d * %d", a, b)
        return a * b

    def dividir(self, a, b):
        """Divide dos números"""
        self.validar_numeros(a, b)
        if b == 0:
            logger.error("Intento de división por cero")
            raise ValueError("No se puede dividir por cero")
        logger.info("Dividiendo %d / %d", a, b)
        return a / b

    # Operaciones avanzadas
    def potencia(self, base, exponente):
        """Calcula la potencia de un número"""
        self.validar_numeros(base, exponente)
        logger.info("Calculando %d ^ %d", base, exponente)
        return math.pow(base, exponente)

    def raiz_cuadrada(self, numero):
        """Calcula la raíz cuadrada de un número"""
        self.validar_numeros(numero)
        if numero < 0:
            logger.error(
                "Intento de calcular raíz cuadrada de número negativo: %d", numero)
            raise ValueError(
                "No se puede calcular la raíz cuadrada de un número negativo")
        logger.info("Calculando raíz cuadrada de %d", numero)
        return math.sqrt(numero)

    def logaritmo_natural(self, numero):
        """Calcula el logaritmo natural de un número"""
        self.validar_numeros(numero)
        if numero <= 0:
            logger.error(
                "Intento de calcular logaritmo de número no positivo: %d", numero)
            raise ValueError(
                "No se puede calcular el logaritmo de un número menor o igual a cero")
        logger.info("Calculando logaritmo natural de %d", numero)
        return math.log(numero)

    def logaritmo_base_10(self, numero):
        """Calcula el logaritmo en base 10 de un número"""
        self.validar_numeros(numero)
        if numero <= 0:
            logger.error(
                "Intento de calcular logaritmo base 10 de número no positivo: {%d}", numero)
            raise ValueError(
                "No se puede calcular el logaritmo de un número menor o igual a cero")
        logger.info("Calculando logaritmo base 10 de %d", numero)
        return math.log10(numero)

    def seno(self, angulo):
        """Calcula el seno de un ángulo en radianes"""
        self.validar_numeros(angulo)
        logger.info("Calculando seno de %d radianes", angulo)
        return math.sin(angulo)

    def coseno(self, angulo):
        """Calcula el coseno de un ángulo en radianes"""
        self.validar_numeros(angulo)
        logger.info("Calculando coseno de %d radianes", angulo)
        return math.cos(angulo)

    def tangente(self, angulo):
        """Calcula la tangente de un ángulo en radianes"""
        self.validar_numeros(angulo)
        logger.info("Calculando tangente de %d radianes", angulo)
        return math.tan(angulo)


def main():
    """Crear instancia de la calculadora"""

    calc = CalculadoraCientifica()

    try:
        # Ejemplos de uso de operaciones básicas
        num1 = int(input("Introduce el primer numero a sumar: "))
        num2 = int(input("Introduce el segundo numero a sumar: "))
        print(f"Suma de {num1} + {num2} = {calc.sumar(num1, num2)}")
        num1 = int(input("Introduce el primer numero a restar: "))
        num2 = int(input("Introduce el segundo numero a restar: "))
        print(f"Resta de {num1} - {num2} = {calc.restar(num1, num2)}")
        num1 = int(input("Introduce el primer numero a multiplicar: "))
        num2 = int(input("Introduce el segundo numero a multiplicar: "))
        print(f"Multiplicación de {num1} * {num2} = {calc.multiplicar(num1, num2)}")
        num1 = int(input("Introduce el primer numero a dividir: "))
        num2 = int(input("Introduce el segundo numero a dividir: "))
        print(f"División de {num1} / {num2} = {calc.dividir(num1, num2)}")

        # Ejemplos de uso de operaciones avanzadas
        print("\n=== Operaciones Avanzadas ===")
        num1 = int(input("Introduce el primer numero a potencia: "))
        num2 = int(input("Introduce el segundo numero a potencia: "))
        print(f"Potencia de {num1}^{num2} = {calc.potencia(num1, num2)}")
        num1 = int(input("Introduce el numero a raíz cuadrada: "))
        print(f"Raíz cuadrada de {num1} = {calc.raiz_cuadrada(num1)}")
        num1 = int(input("Introduce el numero a logaritmo natural: "))
        print(f"Logaritmo natural de {num1} = {calc.logaritmo_natural(num1)}")
        num1 = int(input("Introduce el numero a logaritmo a base 10: "))
        print(f"Logaritmo base 10 de {num1} = {calc.logaritmo_base_10(num1)}")

        # Ejemplos de funciones trigonométricas
        print("\n=== Funciones Trigonométricas ===")
        angulo = math.pi/2
        print(f"Seno de π/2 = {calc.seno(angulo)}")
        print(f"Coseno de π/2 = {calc.coseno(angulo)}")
        print(f"Tangente de π/4 = {calc.tangente(math.pi/4)}")

        # Ejemplo de manejo de errores
        print("\n=== Prueba de Manejo de Errores ===")
        print("Intentando dividir por cero:")
        calc.dividir(5, 0)

    except ValueError as e:
        logger.error("Error de valor: %s", e)
        print(f"Error de valor: {e}")
    except TypeError as e:
        logger.error("Error de tipo: %s", e)
        print(f"Error de tipo: {e}")
    except ImportError as e:
        logger.error("Error inesperado: %s", e)
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
