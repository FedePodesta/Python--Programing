import tkinter as tk
from tkinter import ttk

    
ventana = tk.Tk()

ventana.title("Mi primer ventana")
ventana.config(width=800, height=700)

canvas = tk.Canvas(ventana, width=700, height=600)
canvas.place(x=10, y=10)

archivo = tk.PhotoImage(file="dis.gif")
canvas.create_image(30,30, image=archivo, anchor="nw")

ventana.mainloop()