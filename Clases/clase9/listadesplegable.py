import tkinter as tk
from tkinter import ttk

def boton_presionado():
    print("Bienvenido a nuestro sitio:", texto.get())   
    print(lista.get()) 

    
ventana = tk.Tk()

ventana.title("Mi primer ventana")
ventana.config(width=600, height=400)

lbl = ttk.Label(ventana, text="Nombre:", font=("Arial Bold", 15))
lbl.place(x=10, y=10)

texto = ttk.Entry(ventana)
texto.place(x=130, y=10)

lista = ttk.Combobox(ventana, values=["Paris", "New York", "Roma", "Buenos Aires"])                                      
lista.place(x=130, y=50)

boton = ttk.Button(ventana, text="Presione aqui", command=boton_presionado)
boton.place(x=130, y=150)

ventana.mainloop()