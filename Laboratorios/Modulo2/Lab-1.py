# Ejercicio 1: Orden superior
# Cree una función llamada “superior”, que reciba por
# argumento una función y una lista. La función que se
# pasa por argumento a superior debe elevar al cubo un
# número y retornarlo. Para que luego al aplicarla en la
# de orden superior, esa operación se realice miembro
# a miembro de la lista.
# Para finalizar la función “superior” debe de devolver
# una nueva lista.

#Defino la funcion para elevar al cubo
def cubo(n):
    return n**3  #retorno el numero ingresado elevado al cubo

#defino la funcion superior
def superior (funcion,lista):
    resultado = [] #genero una lista vacia
    for n in lista: #recorro la lista vacia> 
        resultado.append (funcion(n)) #>aplicando la funcion inferior(cubo)
    return resultado #retorno el resultado

#creo una lista para poder agregar a la funcion
elevarAlCubo= [2,3,5]

# Se invoca la funcion superior el cual lleva como parametros(funcion de elevar al cubo, mas la lista creada anteriormente)
print (superior(cubo,elevarAlCubo))
##Metodo Lambda
print(superior(lambda n: n**3,[5,10,6]))


