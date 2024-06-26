from fastapi import APIRouter,HTTPException,Depends
from ..database_utils import get_db
from ...schemas import ReviewRead, ReviewCreate 

router = APIRouter()


#to see all the reviews
@router.get("/", response_model=list[ReviewRead])
def read_reviews(cursor=Depends(get_db)):
    cursor.execute("SELECT * FROM review")
    review_data = cursor.fetchall()
    return [ReviewRead(**data) for data in review_data]


# To get a specific review by ID
@router.get("/{review_id}", response_model=ReviewRead)
def read_review_by_id(review_id: int, cursor=Depends(get_db)):
    cursor.execute("SELECT * FROM review WHERE id = %s", (review_id,))
    review = cursor.fetchone()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return ReviewRead(**review)




#to create review
@router.post("/", response_model=ReviewRead)
def create_review(review: ReviewCreate, cursor=Depends(get_db)):
    sql = "INSERT INTO review (book_id, users_id, review_text, rating) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (review.book_id, review.user_id, review.review_text, review.rating))
    review_id = cursor.lastrowid
    return ReviewRead(id=review_id, **review.dict())
