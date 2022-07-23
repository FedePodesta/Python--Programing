# Dada 2 listas con números enteros, crear una tercera con los
# números que pertenecen a ambas. Pero con la salvedad que
# en esta tercera no debe tener elementos repetidos.
# primera = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2]
# segunda = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2]
# Usar únicamente sentencias de control: condicionales y bucles.
# También es probable que tengas que usar el operador de
# pertenecía.

primera = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2]
segunda = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2]
tercera = []

for n in primera:
    if n in segunda and n not in tercera:
        tercera.append(n)

print(tercera) 