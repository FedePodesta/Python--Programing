# Grid II
from tkinter import *

ventana = Tk()

Label(ventana, text="Nombre:").grid(pady=5, row=0, column=0)
Label(ventana, text="Apellido:").grid( pady=5, row=1, column=0)

#Entry(ventana, width=40).grid(padx=5, row=0, column=1)
#Entry(ventana, width=40).grid(padx=5, row=1, column=1)

Entry(ventana).grid(padx=5, row=0, column=1)
Entry(ventana).grid(padx=5, row=1, column=1)

#Button(ventana, text="Aceptar", width=50).grid(padx=10, pady=10, row=2, column=0, columnspan=2)
Button(ventana, text="Aceptar").grid(padx=10, pady=10, row=2, column=0, columnspan=2)

ventana.mainloop()