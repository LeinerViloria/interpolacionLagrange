from tkinter import*
from tkinter import ttk

class visual ():
    def __init__(self, Titulo,mensaje1,mensaje2,mensaje3) :
      self.raiz = Tk() 
      self.raiz.title(Titulo)
      self.raiz.geometry("1200x600")
      self.lbl1 = ttk.Label(self.raiz, text=mensaje1)
      self.lbl2 = ttk.Label(self.raiz, text=mensaje2)
      self.lbl3 = ttk.Label(self.raiz, text=mensaje3)
      self.tabla = ttk.Treeview(self.raiz, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))

    def definircolumnas(self):
        self.tabla.column("#0", width=120)
        self.tabla.column("col1", width=120, anchor=CENTER)
        self.tabla.column("col2", width=120, anchor=CENTER)
        self.tabla.column("col3", width=120, anchor=CENTER)
        self.tabla.column("col4", width=120, anchor=CENTER)
        self.tabla.column("col5", width=120, anchor=CENTER)
        self.tabla.column("col6", width=120, anchor=CENTER)
        self.tabla.column("col7", width=120, anchor=CENTER)

    def cabeceras(self,datos):
        self.tabla.heading("#0", text="X", anchor=CENTER)
        indice = len(datos)
        for i in range(indice):
            nombrecolumna = "col"+str(i)
            if(nombrecolumna!="col0"):   
                self.tabla.heading(nombrecolumna, text=datos[i]["name"], anchor=CENTER)
            
    
    def insertar (self, datos):
        length = len(datos)
        valoresX = datos[0]["values"]
        filasLength = len(valoresX)

        for i in range(filasLength):
            self.tabla.insert("", END, text=valoresX[i], values=(datos[1]["values"][i],datos[2]["values"][i],
                                                                 datos[3]["values"][i], datos[4]["values"][i],
                                                                 datos[5]["values"][i], datos[6]["values"][i],
                                                                 datos[7]["values"][i]))

    def pintar(self):
        self.tabla.pack()
        self.lbl1.pack()
        self.lbl2.pack()
        self.lbl3.pack()
        self.raiz.mainloop() #una ventana debe permanecer en un bucle infinito



