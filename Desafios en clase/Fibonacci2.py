
semilla = [0,1]
n = 17
lista = [semilla.append(semilla[-1] + semilla[-2])for x in semilla if len(semilla) < n]
print (semilla)
