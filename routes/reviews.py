from fastapi import APIRouter, Response, status, HTTPException
from config.db import conn
from models.review import review
from schemas.review import Review

reviews = APIRouter()
tags = ["Reviews"]
@reviews.get("/reviews", tags=tags)
def get_reviews():
    try: 
        return conn.execute(review.select()).fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        

@reviews.get("/reviews/{review_id}" ,tags=tags)
def get_review(review_id: int):
    return {"name": "Review 1", "id": review_id}

@reviews.delete("/reviews/{review_id}", tags=tags) 
def delete_review(review_id: int):
    try:
        conn.execute(review.delete().where(review.c.id == review_id))
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@reviews.put("/reviews/{review_id}", tags=tags)
def update_review(review_id: int):
    return {"name": "Review 1", "id": review_id}

@reviews.post("/reviews", tags=tags)
def create_review(Review : Review):
    try:
        conn.execute(review.insert().values(Review.dict()))
        return Review
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))