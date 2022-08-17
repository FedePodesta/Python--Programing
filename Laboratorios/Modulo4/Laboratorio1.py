import sqlite3

# Conectarse a la base de datos (se crea automáticamente si no existe).
conn = sqlite3.connect("comercio.sqlite")
cursor = conn.cursor()

# Crear la tabla.
cursor.execute(
    "CREATE TABLE productos (id INT, nombre TEXT, precio INT)")

# Añadir los productos.
productos = (
    (1, "Teclado", 25),
    (2, "Mouse", 18),
    (3, "Monitor", 300),
    (4, "Parlantes", 100),
)

for producto in productos:
    cursor.execute("INSERT INTO productos VALUES (?, ?, ?)", producto)

# Guardar los cambios.
conn.commit()

# Cerrar la conexión.
conn.close()