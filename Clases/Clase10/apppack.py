import tkinter as tk
from tkinter import ttk

ventana=tk.Tk()
ventana.title("Lenguajes de Programacion") 
ventana.geometry("500x100")

frame = tk.Frame(ventana)
frame.pack()

bottomframe = tk.Frame(ventana)
bottomframe.pack( side = tk.BOTTOM )

etiqueta = tk.Label(frame, text="Elija el mejor lenguaje de programación")
etiqueta.pack(side=tk.LEFT)

lista = ttk.Combobox(frame, values=[ "Visual Basic", "Python", "C", "C++", "Java", "Visual Basic 6.0 Microsoft" ])
lista.pack(side=tk.LEFT)

boton = tk.Button(bottomframe, text="Confirmacion", command=lambda: print(lista.get()))
boton.pack(side=tk.BOTTOM)

ventana.mainloop()