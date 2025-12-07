from fastapi import APIRouter
from app.services.product_service import recommend_products_from_db

router = APIRouter()

@router.get("/")
async def recommend(customer_id: str, query: str):
    products = await recommend_products_from_db(customer_id, query)
    return {"products": products}