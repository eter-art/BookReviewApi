from fastapi import APIRouter,HTTPException, Depends
from ..database_utils import get_db
from ...schemas import  AuthorCreate, AuthorRead 

router = APIRouter()


@router.post("/", response_model=AuthorRead)
def create_author(author: AuthorCreate, cursor=Depends(get_db)):
    sql = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
    cursor.execute(sql, (author.name, author.biography))
    author_id = cursor.lastrowid
    cursor.connection.commit()
    return {**author.dict(), "id": author_id}

@router.get("/", response_model=list[AuthorRead]) #aq unda davamta author id rom amomigdos
def read_author(cursor=Depends(get_db)):
    cursor.execute("SELECT * FROM author")
    return cursor.fetchall()

@router.get("/{author_id}", response_model=AuthorRead)
def read_author_by_id(author_id: int, cursor=Depends(get_db)):
    cursor.execute("SELECT * FROM author WHERE id = %s", (author_id,))
    author = cursor.fetchone()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author