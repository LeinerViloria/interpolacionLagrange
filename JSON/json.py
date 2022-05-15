import json

class json():
    def __init__(self):
        self._tabla = [
            {
                "nombre":"X",
                "valores":[]
            },
            {
                "nombre": "Interpolacion Lineal",
                "valores": []
            },
            {
                "nombre": "X",
                "valores": []
            }
        ]

    def definirColumna(self, nombre, valores):
        aux = {
            "name":nombre,
            "values":valores
        }
        self._tabla.append(aux)

    def getTabla(self):
        return self._tabla