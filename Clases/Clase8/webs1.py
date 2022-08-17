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
    r = rq.get("http://www.pagina12.com.ar")
except Exception as e:    
    print(f"Error {e.__class__}")
else:
    print(r.status_code)
#print(r.content)
