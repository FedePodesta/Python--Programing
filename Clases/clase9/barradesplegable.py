import tkinter as tk
from tkinter import BOTTOM, RIGHT, ttk

    
ventana = tk.Tk()

ventana.title("Mi primer ventana")


scl = tk.Scale(ventana, from_=-100, to=100, tickinterval=50, resolution=10)
scl.pack(expand=True, fill=tk.BOTH)

def report():
    print(scl.get())

btn = tk.Button(ventana, text="Estado", command=report)
btn.pack(side=BOTTOM)

ventana.mainloop()