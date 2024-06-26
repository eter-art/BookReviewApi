import os
import mysql.connector
import bcrypt


# Establish a connection to the MySQL database and return the connection object.

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='BookReview'
    )
    return connection



def create_user(username, email, password, is_active=True):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO users (username, email, hashed_password, is_active) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (username, email, hashed_password, is_active))
    conn.commit()
    cursor.close()
    conn.close()

# create_user('testnutzer1', 'testnutzer1@example.com', 'geheimesPasswort123')
# create_user('testnutzer2', 'testnutzer2@example.com', 'geheimesPasswort234')
# create_user('testnutzer3', 'testnutzer3@example.com', 'geheimesPasswort555')
# create_user('testnutzer4', 'testnutzer4@example.com', 'geheimesPasswort777')
# create_user('testnutzer8', 'testnutzer8@example.com', 'geheimesPasswort888')
# create_user('testnutzer9', 'testnutzer9@example.com', 'geheimesPasswort999')



def create_book(title, author_id, publication_date, isbn, summary):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO book (title, author_id, publication_date, isbn, summary) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (title, author_id, publication_date, isbn, summary))
        conn.commit()
        return cursor.lastrowid  # Returns the ID of the new book
    except Exception as e:
        conn.rollback()
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

# book_id = create_book(
#     "1984",
#     1,  # Author ID
#     "1949-06-8",  # Publication Date
#     "123-4567890123",  # ISBN
#     "Winston Smith wrestles with oppression in Oceania, a place where the Party scrutinizes human actions with ever-watchful Big Brother. Defying a ban on individuality, Winston dares to express his thoughts in a diary and pursues a relationship with Julia."  # Summary
# )
# print(f"Book created with ID: {book_id}")


def create_author(name, biography):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO author (name, biography) VALUES (%s, %s)"
        print(f"Executing SQL: {sql} with values ({name}, {biography})")
        cursor.execute(sql, (name, biography))
        conn.commit()
        print("Author successfully added!")
    except mysql.connector.Error as err:
        print("Failed to insert author:", err)
        conn.rollback()  
    finally:
        cursor.close()
        conn.close()


# create_author('Nino Haratischwili', 'Nino Haratischwili wuchs in Tiflis auf Ausnahme waren die Jahre 1995 bis 1997. In dieser Zeit lebte sie in Deutschland, weil ihre Mutter mit ihr vor dem Bürgerkrieg in Georgien geflohen war und in einem Dorf bei Lübbecke Arbeit gefunden hatte.Im Alter von 14 Jahren ging sie allein nach Georgien zurück')



def add_review(book_id, user_id, review_text, rating):
    conn = get_db_connection()  
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO review (book_id, users_id, review_text, rating) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (book_id, user_id, review_text, rating))
        conn.commit()  
        print("Review added successfully!")
    except Exception as e:
        print("Failed to add review:", e)
        conn.rollback()  
    finally:
        cursor.close()
        conn.close()

# add_review(1, 7, "This book was very insightful and engaging.", 5)



# Close the given database connection

def close_db_connection(connection):
     connection.close()