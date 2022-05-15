import sympy

class Interpolacion():
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.p = None
        #Con eso se maneja a X como incognita, asi podria ser Y, Z o cualquier letra
        sympy.init_printing()
        self.x = sympy.symbols('x')

    def calcularPx(self):
        print("Elije la interpolacion lineal, cuadratica o cubica")

    def simplificar(self):
        return sympy.simplify(self.p)

    def getValue(self, value):
        aux = self.p
        return aux.subs(self.x,value)
