import subprocess
import time
import sys
import os


if os.name == "nt":
    comando = "pip"
    borrar = "cls"
else:
    comando = "pip3"
    borrar = "clear"

os.system(borrar)

print("Lanzando el backup...")
print("Espere un momento, por favor")
time.sleep(3)

try:
    p = subprocess.run([comando,"list"],capture_output=True,encoding="cp850")
except Exception:
    print("Revisar hay algun problema con pip, ya que no se puede ejecutar")
    print("Backup terminado sin completar el proceso")
    sys.exit()

texto = p.stdout

listado = (texto.strip()).split()[4:]
listado = listado[::2]

nombres =[]

for n in listado:
    nombres.append(n+"\n")

f = open("backup.txt","w")
f.writelines(nombres)
f.close()

print(f"Backup completo, se salvaron {len(listado)} nombres de módulos")