from tkinter import*
from tkinter import ttk

raiz = Tk() #raiz seria la pagina principal y le asignamos la libreria importada anteriormente

raiz.title("Interpolación de lagrange")

raiz.geometry("1200x600")

tabla = ttk.Treeview(raiz, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))

tabla.column("#0", width=80)
tabla.column("col1", width=80, anchor=CENTER)
tabla.column("col2", width=80, anchor=CENTER)
tabla.column("col3", width=80, anchor=CENTER)
tabla.column("col4", width=80, anchor=CENTER)
tabla.column("col5", width=80, anchor=CENTER)
tabla.column("col6", width=80, anchor=CENTER)
tabla.column("col7", width=80, anchor=CENTER)

tabla.heading("#0", text="X", anchor=CENTER)
tabla.heading("col1", text="Lag.Lineal", anchor=CENTER)
tabla.heading("col2", text="Lag.Cuadratica", anchor=CENTER)
tabla.heading("col3", text="Lag.Cubica", anchor=CENTER)
tabla.heading("col4", text="F. Original", anchor=CENTER)
tabla.heading("col5", text="Error Lineal", anchor=CENTER)
tabla.heading("col6", text="Error Cuadratico", anchor=CENTER)
tabla.heading("col7", text="Error Cubico", anchor=CENTER)

tabla.insert("", END, text="Algo", values=("1", "2", "3", "4","5","6"))
tabla.pack()


raiz.mainloop() #una ventana debe permanecer en un bucle infinito
