from pydantic import BaseModel
from datetime import date


# Assuming continuation from the existing Book models...

class User(BaseModel):
    id: int = None
    username: str
    email: str
    is_active: bool

class Review(BaseModel):
    id: int = None
    book_id: int
    user_id: int
    review_text: str
    rating: int

class BookGenre(BaseModel):
    book_id: int
    genre_id: int


