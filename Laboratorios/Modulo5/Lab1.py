# Para este ejercicio estaremos usando el mismo
# servicio web que en el material de la clase, es decir,
# el servicio web servicio_web.py, que tenés que
# tener en ejecución.
# Desarrollar un programa admin_alumnos.py que
# permita añadir, modificar, eliminar y listar los
# alumnos del servicio web.
# A continuación, encontrará ejemplos de uso (en rojo
# lo que ingresa el usuario).


import requests
import os


def solicitar_entero(mensaje, vacio=False):
    """
    Solicita al usuario que ingrese un número entero en pantalla y repite
    la acción hasta que el dato sea válido.
    Si `vacio` es `True`, solo se realiza el chequeo si el usuario ingresa
    algo. 
    """
    while True:
        dato = input(mensaje)
        if vacio and not dato:
            return None
        try:
            return int(dato)
        except ValueError:
            pass


if os.name == "nt":
    borrar = "cls"
else:
    borrar = "clear"



os.system(borrar)

url = "http://localhost:7001/student"

while True:
    print("1. Agregar un alumno.")
    print("2. Modificar alumno existente.")
    print("3. Listar alumnos.")
    print("4. Eliminar un alumno.")
    print("5. Salir.")
    opcion = input(">>> ")
    if opcion == "1":
        nombre = input("Nombre: ")
        cursos = solicitar_entero("Cursos: ")
        r = requests.post(url, json={"name": nombre, "courses": cursos})
        if r.status_code == 201:
            print("Alumno ingresado correctamente.")
        else:
            print("No se ha podido ingresar el alumno.")
    elif opcion == "2":
        id_alumno = solicitar_entero("Ingrese el ID del alumno: ")
        datos = {}
        nombre = input("Nuevo nombre (o deje vacío para mantener el anterior): ")
        if nombre:
            datos["name"] = nombre
        cursos = solicitar_entero("Nueva cantidad de cursos (o deje vacío): ", vacio=True)
        if cursos:
            datos["courses"] = cursos
        r = requests.put(url + f"/{id_alumno}", json=datos)
        if r.status_code == 204:
            print("Alumno modificado correctamente.")
        else:
            print("No se ha podido modificar el alumno.")
    elif opcion == "3":
        r = requests.get(url)
        if r.status_code == 200:
            alumnos = r.json()["students"]
            for alumno in alumnos:
                print(f'Id:{alumno["id"]} - {alumno["nombre"]} - {alumno["cursos"]} cursos.')
        else:
            print("No se pudo obtener la lista de alumnos.")
    elif opcion == "4":
        id_alumno = solicitar_entero("Ingrese el ID del alumno: ")
        r = requests.delete(url + f"/{id_alumno}")
        if r.status_code == 204:
            print("Alumno eliminado correctamente.")
        else:
            print("No se pudo eliminar el alumno.")
    elif opcion == "5":
        print("¡Gracias por usar nuestro programa!")
        break
    else:
        print("Error de opcion, vuelva a intentarlo")
    input("Toque ENTER para continuar...")
    os.system(borrar)