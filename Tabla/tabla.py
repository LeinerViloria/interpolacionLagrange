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