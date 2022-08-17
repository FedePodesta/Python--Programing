from shutil import ExecError
import pymysql

def conexion():
    try:


        conn = pymysql.connect(
            host='localhost',
            user= 'root',
            passwd='',
            db='movies'

        )
        print("Conexion correcta")
            

    except ExecError as e:
        print(f"Ocurrio un error de conexion{e.__class__}")

    return conn
#_______________________insert
def crear_peliculas(conn):
    
    try:
        with conn.cursor() as cursor:
            insertar = "INSERT INTO peliculas(titulo, anio) VALUES (%s, %s);"
            cursor.execute(insertar, ("Lord of the Rings", 2002))
            cursor.execute(insertar, ("Titanic", 1997))
            cursor.execute(insertar, ("Back to the future", 1985))
            cursor.execute(insertar, ("Rocky", 1976))
            cursor.execute(insertar, ("El Padrino", 1972))
            cursor.execute(insertar, ("Scarface", 1978))
            
            conn.commit()
    except Exception as e:
        print(f"Fallaron los inserts {e.__class__}")

#_______________________insert uno
def crear_una_pelicula(conn, p_nombre, p_anio):
    
    try:
        with conn.cursor() as cursor:
            insertar = "INSERT INTO peliculas(titulo, anio) VALUES (%s, %s);"
            cursor.execute(insertar, (p_nombre, p_anio))
            conn.commit()
    except Exception as e:
        print(f"Fallo el insert {e.__class__}")





#_______________________select
def consultar_peliculas(conn):
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, titulo, anio FROM peliculas;")
            peliculas = cursor.fetchall()
            for pelicula in peliculas:
                print(pelicula)
    except Exception as e:
        print(f"Fallo la consulta {e.__class__}")

#_______________________Update
def actualizar_peliculas(conn, p_id, p_nombre):
    
    try:
        with conn.cursor() as cursor:
            actualiza = "UPDATE peliculas SET titulo = %s WHERE id = %s;"
            cursor.execute(actualiza,(p_nombre, p_id))
            conn.commit()

    except Exception as e:
        print(f"Fallo la actualización {e.__class__}")

#_______________________select variante I

def consultar_peliculas_v1(conn, p_anio):
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, titulo, anio FROM peliculas WHERE anio > %s;", (p_anio))
            peliculas = cursor.fetchall()
            for pelicula in peliculas:
                print(pelicula)
    except Exception as e:
        print(f"Fallo la consulta variante I {e.__class__}")


#_______________________Borrar 

def borrar_pelicula(conn, p_id ):
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM peliculas WHERE id = %s;", (p_id))            
            conn.commit()
    except Exception as e:
        print(f"Fallo al borrar la pelicula id= {p_id}: {e.__class__}")



conn = conexion()

#crear_peliculas(conn)
#consultar_peliculas(conn)
#actualizar_peliculas(conn, 4, "ROCKY I")
#consultar_peliculas_v1(conn, 1984)
#borrar_pelicula(conn, 6)
consultar_peliculas(conn)


lista = [("Tiburon",1980), ("ET", 1981), ("Star Wars", 1976), ("Flashdance", 1982),("Taxi Driver", 1978)]
for pelicula in lista:
    p_peli, p_anio = pelicula
    crear_una_pelicula(conn, p_peli , p_anio)

conn.close()
