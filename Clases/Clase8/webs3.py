import requests as rq
"""
Status code
1xx Respuestas informativas
2xx Peticiones correctas
3xx Redirecciones
4xx Errores del cliente
5xx Errores del servidor
"""

print("Solicitando Información ....")
print("_"*60)
try:
    url = "https://jsonplaceholder.typicode.com/users"
    r = rq.get(url)
except Exception as e:    
    print(f"Error {e.__class__}")
else:
    data = r.json()
    for element in data:
        print(element['name'], element['email'])