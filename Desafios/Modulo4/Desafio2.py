import sqlite3
import sys
import os

try:
    from tabulate import tabulate
except ModuleNotFoundError:
    print("Faltan modulos, verificar e instalar con pip")
    sys.exit()


####################################################################


def ingreso_validar(texto):
    dato = input(texto)
    while dato == "":
        print("Error. ¡Campo Vacio!")
        dato = input("Intente nuevamente. "+texto)
    return dato

def guardar(n,t,e,d):
    try:
        conn = sqlite3.connect("datos.sqlite")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contactos VALUES (null,?,?,?,?)",(n,t,e,d))
        conn.commit()
        conn.close
    except sqlite3.OperationalError:
        conn = sqlite3.connect("datos.sqlite")
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE contactos 
        ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            telefono TEXT,
            email TEXT,
            direccion TEXT
        )
        """)
        cursor.execute("INSERT INTO contactos VALUES (null,?,?,?,?)",(n,t,e,d))
        conn.commit()
        conn.close
    print("¡Se salvo el nuevo contacto!")


def traer():
    try:
        conn = sqlite3.connect("datos.sqlite")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contactos")
        datos = cursor.fetchall()
        conn.commit()
        conn.close()
        return datos
    except sqlite3.OperationalError:
        return None

def buscar(texto):
    palabra = texto.lower()
    todos = traer()
    coincidencias = []
    if todos:
        for n in todos:
            nombre = n[1].lower()
            if nombre.find(palabra)>=0:
                coincidencias.append(n)
        if len(coincidencias) > 0:
            return coincidencias
        else:
            print("Sin coincidencias")
            return None
    else:
        return None

    
####################################################################



if os.name == "nt":
    borrar = "cls"
else:
    borrar = "clear"

os.system(borrar)
while True:
    print("""
    Menú
    1 - Ingresar nuevo contacto
    2 - Mostrar todos los contactos
    3 - Encontrar contacto por aproximación en el nombre
    4 - Salir
    """)
    opcion = input(">>> ")
    if opcion == "1":
        nombre = ingreso_validar("Ingrese nombre del contacto: ")
        telefono = ingreso_validar("Ingrese teléfono: ")
        email = ingreso_validar("Ingrese email: ")
        direccion = ingreso_validar("Ingrese dirección: ")
        guardar(nombre,telefono,email,direccion)
    elif opcion == "2":
        r = traer()
        if r:
            titulo = ["ID","NOMBRE","TELEFONO","EMAIL","DIRECCION"]
            print("\n")
            print(tabulate(r,headers=titulo,tablefmt="pretty"))
            print("\n")
        else:
            print("No hay datos")
    elif opcion == "3":
        print("Las opciones de busqueda son por el nombre.")
        nombre = ingreso_validar("Ingrese nombre o texto coincidente: ")
        if len(nombre) < 2:
            print("Sea más preciso. Ingrese más letras para buscar")
        else:
            r = buscar(nombre)
            if r:
                titulo = ["ID","NOMBRE","TELEFONO","EMAIL","DIRECCION"]
                print("\n")
                print(tabulate(r,headers=titulo,tablefmt="pretty"))
                print("\n")
            else:
                print("No hay datos")
    elif opcion == "4":
        print("Gracias por usar nuestro programa")
        break
    else:
        print("Error de opción")

    input("Toque ENTER para continuar...")
    os.system(borrar)