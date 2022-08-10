class Cliente():
    def __init__(self,persona,identificador):
        self.nombre_apellido = persona
        self.cuit = identificador
    
    def mostrar_info(self):
        print("Nombre y apellido:", self.nombre_apellido)
        print("Cuit:",self.cuit)

        


#########################################################################


cliente1 = Cliente("Jorge Marmol",200000003)
cliente1.mostrar_info()



