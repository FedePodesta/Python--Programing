anios = [1800,1840,1871,1999,2000,2020,2021]
nombres = ["Juan", "Juana", "Alberto", "Andres", "Mario", "Ana", "Alba"]
def nombres_a(x):
    if x[0]=="A":
        return True
    return False

def bisiesto(anio):
    if anio%400 ==0:
        return True
    else:
        if anio%4==0 and anio%100!=0:
            return True
    return False

# resultados = filter (bisiesto,anios)
# print(type(resultados), tuple(resultados))

resultados = filter (nombres_a,nombres)
print(type(resultados), tuple(resultados))