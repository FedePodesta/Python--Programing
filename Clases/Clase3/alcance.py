
a = 100

def sumar (s1,s2):
    a= 999  #El alcanze dentro de la funcion es local
    print("La variable a es ",a)
    return s1+s2

print("1. ===>",a) #output 100 ya que es una variable global.
print(sumar(1,4))
print("2. ===>", a)