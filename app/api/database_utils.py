from ..database import get_db_connection



def get_db():
    """Provide a database cursor via a generator, ensuring cleanup.
    This yields a cursor to the endpoint function, and ensures the database
    connection is closed properly after the operation, whether it fails or succeeds.
    """
    conn = get_db_connection()
    try:
        yield conn.cursor(dictionary=True)
    finally:
        conn.close()

