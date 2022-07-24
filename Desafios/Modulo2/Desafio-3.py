# Al programa anterior, agregarle una opción de ver los
# últimos 5 registros (opción 3 y salir pasa a opción 4).
# Solo los últimos 5 eventos tomarlos directamente del
# txt. Si nuestro archivo está vacío, mostrar el mensaje
# “No hay registros”, en caso de que tengamos menos
# registros que 5, solo mostrar los que se tenga en el
# archivo hasta ese momento.
# Menú:
# 1 – Ingreso de empleado
# 2 – Egreso de empleado
# 3 – Mostrar los últimos 5 registros
# 4 – Salir del sistema
# >>>
# Al elegir la opción 3 deberíamos de ver en la consola
# algo de este estilo:
# Thu Oct 28 21:33:01 2025 - Juan - Ingreso
# Thu Oct 28 22:33:10 2025 - Tomas - Egreso
# Thu Oct 28 22:35:01 2025 - Romina - Egreso
# Thu Oct 28 23:36:02 2025 - Ana – Ingreso
# Thu Oct 28 23:36:02 2025 - Jorge – Ingreso

import time


def comprobar(dato):
    while dato == "":
        print("Error. ¡No debe dejar vacio este campo!")
        dato = input("Ingrese dato nuevamente: ")
    return dato

def guardar(persona,tipo):
    fecha = time.asctime()
    datos = f"{fecha} - {persona} - {tipo} \n"
    f = open("registro.txt","a")
    f.write(datos)
    f.close()
    
def mostrar():
    try:
        f = open("registro.txt","r")
        eventos = f.readlines()
        f.close()
        if len(eventos) < 5:
            for r in eventos:
                print("- " + r.strip())
        else:
            for r in eventos[-5:]:
                print("- " + r.strip())
    except FileNotFoundError:
        print("No hay registros para mostrar")
    

#######################################################

while True:
    print("""
    Menú
    1 - Ingreso de empleado
    2 - Egreso de empleado
    3 - Ver los últimos 5 registros
    4 - Salir del sistema
    """)
    opcion = input(">>> ")
    if opcion == "1":
        nombre = input("Nombre del empleado que ingresa: ")
        nombre = comprobar(nombre)
        guardar(nombre,"Ingreso")
    elif opcion == "2":
        nombre = input("Nombre del empleado que egresa: ")
        nombre = comprobar(nombre)
        guardar(nombre,"Egreso")
    elif opcion == "3":
        print("------------ Los últimos 5 registros ------------\n")
        mostrar()
        print("\n-------------------------------------------------")
    elif opcion == "4":
        print("¡Gracias por usar nuestro programa!")
        break
    else:
        print("Error de opcion")
    print("\n\n")
    input("Toque ENTER para continuar...")