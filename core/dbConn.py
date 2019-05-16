import mysql.connector
from mysql.connector import Error
import conf

try:
    conn = mysql.connector.connect(host=conf.DB_HOST,
                                   database=conf.DB_DATABASE,
                                   user=conf.DB_USER,
                                   password=conf.DB_PASS)
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounting WHERE IdPayment = 2;")
        record = cursor.fetchall()
        print("Your connected to - ", record)
except Error as e:
    print("Error occurred in database operation", e)
finally:
    # closing database connection.
    if (conn.is_connected()):
        cursor.close()
        conn.close()
