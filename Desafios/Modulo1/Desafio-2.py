# Tenemos una lista donde se registran los ingresos del
# personal a un sistema:
# Contar los ingresos en un diccionario. La clave debería
# de ser el nombre y el valor debería ser la cantidad de
# ingresos.


personas = ["Susana","Tamara","Ana","Susana","Susana","Tomas","Ana"]
ingresos = {}

for n in personas:
    if n not in ingresos:
        ingresos[n] = 1
    else:
        ingresos[n] += 1

print(ingresos)