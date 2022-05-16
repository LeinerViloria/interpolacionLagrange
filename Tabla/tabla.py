import json

class tabla():
    def __init__(self):
        self._tabla = []

    def definirColumna(self, nombre, valores):
        aux = {
            "name":nombre,
            "values":valores
        }
        self._tabla.append(aux)

    def getTabla(self):
        return self._tabla

    def calcularErrores(self):
        if(self._tabla[1]['values']!=None):
            self.errorLineal("Error lineal", 1)
        if (self._tabla[2]['values'] != None):
            self.errorLineal("Error cuadratico", 2)
        if (self._tabla[3]['values'] != None):
            self.errorLineal("Error cubico", 3)

    def errorLineal(self, nombre, col):
        valores = []
        interpolacion = self._tabla[col]['values']
        original = self._tabla[4]['values']
        n = len(original)
        for i in range(n):
            valores.append(abs((original[i]-interpolacion[i])/(original[i]))*100)
        self.definirColumna(nombre, valores)