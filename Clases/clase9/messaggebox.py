import tkinter as tk
from tkinter import ttk, messagebox


def boton_presionado():
    messagebox.showinfo(title="Información", message="Esta es su información")
    messagebox.showerror(title="Error", message="Este es su error")
    devolucion = messagebox.showwarning(title="Advertencia", message="Esta es su advertencia")
    print("Lo que devolvio es", devolucion)
    
    messagebox.askokcancel(title="Pregunta", message="Estas seguro?")
    messagebox.askyesno(title="Pregunta", message="Si o no?")
    seleccion = messagebox.askretrycancel(title="Pregunta", message="Reintento o cancelo?")
    print("La selecccion es", seleccion)
    messagebox.askquestion(title="Pregunta", message="Si o no?")
    
    
        
ventana = tk.Tk()

ventana.title("Mi primer ventana")
ventana.config(width=600, height=400)

boton = ttk.Button(ventana, text="Presione aqui", command=boton_presionado)
boton.place(x=130, y=150)

ventana.mainloop()