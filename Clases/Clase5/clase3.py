class Figura:
    tipo = "Figura"
    __atributo_privado = "Soy un atributo inalcanzable desde fuera."
    def area(self):
        pass
    def perímetro(self):
        pass
    def __str__(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return (self.base * 2) + (self.altura * 2)

    def __str__(self):
        nombre =  "Rectangulo de base " + str(self.base) + " y altura " + str(self.altura)
        return nombre

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
        
    def area(self):
        return self.lado * self.lado
    
    def perimetro(self):
        return self.lado * 4
    
    def __str__(self):
        nombre = "Cuadrado de lado " + str(self.lado)
        return nombre

class Circulo(Figura):

    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return self.radio**2 * 3.14

    def perimetro(self):
        return self.radio*2 * 3.14
    
    def __str__(self):
        nombre = "Círculo de radio " + str(self.radio)
        return nombre
    
    def __add__(self, obj):
        return self.radio + obj.radio

    def __eq__(self, obj):
        if self.radio == obj.radio:
            return True
        return False
                 
    def __len__(self):
        return int(self.area())
    

rec = Rectangulo(10, 5)
cua = Cuadrado(6)
cir1 = Circulo(10)
cir2 = Circulo(10)

print(cir1)


#if cir1 == cir2:
#    print("Son iguales")
#else:
#    print("No son iguales")

print("Suma de obj circulo:", (cir1+cir2))
