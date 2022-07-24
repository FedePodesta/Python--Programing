# Crear una función que use lo visto de excepciones
# para que tome por input() el número como str y
# lo transforme directamente a float, sea entero o
# decimal. Deberíamos pasar como argumento la
# frase para mostrar en pantalla el pedido. Además,
# deberíamos de volver a pedir, hasta que se pueda
# hacer el ingreso de forma correcta.
# A partir de ahora cada vez que tomemos un número
# por teclado podemos hacer uso de esta función que
# vamos a crear

def numeric_input(frase):
    valor = input(frase)
    while True:
        try:
            valor = float(valor)
            break
        except ValueError:
            print("Error, este ingreso solo permiten números")
        valor = input("Intente nuevamente. " + frase)
    return valor        

salario = numeric_input("Ingrese su salario: ")