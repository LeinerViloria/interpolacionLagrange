import math

from Lagrange.InterpolacionCuadratica import InterpolacionCuadratica
from Lagrange.InterpolacionCubica import InterpolacionCubica
from Lagrange.InterpolacionLineal import InterpolacionLineal
from MathFunctions.Funciones import Funciones

x=[1, 2, 3, 4]
y=[None, None, None, None]

function = Funciones()
ecuacion = "ln(x+5) + 2/ln(x)"
#ecuacion = "2"
ecuacion = "" if (ecuacion.strip()=="") else function.parsear(ecuacion)

for i in range(len(x)):
    y[i]=function.funcionIngresada(ecuacion, x[i])

#(x0,y0,x1,y1)
def inter1():
    i1 = InterpolacionLineal(x[0], y[0], x[1], y[0])
    px = i1.calcularPx()
    result = "Math error" if (function.contieneZoo(px)) else px
    print(result)
#for value in x:
#    print("X={}, Y={}".format(value,i1.getValue(value)))

def inter2():
    i2 = InterpolacionCuadratica(x[0], y[0], x[1], y[1], x[2], y[2])
    px = i2.calcularPx()
    result = "Math error" if (function.contieneZoo(px)) else px
    print(result)

#for value in x:
#    print("X={}, Y={}".format(value,i2.getValue(value)))

def inter3():
    i3 = InterpolacionCubica(x[0], y[0], x[1], y[1], x[2], y[2], x[3], y[3])
    px = i3.calcularPx()
    result = "Math error" if (function.contieneZoo(px)) else px
    print(result)

if(str(ecuacion).strip()!=""):
    inter1()
    inter2()
    inter3()