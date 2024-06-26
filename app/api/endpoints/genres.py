from fastapi import APIRouter, HTTPException, Depends
from ..database_utils import get_db
from ...schemas import GenreRead, GenreCreate 

router = APIRouter()


@router.post("/", response_model=GenreRead)
def create_genre(genre: GenreCreate, cursor=Depends(get_db)):
    sql = "INSERT INTO genre (name) VALUES (%s)"
    cursor.execute(sql, (genre.name,))
    genre_id = cursor.lastrowid
    cursor.connection.commit()
    return {**genre.dict(), "id": genre_id}

@router.get("/", response_model=list[GenreRead])
def read_genre(cursor=Depends(get_db)):
    cursor.execute("SELECT * FROM genre")
    return cursor.fetchall()

@router.get("/{id}", response_model=GenreRead)
def read_genre_by_id(id: int, cursor = Depends(get_db)):
    cursor.execute("SELECT * FROM genre WHERE id = %s", (id,))
    genre = cursor.fetchone()
    if not genre:
        raise HTTPException(status_code=404, detail="genre not found")
    return genre