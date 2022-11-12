from fastapi import APIRouter, Response, status, HTTPException
from config.db import conn
from models.product import product
from schemas.product import Product

products = APIRouter()

@products.get("/products", tags=['Products'])
def get_products(Response: Response):
    try: 
        prods = conn.execute(product.select()).fetchall()
        if(prods is None):
            Response.status_code = status.HTTP_404_NOT_FOUND
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No products found")
        else:
            return prods
    except Exception as e:
        raise HTTPException(status_code=500 , detail=str(e))


@products.get("/products/{product_id}", tags=['Products'])
def get_product(product_id: int, Response: Response):
    try:
        prod = conn.execute(product.select().where(product.c.id == product_id)).first()
        if(prod is not None):
            return prod
        else:
            Response.status_code = status.HTTP_404_NOT_FOUND
            return HTTPException(status_code=404, detail="Product not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)


@products.delete("/products/{product_id}", tags=['Products'])
def delete_product(product_id: int, Response: Response):
    try:
        prod = conn.execute(product.select().where(product.c.id == product_id)).first()
        if(prod is not None):
            conn.execute(product.delete().where(product.c.id == product_id))
        else:
            Response.status_code = status.HTTP_404_NOT_FOUND
            return HTTPException(status_code=404, detail="Product not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    
    


@products.put("/products/{product_id}", tags=['Products'])
def update_product(Product: Product, product_id: int, Response: Response):
   try:
       prod = conn.execute(product.select().where(product.c.id == product_id)).first()
       if(prod is not None):
           conn.execute(product.update().where(product.c.id == product_id).values(name=Product.name, description=Product.description, price=Product.price))
       else:
           Response.status_code = status.HTTP_404_NOT_FOUND
           return HTTPException(status_code=404, detail="Product not found")
   except Exception as e:
       raise HTTPException(status_code=400, detail=e)
        


@products.post("/products", tags=['Products'])
def create_product(Product : Product):
    try: 
        conn.execute(product.insert().values(Product.dict()))
        return Product
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    