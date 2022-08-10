import os
import sys

try:
    from tabulate import tabulate
except ModuleNotFoundError:
    print("""
    -> Falta el modulo tabulate
    -> Instala desde la consola del sistema operativo
    pip install tabulate
    (pip3 en Linux o iOS)
    """)
    sys.exit()


###########################################################################

def verificar(dato,texto):
    while dato == "":
        print("Error, ¡Campo vacio!")
        dato = input(texto)
    return dato


def listar(rut,ext):
    try:
    # Obtener la lista de archivos en la ruta especificada.
        archivos = os.listdir(rut)
    except FileNotFoundError:
        return False
    # Si la extensión no empieza con un punto, agregárselo.
    if not ext.startswith("."):
        ext = "." + ext
    #lista coincidencias para guardar los archivos con ext y luego armar tabla
    coincidencias =[]
    # para contar los archivos coincidentes
    contador = 0
    # Recorrer la lista de archivos.
    for archivo in archivos:
        # Imprimir únicamente los que terminan con la extensión ingresada.
        if archivo.endswith(ext):
            contador +=1
            coincidencias.append([contador, archivo])
    print(tabulate(coincidencias,headers=["ID","ARCHIVO"],tablefmt="pretty"))
    return True


###############################################################################


if os.name == "nt":
    borrar = "cls"
else:
    borrar = "clear"

os.system(borrar)

while True:
    print("""
    Menú 
    1 - Buscar archivos con determinada extensión
    2 – Salir
    """)
    opcion = input(">>> ")
    if opcion == "1":
        ruta = input("Ingrese ruta: ")
        ruta = verificar(ruta,"Ingrese ruta nuevamente: ")
        extension = input("Ingrese extensión de archivo a buscar: ")
        extension = verificar(extension,"Ingrese extensión de archivo a buscar nuevamente: ")
        if not listar(ruta,extension):
            print("La ruta no existe.")
    elif opcion == "2":
        print("¡Gracias por usar nuestro programa!")
        break
    else:
        print("¡Error de opción!")
    input("Toque ENTER para continuar...")
    os.system(borrar)