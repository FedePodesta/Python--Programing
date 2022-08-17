import os
import sqlite3
from tabulate import tabulate

def pedir_entero(mensaje):
    """
    Pide un número entero a través de la consola hasta que el
    usuario ingrese un dato válido.
    """
    while True:
        try:
            entero = int(input(mensaje))
        except ValueError:
            pass
        else:
            # Si uso "return" adentro de un bucle no es necesario
            # usar "break", está implícito.
            return entero

def guardar(i,n,p):
    conn = sqlite3.connect("comercio.sqlite")
    cursor = conn.cursor()
    try:
        cursor.execute( "INSERT INTO productos VALUES (?, ?, ?)",(i, n, p))
    except sqlite3.OperationalError:
        cursor.execute("CREATE TABLE productos (id INT,nombre TEXT, precio INT)")
        cursor.execute( "INSERT INTO productos VALUES (?, ?, ?)",(i, n, p))
    conn.commit()
    conn.close()
    print("¡Producto guardado con exito!")



def mostrar():
    conn = sqlite3.connect("comercio.sqlite")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM productos")
        datos = cursor.fetchall()
    except (sqlite3.ProgrammingError,sqlite3.OperationalError):
        datos = None
    conn.commit()
    conn.close()
    return datos


########################################################################

if os.name == "nt":
    borrar = "cls"
else:
    borrar = "clear" 

os.system(borrar)

while True:
    print("""
    Menú
    1 - Ingresar producto
    2 - Mostrar productos
    3 - Salir 
    """)
    opcion = input(">>> ")
    if opcion == "1":
        print("Ingrese los datos del nuevo producto.")
        # No uso "id" como nombre de variable porque es el nombre de una
        # función incorporada de Python.
        id_producto = pedir_entero("ID: ")
        nombre = input("Nombre: ")
        precio = pedir_entero("Precio: u$s")
        # Inserto el producto en la base de datos.
        guardar(id_producto,nombre,precio)
    elif opcion == "2":
        r = mostrar()
        if r:
            # tabulate es una funcion (del modulo tabulate) para 
            # crear una tabla con apariencia d tabla en la consola
            # Si te interesa saber como se usa podes ver la documentacion 
            # https://github.com/astanin/python-tabulate
            print("\n")
            print(tabulate(r,headers=["ID","NOMBRE","PRECIO U$S"], tablefmt="pretty"))
            print("\n")
        else:
            print("No hay datos para mostrar")
    elif opcion == "3":
        print("¡Gracias por usar nuestro programa!")
        break
    else:
        print("Error de opcion. Vualva a intentarlo")
    input("Toque ENTER para continuar...")
    os.system(borrar)