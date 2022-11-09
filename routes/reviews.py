from fastapi import APIRouter

reviews = APIRouter()

@reviews.get("/reviews")
def get_reviews():
    return [{"name": "Review 1"}, {"name": "Review 2"}]

@reviews.get("/reviews/{review_id}")
def get_review(review_id: int):
    return {"name": "Review 1", "id": review_id}

@reviews.delete("/reviews/{review_id}")
def delete_review(review_id: int):
    return {"name": "Review 1", "id": review_id}

@reviews.put("/reviews/{review_id}")
def update_review(review_id: int):
    return {"name": "Review 1", "id": review_id}

@reviews.post("/reviews")
def create_review():
    return {"name": "Review 1", "id": 1}