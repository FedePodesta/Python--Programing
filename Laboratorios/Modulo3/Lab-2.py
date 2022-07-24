# Crear una clase “Persona” que sea la clase padre de otra
# clase “Estudiante”.
# La clase “Persona” su método __init__() debe de estar
# preparado para recibir nombre y apellido. Además, esta
# clase , debe tener un método para mostrar
# nombre_completo() el cual debe mostrar el nombre
# acompañado del apellido.
# La otra clase “Estudiante”, debe de poder heredar de
# “Persona”, y además recibir los argumentos nombre y
# edad. También la clase “Estudiante”, recibe el valor
# “carrera”, y además contar con un método
# mostrar_carrera() . Las dos clases son obligatorias. 


class Persona():
 def __init__(self,nom,ape):
    self.nombre = nom
    self.apellido = ape

 

 def nombre_completo(self):
    print(self.nombre +" "+ self.apellido)


class Estudiante(Persona):
 def __init__(self,nom,ape,carr):
     super().__init__(nom,ape)
     self.carrera = carr
 def mostrar_carrera(self):
    print(self.carrera)


alumno = Estudiante("Federico","Podesta","Python Web Developer")

#print (f" {alumno.nombre} {alumno.apellido} {alumno.carrera}")
alumno.nombre_completo()
alumno.mostrar_carrera()