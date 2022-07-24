# Hacer un pequeño programa con un menú
# muy sencillo:
# Menú:
# 1 – Ingreso de empleado
# 2 – Egreso de empleado
# 3 – Salir del sistema
# >>>
# Este sistema es básico, lo utiliza el personal
# de seguridad que registra el nombre de la
# persona que ingresa (opción 1), y que egresa
# del edificio (opción 2).
# Además, es necesario registrar el horario de
# los eventos se podría usar el módulo time, y
# la función asctime() que devuelve un str
# con fecha y hora.
# Cuando se quiere salir del programa se usa la
# opción 3.
# Tanto el ingreso y el egreso se registra en un
# archivo txt. Cada renglón representa un
# registro.
# Ejemplo de lo que se ven en el archivo “registro.txt” :
# Thu Oct 28 21:32:01 2025 - Ignacio - Ingreso
# Thu Oct 28 21:33:01 2025 - Juan - Ingreso
# Thu Oct 28 22:33:10 2025 - Tomas - Egreso
# Thu Oct 28 22:35:01 2025 - Romina - Egreso
# Thu Oct 28 23:36:02 2025 - Ana – Ingreso
# Thu Oct 28 23:36:02 2025 - Jorge – Ingreso
# Nota: No hace falta comprobar si una persona entró varias veces o
# salió varias veces. Sólo registrar y guardar

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
    

while True:
    print("""
    Menú
    1 - Ingreso de empleado
    2 - Egreso de empleado
    3 - Salir del sistema
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
        print("¡Gracias por usar nuestro programa!")
        break
    else:
        print("Error de opcion")
    print("\n\n")
    input("Toque ENTER para continuar...")
