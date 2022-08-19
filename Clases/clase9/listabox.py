import tkinter as tk
from tkinter import ttk

def boton_presionado():
    print("Bienvenido a nuestro sitio:", texto.get())   
    print(lista.get(lista.curselection())) 

    
ventana = tk.Tk()

ventana.title("Mi primer ventana")
ventana.config(width=600, height=400)

lbl = ttk.Label(ventana, text="Nombre:", font=("Arial Bold", 15))
lbl.place(x=10, y=10)

texto = ttk.Entry(ventana)
texto.place(x=130, y=10)

lista = tk.Listbox(ventana, selectmode=tk.EXTENDED,  selectforeground="#ffffff",         
                   selectbackground="#3335FF",
                   selectborderwidth=5)
lista.insert(0, "Python", "Java", "C++", ".Net", "PHP")
lista.place(x=130, y=50, height=90)

boton = ttk.Button(ventana, text="Presione aqui", command=boton_presionado)
boton.place(x=130, y=150)

ventana.mainloop()