from fastapi import APIRouter 

products = APIRouter()

@products.get("/products")
def get_products():
    return [{"name": "Product 1"}, {"name": "Product 2"}]


@products.get("/products/{product_id}")
def get_product(product_id: int):
    return {"name": "Product 1", "id": product_id}


@products.delete("/products/{product_id}")
def delete_product(product_id: int):
    return {"name": "Product 1", "id": product_id}


@products.put("/products/{product_id}")
def update_product(product_id: int):
    return {"name": "Product 1", "id": product_id}


@products.post("/products")
def create_product():
    return {"name": "Product 1", "id": 1}