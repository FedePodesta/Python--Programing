import tkinter as tk
from tkinter import ttk

def boton_presionado():
    print("Bienvenido a nuestro sitio:", texto.get(), tk.END)    
    #texto.insert(0, "Gracias!   ")
    texto.delete(0, tk.END)
    
ventana = tk.Tk()

ventana.title("Mi primer ventana")
ventana.config(width=600, height=400)

lbl = ttk.Label(ventana, text="Ingrese su nombre:")
lbl.place(x=10, y=10)

texto = ttk.Entry(ventana)
texto.place(x=130, y=10)

boton = ttk.Button(ventana, text="Presione aqui", command=boton_presionado)
boton.place(x=130, y=50)

ventana.mainloop()