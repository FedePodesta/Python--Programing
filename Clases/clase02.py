# ### Clase 2 ##

# from cmath import asin
# from os import listxattr
# from ssl import ALERT_DESCRIPTION_BAD_RECORD_MAC
# from turtle import clear
# from xml.sax.handler import property_dom_node


# # **********listas****************** 

# lista= [5,2,3,5,6,1,2,3,56,1]

# lista.append agrega al ultimo lugar de la lista

# lista.insert  agrega un elemento a la lista

# lista[9] = modificacion / cambia el elemento por lo que se le asigne


# lista.pop() borra el ultimo elemento y lo muestra en pantalla

# del lista[5] borra el elemento señalado

# len(lista) cuenta los elementos de la lista

# lista.count(3)  cuenta los elementos repetidos que se haya (asignado)

# lista.index("pedro") consulta en que posicion esta el elemento señalado

# lista[6] imprime el elemento de la lista

# lista[2..5] / slicing, imprime desde el primer numero hasta el ultimo indicado (2..5) del 2 al 5

# lista[-1] apunta al ultimo elemento de la lista(muy util cuando queremos agregar en en un while elementos)

# lista[8:] va desde el 8 hasta el ultimo 

# lista[9][0] si tengo una lista dentro de la lista y quiero imprimir el elemento 0 de esa lista se busca asin

# lista.sort() ordena la lista (datos tipos int por ej) 

# lista vacia 

# lista=[]


### ********* TUPLAS ***********
#Listas inmutables (Meses del año, pi, dias de la semana)

#sintaxis tupla = (1,2,3,4,"asd",[23,1,"hola"])

# tupla vacia 
# tuplav = set() ***UNICA FORMA DE GENERAR UNA TUPLA VACIA 

from doctest import OutputChecker
from re import T
from click import command


# ********IMPORTANTE*******
# si voy a construir una tupla de un unico elemento deboo usar una coma 
# x = (1,)

#***** DICCIONARIIOS*******
#compuestas por claves:valores 
#importante, si repetimos valor de una misma clave se va a tomar el ultimo valor del ultimo agregado
# from typing_extensions import clear_overloads


# diccionario = {
#     "A":1,
#      2:"B",
#     "clave":"CINCO"
#      5:"dos"
#      7:"papa"


#      }
# #Cambiar el valor de la clave
# diccionario["E"]=888 
 
#  #eliminar un valor, tanto clave y valor
#  del diccionario ["B"] 

# #len cuenta los elementos en el diccionario cada elemento cuenta como clave:valor 
#  len(diccionario )

# #imprime la clave y su valor (POCO OPTIMO)
#  for i in diccionario:
#     print(i,diccionario[i])

# #devuelve claves y su valor (cada elemento va a ser una tupla)(OPTIMO)
#  for i,k in diccionario.items():
#     print(i,k)

# # muestra los keys del dicc
# diccionario.keys()
# #muestra los valores del dicc
# diccionario.values()

#generar dicc vacio
# from tkinter.tix import COLUMN
# from xml.dom.expatbuilder import CDATA_SECTION_NODE


# dict ={}


# #*****CONJUNTOS******
# # Estructura Mutable 
# #  NO SE PUEDEN REPETIR ELEMENTOS
# #  Si puedo componerlo con distintos tipos de elementos (bool,float,int,str,tupla)
# # El orden no importa {1,2,3} == {3,2,1} daria TRUE 


# # conjunto ={1,2,3,4,5}

# # agregar elemento
# # conjunto.add(6)

# # borrar elemento
# # conjunto.discard(3) 
# # si el elemento que quiero discard no existe no va a dar error

# # conjunto.remove(2)
# #  si el elemento que quiero remover no existe , dará error

# # generar conjunto vacio
# # dic1= dic() 

# # Borrar todos los elementos de mi conjunto:
# # c1.clear

# ¿para que sirve esta estructura set?

# c1 = {1,2,3,4}
# c2= {3,4,5,6}

# c1 | c2 
# out{1,2,3,4,5,6}

# #devuelve todo en un solo conjunto (sin repetir elementos)
# o también
# c1.union(c2) o viceversa

# c1 & c2 
# out: {3,4} devuelve los elementos en comun 
# o también
# c1.intersection(c2)
# out: {3,4}

# c1 - c2 
# out: {1,2}

# c1.difference(c2) #no es igual si lo hago al reves c2-c2

# (c1-c2)|(c2-c1) #la union de las dos diferencias
# o tambien 
# c1.symmetric_difference(c2)

# b = {2,3}
# b.issubset(c1)
# out {True}
# a la inversa
# c1.issubset(b)

# CASTEO 

# lista = [1,2,3,4,1,2,3,4,1,2,3,4]
# devolveme estos elementos pero que aparezca una sola vez cada elemento repetido

# set(lista) construye un conjunto que devuelve lo solicitado^


# SLICING (para lista y tuplas en donde el orden importa)
# lista2 [1,2,3,4,5,6,7,8]
# lista2[::2] devuelve el primer elemento, salta 2 




# Construir una lista con n dimenciones

# cubo = [[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]
# cubo [0][0][1]

# ************unpacking
# print (dicionario.items())

# for i,j in diccionario.items():
#     print(i,j)

# t= (1,2,3)
# a,b,c = t
# >>>a
# 1
# >>>b
# 2
# >>>c
# 3

# a,b,c,d =1,2,3,"hola"
# #Out:
# >>a
# 1
# >>b
# 2
# >>c
# 3
# >>d
# Hola'

