import pymysql

def obtener_empleados():
    db = pymysql.connect("10.10.10.17","root","Manager1.","employees")
    cursor = db.cursor()
    sql = "SELECT * FORM employees"

    try:
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print(resultado)
        return resultado
    except:
        print("Error: no se obtuvo data")
    db.close()



'''email = input("introduce el email: ")
for fila in resultado:
    id = fila[0]'''


