import sqlite3
#________________________ Creación de tablas
def creardb():
    cursor.execute("CREATE TABLE empleados(id integer PRIMARY KEY, \
                                           nombre text,            \
                                           salario real,           \
                                           departamento text,      \
                                           posicion text,          \
                                           edad numeric\
        )"    
    )
    conn.commit()
#________________________ Insertar
def insertar():
    personas = ((1, "Jose Perez", 100000.50 , "Finanzas", "Jefe", 30), \
                (2, "Maria Perez", 150000.50 , "RRHH", "Jefe", 25), \
                (3, "Pedro Gonzalez", 250000.50 , "RRHH", "Supervisor", 35), \
                (4, "Pedro Diaz", 350000.50 , "Sistemas", "Empleado", 45), \
                (5, "Lucas Gomez", 550000.50 , "Sistemas", "Programador Python", 35), \
    )
    for a,b,c,d,e,f in personas:
        cursor.execute("INSERT INTO empleados VALUES (?,?,?,?,?,?)", (a,b,c,d,e,f))
        
    conn.commit()

#________________________ Consultar
def consultar():
    cursor.execute("SELECT * FROM empleados")
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

#________________________ Consultar un registro
def consultar_uno(id):
    cursor.execute("SELECT * FROM empleados WHERE id = " + str(id))
    fila = cursor.fetchone()
    print(fila)

#________________________ Consultar un conjunto en particular
def consultar_set(patron):
    instruccion = "SELECT * FROM empleados WHERE nombre LIKE ?;" 
    cursor.execute(instruccion, ["%{}%".format(patron)])
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)
    
#________________________ Borrar un registro
def borrar_uno(id):
    instruccion = "DELETE FROM empleados WHERE id = ?;"
    cursor.execute(instruccion, [id])
    conn.commit()

#________________________ Actualizr un registro
def actualizar_uno(id):
    instruccion = "UPDATE empleados SET salario = 600000 WHERE id = ?;"
    cursor.execute(instruccion, [id])
    conn.commit()


conn = sqlite3.connect("empleados.db")
cursor = conn.cursor()

#creardb()
#insertar()
#consultar()
#consultar_uno(2)
#consultar_set("Maria")
#borrar_uno(2)
#actualizar_uno(5)

conn.close()