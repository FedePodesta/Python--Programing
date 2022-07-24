# Cree un algoritmo para volver al diccionario original
# desde el archivo personas.txt creado en el ejercicio
# anterior.
# El nombre se tiene que recuperar en mayúsculas y
# cada valor debe volver a ser del tipo entero.
# El diccionario tendría que volver a verse como:
# personas = {"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}

personas = {}

try:
    with open("personas.txt","r") as f:
        datos = f.readlines()
    for n in datos:
        p = (n.strip()).split("-")
        personas[p[0].capitalize()] = int(p[1])
    print("Rescatados")
    print(personas)
except FileNotFoundError:
    print("No se puede recuperar")
    