# nombres= {"Andres","Juan","Pedro","Ana","Maria"}
# salarios =[100000,400000,60000,500000,1000000]

# for i,x in enumerate(nombres):
#     print (i,x) 
# #enumerate nos devuelve una lista con sus elementos y un contador

# for i,x in zip(nombres, salarios):
#     print (i,x)
#zip va a iterar las dos listas y va a devolverlas en una misma linea

#diccionarios con clave con varios valores

# dic1= {"andres": [1,2,True,"hola"]}

def imprimir ():
    print("hola")

def potencia (base,exp):
    return base**exp
    
print(potencia(2,3))


#*args se pueden colocar multiples parametros los cuales devolverá en una tupla
def sumatoria (*args):
    print(args)
    n=0
    for i in args:
        n += i
    return n
    #return sum(args)/len(args) # devuelve el promedio


print (sumatoria(1,2,3,4,5))

#Argumentos nominales

def argu_nominal(**kwargs):
    print(kwargs)
    for i,j in kwargs.items():
        print(i,j)
    return " "

print(argu_nominal(a=10, b="Hola", c=3.14,d=True))

