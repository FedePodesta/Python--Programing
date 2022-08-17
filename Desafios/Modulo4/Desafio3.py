import sqlite3


def traer():
    try:
        conn = sqlite3.connect("datos.sqlite")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contactos")
        datos = cursor.fetchall()
        conn.commit()
        conn.close()
        return datos
    except sqlite3.OperationalError:
        return None



titulo = "ID,NOMBRE,TELEFONO,EMAIL,DIRECCION \n"

datos = traer()

if datos:
    f = open("contactos.csv","w")
    f.write(titulo)
    for fila in datos:
        f.write(f"{fila[0]},{fila[1]},{fila[2]},{fila[3]},{fila[4]}\n")
    f.close()
else:
    print("No hay datos")