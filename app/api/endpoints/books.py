from fastapi import APIRouter, HTTPException, Depends
from ..database_utils import get_db
from ...schemas import BookRead, BookCreate, ReviewRead


router = APIRouter()





@router.post("/", response_model=BookRead)
def create_book(book: BookCreate, cursor = Depends(get_db)):
    sql = "INSERT INTO book (title, author_id, publication_date, isbn, summary) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (book.title, book.author_id, book.publication_date, book.isbn, book.summary))
    book_id = cursor.lastrowid
    return {**book.dict(), "id": book_id}

@router.get("/", response_model=list[BookRead])
def read_book(cursor = Depends(get_db)):
    cursor.execute("SELECT * FROM book")
    book = cursor.fetchall()
    return book

@router.get("/{book_id}", response_model=BookRead)
def get_book_by_id(book_id: int, cursor = Depends(get_db)):
    cursor.execute("SELECT * FROM book WHERE id = %s", (book_id,))
    book = cursor.fetchone()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.get("/{book_id}/review", response_model=list[ReviewRead])
def get_book_reviews(book_id: int, cursor = Depends(get_db)):
    cursor.execute("""
        SELECT r.id, r.review_text, r.rating
        FROM review r
        WHERE r.book_id = %s
    """, (book_id,))
    reviews = cursor.fetchall()
    if not reviews:
        raise HTTPException(status_code=404, detail="No reviews found for this book")
    return reviews


@router.put("/{book_id}", response_model=BookRead)
def update_book(book_id: int, book: BookCreate, cursor = Depends(get_db)):
    sql = "UPDATE book SET title=%s, author_id=%s, publication_date=%s, isbn=%s, summary=%s WHERE id=%s"
    cursor.execute(sql, (book.title, book.author_id, book.publication_date, book.isbn, book.summary, book_id))
    cursor.connection.commit()
    return {**book.dict(), "id": book_id}

@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, cursor = Depends(get_db)):
    cursor.execute("DELETE FROM book WHERE id = %s", (book_id,))
    cursor.connection.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"ok": True}