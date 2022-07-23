# Crear un script que solicite al usuario el
# código de un país e imprima su nombre,
# de acuerdo con el siguiente diccionario:
# # Diccionario código: país.
# paises = {
#  "ar": "Argentina",
#  "es": "España",
#  "us": "Estados Unidos",
#  "fr": "Francia"
# }
# Si el código ingresado no se encuentra en
# el diccionario, debe imprimir un mensaje en
# pantalla y volver a preguntar. Si el usuario
# escribe “salir”, el programa debe terminar.

paises = {
 "ar": "Argentina",
 "es": "España",
 "us": "Estados Unidos",
 "fr": "Francia"
}

while True:
    codigo = input("Ingrese un codigo o cierre el programa escribiendo salir: ")
    if codigo =="salir":
        break
    try:
        print(paises[codigo])
    except KeyError:
        print("El codigo es invalido, vuelve a intentarlo")
