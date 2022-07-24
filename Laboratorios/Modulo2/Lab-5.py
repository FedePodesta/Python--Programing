# Se tiene una lista de personas como la siguiente:
# Se desea crear una función que ponga mayúscula
# solo en la primera letra, tanto del nombre como del
# apellido, y que devuelva la lista con esta
# modificación.
# Se puede usar funciones de orden superior para
# resolver el ejercicio, no hay limitaciones.


Nombres= ["juan salvo","henry courtney","elizabeth bennet","marge simpson"]


def mayusculas(texto):
    fueraLista= texto.split()
    dentrolista = f"{fueraLista[0].capitalize()}{fueraLista[1].capitalize()}"
    return dentrolista

def primerLetra(funcion,lista):
    nombresNuevo = []
    for n in lista:
        nombresNuevo.append(funcion(n))
    return nombresNuevo


print(primerLetra(mayusculas,Nombres))