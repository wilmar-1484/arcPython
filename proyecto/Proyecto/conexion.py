"""
    @autor: Wilmar Alexander Suarez Sanchez
    @fecha: 24/09/2021
"""



import mysql.connector

def mySQLConn():
    cursor = None
    conn = None

    try:
        conn = mysql.connector.connect(user = "root",
                             password = "",
                             host = 'localhost',
                             database = "empresa")
        # Mostrar las propiedades de la conexion
        # print("Propiedades:", conn.get_dsn_parameters())
        cursor = conn.cursor()
        # cursor.execute('SELECT version();')
        # record = cursor.fetchone()
        # print("Conexion exitosa ...")

    except mysql.connector.Error as e:
        print("* Error: ", e)

    finally:
        return conn, cursor


def consultar(usuario, clave):
    usr = None
    conn, cursor = mySQLConn()

    if cursor and conn:
        # Conexion Exitosa ...
        # construir la consulta
        stmt = "SELECT * FROM usuario WHERE usuario = %s and clave = %s"

        cursor.execute(stmt, (usuario, clave))
        usr = cursor.fetchone()

        if usr is not None:
            for dato in usr:
                print(dato, end=", ")

            print()

        cerrarConn(cursor, conn)
    else:
        # Error
        print("Ha ocurrido un error ...")

    return usr
def insertarPersonas(identificacion, nombre, apellido, direccion, telefono, correo, foto):
    conn, cursor = mySQLConn()
    
    if (direccion="")

def cerrarConn(cursor, conn):
    cursor.close()
    conn.close()
