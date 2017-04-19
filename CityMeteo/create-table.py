import sqlite3

#conectar a base de datos
conexion = sqlite3.connect("dbSqlite/test.sqlite3")

#Seleccionar el cursor para realizar la consulta
consulta = conexion.cursor()

sql = """
CREATE TABLE IF NOT EXISTS test(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
ciudad VARCHAR(50) NOT NULL,
clima VARCHAR(100),
)
"""

#Ejecutar la consulta
if(consulta.execute(sql)): print("Tabla creada con exito")
else: print("Ha ocurrido un error al crear la tabla")

#terminamos la consulta
consulta.close()

#Guardamos los cambios enla base de datos
conexion.commit()

#Cerramos la conexion con la BD
conexion.close()

