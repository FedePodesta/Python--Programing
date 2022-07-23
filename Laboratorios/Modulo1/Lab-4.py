# Ejercicio 4: Promedio variable
# Construir una función que se llame “promedio_variable”.
# Esta función debe tomar un número arbitrario de
# argumentos numéricos y devolver el promedio.

def promedio_variable(*args):
    suma = 0
    for n in args:
        suma += n
    promedio = suma / len(args)
    return promedio

print(promedio_variable(16,2,9,4,2,6,1,3,7,55,33,25,16,72,12))
