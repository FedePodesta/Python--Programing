# Ejercicio 2: Mostrar y eliminar
# Utilizando un bucle “while”, elaborar un código
# que imprima en pantalla cada uno de los
# elementos de una lista y simultáneamente los
# elimine, hasta quedar vacía.


numeros = [16, 12, 63, 24, 51, 26]
print(numeros)

while len(numeros) > 0:
   
    print(numeros[0])
   
    del numeros[0]

print(numeros)