import math
import sympy

class Funciones():
    def __init__(self):
        sympy.init_printing()
        self.x = sympy.symbols('x')

    def parsear(self, ecuacion):
        return sympy.parse_expr(ecuacion)

    def funcionIngresada(self, ecuacion, valor):
        return ecuacion.subs(self.x, valor)

    def contieneZoo(self, resultado):
        return "zoo" in str(resultado)

    def ln(self, valor):
        return math.log(valor)

