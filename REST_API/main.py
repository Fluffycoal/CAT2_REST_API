from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# In-memory storage for products
products = []

# Product model
class Product(BaseModel):
    name: str
    description: str
    price: float

# POST /products
@app.post("/products/", response_model=Product, status_code=201)
async def create_product(product: Product):
    products.append(product)
    return product

# GET /products
@app.get("/products/", response_model=List[Product])
async def get_products():
    return products