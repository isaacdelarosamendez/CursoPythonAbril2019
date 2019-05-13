from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)

from tkinter import messagebox
# Crea una clase Python para definir el interfaz de usuario de
# la aplicación. Cuando se cree un objeto del tipo 'Aplicacion'
# se ejecutará automáticamente el método __init__() qué 
# construye y muestra la ventana con todos sus widgets: 

class Aplicacion():

    def __init__(self):
        #Creamos una nueva ventana
        ventana = Tk()
        ventana.geometry('300x200')
        ventana.title('Alumnos')
        # Crear widgets.
        lblnombres = ttk.Label(ventana,text="Nombres")
        txtnombres = ttk.Entry(ventana)
        lblapellidos =ttk.Label(ventana,text="Apellidos")
        txtapellidos = ttk.Entry(ventana)
        btnSave = Button(text="Guardar", command=lambda: self.Save(txtnombres))
        #    Posicionarla en la ventana.
        #   x es Vertical, y es Horizontal
        lblnombres.place(x=10, y=10)
        txtnombres.place(x=100, y=10)
        lblapellidos.place(x=10, y=50)
        txtapellidos.place(x=100, y=50)
        btnSave.place(x=10, y=100)
        #   Permitimos que la ventana quede visible
        ventana.mainloop()

    def Mess(self,mensaje):
        messagebox.showinfo("Mensaje", mensaje)

    #funcion que ejecuta el boton de SAVE, pide como parametro un puntero a textbox
    def Save(self,txtnombres):
        if(txtnombres.get() == ""):
            self.Mess("Ingrese el nombre del alumno")
            txtnombres.focus()

Aplicacion()   