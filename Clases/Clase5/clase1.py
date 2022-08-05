class Alumno:
    tipo = "Persona"
    
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        
    def __str__(self):
        return f"{self.__apellido}, {self.__nombre}"
        
    def saludar(self):
        return f"Hola {self.__nombre} {self.__apellido}"

norman = Alumno("Norman", "Beltran", 53)
pepe = Alumno("Pepe", "Perez", 30)

#print(f"La edad de el objeto norman es {norman.__edad}")
print(norman.saludar())


#print(f"La edad de el objeto pepe es {pepe.__edad}")
print(pepe.saludar())


print("Obj Norman :", norman)
print("Obj Pepe :", pepe)