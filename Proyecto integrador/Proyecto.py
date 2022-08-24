import tkinter as tk
from tkinter import messagebox
import time
import sqlite3
import requests
import sys
 
##########################


def guardarEncargado(data):
    datosIn = (data["nombre"],data["ingreso"],"IN",0)
    datosOut = (data["nombre"],data["egreso"],"OUT",data["facturado"])
    conn = sqlite3.connect("comercio.sqlite")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO registro VALUES (null,?,?,?,?)", datosIn)
        cursor.execute("INSERT INTO registro VALUES (null,?,?,?,?)", datosOut)
    except sqlite3.OperationalError:
        cursor.execute("""CREATE TABLE registro 
        ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            encargado TEXT,
            fecha TEXT,
            evento TEXT,
            caja REAL
        )
        """)
        cursor.execute("INSERT INTO registro VALUES (null,?,?,?,?)", datosIn)
        cursor.execute("INSERT INTO registro VALUES (null,?,?,?,?)", datosOut)
    conn.commit()
    conn.close

 
def guardarVentas(data):
    datos = tuple(data)
    conn = sqlite3.connect("comercio.sqlite")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO ventas VALUES (null,?,?,?,?,?,?,?)", datos)
    except sqlite3.OperationalError:
        cursor.execute("""CREATE TABLE ventas 
        ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT,
            fecha TEXT,
            ComboS INT,
            ComboD INT,
            ComboT INT,
            Flurby INT,
            total REAL
        )
        """)
        cursor.execute("INSERT INTO ventas VALUES (null,?,?,?,?,?,?,?)", datos)
    conn.commit()
    conn.close

def cotizar():
    try:
        r = requests.get("https://api-dolar-argentina.herokuapp.com/api/dolaroficial")
        valor = r.json()["venta"]
        valor = round(float(valor))
        return valor
    except:
        messagebox.showerror(title="Error grave", message="Sin internet para cotizar. Terminado")
        sys.exit()


def validar(dato):
	try:
		dato = int(dato)
		return dato
	except ValueError:
		return -1
 
 
def borrar():
    #no borramos el encargado, para no tener que estar reescribiendolo siempre
    ccomboUno.delete(0,tk.END)
    ccomboDos.delete(0,tk.END)
    ccomboTres.delete(0,tk.END)
    cpostre.delete(0,tk.END)
    ccliente.delete(0,tk.END)


def cancelar_pedido():
	respuesta = messagebox.askyesno(title="Pregunta", message="¿Desea cancelar el pedido?")
	if respuesta:
		borrar()


 
def pedir():
    cantUno= ccomboUno.get()
    cantUno = validar(cantUno)
    cantDos = ccomboDos.get()
    cantDos = validar(cantDos)
    cantTres = ccomboTres.get()
    cantTres = validar(cantTres)
    cantPostre = cpostre.get()
    cantPostre = validar(cantPostre) 
    dolar = cotizar() 
    if cantUno>=0 and cantDos>=0 and cantTres>=0 and cantPostre>=0:
        cliente = ccliente.get()
        encargado = cencargado.get()
        if cliente and encargado:
            respuesta = messagebox.askyesno(title="Pregunta", message="¿Confirma el pedido?")
            if respuesta:
                costot = ((cantUno*precios["ComboSimple"])+(cantDos*precios["ComboDoble"])+(cantTres*precios["ComboTriple"])+(cantPostre*precios["Flurby"]))
                totalPesos = costot * dolar
                fecha = time.asctime()
                pedido = [cliente,fecha,cantUno,cantDos,cantTres,cantPostre,totalPesos]
                messagebox.showinfo(title="A pagar", message="$"+str(totalPesos))
                guardarVentas(pedido)
                messagebox.showinfo(title="Información", message="Pedido Exitoso")
                if  datosEncargado["nombre"] != encargado and datosEncargado["egreso"] == "" : # cuando inicia la app egreso es vacio
                    datosEncargado["nombre"] = encargado
                    datosEncargado["egreso"] = "SinFecha" # es solo para que la proxima no cumpla la condición, es solo al inicio
                    datosEncargado["facturado"] += totalPesos #voy incrementando totales
                elif datosEncargado["nombre"] == encargado:
                    datosEncargado["facturado"] += totalPesos #voy incrementando totales
                else:
                    datosEncargado["egreso"] = fecha # al cambiar de encargado registro la fecha
                    guardarEncargado(datosEncargado) # guardo
                    #borramos el encargado anterior, en el diccionario ponemos el nuevo
                    datosEncargado["nombre"] = encargado # iniciamos el nuevo encargado
                    datosEncargado["Ingreso"] = fecha
                    datosEncargado["facturado"] = 0
                    datosEncargado["facturado"] += totalPesos
                borrar()
            else:
                messagebox.showinfo(title="Información", message="Pedido en pausa")
        else:
            messagebox.showwarning(title="Advertencia", message="Error, ingrese bien los datos")
    else:
        messagebox.showwarning(title="Advertencia", message="Error, ingrese datos correctos")
 

def salir():
    #salir seguro implica guardar el último encargado
    respuesta = messagebox.askyesno(title="Pregunta", message="¿Desea salir?")
    if respuesta:
        datosEncargado["egreso"] = time.asctime()
        guardarEncargado(datosEncargado)
        sys.exit()
    

 
##########################

precios = {"ComboSimple":5,"ComboDoble":6,"ComboTriple":7,"Flurby":2}
datosEncargado = {"nombre":"","ingreso":time.asctime(),"egreso":"","facturado":0}
 
##########################
 
ventana = tk.Tk()
ventana.config(width = 400, height = 400)
ventana.title("Delivery")
 
#####etiquetas######
ebienvenido = tk.Label(text="------ Pedidos -------")
ebienvenido.place(x = 140, y = 20)

enombreEncargado = tk.Label(text = "Nombre Encargado : ")
enombreEncargado.place(x = 50, y = 70)
ecomboUno = tk.Label(text = "Combo S cantidad : ")
ecomboUno.place(x = 50, y = 110)
ecomboDos = tk.Label(text = "Combo D cantidad : ")
ecomboDos.place(x = 50, y = 150)
ecomboTres = tk.Label(text = "Combo T cantidad : ")
ecomboTres.place(x = 50, y = 190)
ecliente = tk.Label(text = "Postre cantidad : ")
ecliente.place(x = 50, y = 230)
epostre = tk.Label(text = "Nombre del cliente : ")
epostre.place(x = 50, y = 270)
 
#####cajas#########

cencargado = tk.Entry()
cencargado.place(x = 230, y = 70)
ccomboUno = tk.Entry()
ccomboUno.place(x = 230, y = 110)
ccomboDos = tk.Entry()
ccomboDos.place(x = 230, y = 150)
ccomboTres = tk.Entry()
ccomboTres.place(x = 230, y = 190)
cpostre = tk.Entry()
cpostre.place(x = 230, y = 230)
ccliente = tk.Entry()
ccliente.place(x = 230, y = 270)
 
##### Botones #########
 
bpedido = tk.Button(text = "Hacer Pedido", command = pedir)
bpedido.place(x = 270 , y = 330, height=40, width = 100)
 
bcancelar = tk.Button(text = "Cancelar Pedido", command = cancelar_pedido)
bcancelar.place(x = 150 , y = 330, height=40, width = 100)
 
binfo = tk.Button(text = "Salir seguro",command=salir)
binfo.place(x = 30 , y = 330, height=40, width = 100)
 
 
ventana.mainloop()