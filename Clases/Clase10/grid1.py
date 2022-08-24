# Grid
from tkinter import *

# Si deseamos crear un espacio entre las filas o columnas 
# podemos usar pady y padx en cada uno de ellos indicamos la cantidad de espacio
# deseada

ventana = Tk()

for r in range(0, 5):
    for c in range(0, 5):
        celda = Entry(ventana, width=10)
        celda.grid(padx=5, pady=5, row=r, column=c)
        celda.insert(0, '({}, {})'.format(r, c))

ventana.mainloop()