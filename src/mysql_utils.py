import config.credentials as crd
import mysql.connector as mysqlConnector
from mysql.connector import Error


def get_connection():
    connection = {
        "user": crd.DB_USER,
        "password": crd.DB_PASS,
        "host": crd.DB_HOST,
        "database": crd.DB_NAME,
        "port": crd.DB_PORT
    }
    try:
        return mysqlConnector.connect(**connection)
    except Error as e:
        raise e


def fetch_table_data(table_name):
    query = f"SELECT * FROM `{table_name}`"
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                column_names = [desc[0] for desc in cursor.description]
                rows = cursor.fetchall()
        return column_names, rows
    except mysqlConnector.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        raise e
