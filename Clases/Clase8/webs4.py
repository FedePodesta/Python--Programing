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

def modificar_uno(id, nombre, cursos):
    try:
        url = "http://localhost:7001/student/"+str(id)
        args = {"name": nombre, "courses": cursos }
        r = rq.put(url, json=args)
    except Exception as e:    
        print(f"Error {e.__class__}")
        print(f"{r.json()}")
    else:
        print(f"Status Code {r.status_code}")
        
def borrar_uno(id):
    try:
        url = "http://localhost:7001/student/"+str(id)
        r = rq.delete(url)
    except Exception as e:    
        print(f"Error {e.__class__}")
        print(f"{r.json()}")
    else:
        print(f"Status Code {r.status_code}")
        
def consultar_uno(id):
    try:
        url = "http://localhost:7001/student/"+str(id)
        r = rq.get(url)
    except Exception as e:    
        print(f"Error {e.__class__}")
        print(f"{r.json()}")
    else:
        print(f"Status Code {r.status_code}")
        print(f"{r.json()}")
        
def consultar():
    try:
        url = "http://localhost:7001/student"
        r = rq.get(url)
    except Exception as e:    
        print(f"Error {e.__class__}")
        print(f"{r.json()}")
    else:
        print(f"Status Code {r.status_code}")
        print(f"{r.json()}")

def agregar(nombre, cursos):
    try:
        url = "http://localhost:7001/student"
        args = {"name":nombre, "courses":cursos}
        r = rq.post(url, json=args)
    except Exception as e:    
        print(f"Error {e.__class__}")
        print(f"{r.json()}")
    else:
        print(f"Status Code {r.status_code}")
        print(f"{r.json()}")

def mostrar():
    try:
        url = "http://localhost:7001/student"
        r = rq.get(url)
    except Exception as e:    
        print(f"Error {e.__class__}")
        print(f"{r.json()}")
    else:
        alumnos = r.json()
        for alumno in alumnos["students"]:
            print (f"Alumno: {alumno['id']}, {alumno['nombre']}, Cursos: {alumno['cursos']}")
    

alumnos = (
    ("Mauricio", 5),
    ("Rodrigo", 6),
    ("Alan", 7),
    ("Alejandro", 10),
    ("Andres", 11),
)

#for i, j in alumnos:
#    agregar(i, j)

   
#consultar()
#mostrar()
#consultar_uno(3)
#modificar_uno(3, "Alan Oscar", 99)
borrar_uno(3)
mostrar()