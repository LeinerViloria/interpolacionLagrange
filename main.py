import asyncio
from Tabla.tabla import tabla
from Lagrange.InterpolacionCuadratica import InterpolacionCuadratica
from Lagrange.InterpolacionCubica import InterpolacionCubica
from Lagrange.InterpolacionLineal import InterpolacionLineal
from MathFunctions.Funciones import Funciones
from Grafica.Grafica import Grafica
from interfaz.visual import visual

#Variable para los valores de X
x = [-1,-0.5,0,0.5]
#Variable para los valores de y, en caso de no haber ecuacion
y = []
#y = [0,1.3862,1.7917,2.1]

#Desde dónde hasta dónde quiere evaluar las ecuaciones
desde=-1
hasta=3
limite = range(desde,hasta+1)

#Para saber qué correr
ejecutarLineal = True
ejecutarCuadratico = True
ejecutarCubico = True

#En caso de no tener valores en Y, puede escribir su ecuacion aqui
ecuacion = "1/(1+25*x**2)"

lineal = [None, None]
cuadratica = [None, None]
cubica = [None, None]

JSON = tabla()
function = Funciones()

def calcularY(ecuacion, rango, valoresX):
    aux = []
    if "ln" in ecuacion:
        for i in rango:
            resultado = function.ln(valoresX[i])
            if (resultado.is_rational):
                resultado = resultado.p / resultado.q
            aux.append(resultado)
    else:
        ecuacion = "" if (ecuacion.strip() == "") else function.parsear(ecuacion)
        if (ecuacion != ""):
            for i in rango:
                if(i<len(valoresX)):
                    resultado = function.funcionIngresada(ecuacion, valoresX[i])
                    if(resultado.is_rational):
                        resultado = resultado.p/resultado.q
                    aux.append(resultado)
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
    if(len(x)>=2):
        i1 = InterpolacionLineal(x[0], y[0], x[1], y[1])
        px = i1.calcularPx()
        result = "Math error" if (function.contieneZoo(px)) else px
        valores = None if result == "Math error" else getValores(i1)

        return [result, valores]
    else:
        return [None,None]

async def inter2():
    if(len(x)>=3):
        i2 = InterpolacionCuadratica(x[0], y[0], x[1], y[1], x[2], y[2])
        px = i2.calcularPx()
        result = "Math error" if (function.contieneZoo(px)) else px
        valores = None if result == "Math error" else getValores(i2)
        return [result, valores]
    else:
        return [None,None]

async def inter3():
    if(len(x)==4):
        i3 = InterpolacionCubica(x[0], y[0], x[1], y[1], x[2], y[2], x[3], y[3])
        px = i3.calcularPx()
        result = "Math error" if (function.contieneZoo(px)) else px
        valores = None if result == "Math error" else getValores(i3)
        return [result, valores]
    else:
        return [None, None]

if ((str(ecuacion).strip() != "" or y[0]!=None) and (ejecutarLineal==True or ejecutarCuadratico==True or ejecutarCubico==True)):
    if(ejecutarLineal):
        lineal = asyncio.run(inter1())
    if(ejecutarCuadratico):
        cuadratica = asyncio.run(inter2())
    if(ejecutarCubico):
        cubica = asyncio.run(inter3())


    JSON.definirColumna("X", list(limite))
    JSON.definirColumna("Lineal", lineal[1])
    JSON.definirColumna("Cuadratica", cuadratica[1])
    JSON.definirColumna("Cubica", cubica[1])
    JSON.definirColumna("Original", calcularY(ecuacion, range(len(list(limite))), list(limite)))
    JSON.calcularErrores()

    tablavisual = visual("Interpolación de lagrange", "Interpolacion lineal: {}".format(lineal[0]),
                         "Interpolacion cuadratica: {}".format(cuadratica[0]),
                         "Interpolacion cubica: {}".format(cubica[0]))
    tablavisual.definircolumnas()
    tablavisual.cabeceras(JSON.getTabla())
    tablavisual.insertar(JSON.getTabla())
    tablavisual.pintar()

    grafica = Grafica("Interpolacion", "Eje x", "Eje y")
    grafica.recibirDatos(JSON.getTabla(),1,2,3,4)
    asyncio.run(grafica.crearGrafico())

    if(str(ecuacion).strip() != ""):
        grafica2 = Grafica("Errores", "Eje x", "Eje y")
        grafica2.recibirDatos(JSON.getTabla(), 5, 6, 7)
        asyncio.run(grafica2.crearGrafico())
    else:
        print("No hay una ecuacion para calcular los errores")

else:
    print("No es posible calcular, por favor ingrese valores y asegurese de elegir, al menos, una interpolacion")