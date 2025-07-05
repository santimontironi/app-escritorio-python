import pyodbc
import os
from dotenv import load_dotenv

# se cargan las variables de entorno
load_dotenv()

# credenciales de la base de datos
server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE")
username = os.getenv("SQL_USERNAME")
password = os.getenv("SQL_PASSWORD")
trusted_connection = os.getenv("SQL_TRUSTED_CONNECTION")

# se arma la cadena de conexión
conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection=yes;"
)

# Conectar y consultar
def getConnection():
    try:
        return pyodbc.connect(conn_str)
    except Exception as e:
        print("Error al conectar: ", e)
        
def queryFunction(query, params=None, fetch=True):
    connection = getConnection()
    if connection == None:
        print("No se conectó a la base de datos.")
        return
    try:
        cursor = connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        results = cursor.fetchall() if fetch else True #fetch es si querés que la función devuelva los resultados de la consulta o no.

        cursor.close()
        connection.commit()  # Para operaciones insert, update, delete
        connection.close()

        return results

    except Exception as e:
        print("Error al ejecutar la consulta:", e)
        return None
    
    
    

