from pydantic import BaseModel, Field
from datetime import date

class BookCreate(BaseModel):
    title: str = Field(..., example="Animal Farm")
    author_id: int = Field(..., example=1)  # Link to the Author's ID
    publication_date: date = Field(..., example="1945-08-17")
    isbn: str = Field(..., example="978-0451526342")
    summary: str = Field(..., example="A farm is taken over by its overworked, mistreated animals.")

class BookRead(BookCreate):
    id: int  # Additional ID field for reading data



class BookGenreCreate(BaseModel):
    book_id: int
    genre_id: int

class BookGenreRead(BookGenreCreate):
    id: int = None




class GenreCreate(BaseModel):
    id: int
    name: str

class GenreRead(GenreCreate):
    id: int
    name: str




class AuthorCreate(BaseModel):
    name: str
    biography: str = None

class AuthorRead(AuthorCreate):
    id: int





class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool

class UserCreate(BaseModel):
    username: str = Field(..., example="john_doe")
    email: str = Field(..., example="john.doe@example.com")
    password: str = Field(..., example="Das ist Password")  # Nur Klartextpasswort hier
    is_active: bool = Field(default=True, example=True)  # Default-Wert direkt setzen

class UserRead(User):
    pass





class ReviewBase(BaseModel):
    book_id: int = Field(..., example=1)
    users_id: int = Field(..., example=1)
    review_text: str = Field(..., example="A thought-provoking novel.")
    rating: int = Field(..., example=5)

class ReviewCreate(ReviewBase):
    pass

class ReviewRead(ReviewBase):
    id: int 


class ReviewRead(BaseModel):
    id: int
    review_text: str
    rating: int





































