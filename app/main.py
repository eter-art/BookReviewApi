from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.endpoints.books import router as book_router
from .api.endpoints.users import router as users_router
from .api.endpoints.authors import router as author_router
from .api.endpoints.reviews import router as review_router
from .api.endpoints.genres import router as genre_router
from .api.endpoints.bookGenres import router as bookgenre_router

app = FastAPI(title="Book Reviews API")


app.include_router(book_router, prefix="/api/book", tags=["book"])
app.include_router(users_router, prefix="/api/users", tags=["users"])
app.include_router(author_router, prefix="/api/author", tags=["author"])
app.include_router(review_router, prefix="/api/review", tags=["review"])
app.include_router(genre_router, prefix="/api/genre", tags=["genre"])
app.include_router(bookgenre_router, prefix="/api/bookgenre", tags=["bookgenre"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=[" "],  # Allows all origins
    allow_credentials=True,
    allow_methods=[" "],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def read_root():
    return {"Hello": "World"}




