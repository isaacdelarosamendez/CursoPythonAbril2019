from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)

from tkinter import messagebox
# Crea una clase Python para definir el interfaz de usuario de
# la aplicación. Cuando se cree un objeto del tipo 'Aplicacion'
# se ejecutará automáticamente el método __init__() qué 
# construye y muestra la ventana con todos sus widgets: 

class Aplicacion():
    def __init__(self):
        raiz = Tk()
        raiz.geometry('300x200')
        raiz.title('Alumnos')
        # Crear widgets.
        lblnombres = ttk.Label(raiz,text="Nombres")
        txtnombres = ttk.Entry(raiz)
        lblapellidos =ttk.Label(raiz,text="Apellidos")
        txtapellidos = ttk.Entry(raiz)
        btnGuardar = Button(text="Guardar alumno", command=lambda: self.Save(txtnombres))
        #    Posicionarla en la ventana.
        lblnombres.place(x=10, y=10)
        txtnombres.place(x=100, y=10)
        lblapellidos.place(x=10, y=50)
        txtapellidos.place(x=100, y=50)
        btnGuardar.place(x=10, y=100)
        raiz.mainloop()
    def Mess(self,mensaje):
        messagebox.showinfo("Mensaje", mensaje)
    #funcion que ejecuta el boton de SAVE, pide como parametro un puntero a textbox
    def Save(self,txtnombres):
        if(txtnombres.get() == ""):
            self.Mess("Ingrese el nombre del alumno")
            txtnombres.focus()

Aplicacion()   