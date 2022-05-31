import matplotlib.pyplot as plt

class Grafica():
    def __init__(self, titulo, ejeX, ejeY):
        self.n = None
        self.titulo=titulo
        self.ejeX = ejeX
        self.ejeY = ejeY
        self.X = None
        self.tituloData1 = None
        self.tituloData2 = None
        self.tituloData3 = None
        self.tituloData4 = None
        self.data1 = None
        self.data2 = None
        self.data3 = None
        self.data4 = None

    def mostrarData(self):
        print(self.data)

    def _definirData1(self, titulo, valores):
        self.tituloData1 = titulo
        self.data1=valores

    def _definirData2(self, titulo, valores):
        self.tituloData2 = titulo
        self.data2=valores

    def _definirData3(self, titulo, valores):
        self.tituloData3 = titulo
        self.data3=valores

    def _definirData4(self, titulo, valores):
        self.tituloData4 = titulo
        self.data4=valores

    def recibirDatos(self, datos, i1, i2, i3, iOriginal=None):
        self.n = len(datos[0]['values'])
        self.X = datos[0]['values'];
        if(i1<self.n):
            if (datos[i1]['values'] != [None]):
                self._definirData1(datos[i1]['name'],datos[i1]['values'])
        if(i2<self.n):
            if (datos[i2]['values'] != [None]):
                self._definirData2(datos[i2]['name'],datos[i2]['values'])
        if(i3<self.n):
            if (datos[i3]['values'] != [None]):
                self._definirData3(datos[i3]['name'],datos[i3]['values'])
        if(iOriginal!=None):
            if (datos[iOriginal]['values'] != [None]):
                self._definirData4(datos[iOriginal]['name'],datos[iOriginal]['values'])

    async def crearGrafico(self):
        plt.xlabel(self.ejeX)
        plt.ylabel(self.ejeY)
        plt.title(self.titulo)
        if(self.data1!=None):
            plt.plot(self.X,self.data1, label=self.tituloData1)
        if(self.data2!=None):
            plt.plot(self.X,self.data2, label=self.tituloData2)
        if(self.data3!=None):
            plt.plot(self.X,self.data3, label=self.tituloData3)
        if (self.data4 != None):
            plt.plot(self.X, self.data4, label=self.tituloData4)
        if(self.tituloData1!=None or self.tituloData2!=None or self.tituloData3!=None or self.tituloData4!=None):
            plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
            plt.tight_layout()
        plt.grid(axis='y', color='gray', linestyle='dashed')
        plt.show()