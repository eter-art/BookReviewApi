from fastapi import APIRouter, HTTPException, Depends
from ..database_utils import get_db
from ...schemas import BookGenreRead, BookGenreCreate

router = APIRouter()

@router.post("/", response_model=BookGenreRead)
def create_book_genre(book_genre: BookGenreCreate, cursor=Depends(get_db)):
    sql = "INSERT INTO book_genres (book_id, genre_id) VALUES (%s, %s)"
    cursor.execute(sql, (book_genre.book_id, book_genre.genre_id))
    return {"book_id": book_genre.book_id, "genre_id": book_genre.genre_id}



