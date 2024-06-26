from .database import get_db_connection, close_db_connection

def get_db():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        yield cursor
    finally:
        cursor.close()
        close_db_connection(conn)

