from Lagrange.Interpolacion import Interpolacion

class InterpolacionCuadratica(Interpolacion):
    def __init__(self, x0, y0, x1, y1, x2, y2):
        Interpolacion.__init__(self, x0, y0, x1, y1)
        self.x2 = x2
        self.y2 = y2

    # Metodos privados
    def __p0(self):
        return ((self.x - self.x1)*(self.x-self.x2)) / ((self.x0 - self.x1)*(self.x0 - self.x2))

    def __p1(self):
        return ((self.x - self.x0)*(self.x-self.x2)) / ((self.x1 - self.x0)*(self.x1 - self.x2))

    def __p2(self):
        return ((self.x - self.x0)*(self.x-self.x1)) / ((self.x2 - self.x0)*(self.x2 - self.x1))

    def calcularPx(self):
        self.p = self.y0 * self.__p0() + self.y1 * self.__p1() + self.y2 * self.__p2()
        return self.simplificar()