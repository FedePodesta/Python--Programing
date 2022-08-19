import tkinter as tk
from tkinter import ttk

def boton_presionado():
    print("La opcion 1 es ", ckb_st1.get())
    print("La opcion 2 es ", ckb_st2.get())
    print("La opcion 3 es ", ckb_st3.get())
    
ventana = tk.Tk()

ventana.title("Mi primer ventana")
ventana.config(width=600, height=400)

ckb_st1 = tk.BooleanVar()
checkbutton = ttk.Checkbutton(ventana, text="Opcion 1", variable=ckb_st1)
checkbutton.place(x=10, y=10)
ckb_st2 = tk.BooleanVar()
checkbutton2 = ttk.Checkbutton(ventana, text="Opcion 2", variable=ckb_st2)
checkbutton2.place(x=10, y=30)
ckb_st3 = tk.BooleanVar()
checkbutton3 = ttk.Checkbutton(ventana, text="Opcion 3", variable=ckb_st3)
checkbutton3.place(x=10, y=50)


boton = ttk.Button(ventana, text="Presione aqui", command=boton_presionado)
boton.place(x=130, y=150)

ventana.mainloop()