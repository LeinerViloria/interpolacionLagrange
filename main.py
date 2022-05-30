import asyncio
from Tabla.tabla import tabla
from Lagrange.InterpolacionCuadratica import InterpolacionCuadratica
from Lagrange.InterpolacionCubica import InterpolacionCubica
from Lagrange.InterpolacionLineal import InterpolacionLineal
from MathFunctions.Funciones import Funciones

x = [1,4,6,8]
y = []
#y = [1,3,0,-8]
limite = range(1,7)#[-5,5]

lineal = [None, None]
cuadratica = [None, None]
cubica = [None, None]

JSON = tabla()
function = Funciones()
ecuacion = "Ln(x)"

def calcularY(ecuacion, rango, valoresX):
    aux = []
    if "ln" in ecuacion:
        for i in rango:
            aux.append(function.ln(valoresX[i]))
    else:
        ecuacion = "" if (ecuacion.strip() == "") else function.parsear(ecuacion)
        if (ecuacion != ""):
            for i in rango:
                aux.append(function.funcionIngresada(ecuacion, valoresX[i]))
        else:
            aux.append(None)
    return aux

if(len(y)==0):
    y = calcularY(ecuacion, range(0,4), x)

def getValores(interpolacion):
    aux=[]
    for i in limite:
        aux.append(interpolacion.getValue(i))
    return aux

async def inter1():
    i1 = InterpolacionLineal(x[0], y[0], x[1], y[1])
    px = i1.calcularPx()
    result = "Math error" if (function.contieneZoo(px)) else px
    valores = None if result == "Math error" else getValores(i1)

    return [result, valores]

async def inter2():
    i2 = InterpolacionCuadratica(x[0], y[0], x[1], y[1], x[2], y[2])
    px = i2.calcularPx()
    result = "Math error" if (function.contieneZoo(px)) else px
    valores = None if result == "Math error" else getValores(i2)
    return [result, valores]

async def inter3():
    i3 = InterpolacionCubica(x[0], y[0], x[1], y[1], x[2], y[2], x[3], y[3])
    px = i3.calcularPx()
    result = "Math error" if (function.contieneZoo(px)) else px
    valores = None if result == "Math error" else getValores(i3)
    return [result, valores]

if (str(ecuacion).strip() != "" or y[0]!=None):
    lineal = asyncio.run(inter1())
    cuadratica = asyncio.run(inter2())
    #cubica = asyncio.run(inter3())

    print("Interpolacion lineal: {}".format(lineal[0]))
    print("Interpolacion cuadratica: {}".format(cuadratica[0]))
    print("Interpolacion cubica: {}".format(cubica[0]))

    JSON.definirColumna("X", list(limite))
    JSON.definirColumna("Lineal", lineal[1])
    JSON.definirColumna("Cuadratica", cuadratica[1])
    JSON.definirColumna("Cubica", cubica[1])
    JSON.definirColumna("Original", calcularY(ecuacion, range(len(list(limite))), list(limite)))
    JSON.calcularErrores()
    print(JSON.getTabla())
else:
    print("No es posible calcular")