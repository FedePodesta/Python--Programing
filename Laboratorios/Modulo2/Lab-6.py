# Cree un algoritmo para guarda cada una de las
# personas del diccionario personas en un txt.

# personas = {"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}

# El nombre se tiene que guardar en minúsculas y
# cada persona debe quedar en un renglón con un
# guión del medio separando el nombre y la edad.
# Ejemplo dentro del personas.txt se tendría que ver:
# roberto-20
# romina-32
# …..

personas = {"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}

try:
    with open("personas.txt","w") as f:
        for n in personas:
            texto = f.write(f"{n.lower()}-{personas[n]}"+"\n")
    print("Salvado")
except FileNotFoundError:
    print("No se puede grabar")