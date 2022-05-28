import matplotlib.pyplot as plt

class Grafica():
    def __init__(self, titulo, ejeX, ejeY):
        self.n = None
        self.titulo=titulo
        self.ejeX = ejeX
        self.ejeY = ejeY
        self.X = None
        self.data1 = None
        self.data2 = None
        self.data3 = None

    def mostrarData(self):
        print(self.data)

    def _definirData1(self, valores):
        self.data1=valores

    def _definirData2(self, valores):
        self.data2=valores

    def _definirData3(self, valores):
        self.data3=valores

    def recibirDatos(self, datos, i1, i2, i3):
        self.n = len(datos[0]['values'])
        self.X = datos[0]['values'];
        if(i1<self.n):
            if (datos[i1]['values'] != [None]):
                self._definirData1(datos[i1]['values'])
        if(i2<self.n):
            if (datos[i2]['values'] != [None]):
                self._definirData2(datos[i2]['values'])
        if(i3<self.n):
            if (datos[i3]['values'] != [None]):
                self._definirData3(datos[i3]['values'])


    async def crearGrafico(self):
        plt.xlabel(self.ejeX)
        plt.ylabel(self.ejeY)
        plt.title(self.titulo)
        if(self.data1!=None):
            plt.plot(self.X,self.data1)
        if(self.data2!=None):
            plt.plot(self.X,self.data2)
        if(self.data3!=None):
            plt.plot(self.X,self.data3)
        plt.show()