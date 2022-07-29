def cuadrado(x):
    return x ** 2

def cubo(x):
    return x ** 3


enteros = [1,2,4,7]
cuadrados = map(cuadrado,enteros)
print(type(cuadrados), list(cuadrados))

cubos = map(cubo,enteros)
print(type(cubos), list(cubos))