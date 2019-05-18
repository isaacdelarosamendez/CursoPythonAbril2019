from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)

ventana = Tk()
ventana.title("Mi aplicación")
ventana.geometry("300x200")


lblnombre = ttk.Label(ventana,text="Nombre")
lblnombre.place(x=10, y=10)

txtnombre = ttk.Entry(ventana)
txtnombre.place(x=10, y=50)

btn = ttk.Button(ventana,text="Clic me please")
btn.place(x=10, y=80)
ventana.mainloop()


