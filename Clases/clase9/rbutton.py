import tkinter as tk
from tkinter import ttk


def opcion():
    print("La opcion seleccionada es ", rb_st.get())
        
ventana = tk.Tk()

ventana.title("Mi primer ventana")
ventana.config(width=600, height=400)

rb_st = tk.IntVar()
rbutton1 = tk.Radiobutton(ventana, text="Opcion 1", variable=rb_st, value=1, command=opcion)
rbutton1.place(x=10, y=10)
rbutton2 = tk.Radiobutton(ventana, text="Opcion 2", variable=rb_st, value=2, command=opcion)
rbutton2.place(x=10, y=30)
rbutton3 = tk.Radiobutton(ventana, text="Opcion 3", variable=rb_st, value=3, command=opcion)
rbutton3.place(x=10, y=50)

ventana.mainloop()