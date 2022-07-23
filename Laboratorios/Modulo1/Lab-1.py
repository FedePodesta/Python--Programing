# Ejercicio 1: Sumatoria
# Crear un bucle que almacene en una variable la
# suma de todos los elementos numéricos de una
# lista, con excepción del último.

numeros = [1, 2, 15, 32, 55, 6]
suma = 0

for n in numeros[:-1]:
    suma = suma + n

print(suma)