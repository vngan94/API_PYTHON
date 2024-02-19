import mysql.connector
import logging

# Global variable to track the database connection
db_connection = None

def get_db_connection():
    global db_connection

    if db_connection is None:
        host = "127.0.0.1"
        user = "root"
        password = "1234"
        database = "crm"

        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )

            if connection.is_connected():
                print("Connected to the database successfully")

            db_connection = connection
        except mysql.connector.Error as err:
            logging.error(f"Error: {err}")
            raise

    return db_connection

def execute_query(query, params=None, fetchall=False):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall() if fetchall else cursor.fetchone()
        return result
    finally:
        cursor.close()

def commit_query(query, params=None):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
    finally:
        cursor.close()

# ... rest of the code remains the same
