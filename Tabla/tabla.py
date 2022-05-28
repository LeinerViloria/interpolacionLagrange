
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
        if(self._tabla[1]['values']!=[None]):
            self.error("Error lineal", 1)
        if (self._tabla[2]['values'] != [None]):
            self.error("Error cuadratico", 2)
        if (self._tabla[3]['values'] != [None]):
            self.error("Error cubico", 3)

    def error(self, nombre, col):
        valores = []
        interpolacion = self._tabla[col]['values']
        original = self._tabla[4]['values']
        n = len(original)
        for i in range(n):
            if(interpolacion!=None):
                division = (original[i]-interpolacion[i])/(original[i]) if (original[i]!=None and interpolacion[i]!=None) else None
                resultAbs = abs(division)*100 if (division != None) else None
                valores.append(resultAbs)
        self.definirColumna(nombre, valores)