# Crea una clase “Persona”. Con atributos nombre y edad.
# Además, hay que crear un método “cumpleaños”, que
# aumente en 1 la edad de la persona cuando se invoque
# sobre un objeto creado con “Persona”.
# Tendríamos que lograr ejecutar el siguiente código con
# la clase creada:
# p = Persona("Juan", 21)
# p.cumpleaños()
# print(f"{p.nombre} cumple {p.edad} años")


class Persona:
    def __init__(self,n,e):
        self.nombre = n
        self.edad = e

    def cumpleaños(self):
        self.edad+=1


        
p = Persona("Juan", 21)
p.cumpleaños()
print(f"{p.nombre} cumple {p.edad} años")