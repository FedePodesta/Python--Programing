import tkinter as tk
from tkinter import ttk

veces = 0

def boton_presionado():
    global veces
    veces += 1
    print("Se presiono el boton ", veces)
    boton.config(text="Otro Presione")
    
ventana = tk.Tk()

ventana.title("Mi primer ventana")
ventana.config(width=600, height=400)

boton = ttk.Button(ventana, text="Presione aqui", command=boton_presionado)
boton.place(x=20, y=20)

ventana.mainloop()