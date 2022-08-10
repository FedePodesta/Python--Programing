import os
import sys

try:
    # Acceder a los argumentos pasados al programa por el usuario.
    ruta = sys.argv[1]
    ext = sys.argv[2]
except IndexError:
    print("Argumentos insuficientes. Indique la ruta en donde buscar y la extensión.")
    sys.exit()

try:
    # Obtener la lista de archivos en la ruta especificada.
    archivos = os.listdir(ruta)
except FileNotFoundError:
    print("La ruta no existe.")
    sys.exit()

# Si la extensión no empieza con un punto, agregárselo.
if not ext.startswith("."):
    ext = "." + ext

print(f"Archivos con extensión {ext}:")
# Recorrer la lista de archivos.
for archivo in archivos:
    # Imprimir únicamente los que terminan con la extensión ingresada.
    if archivo.endswith(ext):
        print("-", archivo)