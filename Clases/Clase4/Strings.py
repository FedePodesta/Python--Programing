# Strings

# Hay dos operadores aritmeticos que se pueden utilizar con cadenas
 #suma
 # multiplicacion
n="hola mundo"
sumaString= "hola" + " como andas"
#out = hola como andas
multiplicacionstring= "pablo" * 3 
#out = pablopablopablo

#Usar comillas dentro de un string
comillas = "Dios no juega a los dados 'Albert Einstein' "
#out = Dios no juega a los dados 'Albert Einstein'

# Distintos tipos de caracteres epeciales
#\n Salto de linea
m = "Hola \nMundo"
#out = Hola
#      Mundo

#\t tabulacion entre palabras
t = "Hola \tMundo"
#out = Hola    Mundo

#\b junta palabras 
b = "Hola\bMundo"
#out = "HolMundo"

#para imprimir los caracteres especiales y no aplique su funcion
# \\n,b,t
p = "Hola \\norman"
#out Hola \norman

#no ejecutar el salto de linea
#repr(var)
print(repr(m))
#out hola\nmundo

#Split, realiza una lista con los caracteres ingresados
l = "A B C D E F G".split()#en este caso separa por comas
#out = ["A","B","C","D","E","F","G"]

#.Strip
#saca los espacios en blanco antes y despues
"    jose   ".strip
#out = jose

#STARTSWITH Y .ENDSWITH
n.startswith ("Dios")
n.endswith ("Dios")
# devuelve si la palabra señalada esta al principio o al final
#o
n.find("dados")

#.COUNT
n.count("a")

#CAPITALIZE()
#Primera letra en mayuscula demás en miniscula
#.UPPER()
#Todas las palabras en mayuscula
#.LOWER()
#Todas las palabras en minuscula
#.TITTLE()
#primer letra en mayuscula de cada palabra

#.isdecimal()
#123.isdecimal()
#out=True
#12.3.isdecimal()
#out =False

#.swapcase()
#Intercambia las letras de miniscula a mayus y viceversa

#.slicing
n[5:15]
#corta desde el indice 5 hasta el 15

listas = [x for x in "ABCDEFGHI"]
#OUT = ["A","B","C","D","E","F","G"]

#.replace("dados", "monedas")
#remplaza lo señalado por el valor que sigue despues de la ,
