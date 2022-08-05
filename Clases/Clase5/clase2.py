class Vivienda:
	temperatura_maxima = -100 #inicializamos a un valor ficticio muy pequeño

	def __init__(self, temperatura):
		self.temperatura_actual = temperatura
		self.registrar_temperatura(temperatura)

	def registrar_temperatura(self, nueva_temperatura):
		self.temperatura_actual = nueva_temperatura
		# si alguna vivienda supera la temperatura máxima se actualiza la variable de clase
		if self.temperatura_actual > self.temperatura_maxima:
			self.__class__.temperatura_maxima = self.temperatura_actual

#creamos tres viviendas y registramos su temperatura inicial
v1 = Vivienda(20)
v2 = Vivienda(23)
v3 = Vivienda(18)

#mostramos la temperatura máxima
print(f'La temperatura máxima es {Vivienda.temperatura_maxima}')

#registramos algunas temperaturas nuevas
v1.registrar_temperatura(25)
v2.registrar_temperatura(22)
v3.registrar_temperatura(21)

#mostramos las temperaturas de las viviendas y la temperatura máxima
print(f'Temperatura vivienda 1: {v1.temperatura_actual}')
print(f'Temperatura vivienda 2: {v2.temperatura_actual}')
print(f'Temperatura vivienda 3: {v3.temperatura_actual}')
print(f'La temperatura máxima es {Vivienda.temperatura_maxima}')