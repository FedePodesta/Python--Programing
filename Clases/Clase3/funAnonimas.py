
cuadrado = lambda x:x**2

print(cuadrado(11))

nombres= ["jUan", " ricardo","ANA","alberto ", " maria", "Juana"]
print(list(map(lambda x:x.strip().capitalize(),nombres)))


#.strip saca los espacios en blanco 
#.capitalize Hace que los STR comienzen con mayuscula y siga con min
#.title en caso que haya un nobmre compuesto .title pone en MAYUS las dos partes
