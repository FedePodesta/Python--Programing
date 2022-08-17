import requests
r = requests.post("http://localhost:8880/form")

datos = {
 "name": "Mariano",
 "email": "mariano@ejemplo.com",
 "message": "¡Hola, mundo!"
}
r = requests.post("http://localhost:8880/form", data=datos)
contenido = r.content.decode("utf-8")
#print(contenido)
if "Mensaje enviado" in contenido:
    print("¡Formulario enviado!")
else:
    print("Ocurrió un error.")