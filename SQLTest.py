import mysql.connector
try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="password",
        port=3333,
        database="online_store"
    )
    if conn.is_connected():
        print("Successfully connected to MySQL database")
except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn.is_connected():
        conn.close()
        print("MySQL connection is closed")
