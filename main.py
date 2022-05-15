import asyncio
from JSON.json import json
from Lagrange.InterpolacionCuadratica import InterpolacionCuadratica
from Lagrange.InterpolacionCubica import InterpolacionCubica
from Lagrange.InterpolacionLineal import InterpolacionLineal
from MathFunctions.Funciones import Funciones

x=[1, 4, 6, 8]
y=[None, None, None, None]
limite = x[2]

JSON = json()
function = Funciones()
ecuacion = "ln(x)"

if "ln" in ecuacion:
    for i in range(len(x)):
        y[i]=function.ln(x[i])
else:
    ecuacion = "" if (ecuacion.strip()=="") else function.parsear(ecuacion)
    for i in range(len(x)):
        y[i]=function.funcionIngresada(ecuacion, x[i])

def getValores(interpolacion):
    for i in range(limite):
       print("X={}, Y={}".format(i+1,interpolacion.getValue(i+1)))

#print(y)
#(x0,y0,x1,y1)
async def inter1():
    i1 = InterpolacionLineal(x[0], y[0], x[1], y[1])
    px = i1.calcularPx()
    result = "Math error" if (function.contieneZoo(px)) else px
    print("Interpolacion lineal")
    print(result)
    getValores(i1)
#for value in x:
#    print("X={}, Y={}".format(value,i1.getValue(value)))

async def inter2():
    i2 = InterpolacionCuadratica(x[0], y[0], x[1], y[1], x[2], y[2])
    px = i2.calcularPx()
    result = "Math error" if (function.contieneZoo(px)) else px
    print("Interpolacion cuadratica")
    print(result)
    getValores(i2)

#for value in x:
#    print("X={}, Y={}".format(value,i2.getValue(value)))

async def inter3():
    i3 = InterpolacionCubica(x[0], y[0], x[1], y[1], x[2], y[2], x[3], y[3])
    px = i3.calcularPx()
    result = "Math error" if (function.contieneZoo(px)) else px
    print("Interpolacion cubica")
    print(result)
    getValores(i3)

if(str(ecuacion).strip()!=""):
    print("")
    asyncio.run(inter1())
    asyncio.run(inter2())
    asyncio.run(inter3())