from Lagrange.Interpolacion import Interpolacion

class InterpolacionLineal(Interpolacion):
    def __init__(self, x0, y0, x1, y1):
        Interpolacion.__init__(self, x0, y0, x1, y1)

    #Metodos privados
    def __p0(self):
        return (self.x-self.x1)/(self.x0-self.x1)

    def __p1(self):
        return (self.x-self.x0)/(self.x1-self.x0)

    def calcularPx(self):
        self.p = self.y0 * self.__p0() + self.y1 * self.__p1()
        return self.simplificar()
