# Ejercicio 1: Calculadora
# Crear un programa que solicite dos números
# en consola e imprima el resultado de las
# cuatro operaciones aritméticas aplicadas
# sobre ellos. Por ejemplo (en rojo la entrada
# del usuario):
# Escribe un número: 7
# Escribe otro número: 5
# a + b: 12
# a - b: 2
# a * b: 35
# a / b: 1.4
# Teniendo en cuenta lo siguiente:
# ● Si el usuario ingresa cualquier otra cosa
# que no sea un número, debe volver a
# preguntar, en ambos casos.
# ● Contemplar que el segundo número
# puede ser cero y, por ende, llegado el
# momento de la división el programa
# debe imprimir “No se puede dividir por
# cero”.
# Como restricción, no se pueden usar
# condicionales (if).

def numeros(tipoinput):
    while True:
        try:
            return float(input(tipoinput))
        except ValueError:
            print("error introduzca unicamente un numero entero")


n1= numeros("ingresa un numero: ")
n2= numeros("ingresa otro numero: ")

print("La Suma de",n1,"y", n2,"es: ", n1+n2)
print("La resta de",n1,"y", n2,"es: ", n1-n2)
print("La multiplicacion de",n1,"y", n2,"es: ", n1*n2)
try:
    print("La division de",n1,"y", n2,"es: ", n1/n2)
except ZeroDivisionError:
    print("No se puede dividir por cero.")







