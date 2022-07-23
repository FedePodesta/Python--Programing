#Ejercicio 3: Crear una función en Python que tome como argumento
# un entero que indique la cantidad de términos y retorne
# una lista como la anterior. Por ejemplo:
# >>> fib(10)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# La función debe, además, chequear que el argumento
# pasado sea mayor a 2. En caso de ser menor, debe
# mostrar un mensaje en pantalla y no retornar nada.
# >>> fib(1)
# La cantidad debe ser mayor a 2.

def fibo(cantidad):
    if cantidad <= 2:
        return "La cantidad de terminos debe ser mayor que 2"
    f = [0, 1]
   
    while len(f) < cantidad:
       
        f.append(f[-1] + f[-2])
    return f


print(fibo(1))
print(fibo(10))