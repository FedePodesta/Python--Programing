import requests as rq
"""
Status code
1xx Respuestas informativas
2xx Peticiones correctas
3xx Redirecciones
4xx Errores del cliente
5xx Errores del servidor
"""

try:
    url = "http://httpbin.org/get"
    args = {"nombre":"Norman", "apellido":"Beltran", "edad":53}
    r = rq.get(url, params=args)
except Exception as e:    
    print(f"Error {e.__class__}")
else:
    print(r.status_code)
    print(r.url)
    print(r.json())
    print(r)
